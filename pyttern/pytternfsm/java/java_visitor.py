from antlr4 import TerminalNode
from loguru import logger

from ...antlr.java.JavaParserVisitor import JavaParserVisitor
from ...antlr.java.JavaParser import JavaParser
from ...simulator.pyttern_fsm import FSM, Movement
from ...simulator.transitions import ClassTransition, StringTransition, VarTransition, ObjectTransition, ExceptTransition

class Java_Visitor(JavaParserVisitor):
    def __init__(self, strict=False):
        super().__init__()
        self.strict = strict
        self.depth = 0
        self.current_fsm_node = None
        self.up_to = []
        self.brace_count = 0
        self.has_seen_brace = False

    def text_node(self, text):
        if text == "{":
            self.brace_count += 1
            self.has_seen_brace = True
        elif text == "}":
            self.brace_count -= 1

        next_node = FSM()
        transition = self.get_up_transition(next_node, StringTransition(text))
        self.current_fsm_node.add_transition(*transition)

        self.current_fsm_node = next_node
        return next_node

    def get_up_transition(self, next_node, pred=None):
        if pred is None:
            pred = ObjectTransition()

        up_to = self.up_to.pop() if self.up_to else None
        if up_to is not None:
            node, depth = up_to
            null_node = FSM()
            null_transition = (null_node, pred, [])
            self.current_fsm_node.add_transition(*null_transition)
            self.current_fsm_node = null_node

            self_transition = (null_node, ExceptTransition(node), [Movement.MP])
            self.current_fsm_node.add_transition(*self_transition)

            if self.has_seen_brace and self.brace_count == 0:
                transition = (next_node, VarTransition(node), [])
            else:
                transition = (next_node, VarTransition(node), [Movement.MP] * depth + [Movement.MRS])

            self.depth = 0
            return transition

        if self.has_seen_brace and self.brace_count == 0:
            transition = (next_node, pred, [])
        else:
            transition = (next_node, pred, [Movement.MP] * self.depth + [Movement.MRS])

        self.depth = 0
        return transition
        
    def visit(self, tree):
        FSM.default_name = 1
        self.depth = 0
        start_node = FSM("START")
        self.current_fsm_node = start_node
        super().visit(tree)

        return start_node

    def visitChildren(self, node, clazz=None): # clazz -> type of node

        if isinstance(node, TerminalNode): # TerminalNode -> leaf
            logger.debug(f"Handling {node.__class__.__name__} as Terminal")
            return self.text_node(node.getText())

        children = list(node.children) if getattr(node, "children", None) else []

        if clazz is None:
            clazz = node.__class__

        start = (node.start.line - 1, node.start.column) if node.start else None
        end = (node.stop.line - 1, node.stop.column) if node.stop else None

        next_node = FSM(start=start, end=end)
        transition = (next_node, ClassTransition(clazz), [Movement.MLC])
        self.current_fsm_node.add_transition(*transition)
        self.current_fsm_node = next_node

        old_depth = self.depth
        self.depth = 0
        up_to = self.up_to
        self.up_to = []

        for i, child in enumerate(children):
            if i == len(children) - 1:
                self.depth = old_depth + 1
                self.up_to = up_to + self.up_to

            if isinstance(child, TerminalNode):
                self.text_node(child.getText())
            else:
                child.accept(self)

        return next_node

    def visitVar_wildcard(self, ctx: JavaParser.Var_wildcardContext):
        var_name = ctx.identifier().getText()
        print("VN:::", var_name)
        next_node = FSM()
        transition = self.get_up_transition(next_node, VarTransition(var_name))
        self.current_fsm_node.add_transition(*transition)
        self.current_fsm_node = next_node
        return next_node

    def visitSimple_wildcard(self, ctx: JavaParser.Simple_wildcardContext):
        pred = ObjectTransition()

        next_node = FSM()
        transition = self.get_up_transition(next_node, pred)
        self.current_fsm_node.add_transition(*transition)

        self.current_fsm_node = next_node
        return next_node

    def visitPrimitiveType(self, ctx: JavaParser.PrimitiveTypeContext):
        text = ctx.getText()
        logger.debug("Find visitPrimitiveType")

        primitive_node = FSM()
        transition = (primitive_node, ClassTransition(JavaParser.PrimitiveTypeContext), [Movement.MLC])
        self.current_fsm_node.add_transition(*transition)
        self.current_fsm_node = primitive_node
        self.depth += 1

        next_node = FSM()
        if ctx.WILDCARD_SPACE():
            logger.debug("Find primitive wildcard (# or # )")
            transition = self.get_up_transition(next_node, ObjectTransition())
        else:
            transition = self.get_up_transition(next_node, StringTransition(text))

        self.current_fsm_node.add_transition(*transition)
        self.current_fsm_node = next_node

        return primitive_node

    def visitIdentifier(self, ctx: JavaParser.IdentifierContext):
        text = ctx.getText()
        logger.debug("Find visitIdentifier")
        print(f"TEXT {text}")

        identifier_node = FSM()
        transition = (identifier_node, ClassTransition(JavaParser.IdentifierContext), [Movement.MLC])
        self.current_fsm_node.add_transition(*transition)
        self.current_fsm_node = identifier_node
        self.depth += 1

        next_node = FSM()
        if text == "#":
            logger.debug("Find #")
            transition = self.get_up_transition(next_node, ObjectTransition())
        else:
            transition = self.get_up_transition(next_node, StringTransition(text))

        self.current_fsm_node.add_transition(*transition)
        self.current_fsm_node = next_node

        return identifier_node

    def visitList_wildcard(self, ctx: JavaParser.List_wildcardContext):
        next_node = FSM()
        transition = self.get_up_transition(next_node)
        self.current_fsm_node.add_transition(*transition)
        self_transition = (next_node, ObjectTransition(), [Movement.MRS])
        next_node.add_transition(*self_transition)
        self.current_fsm_node = next_node

        return next_node

    def visitSimple_compound_wildcard(self, ctx: JavaParser.Simple_compound_wildcardContext):
        next_node = FSM()
        pred = ObjectTransition()
        self.depth += 1

        self.current_fsm_node.add_transition(next_node, pred, [Movement.MLC])
        next_node.add_transition(next_node, ObjectTransition(), [Movement.MRS])

        self.current_fsm_node = next_node

        statement = ctx.statement()
        if statement is not None:
            statement.accept(self)

        return next_node




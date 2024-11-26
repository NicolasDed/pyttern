from antlr4 import TerminalNode
from loguru import logger

from ...antlr.java.JavaParserVisitor import JavaParserVisitor
from ...simulator.pyttern_fsm import FSM, Movement
from ...simulator.transitions import ClassTransition

class Java_Visitor(JavaParserVisitor):
    def __init__(self, strict=False):
        super().__init__()
        self.strict = strict
        self.depth = 0
        self.current_fsm_node = None
        self.up_to = []
        
    def visit(self, tree):
        FSM.default_name = 1
        self.depth = 0
        start_node = FSM("START")
        self.current_fsm_node = start_node
        super().visit(tree)

        return start_node

    def visitChildren(self, node, clazz=None):
        children = list(node.getChildren())
        if len(children) == 0:
            logger.debug(f"Handling {node.__class__.__name__} as Terminal")
            return self.text_node(node.getText())

        if clazz is None:
            clazz = node.__class__

        start = None
        end = None
        if node.start is not None and node.stop is not None:
            start = (node.start.line - 1, node.start.column)
            end = (node.stop.line - 1, node.stop.column)
        next_node = FSM(start=start, end=end)
        transition = (next_node, ClassTransition(clazz), [Movement.MLC])
        self.current_fsm_node.add_transition(*transition)

        self.current_fsm_node = next_node

        old_depth = self.depth
        self.depth = 0
        up_to = self.up_to
        self.up_to = []

        for i in range(len(children)):
            if i == len(children) - 1:
                self.depth = old_depth + 1
                self.up_to = up_to + self.up_to
            c = children[i]
            c.accept(self)

        return next_node
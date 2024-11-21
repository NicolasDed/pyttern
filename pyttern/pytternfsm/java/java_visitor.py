from antlr4 import TerminalNode
from loguru import logger

from ...antlr.java.JavaParserVisitor import JavaParserVisitor
from ...simulator.pyttern_fsm import FSM

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
"""
This module contains the ASTMatcher class.
"""

import ast
from ast import BinOp

from .astpyttern import AstPyttern


class AstMatcher:
    """
    ASTMatcher class is responsible for custom matching of Python AST nodes.
    If a method is defined with the name visit_<node_name>_<pattern_name> or visit_<node_name>,
    it will be called when visiting the nodes.
    """

    def __init__(self, matcher):
        """
        Constructor for ASTMatcher class.
        :param matcher: Matcher object for further matching.
        """
        self.matcher = matcher

    def generic_visit(self, pattern, node) -> bool:
        """
        Generic visit method for ASTMatcher class.
        :param pattern: Pattern node to be matched.
        :param node: Node to be matched.
        :return: False if the nodes are from different types, True otherwise.
        """
        return type(pattern) is type(node)

    def visit(self, pattern: ast.AST | AstPyttern, node: ast.AST | AstPyttern) -> bool:
        """
        Visit method for ASTMatcher class.
        This method is responsible for calling the correct visit method for the
        given pattern and node.
        If no specific method is found, it calls the generic_visit method.
        :param pattern: Pattern node to be matched.
        :param node: Node to be matched.
        :return: Result of the visit method for the given pattern and node.
        """
        method1 = 'visit_' + node.__class__.__name__ + "_" + pattern.__class__.__name__
        method2 = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method1, getattr(self, method2, self.generic_visit))
        return visitor(pattern, node)

    # Careful of __iadd__ method
    def visit_AugAssign_Assign(self, pattern, node):
        """Handle var += value and var = var + value patterns."""
        node_target = node.target
        node_op = node.op
        node_value = node.value
        pattern_targets = pattern.targets

        if len(pattern_targets) != 1:
            return False
        from pyttern.matcher import Matcher
        target_matcher = Matcher()
        target_matcher.variables = self.matcher.variables
        pattern_target = pattern_targets[0]
        if not target_matcher.match(pattern_target, node_target):
            return False

        pattern_expr = pattern.value
        if not isinstance(pattern_expr, BinOp):
            return False

        if type(pattern_expr.op) is not type(node_op):
            return False

        left_matcher = Matcher()
        left_matcher.variables = self.matcher.variables
        left_match = left_matcher.match(pattern_expr.left, node_value)
        right_matcher = Matcher()
        right_matcher.variables = self.matcher.variables
        right_match = right_matcher.match(pattern_expr.right, node_value)
        if not right_match and not left_match:
            return False

        self.matcher.code_walker.select_specific_child("")
        self.matcher.pattern_walker.select_specific_child("")

        return True

    def visit_Assign_AugAssign(self, pattern, node):
        """Handle var = var + value and var += value patterns."""
        pattern_target = pattern.target
        pattern_op = pattern.op
        pattern_value = pattern.value
        node_targets = node.targets

        if len(node_targets) != 1:
            return False
        from pyttern.matcher import Matcher
        target_matcher = Matcher()
        target_matcher.variables = self.matcher.variables
        node_target = node_targets[0]
        if not target_matcher.match(pattern_target, node_target):
            return False

        node_expr = node.value
        if not isinstance(node_expr, BinOp):
            return False

        if type(node_expr.op) is not type(pattern_op):
            return False

        left_matcher = Matcher()
        left_matcher.variables = self.matcher.variables
        left_match = left_matcher.match(pattern_value, node_expr.left)
        right_match = False
        if isinstance(pattern_op, (ast.Add, ast.Mult)):
            right_matcher = Matcher()
            right_matcher.variables = self.matcher.variables
            right_match = right_matcher.match(pattern_value, node_expr.right)
        if not right_match and not left_match:
            return False

        self.matcher.code_walker.select_specific_child("")
        self.matcher.pattern_walker.select_specific_child("")

        return True

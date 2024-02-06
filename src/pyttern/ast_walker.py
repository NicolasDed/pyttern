"""
Module for handling the AST tree traversal.
"""

import ast

from .astpyttern import iter_child_nodes, AstPyttern


class ast_walker:
    """
    Class responsible for handling the AST tree traversal. It is used to walk through the AST.
    It uses 3 methods to move through the tree: next, next_child and next_sibling.
    THis ensures the faisability of the tree traversal.
    """

    def __init__(self, tree: ast.AST | AstPyttern):
        """
        Constructor for AstWalker class.
        :param tree: AST tree to be walked through.
        """
        self.tree = tree
        self._node = None
        self._set_node(tree, None)

    def current(self) -> ast.AST | AstPyttern:
        """
        Returns the current node.
        :return: Current node.
        """
        return self._node.node

    def _set_node(self, tree, parent):
        self._node = _Node(tree, parent)

    def next(self) -> ast.AST | AstPyttern | None:
        """
        Moves to the next node in the tree.
        Try to move to the next child, if it is not possible, tries to move to the next sibling,
        if it is not possible, tries to move to the next parent.
        :return: Next node in the tree or None if no next node.
        """
        nxt = self.next_child()
        if nxt is not None:
            return nxt

        nxt = self.next_sibling()
        if nxt is not None:
            return nxt

        nxt = self.next_parent()
        if nxt is not None:
            return nxt

        return None

    def select_specific_child(self, field: str):
        """
        Selects the children of the current node based on the field.
        :param field: Field to be selected.
        """
        self._node.children = getattr(self._node.node, field, [])

    def select_body_children(self):
        """Selects the children of the current node based on the body field."""
        children = []
        for _, vals in ast.iter_fields(self._node.node):
            if isinstance(vals, list) and len(vals) > 0 and isinstance(vals[0], ast.stmt):
                children.extend(vals)
        self._node.children = children

    def next_child(self):
        """
        Moves to the next child of the current node.
        :return: Next child of the current node or None if no next child.
        """
        nxt = self._node.next_child()
        if nxt is None:
            return None
        self._set_node(nxt, self._node)
        return nxt

    def next_parent(self):
        """
        Moves to the next parent of the current node.
        :return: Next parent of the current node or None if no next parent.
        """
        parent = self._node.parent
        if parent is None:
            return None
        next_parent = parent.parent
        if next_parent is None:
            return None
        next_child = next_parent.next_child()
        while next_child is None:
            parent = next_parent
            if parent is None:
                return None
            next_parent = parent.parent
            if next_parent is None:
                return None
            next_child = next_parent.next_child()

        self._set_node(next_child, next_parent)
        return next_child

    def next_sibling(self):
        """
        Moves to the right sibling of the current node.
        :return: Right sibling of the current node or None if no right sibling.
        """
        parent = self._node.parent
        if parent is None:
            return None
        next_child = parent.next_child()
        if next_child is None:
            return None
        self._set_node(next_child, parent)
        return next_child


def _is_load_store(obj):
    return not isinstance(obj, (ast.Store, ast.Load))


class _Node:
    """
    Class responsible for keeping information about the current node in the tree.
    Used for the tree traversal.
    """
    def __init__(self, node, parent):
        self.node = node
        self.parent = parent
        self.children = list(filter(_is_load_store, iter_child_nodes(node)))
        self.child_index = 0

    def next_child(self):
        """
        Returns the next child of the current node.
        :return: Next child of the current node or None if no next child.
        """
        if len(self.children) <= self.child_index:
            return None
        next_child = self.children[self.child_index]
        self.child_index += 1
        return next_child

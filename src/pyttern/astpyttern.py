"""
Defines the Pyttern AST classes and helper functions.
"""

import ast
from ast import AST, Name, Load


class AstPyttern:
    """
    Abstract class for pyttern AST nodes.
    """

    def __init__(self, types=None):
        """Constructor for ast_pyttern class."""
        self._attributes = ["lineno", "lineno_end"]
        self._fields = []
        self.lineno = None
        self.lineno_end = None
        self.types = types
        if types is not None and not isinstance(types, list):
            raise ValueError(f"Argument types should be of type list not {type(types)}.")

    def __str__(self):
        return type(self).__name__

    def __repr__(self):
        return repr(self.__str__())

    def visit(self, matcher, current_node):
        """
        Visit method for ast_pyttern class.
        Handle the matching of pyttern node with the current node.
        :param matcher: Matcher object for further matching.
        :param current_node: Current node to be matched.
        :return: True if the subtree match, False otherwise.
        """
        raise NotImplementedError()

    def check_type(self, node) -> bool:
        """Check if the node type is in the types list."""
        if self.types is None:
            return True
        return f"{type(node).__name__}" in self.types

    def _recursive_match(self, pattern_node, code_node, matcher, lineno):
        matcher.save_walkers_state()
        if matcher.rec_match(pattern_node, code_node):
            end_lineno = getattr(code_node, "lineno", None)
            if end_lineno != lineno and end_lineno is not None:
                matcher.pattern_match.add_line_skip_match(lineno, end_lineno - 1)
            return True
        matcher.load_walkers_state()
        matcher.pattern_match.match(code_node, self)
        if lineno and lineno not in matcher.pattern_match.pattern_match:
            matcher.pattern_match.add_pattern_match(lineno, self)
        return False


class SimpleWildcard(AstPyttern):
    """SimpleWildcard class is responsible for matching the "?" wildcard."""

    def __init__(self, types=None, low=1, high=1):
        super().__init__(types=types)
        self.low = low
        self.high = high

    def __str__(self):
        return 'ANY'

    def _handle_zero(self, matcher, current_node):
        """Handle the case where we don't want to match the current node."""
        next_pattern_node = matcher.pattern_walker.next_sibling()
        while isinstance(next_pattern_node, AnyWildcard):
            next_pattern_node = matcher.pattern_walker.next_sibling()

        lineno = getattr(current_node, "lineno", None)

        if next_pattern_node is None:

            # We cannot juste skip, we have to check every type inside
            if self.types is not None:
                current_node = matcher.code_walker.next_sibling()
                while current_node is not None:
                    if not self.check_type(current_node):
                        return False
                    current_node = matcher.code_walker.next_sibling()

            next_pattern_node = matcher.pattern_walker.next()
            next_code_node = matcher.code_walker.next_parent()

            if next_pattern_node is None:
                if next_code_node is None or not matcher.strict:
                    if lineno and lineno not in matcher.pattern_match.pattern_match:
                        matcher.pattern_match.add_pattern_match(lineno, self)
                    return True
                return False
            if (lineno and lineno not in matcher.pattern_match.pattern_match
                    and next_code_node is not None):
                matcher.pattern_match.add_pattern_match(lineno, self)
                end_lineno = next_code_node.lineno - 1
                if lineno != end_lineno:
                    matcher.pattern_match.add_line_skip_match(lineno, end_lineno)
            return matcher.rec_match(next_pattern_node, next_code_node)

        code_node = current_node
        while code_node is not None:
            if not self.check_type(code_node):
                return False

            if self._recursive_match(next_pattern_node, code_node, matcher, lineno):
                return True

            code_node = matcher.code_walker.next_sibling()

        return False

    def visit(self, matcher, current_node):
        if self.low == 0 == self.high:
            return self._handle_zero(matcher, current_node)

        if not self.check_type(current_node):
            matcher.error = (f"Type missmatch, expecting one of {self.types} but "
                             f"got {type(current_node).__name__} instead")
            return False

        lineno = getattr(current_node, "lineno", None)

        code_node = current_node
        count = 0
        while count < self.low:
            if code_node is None or not self.check_type(code_node):
                return False

            code_node = matcher.code_walker.next_sibling()
            count += 1

        pattern_node = matcher.pattern_walker.next()
        if pattern_node is None:
            code_node = matcher.code_walker.next_sibling()
            if matcher.strict and code_node is not None:
                return False

            code_node = matcher.code_walker.next_parent()
            if matcher.strict and code_node is not None:
                return False

            if hasattr(current_node, "lineno"):
                matcher.pattern_match.add_pattern_match(current_node.lineno, self)
            return matcher.count_and_return()

        if code_node is None:
            matcher.code_walker.select_specific_child("")
            code_node = matcher.code_walker.next()
            return self._recursive_match(pattern_node, code_node, matcher, lineno)

        while count <= self.high:
            # if not self.check_type(code_node):
            #     return False

            if self._recursive_match(pattern_node, code_node, matcher, lineno):
                return matcher.count_and_return()

            code_node = matcher.code_walker.next_sibling()
            count += 1

        return False


class AnyWildcard(AstPyttern):
    """AnyWildcard class is responsible for matching the "?*" wildcard."""
    def __str__(self):
        return 'ANY*'

    def visit(self, matcher, current_node):
        next_pattern_node = matcher.pattern_walker.next_sibling()
        # while isinstance(next_pattern_node, AnyWildcard):
        #    next_pattern_node = matcher.pattern_walker.next_sibling()

        lineno = getattr(current_node, "lineno", None)

        if next_pattern_node is None:

            # We cannot juste skip, we have to check every type inside
            if self.types is not None:
                if not self.check_type(current_node):
                    return False
                current_node = matcher.code_walker.next_sibling()
                while current_node is not None:
                    if not self.check_type(current_node):
                        return False
                    current_node = matcher.code_walker.next_sibling()

            next_pattern_node = matcher.pattern_walker.next()
            next_code_node = matcher.code_walker.next_parent()

            if next_pattern_node is None:
                if next_code_node is None or not matcher.strict:
                    if lineno and lineno not in matcher.pattern_match.pattern_match:
                        matcher.pattern_match.add_pattern_match(lineno, self)
                    return matcher.count_and_return()
                return False
            if (lineno and lineno not in matcher.pattern_match.pattern_match
                    and next_code_node is not None):
                matcher.pattern_match.add_pattern_match(lineno, self)
                end_lineno = next_code_node.lineno - 1
                if lineno != end_lineno:
                    matcher.pattern_match.add_line_skip_match(lineno, end_lineno)
            return matcher.rec_match(next_pattern_node, next_code_node)

        code_node = current_node
        while code_node is not None:
            if not self.check_type(code_node):
                return False

            if self._recursive_match(next_pattern_node, code_node, matcher, lineno):
                return matcher.count_and_return()

            code_node = matcher.code_walker.next_sibling()

        return False


class ContainerWildcard(AstPyttern):
    """ContainerWildcard class is responsible for matching the "<>" wildcard. Still [WIP]"""
    def __init__(self, values, types=None):
        super().__init__(types)
        self.values = values
        self._fields = ['values']

    def visit(self, matcher, current_node):
        if not self.check_type(current_node):
            return False

        from .matcher import Matcher
        from .ast_walker import ast_walker

        matcher.code_walker.select_specific_child("")
        matcher.code_walker.next()
        code_walker = ast_walker(current_node)

        while current_node is not None:
            sub_matcher = Matcher()
            sub_matcher.variables = matcher.variables
            if sub_matcher.match(self.values, current_node):
                return matcher.count_and_return()
            current_node = code_walker.next()

        return False

    def __str__(self):
        return f"Contains {self.values}"


class BodyWildcard(AstPyttern):
    """BodyWildcard class is responsible for matching the "?:" wildcard."""
    def __init__(self, body, types=None, low=1, high=1):
        super().__init__(types)
        self.body = body
        self._fields = ['body']
        self.low = low
        self.high = high

    def __str__(self):
        return 'ANY:'

    def _get_next_body(self, matcher, current_node):
        while not has_body_elements(current_node) or not self.check_type(current_node):
            current_node = matcher.code_walker.next_sibling()
            if current_node is None:
                return None
        return current_node

    def _recursive_visit(self, matcher, current_node, next_pattern_node, depth):
        if depth >= self.high:
            return False

        matcher.save_walkers_state()
        matcher.code_walker.select_body_children()
        next_code_node = matcher.code_walker.next_child()
        if next_code_node is None:
            matcher.drop_walkers_state()
            return False
        # next_pattern_node = matcher.pattern_walker.next()
        if matcher.rec_match(next_pattern_node, next_code_node):
            matcher.drop_walkers_state()
            return matcher.count_and_return()

        if hasattr(current_node, "lineno"):
            matcher.pattern_match.add_pattern_match(current_node.lineno, self)
        matcher.pattern_match.match(current_node, self)

        if self._recursive_visit(matcher, next_code_node, next_pattern_node, depth + 1):
            matcher.drop_walkers_state()
            return matcher.count_and_return()

        matcher.load_walkers_state()
        next_code_node = self._get_next_body(matcher, next_code_node)
        if next_code_node is None:
            return False

        return self._recursive_visit(matcher, next_code_node, next_pattern_node, depth + 1)

    def visit(self, matcher, current_node):
        # matcher.pattern_match.add_match(self, current_node)
        count = 0
        if not self.check_type(current_node):
            return False

        while count < self.low - 1:
            current_node = self._get_next_body(matcher, current_node)
            if current_node is None:
                return False

            matcher.code_walker.select_specific_child("body")
            current_node = matcher.code_walker.next_child()
            if current_node is None:
                return False

            count += 1

        next_pattern_node = matcher.pattern_walker.next()
        return self._recursive_visit(matcher, current_node, next_pattern_node, count)


class VarWildcard(AstPyttern):
    """VarWildcard class is responsible for matching the "?var" wildcard."""
    def __init__(self, name, types=None):
        super().__init__(types)
        self.name = name
        self._fields = ['name']

    def __str__(self):
        return f"ANY but same as other {self.name}"

    def visit(self, matcher, current_node):
        if self.name in matcher.variables:
            pattern_node = matcher.variables[self.name]
            from .matcher import Matcher
            if not Matcher().match(pattern_node, current_node):
                return False
            if hasattr(current_node, "lineno"):
                matcher.pattern_match.add_pattern_match(current_node.lineno, self)
            matcher.pattern_match.match(current_node, self)

            pattern_node = matcher.pattern_walker.next_sibling()
            if pattern_node is None:
                code_node = matcher.code_walker.next_sibling()
                if matcher.strict and code_node is not None:
                    return False

                code_node = matcher.code_walker.next_parent()
                if matcher.strict and code_node is not None:
                    return False

                if hasattr(current_node, "lineno"):
                    matcher.pattern_match.add_pattern_match(current_node.lineno, self)
                return matcher.count_and_return()

            code_node = matcher.code_walker.next_sibling()
            if code_node is None:
                code_node = matcher.code_walker.next_parent()
                if code_node is None:
                    return False

            return matcher.rec_match(pattern_node, code_node)

        # Handle func name and class name
        if not isinstance(current_node, AST):
            current_node = Name(current_node, Load())

        # Handle arguments
        if isinstance(current_node, ast.arg):
            current_node = Name(current_node.arg, Load())

        if not self.check_type(current_node):
            return False

        matcher.variables[self.name] = current_node

        next_pattern_node = matcher.pattern_walker.next_sibling()
        if next_pattern_node is None:
            next_pattern_node = matcher.pattern_walker.next_parent()
            if next_pattern_node is None:
                next_code_node = matcher.code_walker.next_sibling()
                if next_code_node is None:
                    return matcher.count_and_return()
                next_code_node = matcher.code_walker.next_parent()
                if next_code_node is None:
                    return matcher.count_and_return()
                return False
            else:
                next_code_node = matcher.code_walker.next_parent()
        else:
            next_code_node = matcher.code_walker.next_sibling()

        if not matcher.rec_match(next_pattern_node, next_code_node):
            del matcher.variables[self.name]
            return False

        if hasattr(current_node, "lineno"):
            matcher.pattern_match.add_pattern_match(current_node.lineno, self)
        matcher.pattern_match.match(current_node, self)
        return matcher.count_and_return()


class AnyBodyWildcard(AstPyttern):
    """AnyBodyWildcard class is responsible for matching the "?:*" wildcard."""
    def __init__(self, body, types=None):
        super().__init__(types)
        self.body = body
        self._fields = ['body']

    def __str__(self):
        return "ANY Depth"

    def visit(self, matcher, current_node):
        next_pattern_node = matcher.pattern_walker.next()
        if next_pattern_node is None:
            return False

        code_node = current_node
        lineno = code_node.lineno if hasattr(code_node, "lineno") else None
        #if not has_body_elements(code_node):
        #    return False
        if not self.check_type(code_node):
            return False

        while code_node is not None:
            if self._recursive_match(next_pattern_node, code_node, matcher, lineno):
                return matcher.count_and_return()

            matcher.code_walker.select_body_children()
            code_node = matcher.code_walker.next()

        return False


class StrictMode(AstPyttern):
    """StrictMode class is responsible for matching the "?![]" wildcard."""
    def __init__(self, body, enable):
        super().__init__()
        self.body = body
        self._fields = ['body']
        self.enable = enable

    def __str__(self):
        return "STRICT"

    def visit(self, matcher, current_node):
        matcher.set_strict(self.enable)
        next_pattern_node = matcher.pattern_walker.next()
        if next_pattern_node is None:
            return matcher.count_and_return()
        if not matcher.rec_match(next_pattern_node, current_node):
            matcher.set_strict(not self.enable)
            return False
        return matcher.count_and_return()


# Static methods #

def has_body_elements(node):
    """:return: True if the node has body elements, False otherwise."""
    for (_, value) in iter_fields(node):
        if isinstance(value, list):
            if len(value) > 0 and isinstance(value[0], ast.stmt):
                return True
    return False


def iter_child_nodes(node):
    """
    Yield all direct child nodes of *node*, that is, all fields that are nodes
    and all items of fields that are lists of nodes.
    """
    for _, field in iter_fields(node):
        if isinstance(field, list):
            for item in field:
                if isinstance(item, AST):
                    yield item
                elif isinstance(item, AstPyttern):
                    yield item
        elif field is not None:
            yield field


def iter_constant_field(node):
    """
    Yield all direct child nodes of *node*, that is, all fields that are constants
    """
    for _, field in iter_fields(node):
        if isinstance(field, SimpleWildcard) or not isinstance(field, (AST, AstPyttern, list)):
            if field is not None:
                yield field


def iter_fields(node):
    """
    Yield a tuple of ``(fieldname, value)`` for each field in ``node._fields``
    that is present on *node*.
    """
    if not hasattr(node, "_fields"):
        return
    for field in node._fields:
        try:
            yield field, getattr(node, field)
        except AttributeError:
            print(f"No such attribute: {field} in {node} with attributes: {node.__dict__}")

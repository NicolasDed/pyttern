import ast
from ast import AST, Name, Load


class PytternAST:
    def __init__(self, types=None):
        self._attributes = ["lineno", "lineno_end"]
        self._fields = []
        self.lineno = None
        self.lineno_end = None
        self.types = types
        if types is not None and type(types) is not list:
            raise ValueError(f"Argument types should be of type list not {type(types)}.")

    def __str__(self):
        return type(self).__name__

    def __repr__(self):
        return repr(self.__str__())

    def visit(self, matcher, current_node):
        raise NotImplementedError()

    def check_type(self, node):
        if self.types is None:
            return True
        return f"{type(node).__name__}" in self.types


class SimpleWildcard(PytternAST):
    def __str__(self):
        return 'ANY'

    def visit(self, matcher, current_node):
        if not self.check_type(current_node):
            matcher.error = (f"Type missmatch, expecting one of {self.types} but got {type(current_node).__name__} "
                             f"instead")
            return False

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
            return True

        code_node = matcher.code_walker.next_sibling()
        if code_node is None:
            code_node = matcher.code_walker.next_parent()
            if code_node is None:
                return False

        if hasattr(current_node, "lineno"):
            matcher.pattern_match.add_pattern_match(current_node.lineno, self)
        matcher.pattern_match.match(code_node, self)
        return matcher.rec_match(pattern_node, code_node)


class AnyWildcard(PytternAST):
    def __str__(self):
        return 'ANY*'

    def visit(self, matcher, current_node):
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
            else:
                if lineno and lineno not in matcher.pattern_match.pattern_match and next_code_node is not None:
                    matcher.pattern_match.add_pattern_match(lineno, self)
                    end_lineno = next_code_node.lineno - 1
                    if lineno != end_lineno:
                        matcher.pattern_match.add_line_skip_match(lineno, end_lineno)
                return matcher.rec_match(next_pattern_node, next_code_node)

        code_node = current_node
        while code_node is not None:
            if not self.check_type(code_node):
                return False

            matcher.save_walkers_state()
            if matcher.rec_match(next_pattern_node, code_node):
                end_lineno = code_node.lineno
                if end_lineno != lineno:
                    matcher.pattern_match.add_line_skip_match(lineno, end_lineno - 1)
                return True
            matcher.load_walkers_state()
            matcher.pattern_match.match(code_node, self)
            if lineno and lineno not in matcher.pattern_match.pattern_match:
                matcher.pattern_match.add_pattern_match(lineno, self)
            code_node = matcher.code_walker.next_sibling()

        return False


class BodyWildcard(PytternAST):
    def __init__(self, body, types=None):
        super().__init__(types)
        self.body = body
        self._fields = ['body']

    def __str__(self):
        return 'ANY:'

    def visit(self, matcher, current_node):
        # matcher.pattern_match.add_match(self, current_node)
        if not self.check_type(current_node):
            return False

        matcher.code_walker.select_specific_child('body')
        next_code_node = matcher.code_walker.next_child()
        if next_code_node is None:
            return False
        next_pattern_node = matcher.pattern_walker.next()
        if not matcher.rec_match(next_pattern_node, next_code_node):
            return False
        if hasattr(current_node, "lineno"):
            matcher.pattern_match.add_pattern_match(current_node.lineno, self)
        matcher.pattern_match.match(current_node, self)
        return True


class VarWildcard(PytternAST):
    def __init__(self, name, types=None):
        super().__init__(types)
        self.name = name
        self._fields = ['name']

    def __str__(self):
        return f"ANY but same as other {self.name}"

    def visit(self, matcher, current_node):
        if self.name in matcher.variables:
            pattern_node = matcher.variables[self.name]
            from .Matcher import Matcher
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
                return True

            code_node = matcher.code_walker.next_sibling()
            if code_node is None:
                code_node = matcher.code_walker.next_parent()
                if code_node is None:
                    return False

            return matcher.rec_match(pattern_node, code_node)

        # Handle func name and class name
        if not isinstance(current_node, AST):
            current_node = Name(current_node, Load())

        if not self.check_type(current_node):
            return False

        matcher.variables[self.name] = current_node

        next_pattern_node = matcher.pattern_walker.next_sibling()
        if next_pattern_node is None:
            next_code_node = matcher.code_walker.next_sibling()
            if next_code_node is None:
                return True
            else:
                next_code_node = matcher.code_walker.next_parent()
                if next_code_node is None:
                    return True
                else:
                    return False

        next_code_node = matcher.code_walker.next_sibling()

        if not matcher.rec_match(next_pattern_node, next_code_node):
            del matcher.variables[self.name]
            return False

        if hasattr(current_node, "lineno"):
            matcher.pattern_match.add_pattern_match(current_node.lineno, self)
        matcher.pattern_match.match(current_node, self)
        return True


class AnyBodyWildcard(PytternAST):
    def __init__(self, body, types=None):
        super().__init__(types)
        self.body = body
        self._fields = ['body']

    def __str__(self):
        return f"ANY Depth"

    def visit(self, matcher, current_node):
        next_pattern_node = matcher.pattern_walker.next()
        if next_pattern_node is None:
            return False

        code_node = current_node
        lineno = code_node.lineno if hasattr(code_node, "lineno") else None
        if not has_body_elements(code_node):
            return False
        while code_node is not None:
            if not self.check_type(code_node):
                return False

            matcher.save_walkers_state()
            if matcher.rec_match(next_pattern_node, code_node):
                end_lineno = code_node.lineno
                if end_lineno != lineno:
                    matcher.pattern_match.add_line_skip_match(lineno, end_lineno - 1)
                return True
            matcher.load_walkers_state()
            if lineno and lineno not in matcher.pattern_match.pattern_match:
                matcher.pattern_match.add_pattern_match(lineno, self)
            matcher.pattern_match.match(code_node, self)
            matcher.code_walker.select_body_children()
            code_node = matcher.code_walker.next()

        return False


class StrictMode(PytternAST):
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
            return True
        if not matcher.rec_match(next_pattern_node, current_node):
            matcher.set_strict(not self.enable)
            return False
        return True


# Static methods #

def has_body_elements(node):
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
                elif isinstance(item, PytternAST):
                    yield item
        elif field is not None:
            yield field


def iter_constant_field(node):
    for name, field in iter_fields(node):
        if isinstance(field, SimpleWildcard) or not (
                isinstance(field, AST) or isinstance(field, PytternAST) or isinstance(field, list)):
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
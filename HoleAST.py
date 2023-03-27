from ast import AST


class HoleAST:
    def __init__(self):
        self._fields = []

    def __str__(self):
        return type(self).__name__

    def __repr__(self):
        return repr(self.__str__())

    def visit(self, matcher, current_node):
        raise NotImplementedError()


class SimpleHole(HoleAST):
    def __str__(self):
        return 'ANY'

    def visit(self, matcher, current_node):
        pattern_node = matcher.pattern_walker.next()
        if pattern_node is None:
            code_node = matcher.code_walker.next_sibling()
            if code_node is not None:
                return False

            code_node = matcher.code_walker.next_parent()
            if code_node is not None:
                return False

            return True

        code_node = matcher.code_walker.next_sibling()
        if code_node is None:
            code_node = matcher.code_walker.next_parent()
            if code_node is None:
                return False

        return matcher.rec_match(pattern_node, code_node)


class DoubleHole(HoleAST):
    def __str__(self):
        return 'ANY*'

    def visit(self, matcher, current_node):
        next_pattern_node = matcher.pattern_walker.next_sibling()
        while isinstance(next_pattern_node, DoubleHole):
            next_pattern_node = matcher.pattern_walker.next_sibling()

        if next_pattern_node is None:
            next_pattern_node = matcher.pattern_walker.next()
            next_code_node = matcher.code_walker.next_parent()
            if next_pattern_node is None:
                if next_code_node is None:
                    return True
                else:
                    return False
            else:
                return matcher.rec_match(next_pattern_node, next_code_node)

        code_node = current_node
        while code_node is not None:
            matcher.save_walkers_state()
            if matcher.rec_match(next_pattern_node, code_node):
                return True
            matcher.load_walkers_state()
            code_node = matcher.code_walker.next_sibling()

        return False


class CompoundHole(HoleAST):
    def __init__(self, body=None):
        super().__init__()
        self.body = body
        self._fields = ['body']

    def __str__(self):
        return 'ANY:'

    def visit(self, matcher, current_node):
        matcher.code_walker.select_specific_child('body')
        return matcher.simple_match()


class VarHole(HoleAST):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._fields = ['name']

    def __str__(self):
        return f"ANY but same as other {self.name}"

    def visit(self, matcher, current_node):
        if self.name in matcher.variables:
            pattern_node = matcher.variables[self.name]
            from Matcher import Matcher
            return Matcher().match(pattern_node, current_node)

        matcher.variables[self.name] = current_node

        next_pattern_node = matcher.pattern_walker.next()
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

        return True

class MultipleCompoundHole(HoleAST):
    def __init__(self, body):
        super().__init__()
        self.body = body
        self._fields = ['body']

    def visit(self, matcher, current_node):
        return False



# Static methods #

def walk(node):
    """
    Recursively yield all descendant nodes in the tree starting at *node*
    (including *node* itself), in no specified order.  This is useful if you
    only want to modify nodes in place and don't care about the context.
    """
    from collections import deque
    todo = deque([node])
    while todo:
        node = todo.popleft()
        # todo.extend(iter_child_nodes(node))
        to_add = list(iter_child_nodes(node))
        to_add.reverse()
        todo.extendleft(to_add)
        yield node


def iter_child_nodes(node):
    """
    Yield all direct child nodes of *node*, that is, all fields that are nodes
    and all items of fields that are lists of nodes.
    """
    for name, field in iter_fields(node):
        if isinstance(field, AST):
            yield field
        elif isinstance(field, HoleAST):
            yield field
        elif isinstance(field, list):
            for item in field:
                if isinstance(item, AST):
                    yield item
                elif isinstance(item, HoleAST):
                    yield item


def iter_constant_field(node):
    for name, field in iter_fields(node):
        if not (isinstance(field, AST) or isinstance(field, HoleAST) or isinstance(field, list)):
            if field is not None:
                yield field


def iter_fields(node):
    """
    Yield a tuple of ``(fieldname, value)`` for each field in ``node._fields``
    that is present on *node*.
    """
    for field in node._fields:
        try:
            yield field, getattr(node, field)
        except AttributeError:
            print("No such attribute")

"""
Module for keeping match details.
"""

from .astpyttern import AstPyttern


class PatternMatch:
    """
    Class responsible for keeping match details.
    """
    def __init__(self):
        """
        Constructor for PatternMatch class.
        """
        self.matches = []
        self.line_skip_matches = {}
        self.pattern_match = {}
        self.links: list[Link] = []

    def add_match(self, pattern, code):
        """Add a match to the list of matches."""
        self.matches.append((pattern, code))

    def add_line_skip_match(self, start, end):
        """Add a line skip match to the list of line skip matches."""
        self.line_skip_matches[start] = end

    def add_pattern_match(self, line, pattern):
        """Add a pattern match to the list of pattern matches."""
        self.pattern_match[line-1] = pattern

    def match(self, code, pattern):
        """Links a code node to a pattern node."""
        self.links.append(Link(code, pattern))

    def __str__(self):
        return f'[{",".join(str(s) for s in self.links)}]'


class Link:
    """Class responsible for keeping the link between a code node and a pattern node."""
    def __init__(self, code_node, pattern_node):
        """Constructor for Link class."""
        self._code_node = code_node
        self._pattern_node = pattern_node

    @property
    def code_node(self):
        """Getter for code node."""
        return self._code_node

    @property
    def pattern_node(self):
        """Getter for pattern node."""
        return self._pattern_node

    @property
    def code_line(self):
        """Getter for code line."""
        if hasattr(self._code_node, "lineno"):
            return self._code_node.lineno
        return None

    @property
    def pattern_line(self):
        """Getter for pattern line."""
        if hasattr(self._pattern_node, "lineno"):
            return self._pattern_node.lineno
        return None

    def __str__(self):
        if isinstance(self._pattern_node, AstPyttern):
            return f"({type(self._code_node).__name__}, {self._pattern_node})"

        return f"({type(self._code_node).__name__}, {type(self._pattern_node).__name__})"

    def __repr__(self):
        return repr(str(self))

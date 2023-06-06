class PatternMatch:
    def __init__(self):
        self.matches = []
        self.line_skip_matches = []
        self.pattern_match = {}

    def add_match(self, pattern, code):
        self.matches.append((pattern, code))

    def add_line_skip_match(self, pattern, code):
        self.line_skip_matches.append((pattern, code))

    def add_pattern_match(self, line, pattern):
        self.pattern_match[line-1] = pattern

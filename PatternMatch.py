class PatternMatch:
    def __init__(self):
        self.matches = []
        self.line_skip_matches = []

    def add_match(self, pattern, code):
        self.matches.append((pattern, code))

    def add_line_skip_match(self, pattern, code):
        self.line_skip_matches.append((pattern, code))

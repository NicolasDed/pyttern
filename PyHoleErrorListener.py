from antlr4.error.ErrorListener import ErrorListener


class Python3ErrorListener(ErrorListener):
    def __init__(self, output):
        self.output = output
        self._symbol = ''

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        self.output.write(msg)
        self._symbol = offending_symbol.text
        stack = recognizer.getRuleInvocationStack()
        stack.reverse()
        print("rule stack: {}".format(str(stack)))
        print("line {} : {} at {} : {}".format(str(line),
                                               str(column),
                                               str(offending_symbol).replace(" ", u'\u23B5'),
                                               msg.replace(" ", u'\u23B5')))

    @property
    def symbol(self):
        return self._symbol

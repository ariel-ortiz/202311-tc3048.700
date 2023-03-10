from arpeggio import PTNodeVisitor


class SemanticMistake(Exception):

    def __init__(self, message):
        super().__init__(f'Semantic error: {message}')


class SemanticVisitor(PTNodeVisitor):

    MAX_INT32_VALUE = 2 ** 31 - 1

    def __init__(self, parser, **kwargs):
        super().__init__(**kwargs)
        self.__parser = parser

    def position(self, node):
        return self.__parser.pos_to_linecol(node.position)

    def visit_decimal(self, node, children):
        value = int(node.value)
        if value > SemanticVisitor.MAX_INT32_VALUE:
            raise SemanticMistake(
                'Out of range decimal integer literal at position '
                f'{self.position(node)} => {value}'
            )

from arpeggio import PTNodeVisitor


class SemanticMistake(Exception):

    def __init__(self, message):
        super().__init__(f'Semantic error: {message}')


class SemanticVisitor(PTNodeVisitor):

    def __init__(self, parser, **kwargs):
        super().__init__(**kwargs)
        self.__parser = parser

    def position(self, node):
        return self.__parser.pos_to_linecol(node.position)

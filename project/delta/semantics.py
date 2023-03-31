from arpeggio import PTNodeVisitor


class SemanticMistake(Exception):

    def __init__(self, message):
        super().__init__(f'Semantic error: {message}')


class SemanticVisitor(PTNodeVisitor):

    MAX_INT32_VALUE = 2 ** 31 - 1

    def __init__(self, parser, **kwargs):
        super().__init__(**kwargs)
        self.__parser = parser
        self.__symbol_table = []

    def position(self, node):
        return self.__parser.pos_to_linecol(node.position)

    @property
    def symbol_table(self):
        return self.__symbol_table

    def visit_decimal(self, node, _):
        value = int(node.value)
        if value > SemanticVisitor.MAX_INT32_VALUE:
            raise SemanticMistake(
                'Out of range decimal integer literal at position '
                f'{self.position(node)} => {value}'
            )

    def visit_decl_variable(self, node, _):
        if node.value in self.__symbol_table:
            raise SemanticMistake(
                'Duplicate variable declaration at position '
                f'{self.position(node)} => {node.value}'
            )
        else:
            self.__symbol_table.append(node.value)

    def visit_lhs_variable(self, node, _):
        if node.value not in self.__symbol_table:
            raise SemanticMistake(
                'Assignment to undeclared variable at position '
                f'{self.position(node)} => {node.value}'
            )

    def visit_rhs_variable(self, node, children):
        if node.value not in self.__symbol_table:
            raise SemanticMistake(
                'Undeclared variable reference at position '
                f'{self.position(node)} => {node.value}'
            )

from arpeggio import PTNodeVisitor


class CodeGenerationVisitor(PTNodeVisitor):

    WAT_TEMPLATE = ''';; Code generated by the Delta compiler
(module
  (func
    (export "_start")
    (result i32)
{}  )
)
'''

    def __init__(self, symbol_table, **kwargs):
        super().__init__(**kwargs)
        self.__symbol_table = symbol_table

    def visit_expression_start(self, _, children):
        return CodeGenerationVisitor.WAT_TEMPLATE.format(children[0])

    def visit_decimal(self, node, _):
        return f'    i32.const {node.value}\n'

    def visit_boolean(self, node, children):
        if children[0] == 'true':
            return f'    i32.const 1\n'
        else:
            return f'    i32.const 0\n'

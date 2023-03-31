from delta import Compiler, Phase

source = '''
var x, y, z, w;
w = 4;
x = 1 + w;
x
'''

c = Compiler('program_start')
c.realize(source, Phase.CODE_GENERATION)
print(c.parse_tree_str)
print()
print(c.symbol_table)
print()
print(c.wat_code)
print()
print(c.result)

from delta import Compiler, Phase

source = '(1 + 2) * 3'

c = Compiler('expression_start')
c.realize(source, Phase.CODE_GENERATION)
print(c.parse_tree_str)
print()
print(c.wat_code)
# print()
# print(c.result)

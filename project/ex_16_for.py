from delta import Compiler, Phase

source = '''
var r, i;
r = 1;
for i = 1 upto 5 {
    r = r * i;
}
r
'''

c = Compiler('program_start')
c.realize(source, Phase.EVALUATION)
# print(c.parse_tree_str)
# print()
# print(c.symbol_table)
# print()
print(c.wat_code)
print()
print(c.result)

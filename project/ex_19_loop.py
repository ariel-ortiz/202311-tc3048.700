from delta import Compiler, Phase

source = '''
var n, r, i;
n = 5;
r = 1;
i = 0;
loop {
    i = i + 1;
    exit when !((n + 1) - i);
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

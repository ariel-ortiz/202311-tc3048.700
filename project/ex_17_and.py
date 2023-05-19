from delta import Compiler, Phase

source = '''
var x, y;
x = 10;
y = x && 100/x && 30 && 40;
/* if x {
  if 100 / x {
    if 30 {
      if 40 {
        y = true;
      } else {
        y = false;
      }
    } else {
      y = false;
    }
  } else {
    y = false;
  }
} else {
  y = false;
} */
y
'''

c = Compiler('program_start')
c.realize(source, Phase.EVALUATION)
# print(c.parse_tree_str)
# print()
# print(c.symbol_table)
# print()
# print(c.wat_code)
# print()
print(c.result)

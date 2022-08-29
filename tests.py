from BrainFuck import *

with open("code.bf") as f:
    code = f.read()

interpreter = Interpreter(30000, 255)
interpreter.interpret(code)
with open("result.txt") as res:
    assert list(map(int, res)) == [3, 23, 27, 47, 52, 244, 253]

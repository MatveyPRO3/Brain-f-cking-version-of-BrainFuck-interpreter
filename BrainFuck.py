class Interpreter():

    #  Local variables
    #  here is an empty place because there is no unchangeable vars
    #  there are only some vars with default values but you can change them

    def __init__(self, memory_limit, cell_value_limit, memory=[], current_cell=0) -> None:
        self.ribbon_limit = memory_limit
        self.cell_value_limit = cell_value_limit
        self.memory = memory
        self.current_cell = current_cell
        with open("result.txt", "w"):pass

    def interpret(self, code):

        #  preparing string for interpretering
        code = code.replace(" ", "")
        code = code.replace("\n", "")

        for i, j in zip(code, range(0, len(code)+1)):
            if i == ">":
                if self.current_cell == self.ribbon_limit-1:
                    self.current_cell = 0
                else:
                    self.current_cell += 1
            elif i == "<":
                if self.current_cell == 0:
                    self.current_cell = self.ribbon_limit
                else:
                    self.current_cell -= 1
            elif i == "+":
                try:
                    if self.memory[self.current_cell] == self.cell_value_limit:
                        self.memory[self.current_cell] = 0
                    else:
                        self.memory[self.current_cell] += 1
                except:
                    self.memory.extend(
                        [0]*(self.current_cell-len(self.memory))+[1])
            elif i == "-":
                try:
                    if self.memory[self.current_cell] == 0:
                        self.memory[self.current_cell] = self.cell_value_limit
                    else:
                        self.memory[self.current_cell] -= 1
                except:
                    self.memory.extend(
                        [0]*(self.current_cell-len(self.memory))+[self.cell_value_limit])
            elif i == ".":
                with open("result.txt", "a") as res:
                    try:
                        res.write(str(self.memory[self.current_cell])+"\n")
                        print(self.memory[self.current_cell])
                    except:
                        res.write(str(0)+"\n")
                        print(0)
            elif i == "[":
                len_loop_code = 0
                opened_brackets = 1
                for x in code[j+1:]:
                    if x == "[":
                        opened_brackets += 1
                        len_loop_code += 1
                    elif x == "]":
                        opened_brackets -= 1
                        if opened_brackets == -1:
                            raise SyntaxError("Incorrect brackets order!")
                        if opened_brackets == 0:
                            break
                        else:
                            len_loop_code += 1
                    else:
                        len_loop_code += 1
                else:
                    raise SyntaxError("Incorrect brackets order!")
                try:
                    current_cell_value = self.memory[self.current_cell]
                except:
                    current_cell_value = 0
                while current_cell_value != 0:
                    self.interpret(code[j+1:j+1+len_loop_code])
                    try:
                        current_cell_value = self.memory[self.current_cell]
                    except:
                        current_cell_value = 0
                self.interpret(code[j+1+len_loop_code+1:])
                break
            elif i == "]":
                raise SyntaxError("Incorrect brackets order!")
            else:
                raise SyntaxError(f"Unknown symbol: {i}!")

    def __str__(self) -> str:
        return str(self.memory)


if __name__ == '__main__':
    interpreter = Interpreter(4, 255, memory=[0, 0, 0, 0])
    interpreter.interpret(input())
    print(interpreter)  # debug

from Types import Types

class REPL:
    def __init__(self):
        self.types = Types()
    
    def start(self):
        self.__loop()
    
    def __loop(self):
        while True:
            input = (self.__read()).strip()
            
            if input == "":
                continue

            output = self.eval(input)
            if output:
                print(output)

    def __read(self):
        try:
            return input("> ")
        except (KeyboardInterrupt, EOFError) as e:
            print("\n", end='')
            self.__exit()

    def eval(self, input):
        try:
            return self.__eval_repl_command(input)
        except Exception as e:
            return "ERROR: {} ==> {}".format(input, e)

    def __eval_repl_command(self, input):
        command, input = self.__extract_command_from_input(input)

        if command == "SALIR":
            self.__exit()

        try:
            return {
                "ATOMICO": self.types.addAtomic,
                "STRUCT": self.types.addStruct,
                "ARREGLO": self.types.addArray,
                "DESCRIBIR": self.types.describe
            }[command](input)
        except KeyError:
            return 'ERROR: {} is not recognized as a command'.format(command)

    def __extract_command_from_input(self, input):
        split_input = input.split(" ")
        
        return split_input[0], " ".join(split_input[1:])

    def __exit(self):
        print("Hasta luego!")
        exit()

if __name__ == "__main__":
    (REPL()).start()
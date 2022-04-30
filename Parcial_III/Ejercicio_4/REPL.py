from VirtualMethodsSystem import VirtualMethodsSystem

class REPL:
    def __init__(self):
        self.system = VirtualMethodsSystem()
    
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
                "CLASS": self.system.add_class,
                "DESCRIBIR": self.system.describe
            }[command](*input)
        except KeyError:
            return 'ERROR: no se reconoce como comando {}'.format(command)

    def __extract_command_from_input(self, input):
        name = ""
        methods = []
        super_class_name = None
        command = ""

        if input.find(":") != -1:
            split = input.split(":")
            first_half = split[0].strip(" ").split(" ")
            second_half = split[1].strip(" ").split(" ")

            if len(first_half) == 2:
                command = first_half[0]
                name = first_half[1]
            
            if len(second_half) > 0:
                super_class_name = second_half[0]
                methods = second_half[1:]

        else:
            split = input.split(" ")      

            if len(split) == 1:    
                command = split[0]
            if len(split) == 2:
                command, name = split
            if len(split) >  3:
                command, name, *methods = split

        
        return command, [name, methods, super_class_name]

    def __exit(self):
        print("Hasta luego!")
        exit()

if __name__ == "__main__":
    (REPL()).start()
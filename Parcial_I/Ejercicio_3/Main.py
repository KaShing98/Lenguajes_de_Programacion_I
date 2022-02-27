from BuddySystem import BuddySystem

def main():
    
    while True:
        value = input('Enter memory size: ')
        try:
            value = int(value)
            if (not (value & (value-1) == 0) or value == 0):
                raise ValueError
            else:
                break
        except ValueError:
            print('Valid number (power of 2), please')
            continue

    bs = BuddySystem(value)

    actions = {
        "RESERVAR": bs.Reservar,
        "LIBERAR": bs.Liberar,
        "MOSTRAR": bs.Mostrar
    }

    while True:
        print('\n')
        value = input('>')
        value = value.split(" ")

        if len(value) < 1:
            continue

        if value[0] in actions:
            args =  value[1: len(value)] if (len(value) > 1 ) else []
            text = actions[value[0]](*args)

            if (isinstance(text,str)):
                print(text)
        else:
            if value[0] == "SALIR":
                break

if __name__ == '__main__':
    main() 
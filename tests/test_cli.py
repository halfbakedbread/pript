from pript import pript

from test_unit import draw_unit, test_data
from test_flag import draw_flag
from test_receipt import draw_receipt


def draw_cli():
    state = 0
    while True:
        # In state 0 the program draws the menu
        if state == 0:
            pript(sep='=')
            pript(' PRIPT CLI TEST MENU ', sep='-', pos='center')
            pript(sep='=')
            pript('Command', '/', ' Description')
            pript(sep='=')
            pript('unit ', ' Run unit tests', sep='.')
            pript('flag ', ' Draw a flag', sep='.')
            pript('receipt ', ' Print a receipt', sep='.')
            pript('exit ', ' Exit the program', sep='.')
            pript(sep='=')
            pript()
            state = 1
        if state == 1 or state == 2:
            command = input('Prompt: ')
            # In state 1 the program expects a valid input
            if state == 1:
                if command == 'unit':
                    draw_unit(test_data)
                    state = 4
                elif command == 'flag':
                    draw_flag()
                    state = 4
                elif command == 'receipt':
                    draw_receipt()
                    state = 4
                # Using 'start' in the main menu is not valid
                elif command == 'start':
                    state = 3
                elif command == 'exit':
                    state = 4
                else:
                    state = 3
            # In state 2 the program comes from an error
            elif state == 2:
                if command == 'start':
                    state = 0
                elif command == 'exit':
                    state = 4
                else:
                    state = 3
        # In state 3 the program has encountered an error
        if state == 3:
            pript(sep='=')
            pript('| ERROR ',   ' INVALID COMMAND |', sep=' ')
            pript('| ', ' |', sep='-')
            pript('| Type "start" to go', 'back to the menu  |')
            pript('| Type "exit" to lea', 've the tests       |')
            pript(sep='=')
            pript()
            state = 2
        # In state 4 exit the program
        if state == 4:
            break


if __name__ == '__main__':
    draw_cli()

import tempfile

from pript import pript

test_data = [{
    'name': 'No arguments ',
    'expected': '****************************************',
    'args': [],
    'kwargs': {
        'sep': '*'
    }
}, {
    'name': 'One argument ',
    'expected': 'Hello World!                            ',
    'args': ['Hello World!'],
    'kwargs': {}
}, {
    'name': 'Two arguments ',
    'expected': 'Hello                             World!',
    'args': ['Hello ', ' World!'],
    'kwargs': {}
}, {
    'name': 'Three arguments ',
    'expected': 'Hello            World            Pript!',
    'args': ['Hello ', ' World ', ' Pript!'],
    'kwargs': {}
}, {
    'name': "One arg with sep",
    'expected': 'Hello World! ...........................',
    'args': ['Hello World! '],
    'kwargs': {
        'sep': '.'
    }
}, {
    'name': "Two args with sep",
    'expected': 'Hello *************************** World!',
    'args': ['Hello ', ' World!'],
    'kwargs': {
        'sep': '*'
    }
}, {
    'name': "Three args with sep",
    'expected': 'Hello ---------- World ---------- Pript!',
    'args': ['Hello ', ' World ', ' Pript!'],
    'kwargs': {
        'sep': '-'
    }
}, {
    'name': "One arg with pos start",
    'expected': 'Hello World!                            ',
    'args': ['Hello World!'],
    'kwargs': {
        'pos': 'start'
    }
}, {
    'name': "Two args with pos start",
    'expected': 'Hello                World!             ',
    'args': ['Hello ', ' World!'],
    'kwargs': {
        'pos': 'start'
    }
}, {
    'name': "Three args with pos start",
    'expected': 'Hello  World  Pript!                    ',
    'args': ['Hello ', ' World ', ' Pript!'],
    'kwargs': {
        'pos': 'start'
    }
}, {
    'name': "One arg with pos center ",
    'expected': '              Hello World!              ',
    'args': ['Hello World!'],
    'kwargs': {
        'pos': 'center'
    }
}, {
    'name': "Two args with pos center ",
    'expected': '              Hello  World!             ',
    'args': ['Hello ', ' World!'],
    'kwargs': {
        'pos': 'center'
    }
}, {
    'name': "Three args with pos center ",
    'expected': '           Hello  World  Pript!         ',
    'args': ['Hello ', ' World ', ' Pript!'],
    'kwargs': {
        'pos': 'center'
    }
}, {
    'name': "One arg with pos end ",
    'expected': '                            Hello World!',
    'args': ['Hello World!'],
    'kwargs': {
        'pos': 'end'
    }
}, {
    'name': "Two args with pos end ",
    'expected': '              Hello               World!',
    'args': ['Hello ', ' World!'],
    'kwargs': {
        'pos': 'end'
    }
}, {
    'name': "Three args with pos end ",
    'expected': '                    Hello  World  Pript!',
    'args': ['Hello ', ' World ', ' Pript!'],
    'kwargs': {
        'pos': 'end'
    }
}, {
    'name': "One arg with length 60 ",
    'expected': 'Hello World!                                                ',
    'args': ['Hello World!'],
    'kwargs': {
        'length': 60
    }
}, {
    'name': "Two args with length 60",
    'expected': 'Hello                                                 World!',
    'args': ['Hello ', ' World!'],
    'kwargs': {
        'length': 60
    }
}, {
    'name': "Three args with length 60",
    'expected': 'Hello                      World                      Pript!',
    'args': ['Hello ', ' World ', ' Pript!'],
    'kwargs': {
        'length': 60
    }
}, {
    'name': 'One arg with snip ',
    'expected': 'Helloooooooooooooooo Woooooooooooooooorl',
    'args': ['Helloooooooooooooooo Woooooooooooooooorld!'],
    'kwargs': {
        'snip': True
    }
}, {
    'name': 'One arg with int ',
    'expected': '101                                     ',
    'args': [101],
    'kwargs': {}
}, {
    'name': 'Two args with int and str ',
    'expected': '101                         Hello World!',
    'args': [101, 'Hello World!'],
    'kwargs': {}
}, {
    'name': 'Three args with list and str ',
    'expected': "[101]       ['Pript']       Hello World!",
    'args': [[101], ['Pript'], 'Hello World!'],
    'kwargs': {}
}, {
    'name': 'More than three args ',
    'expected': "[101] ['Pript'] Hello World! ('Hello', 'World', '!')",
    'args': [[101], ['Pript'], 'Hello World!', ('Hello', 'World', '!')],
    'kwargs': {}
}]


def draw_unit(test_data):
    pript(' Starting tests ', sep='-', pos='center', length=60)
    passing = 0
    failing = 0
    with tempfile.NamedTemporaryFile('w+') as temp:
        for i, t in enumerate(test_data):
            pript(*t['args'], **t['kwargs'], file=temp, end="")
            temp.seek(0)
            contents = temp.read()
            try:
                assert contents == t['expected']
                passing += 1
                pript(t['name'], ' Passing ✓', sep='.', length=60)
            except AssertionError as error:
                failing += 1
                pript(t['name'], ' Failing X', sep='.', length=60)
            temp.seek(0)
            temp.truncate(0)
        temp.close()
    pript(' Tests completed ', sep='-', pos='center', length=60)
    pript('Passing: ', ' ' + str(passing) + ' Tests', sep='.', length=60)
    pript('Failing: ', ' ' + str(failing) + ' Tests', sep='.', length=60)


if __name__ == '__main__':
    draw_unit(test_data)

from pript import pript


def draw_flag():
    pript(sep='~')
    for i in range(6):
        if i % 2 == 0:
            pript(' *  ' * 6, '-' * 20)
        else:
            pript('   *' * 4, '~' * 20)
    pript(sep='-')
    for i in range(4):
        if i % 2 == 0:
            pript(sep='~')
        else:
            pript(sep='-')
    pript(sep='~')


if __name__ == '__main__':
    draw_flag()

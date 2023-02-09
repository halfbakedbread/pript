import sys


def pript(*args, sep=' ', end='\n', file=None, flush=False,
          pos=None, length=40, snip=True):
    r"""pript(value, ..., sep=' ', end='\n', file=sys.stdout, 
    flush=False, pos='start', length=40, snip=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    The first three arguments can be formatted in the style of a receipt.
    Optional keyword arguments:
    file:   a file-like object (stream); defaults to the current sys.stdout.
    sep:    string inserted between values, default a space.
    end:    string appended after the last value, default a newline.
    flush:  whether to forcibly flush the stream.
    pos:    alignment of the output. defaults to start and between.
    length: maximum length of the output. defaults to 40 characters.
    snip:   remove excess characters when using a single argument.
    """
    fp = file
    if fp is None:
        fp = sys.stdout
        if fp is None:
            return
    if sep is None:
        sep = ' '
    if not isinstance(sep, str):
        raise TypeError("sep must be None or a string")
    if end is None:
        end = '\n'
    if not isinstance(end, str):
        raise TypeError("end must be None or a string")
    if pos is None:
        pos = 'default'
    if not isinstance(pos, str):
        raise TypeError("pos must be None or a string")
    if length is None:
        length = 40
    if not isinstance(length, int):
        raise TypeError("length must be None or an integer")
    if snip is None:
        snip = True
    if not isinstance(snip, bool):
        raise TypeError("snip must be None or an boolean")
    if pos == 'start':
        align = [['<'], ["<", "<"], ["<", "<", "<"]]
    elif pos == 'center':
        align = [['^'], [">", "<"], [">", "^", "<"]]
    elif pos == 'end':
        align = [['>'], [">", ">"], [">", ">", ">"]]
    else:
        align = [['<'], ["<", ">"], ["<", "^", ">"]]
    if len(args) == 0:
        if sep != ' ':
            fp.write(str(sep[0]) * length)
    elif len(args) == 1:
        arg = str(args[0])
        if snip is True:
            out_single = arg[0:length]
        else:
            out_single = arg
        out = '{:{}{}{}}'
        fp.write(out.format(out_single, sep, align[0][0], length))
    elif len(args) == 2:
        compensate = length % 2
        half_len = length // 2
        arg_left = str(args[0])
        arg_right = str(args[1])
        total_len = len(arg_left) + len(arg_right)
        if total_len <= length or total_len >= length:
            out_right = arg_left[0:half_len]
            out_left = arg_right[0:half_len]
            pad_right = pad_left = half_len
        else:
            out_right = arg_left
            out_left = arg_right
            pad_right, pad_left = len(out_right), len(out_left)
        if compensate == 1:
            pad_left += compensate
        out = '{:{}{}{}}{:{}{}{}}'
        fp.write(out.format(out_right, sep,
                 align[1][0], pad_right, out_left, sep, align[1][1], pad_left))
    elif len(args) == 3:
        compensate = length % 3
        third_len = length // 3
        arg_left = str(args[0])
        arg_center = str(args[1])
        arg_right = str(args[2])
        total_len = len(arg_left) + len(arg_center) + len(arg_right)
        if total_len <= length or total_len >= length:
            out_left = arg_left[0:third_len]
            out_center = arg_center[0:third_len]
            out_right = arg_right[0:third_len]
            pad_left = pad_center = pad_right = third_len
        else:
            out_left, out_center, out_right = arg_left, arg_center, arg_right
            pad_left = len(out_left)
            pad_center = len(out_center)
            pad_right = len(out_right)
        if pos == 'center':
            pad_center = len(out_center)
            missing = length - (pad_left + pad_center + pad_right)
            if missing > 0:
                half_missing = missing // 2
                if missing % 2 == 0:
                    pad_left += half_missing
                else:
                    pad_left += half_missing + 1
                pad_right += half_missing
            out_center = out_center[0:pad_center]
        elif pos == 'start':
            pad_center = (pad_center-len(out_center))
            pad_left = (pad_left-len(out_left))
            pad_right += pad_center + pad_left + compensate
            pad_center = pad_left = 0
        elif pos == 'end':
            pad_center = (pad_center-len(out_center))
            pad_right = (pad_right-len(out_right))
            pad_left += pad_center + pad_right + compensate
            pad_center = pad_right = 0
        else:
            pad_left = (pad_left-len(out_left))
            pad_right = (pad_right-len(out_right))
            pad_center += pad_left + pad_right + compensate
            pad_left = pad_right = 0
        out = '{:{}{}{}}{:{}{}{}}{:{}{}{}}'
        fp.write(out.format(out_left, sep, align[2][0], pad_left, out_center,
                 sep, align[2][1], pad_center, out_right, sep, align[2][2], pad_right))
    else:
        for i, arg in enumerate(args):
            if i:
                fp.write(sep)
            fp.write(str(arg))
    fp.write(end)
    if flush:
        fp.flush()

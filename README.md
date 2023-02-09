# Pript



[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



## About Pript

Pript is a function that prints values to a stream, or to sys.stdout in the style of a receipt. It is based on the Python 3 `print()` built-in function. 

This package is meant to be a development aid by allowing you to print data in a format that is more readable. Keep in mind this function is only meant to be used in development. You should always consider using a package like `logging` for production.

### How different it is from `print()`?

Not much. To prevent compatibility issues, `pript()` was written using the original [`print()`](https://foss.heptapod.net/pypy/pypy/-/blob/branch/py3.10/pypy/module/__builtin__/app_io.py) built-in implementation from PyPy.

### Why `format()` instead of f-strings?

Even though f-strings are known to be faster, they were introduced in Python 3.6. For that reason, `pript()` relies on `format()` to bring compatibility down to Python 3.



## Getting Started

You can install Pript with pip or by copying the `pript.py` file to your project's root directory.

### Prerequisites

* Python 3 or above.
* pip

### Installation 

1. Install pript from pip
   ```sh
   pip install pript
   ```
2. Import it into your project
   ```py
   from pript import pript

   pript('Hello World!')
   ```

## Usage

Pript will format zero to three arguments, otherwise it behaves similarly to `print()`. You can customize the formatting by using the `sep`, `pos`, `length` and `snip` optional keyword arguments.

_For more information about optional keywords, please refer to the [Documentation](#documentation)._

### With no arguments

You can print separators using zero arguments:
```py
pript(sep='~')
```

Output:
```console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
```

### With one argument

Pript can be used, not ideally, as a replacement for print:
```py
pript('This will print a line like print()')
```

Output:
```console
This will print a line like print()     
```

### With two arguments

When using two arguments, pript will format each argument to the left and right by default, unless `pos` is specified:
```py
pript('Hello ', ' World!', sep='>')
```

Output:
```console
Hello >>>>>>>>>>>>>>>>>>>>>>>>>>> World!
```

### With three arguments

When using three arguments, pript will format each argument to the left, center and right respectively as default, unless `pos` is specified:
```py
pript('THIS ', ' IS ', ' PRIPT', length='20')
```

Output:
```console
THIS    IS     PRIPT
```

### With more than three arguments

When using more than three arguments, the behaviour of Pript is exactly the same as `print()`:
```py
pript([101], ['Pript'], 'Hello Pript!', ('Hello', 'Pript', '!'))
```

Output:
```console
[101] ['Pript'] Hello Pript! ('Hello', 'Pript', '!')
```

### Simple example with a single argument

Suppose we want to center a single string, and style it with a symbol on each side of the text filling the remaining space, and a maximum length of 30 characters:
```py
pript(' Hello Pript! ', sep='|', length=30, pos='center')
```

Output:
```console
|||||||| Hello Pript! ||||||||
```

### Printing a receipt

Minimum customization with default length:
```py
from pript import pript

def receipt():
  pript(sep='*')
  pript('HalfBakedCoffee Company', pos='center')
  pript('014210 Half Baked Ave.', pos='center')
  pript(' Receipt ', pos='center', sep="*")
  pript('Date: ', ' 04/02/2023 11:54:02')
  pript()
  pript(' Item list ', pos='center', sep="*")
  pript('Item: ', ' Big Coffee')
  pript('Quantity: ', ' 2')
  pript('Price: ', ' $5.00', sep='.')
  pript()
  pript(sep="*")
  pript('Item: ', ' Small Coffee')
  pript('Quantity: ', ' 2')
  pript('Price: ', ' $2.50', sep='.')
  pript()
  pript(sep="*")
  pript('Total: ', ' $15.00', sep='.')
  pript('Paid: ', ' $15.00', sep='.')
  pript('Thank you! ', ' Mr. Buyer')
  pript(sep='*')

receipt()
```

Output:
```console
****************************************
        HalfBakedCoffee Company
         014210 Half Baked Ave.
*************** Receipt ****************
Date:                04/02/2023 11:54:02

************** Item list ***************
Item:                         Big Coffee
Quantity:                              2
Price: ........................... $5.00

****************************************
Item:                       Small Coffee
Quantity:                              2
Price: ........................... $2.50

****************************************
Total: .......................... $15.00
Paid: ........................... $15.00
Thank you!                     Mr. Buyer
****************************************
```



## Documentation

### `pript` (Function)

**Positional arguments:**
- `args`: Arguments to print.

**Keyword arguments:**
- `file`: A file-like object (stream). Defaults to the current sys.stdout. 
- `sep`: String inserted between values. Default a space.
- `end`: String appended after the last value. Default a newline.
- `flush`: Whether to forcibly flush the stream. Defaults to `False`.
- `pos`: String determining the alignment of the output. Defaults to `start` (`between` for two and three arguments). Receives `start`, `center`, `end` or `None` as valid arguments.
- `length`: Maximum length of the output. Defaults to 40 characters.
- `snip`: Whether to remove excess characters when using a single argument. Defaults to `True`.

### About the `pos` optional keyword:

There are slight differences when providing the optional keyword `pos` with `start`, `center` or `end` using two or three arguments.

For example, when using two arguments with `pos='start'` and `sep='-'` for reference:
```py
pript('Hello', 'World!', pos='start', sep='-')
```

Pript will position each argument to the start of each column (one column per argument):
```console
Hello---------------World!--------------
```

On the contrary, while using three arguments with  `pos='start'` and `sep='-'` for reference:
```py
pript('Hello', 'World', 'Pript!', pos='start', sep='-')
```

Pript will compress each argument to the start of the line, and fill all the remaning empty space of each column:
```console
HelloWorldPript!------------------------
```
This was purposely made to extend the formatting capabilities of Pript while reducing the complexity of the function itself.

With two arguments, each one will be allocated to their asignated position inside their respective column. With three arguments, each argument will be compressed to their asignated position and the remaining space will be automatically filled.

### About the `snip` optional keyword:

When using a single argument, `snip` (`True` by default) will trim any excess characters if the argument is longer than `length` (`40` by default):
```py
pript('This string is exactly 41 characters long')
```

Output:
```console
This string is exactly 41 characters lon
```

This behaviour can be disabled by passing `False` to `snip`:
```py
pript('This string is exactly 41 characters long', snip=False)
```

Output:
```console
This string is exactly 41 characters long
```

### `snip` with more than a single argument

Be aware that disabling `snip` is not currently supported when using two and three arguments, Pript will always trim the end of any argument that is longer than its designated column length. This is specially important when debugging numeric values as they will get trimmed, in example:
```py
pript('The current price of EXAMPLE is: ', '0.00000000000000024984 USD')
```

Output:
```console
The current price of0.000000000000000249
```

This bug is a product of the way Pript formats strings into grids. It can be temporarily solved by setting `length` to an amount double the longest argument:
```py
arg0 = 'The current price of EXAMPLE is: '
arg1 = '0.00000000000000024984 USD'
longest_arg = max(len(arg0), len(arg1))
pript(arg0, arg1, length=longest_arg*2)
```

This will prevent Pript from trimming the output:
```console
The current price of EXAMPLE is:        0.00000000000000024984 USD
```

An easier approach would be to use string concatenation with `snip` in a single argument:
```py
arg0 = 'The current price of EXAMPLE is: '
arg1 = '0.00000000000000024984 USD'
pript(arg0 + arg1, snip=False)
```

This will also prevent Pript from trimming the output:
```console
The current price of EXAMPLE is: 0.00000000000000024984 USD
```

This is a known bug and it is planned to be fixed in the following revisions of Pript. 



## Contributing

The code has room for improvement, particularly in the calculations. Currently, it serves only as a proof of concept. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make Pript better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## License

Distributed under the MIT License. See `LICENSE` for more information.



## Contact

HalfBakedBread/Ash Bauer 
- [HalfBakedBread - Portfolio](https://halfbakedbread.github.io)
- [HalfBakedServer - Discord](https://discord.gg/HUjks45JYC) 
- [@halfbakedash - Twitter](https://twitter.com/halfbakedash)

Project Link: [https://github.com/halfbakedbread/pript](https://github.com/halfbakedbread/pript)



[contributors-shield]: https://img.shields.io/github/contributors/halfbakedbread/pript.svg?style=flat-square
[contributors-url]: https://github.com/halfbakedbread/pript/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/halfbakedbread/pript.svg?style=flat-square
[forks-url]: https://github.com/halfbakedbread/pript/network/members
[stars-shield]: https://img.shields.io/github/stars/halfbakedbread/pript.svg?style=flat-square
[stars-url]: https://github.com/halfbakedbread/pript/stargazers
[issues-shield]: https://img.shields.io/github/issues/halfbakedbread/pript.svg?style=flat-square
[issues-url]: https://github.com/halfbakedbread/pript/issues
[license-shield]: https://img.shields.io/github/license/halfbakedbread/pript.svg?style=flat-square
[license-url]: https://github.com/halfbakedbread/pript/blob/main/LICENSE
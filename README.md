# Pynini for Windows

This project is maintained by [@SystemPanic](https://github.com/SystemPanic)

If you use Pynini in your research, we would appreciate if you cite the
following paper:

> K. Gorman. 2016.
> [Pynini: A Python library for weighted finite-state grammar compilation](http://openfst.cs.nyu.edu/twiki/pub/GRM/Pynini/pynini-paper.pdf).
> In *Proc. ACL Workshop on Statistical NLP and Weighted Automata*, 75-80.

(Note that some of the code samples in the paper are now out of date and not
expected to work.)

## Windows Dependencies

-   Microsoft Visual Studio 2019 or newer
-   [Python 3.6+](https://www.python.org) and headers

## Installation instructions

Clone the repository and install as a normal python project. For example:

`pip install .` or  `python setup.py bdist_wheel && pip install dist\pynini-VERSION-cp312-cp312-win_amd64.whl`

## Testing

To confirm successful installation, run `pip install -r requirements`, then
`python tests/pynini_test.py`. If all tests pass, the final line will read `OK`;
a successful run will log some errors to STDERR (this is working as expected).

## Python version support

Pynini 2.0.0 and onward support Python 3. Pynini 2.1 versions (onward) drop
Python 2 support. The current release supports Python 3.8--3.13.

# License

Pynini is released under the Apache license. See [`LICENSE`](LICENSE) for more
information.

# Interested in contributing?

See [`CONTRIBUTING`](CONTRIBUTING) for more information.

# Mandatory disclaimer

This is not an official Google product.

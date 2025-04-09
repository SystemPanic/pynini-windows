# Pynini for Windows

This repository is a fork of Pynini and will be updated when new release versions of Pynini are published, until Pynini decides to support Windows.

**Don't open a new Issue to request a specific commit build. Wait for a new stable release.**

**Don't open Issues for general Pynini questions or non Windows related problems. Only Windows specific issues.** Any Issue opened that is not Windows specific will be closed automatically.

**Don't request a wheel for your specific environment.**

This project is maintained by [@SystemPanic](https://github.com/SystemPanic)

If you use Pynini in your research, we would appreciate if you cite the
following paper:

> K. Gorman. 2016.
> [Pynini: A Python library for weighted finite-state grammar compilation](http://openfst.cs.nyu.edu/twiki/pub/GRM/Pynini/pynini-paper.pdf).
> In *Proc. ACL Workshop on Statistical NLP and Weighted Automata*, 75-80.

(Note that some of the code samples in the paper are now out of date and not
expected to work.)

### Windows instructions:

#### Installing an existing release wheel:

1. Ensure that you have the correct Python version of the wheel. The Python version of the wheel is specified in the release version
2. Download the wheel from the release version of your preference
3. Install it with ```pip install DOWNLOADED_WHEEL_PATH```

#### Building from source:

A Visual Studio 2019 or newer is required to launch the compiler x64 environment. The installation path is referred in the instructions as VISUAL_STUDIO_INSTALL_PATH. For example, for Visual Studio 2022 default installation, replace VISUAL_STUDIO_INSTALL_PATH with C:\Program Files\Microsoft Visual Studio\2022\Community

1. Open a Command Line (cmd.exe)
2. Clone the Pynini for Windows repository: `cd C:\ & git clone https://github.com/SystemPanic/pynini-windows.git`
3. Execute (in cmd) `VISUAL_STUDIO_INSTALL_PATH\VC\Auxiliary\Build\vcvarsall.bat x64`
4. Change the working directory to the cloned repository path, for example: `cd C:\pynini-windows`
6. Build & install: `pip install . --no-build-isolation`

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

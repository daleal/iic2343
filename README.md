# IIC2343

## Installation

Install using `pip`!

```sh
pip install iic2343
```

## Usage

To use the library, import the `Basys3` object directly and use the `begin`, `write` and `end` methods!

```python
from iic2343 import Basys3

instance = Basys3()

instance.begin(port_number=2)  # port_number is optional
instance.write(1, bytearray([0x00, 0x00, 0x10, 0x16, 0x01]))
instance.write(2, bytearray([0x00, 0x00, 0x00, 0x18, 0x03]))
instance.write(3, bytearray([0x00, 0x00, 0x20, 0x18, 0x03]))
instance.write(4, bytearray([0x00, 0x00, 0x00, 0x20, 0x00]))
instance.end()
```

Here, a `Basys3` instance has 3 methods:

### `begin`

The method receives an optional `port_number` parameter (in needs to be an `int`). If the parameter is not present and there is only one available serial port on your machine, the `Basys3` instance will use that serial port. Otherwise, it will raise an exception. The method initializes a port to `write` to.

### `write`

The method receives an `address` parameter (an `int`) and a `word` parameter (a `bytearray`). It then attempts to write the `word` on the specified `address`. If the `Basys3` instance fails, it returns a `0`. Otherwise, it returns an `int`.

### `end`

The method receives no parameters, and simply closes the port initialized on the `begin` method.


## Developing

This library uses `PyTest` as the test suite runner, and `PyLint`, `Flake8`, `Black`, `ISort` and `MyPy` as linters. It also uses `Poetry` as the default package manager.

The library includes a `Makefile` that has every command you need to start developing. If you don't have it, install `Poetry` using:

```sh
make get-poetry
```

Then, create a virtualenv to use throughout the development process, using:

```sh
make build-env
```

Activate the virtualenv using:

```sh
. .venv/bin/activate
```

Deactivate it using:

```sh
deactivate
```

To add a new package, use `Poetry`:

```sh
poetry add <new-package>
```

To run the linters, you can use:

```sh
# The following commands auto-fix the code
make black!
make isort!

# The following commands just review the code
make black
make isort
make flake8
make mypy
make pylint
```

To run the tests, you can use:

```sh
make tests
```

## Releasing

To make a new release of the library, `git switch` to the `master` branch and execute:

```sh
make bump! minor
```

The word `minor` can be replaced with `patch` or `major`, depending on the type of release. The `bump!` command will bump the versions of the library, create a new branch, add and commit the changes. Then, just _merge_ that branch to `master`. Finally, execute a _merge_ to the `stable` branch. Make sure to update the version before merging into `stable`, as `PyPi` will reject packages with duplicated versions.

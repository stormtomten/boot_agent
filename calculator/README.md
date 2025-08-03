# Calculator App

This is a simple calculator application that evaluates mathematical expressions.

## Project Structure

The project has the following structure:

- `main.py`: The main application file. It takes an expression as a command-line argument and evaluates it using the `Calculator` class.
- `pkg/`: This directory contains the following modules:
  - `calculator.py`: Defines the `Calculator` class, which evaluates mathematical expressions.
  - `render.py`: Defines the `render` function, which formats the expression and result in a box.
- `tests.py`: Contains unit tests for the `Calculator` class.
- `lorem.txt`: This file contains the text "wait, this isn't lorem ipsum".
- `lorem_full.txt`: This file contains a large block of Lorem Ipsum text, likely used for testing or placeholder purposes.
- `nope.txt`: This file simply contains the word "nope".
- `README.md`: This file.

## Usage

To use the calculator, run the `main.py` file with the expression as a command-line argument:

```bash
python main.py "3 + 5"
```

This will print the result of the expression in a formatted box.

## Examples

```bash
python main.py "10 - 4"
python main.py "3 * 4 + 5"
python main.py "2 * 3 - 8 / 2 + 5"
```

## Testing

To run the unit tests, run the `tests.py` file:

```bash
python tests.py
```

## Author

- Calculator logic: boot.dev
- Render box and argument parsing: boot.dev
- README.md crafted with care and a dash of AI magic by Gemini, your friendly neighborhood large language model.

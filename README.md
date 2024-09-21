# Fortune Wheel

Fortune Wheel is a Python application that simulates a spinning wheel of fortune. Users can spin the wheel and win random prizes defined in a JSON configuration file.

## Features

- Visualization of a fortune wheel with customizable prizes.
- Buttons to spin the wheel and stop it on a random prize.
- Simple prize configuration via a `fortuneWheel.json` file.

## Requirements

- Python 3.x
- The following Python libraries must be installed:
  - `tkinter` (included in standard Python)
  - `matplotlib`
  - `numpy`

## Configuration

The `fortuneWheel.json` file contains the items for the wheel. You can modify it to add or remove prizes. Here’s an example of how the file should look:

```json
{
    "title": "Ruota della fortuna",
    "description": "Gira la ruota e scopri la prossima attività!",
    "btnSpinText": "Gira la ruota",
    "btnStopText": "Ferma la ruota",
    "items": [
        "Prize 1",
        "Prize 2",
        "Prize 3",
        "Prize 4",
        "Prize 5",
        "Prize 6",
        "Prize 7",
        "Prize 8"
    ]
}
```

## Running the Application
To run the application, make sure to have the `fortuneWheel.json` file in the same directory as the executable. You can start the app with the following command:

```bash
python fortuneWheel.py
```

### Creating the Executable
You can generate an executable using `pyinstaller`. Make sure you have `pyinstaller` installed:

```bash
pip install pyinstaller
```

Then, run the command:

```bash
pyinstaller --clean fortuneWheel.spec
```

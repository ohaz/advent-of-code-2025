# adventofcode base template

This is a base template in python to use for new repos for advent of code solutions

## Requirements

These scripts require python 3.10 to run, as some features introduced in that version are used.

### Installing

To install the requirements, if a `requirements.txt` exists, run:

`pip install -r requirements.txt`

If you want to use this script to create folders and download inputs for new days:

* Log in to AOC in a browser
* Run aocd-token in a console. This searches for the session cookie of your login and stores it in `~/.config/aocd/token`. It's used to download the current days input (see https://pypi.org/project/advent-of-code-data/).
* Now you can use `python create.py` to download the next available day.

### Configuration

Edit create.py to set `YEAR` to the correct value

### Running

To run all days, just run:

`python main.py`

To run just one day, run:

`python main.py <number_of_day>`, e.g. `python main.py 11`
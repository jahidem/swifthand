# SwiftHand
The player wants to play a general non-transitive one-move game. Not the Rock/Paper/Scissors, but any game he comes up with. The main idea is the non-transitivity of the moves (the second move wins over the first, the third wins over the second, but the third loses to the first). Accordingly, no move can be hardcoded in the code, moves are passed as arguments.
- demo: https://www.loom.com/share/090f7d9d6378439abad44c1c6335c0f7?sid=776445ba-7ef4-44be-bb56-d9e43e1ddc55
## installation & run (python 3.11.7 - windows)
project is setup with pyproject.toml

```shell
python -m venv venv 
./venv/Scripts/activate
pip install -e .
swifthand.exe Rock Paper Scissor
```
## main libraries
- prettytable
- setuptools


from random import choice

class colorizer:
    """
|    A context manager for changing terminal text color with optional random color selection.
|
|    Available colors:
|    - grey
|    - red
|    - green
|    - yellow
|    - blue
|    - pink
|    - turquoise
|    - reset (default)
|
|    Usage:
|        Basic usage:
|            with colorizer('red'):
|                print("This text will be red.")
|
|        Random color usage:
|            with colorizer(random_flag=True):
|                print("This text will have a random color.")
|
|    Attributes:
|        color (str): The name of the color to apply. Defaults to 'reset'.
|        random_flag (bool): If True, applies a random color from the available set.

  """

    COLORS = {
        'grey': '\033[90m',
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'pink': '\033[95m',
        'turquoise': '\033[96m',
        'reset': '\033[0m'
    }

    def __init__(self, color: str = "reset", *, random_flag=False):
        try:
            if not isinstance(color, str):
                raise TypeError("Color must be a string. Color switched to default")
            else:
                self.color = color
                self.random_flag = random_flag
        except TypeError as error:
            print(f"ERROR: {error}")
            self.color = "reset"
            self.random_flag = random_flag

    def __enter__(self):
        if not self.random_flag:
            print(self.COLORS.get(self.color.lower()))
        else:
            print(choice(list(self.COLORS.values())))

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('\033[0m')

import pandas as pd
import random


class Dracula:
    '''Dracula Color.
        Available colors as attribute: 
                background, current_line, foreground, comment, cyan, green, orange, pink, purple, red, yellow
        Method: random_color() -> picks a random color from Dracula scheme

        Reference: https://en.wikipedia.org/wiki/Dracula_(color_scheme)
    '''
    URL = "https://en.wikipedia.org/wiki/Dracula_(color_scheme)"

    def __init__(self):
        self.color_table = pd.read_html(Dracula.URL)[1][['Name', 'Hex']]
        self.color_table['Name'] = self.color_table['Name'].apply(lambda x: '_'.join(x.lower().split()))
        self.color_table = self.color_table.set_index('Name')
        self.colors = self.color_table.index
        for row in self.color_table.itertuples():
            setattr(self, row[0], row[1])
        print(f"Loaded {self.__repr__()}")

    def color(self, color, verbose=False):
        if verbose:
            print("Picked:", color)
        return self.color_table.loc[color, 'Hex']

    def random_color(self, verbose=True):
        # self.color(self.color_table.sample(1).index[0], verbose)
        self.color(random.choice(self.colors), verbose=verbose)

    def __repr__(self):
        return f"Dracula Color.\n\tAvailable colors: {', '.join(self.colors)}"
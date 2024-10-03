from math import prod

class Matrix:

    """ Constructor definition """
    def __init__(self, matrix: list):
        self.matrix = matrix

    """ Function definition """
    def row_sum(self) -> list:
        return [sum(row) for row in self.matrix]

    def row_prod(self) -> list:
        return [prod(row) for row in self.matrix]

    def col_sum(self) -> list:
        return [sum(col) for col in zip(*self.matrix)]

    def col_prod(self) -> list:
        return [prod(col) for col in zip(*self.matrix)]
from Matrix import *

class Solution:

    """ Constructor definition """
    def __init__(self):
       self.size = 10

    """ Function definition """
    def resolve_flag(self, size: int):

        symmetricMap = {key: self.symmetric_map(key)
                        for key in range(1, size)}

        matrix = [list(value.values()) for value in symmetricMap.values()]
        symmetricMatrix = Matrix(matrix)

        rowSum = symmetricMatrix.row_sum()
        rowProd = symmetricMatrix.row_prod()
        colSum = symmetricMatrix.col_sum()
        colProd = symmetricMatrix.col_prod()

        print()
        print(rowSum, colSum)
        print(rowProd, colProd)

        rowSumSub = self.subdivision_vector(rowSum)
        rowProdSub = self.subdivision_vector(rowProd)
        colSumSub = self.subdivision_vector(colSum)
        colProdSub = self.subdivision_vector(colProd)

        print()
        print(rowSumSub, colSumSub)
        print(rowProdSub, colProdSub)

    def symmetric_map(self, size: int) -> dict:

        symNum = lambda x, s: self.symmetric_number(x, s)

        keys = [symNum(k, size) for k in range(10)]
        intKeys = [int(key) for key in keys]
        values = self.subdivision_vector(intKeys)

        return {key: value for key, value in zip(keys, values)}

    @staticmethod
    def symmetric_number(digit: int, size: int) -> str:

        numberList = ([digit] * size + size * [(digit + 1) % 9
                                               if digit == 9 else digit + 1])
        return "".join(str(digit) for digit in numberList)

    def subdivision_vector(self, vector: list) -> list:

        subDiv = lambda y: self.subdivisions_of(y)[-1]
        return [subDiv(value) for value in vector]

    @staticmethod
    def subdivisions_of(number: int) -> list:

        numberList = [number]
        digitSum = lambda x: sum(int(d) for d in str(x))
        while number >= 10:

            number = digitSum(number)
            numberList.append(number)

        return numberList

    def solve(self):
        self.resolve_flag(self.size)

if __name__ == "__main__":

    solution = Solution()
    solution.solve()

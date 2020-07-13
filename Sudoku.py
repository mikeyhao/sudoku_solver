

class Sudoku:

    def __init__(self, txt):
        """
        Reads a .txt file and creates a 2D-matrix that represents
        a 9x9 sudoku board
        :param txt: A .txt file representing a sudoku board
        """
        f = open("ex/"+txt, "r")
        text = f.read()
        text = text.split("\n")
        self.matrix = []
        for i in range(9):
            self.matrix.append(text[i].split(" "))
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                self.matrix[y][x] = int(self.matrix[y][x])
        self.blanks_cr8()

    def blanks_cr8(self):
        """
        Creates an array of the empty sudoku cells to be filled in
        """
        self.blanks = []
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                if self.matrix[y][x] == 0:
                    self.blanks.append((y,x))

    def grid(self, y, x):
        """
        :param y: position Y
        :param x: position X
        :return: An array representing the grid the (y,x) cell exists in
        """
        ret = []
        py, px = (y//3)*3, (x//3)*3
        for i in range(py, py+3):
            for j in range(px, px+3):
                ret.append(self.matrix[i][j])
        return ret

    def row(self, y, x):
        """
        :param y: position Y
        :param x: position X
        :return: An array representing the row the (y,x) cell exists in
        """
        ret = []
        for i in self.matrix[y]:
            ret.append(i)
        return ret

    def col(self, y, x):
        """
        :param y: position Y
        :param x: position X
        :return: An array representing the column the (y,x) cell exists in
        """
        ret = []
        for i in range(len(self.matrix)):
            ret.append(self.matrix[i][x])
        return ret

    def is_possible(self, num, y, x):
        """
        Finds whether num is valid at position (y,x). If duplicates
        exists in the grid, row or column, it is not valid.
        :param num: number to be checked for repetition
        :param y: position Y
        :param x: position X
        :return: True/False depending on validity
        """
        arr = [self.grid(y,x), self.row(y,x), self.col(y,x)]
        for ar in arr:
            for a in ar:
                if num == a:
                    return False
        return True

    def solve(self):
        """
        Call me to solve sudoku! Prints either the answer to the
        puzzle or indication that solution does not exist
        :return: None
        """
        res = self.solve_aux(0)
        if res:
            print(str(self))
        else:
            print("There are no solutions to this puzzle!")

    def solve_aux(self, idx):
        """
        Solves the sudoku based on recursion and backtracking algorithm
        :param idx: position of current empty cell
        :return: True if can continue, False if no solution is valid (backtracks)
        """
        if idx >= len(self.blanks):
            return True
        y,x = self.blanks[idx]
        for n in range(1,10):
            if self.is_possible(n, y, x):
                self.matrix[y][x] = n
                if self.solve_aux(idx+1):
                    return True
                self.matrix[y][x] = 0
        return False

    def __str__(self):
        ret_string = ""
        for i in range(9):
            # print("---------------")
            for j in range(9):
                ret_string += " "
                ret_string += str(self.matrix[i][j])
                ret_string += " "
                if j == 2 or j == 5:
                    ret_string += "|"
            ret_string += "\n"
            if i == 2 or i == 5:
                ret_string += ("-----------------------------")
                ret_string += "\n"
        return ret_string


def testr():
    """
    Runs the test cases in the ex folder
    """
    for i in range(5):
        sdo = "sdo_"+str(i)+".txt"
        sol = "sdo_"+str(i)+"_sol.txt"
        sd = Sudoku(sdo)
        ans = Sudoku(sol)
        sd.solve()
        if sd.matrix != ans.matrix:
            assert False
    print("passed everything!")


if __name__ == "__main__":

    # sd = Sudoku("sdo_4.txt")
    # sd.solve()
    # testr()
    pass
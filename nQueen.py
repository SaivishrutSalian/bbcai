class QueenChessBoard:
    def __init__(self, size):
        self.size = size
        self.columns = []

    def place_in_next_row(self, column):
        self.columns.append(column)

    def remove_in_current_row(self):
        if self.columns:  
            return self.columns.pop()
        return None 

    def is_this_column_safe_in_next_row(self, column):
        row = len(self.columns)
        for queen_column in self.columns:
            if column == queen_column:
                return False
        for queen_row, queen_column in enumerate(self.columns):
            if queen_column - queen_row == column - row:
                return False
        for queen_row, queen_column in enumerate(self.columns):
            if (self.size - queen_column) - queen_row == (self.size - column) - row:
                return False
        return True

    def display(self):
        for row in range(self.size):
            for column in range(self.size):
                if column == self.columns[row]:
                    print('Q', end=' ')
                else:
                    print('. ', end=' ')
            print() 

def solve_queen(size):
    board = QueenChessBoard(size)
    number_of_solutions = 0
    row = 0
    column = 0

    while True:
        while column < size:
            if board.is_this_column_safe_in_next_row(column):
                board.place_in_next_row(column)
                row += 1
                column = 0
                break
            else:
                column += 1

        if column == size or row == size:
            if row == size:
                board.display()
                print()
                number_of_solutions += 1

            row -= 1
            if row < 0:
                break  
            prev_column = board.remove_in_current_row()
            column = 1 + prev_column if prev_column is not None else 0  # Move to the next column

    print('Number of solutions:', number_of_solutions)

n = int(input('Enter n: '))
solve_queen(n)

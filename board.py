class HidatoBoard:
    def __init__(self, length):
        """
        Initialize the Hidato board.
        :param board: 2D list of integers, where 0 represents an empty cell,
                      and positive integers represent numbers on the board.
        """
        self.head = None
        self.size = length
        self.board = [[0 for _ in range(length)] for _ in range(length)]
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def copy(self):
        """Create a deep copy of the HidatoBoard."""
        new_board = HidatoBoard(self.size)
        new_board.board = [row[:] for row in self.board]  # Deep copy the board
        new_board.head = self.head  # Copy the head position
        return new_board

    def place(self, num, x, y):
        new_board = self.copy()
        new_board.board[y][x] = num
        return new_board

    def setBoard(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.board[i][j] = board[i][j]

    def find(self, num):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == num:
                    return (j, i)
        return None

    def isNeighbor(self, num, pos):
        x, y = pos
        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                if self.board[ny][nx] == num:
                    return (nx,ny)
        return None

    def isSolved(self):

        start = self.find(1)
        if start == None: return False

        end = self.find(self.size**2)
        if end == None: return False

        for i in range(2, self.size**2):
            nei = self.isNeighbor(i, start)
            if nei == None: return False
            start = nei

        return True

    def print_board(self):
        """Print the Hidato board."""
        for row in self.board:
            print(' '.join(str(cell).rjust(3, ' ') if cell != 0 else ' __' for cell in row))

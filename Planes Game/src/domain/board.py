class Board:
    def __init__(self):
        """
        Creates a 11x11 board with the first row and column being the numbers and letters of the board.
        """
        self._board = [[-1 for _ in range(11)] for _ in range(11)]
        for i in range(0, 11):
            self._board[0][i] = i
            self._board[i][0] = ' ABCDEFGHIJ'[i]

    def __getitem__(self, item):
        """
        Allows indexing using either integers (board[row][col]) or chess-like notation (board['A', 1]).
        """
        if isinstance(item, tuple) and len(item) == 2:
            row, col = item
            if isinstance(row, str):
                row = ' ABCDEFGHIJ'.index(row)  # Convert 'A'->1, 'B'->2, ...
            return self._board[row][col]
        return self._board[item]  # Default integer-based indexing
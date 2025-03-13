import copy


class UserService:
    def __init__(self, user_board, computer_board):
        """
        :type user_board: Board
        :param user_board:
        :param computer_board:
        """
        self._user_board = user_board
        self._computer_board = computer_board

    def valid_placement(self, x, y, orientation):
        """
        Checks if the plane can be placed on the board.
        :param x: int
        :param y: int
        :param orientation: int
        :return: bool
        """
        user_board = self._user_board.return_board()

        # Check if the placement is within bounds
        if not self._is_within_bounds(x, y, orientation):
            return False

        # Get the positions to check and update based on orientation
        placement_positions_to_check, placement_positions_to_update, placement_special_position = self._get_positions(x, y, orientation)

        # Validate and update the board
        if self._check_and_update_board(user_board, placement_positions_to_check, placement_positions_to_update, placement_special_position):
            self._user_board.update_board(user_board)
            return True

        return False

    @staticmethod
    def _is_within_bounds(x, y, orientation):
        """
        Checks if the coordinates are within valid bounds for the given orientation.
        """
        if orientation == 0:
            return 2 < x < 10 and 2 < y < 9
        elif orientation == 1:
            return 2 < x < 9 and 1 < y < 9
        elif orientation == 2:
            return 1 < x < 9 and 2 < y < 9
        elif orientation == 3:
            return 2 < x < 9 and 2 < y < 10
        return False

    @staticmethod
    def _get_positions(x, y, orientation):
        """
        Returns the positions to check, update, and the special position based on orientation.
        """
        positions_to_check, positions_to_update, special_position = None, None, None
        if orientation == 0:
            positions_to_check = [
                (x, y), (x + 1, y), (x + 1, y - 1), (x + 1, y + 1),
                (x - 1, y), (x - 1, y - 1), (x - 1, y - 2), (x - 1, y + 1),
                (x - 1, y + 2), (x - 2, y)
            ]
            positions_to_update = [
                (x + 1, y), (x + 1, y - 1), (x + 1, y + 1),
                (x, y), (x - 1, y), (x - 1, y - 1), (x - 1, y - 2),
                (x - 1, y + 1), (x - 1, y + 2)
            ]
            special_position = (x - 2, y)

        elif orientation == 1:
            positions_to_check = [
                (x, y), (x, y - 1), (x - 1, y - 1), (x + 1, y - 1),
                (x, y + 1), (x - 1, y + 1), (x - 2, y + 1),
                (x + 1, y + 1), (x + 2, y + 1), (x, y + 2)
            ]
            positions_to_update = [
                (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                (x, y), (x, y + 1), (x - 1, y + 1), (x - 2, y + 1),
                (x + 1, y + 1), (x + 2, y + 1)
            ]
            special_position = (x, y + 2)

        elif orientation == 2:
            positions_to_check = [
                (x, y), (x - 1, y), (x - 1, y - 1), (x - 1, y + 1),
                (x + 1, y), (x + 1, y - 1), (x + 1, y - 2),
                (x + 1, y + 1), (x + 1, y + 2)
            ]
            positions_to_update = [
                (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                (x, y), (x + 1, y), (x + 1, y + 1), (x + 1, y + 2),
                (x + 1, y - 1), (x + 1, y - 2)
            ]
            special_position = (x + 2, y)

        elif orientation == 3:
            positions_to_check = [
                (x, y), (x, y + 1), (x + 1, y + 1), (x - 1, y + 1),
                (x, y - 1), (x + 1, y - 1), (x + 2, y - 1),
                (x - 1, y - 1), (x - 2, y - 1), (x, y - 2)
            ]
            positions_to_update = [
                (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
                (x, y), (x, y - 1), (x + 1, y - 1), (x + 2, y - 1),
                (x - 1, y - 1), (x - 2, y - 1)
            ]
            special_position = (x, y - 2)

        return positions_to_check, positions_to_update, special_position

    @staticmethod
    def _check_and_update_board(user_board, positions_to_check, positions_to_update, special_position):
        """
        Checks if all positions are available and updates the board.
        """
        for pos in positions_to_check:
            if user_board[pos[0]][pos[1]] != -1:
                return False

        for pos in positions_to_update:
            user_board[pos[0]][pos[1]] = 1

        user_board[special_position[0]][special_position[1]] = 2
        return True

    def attack(self, row, column):
        """
        Attacks the computer board.
        """
        computer_board = self._computer_board.return_board()

        # Check if the space has already been attacked
        if computer_board[row][column] in {3, 4, 5}:
            return "used_space"

        # Handle different types of spaces
        if computer_board[row][column] == -1:
            computer_board[row][column] = 3
            self._computer_board.update_board(computer_board)
            return "empty_space"
        elif computer_board[row][column] == 1:
            computer_board[row][column] = 4
            self._computer_board.update_board(computer_board)
            return "plane_piece"
        elif computer_board[row][column] == 2:
            return self._handle_cockpit_attack(computer_board, row, column)

        return "invalid"

    def _handle_cockpit_attack(self, computer_board, row, column):
        """
        Handles the logic for attacking the cockpit of a plane.
        """
        orientations = {
            "1": (range(4, 11), range(3, 9), [
                (row - 1, column), (row - 2, column), (row - 3, column),
                (row - 1, column - 1), (row - 1, column - 2),
                (row - 1, column + 1), (row - 1, column + 2),
                (row - 3, column - 1), (row - 3, column + 1)
            ]),
            "2": (range(1, 8), range(3, 9), [
                (row + 1, column), (row + 2, column), (row + 3, column),
                (row + 1, column - 1), (row + 1, column - 2),
                (row + 1, column + 1), (row + 1, column + 2),
                (row + 3, column - 1), (row + 3, column + 1)
            ]),
            "3": (range(3, 9), range(4, 11), [
                (row, column - 1), (row, column - 2), (row, column - 3),
                (row - 1, column - 1), (row - 2, column - 1),
                (row + 1, column - 1), (row + 2, column - 1),
                (row - 1, column - 3), (row + 1, column - 3)
            ]),
            "4": (range(3, 9), range(1, 8), [
                (row, column + 1), (row, column + 2), (row, column + 3),
                (row - 1, column + 1), (row - 2, column + 1),
                (row + 1, column + 1), (row + 2, column + 1),
                (row - 1, column + 3), (row + 1, column + 3)
            ])
        }

        for orientation, (row_range, col_range, positions) in orientations.items():
            if row in row_range and column in col_range:
                if all(computer_board[r][c] in {1, 4} for r, c in positions) and self.is_correct(row, column,
                                                                                                 orientation):
                    for r, c in positions:
                        computer_board[r][c] = 5
                    computer_board[row][column] = 5
                    self._computer_board.update_board(computer_board)
                    return "plane_cockpit"

        return "invalid"

    def clean_board(self):
        """
        Cleans the user board
        :return:
        """
        user_board = self._user_board.return_board()
        for x in range(1, 11):
            for y in range(1, 11):
                user_board[x][y] = -1
        self._user_board.update_board(user_board)

    def get_board(self):
        """
        Returns the user board
        :return:
        """
        return self._user_board.return_board()

    def is_correct(self, probable_x, probable_y, orientation):
        """
        Checks if the plane is correctly placed relative to the other planes on the board
        :param probable_x:
        :param probable_y:
        :param orientation:
        :return:
        """
        board = self._computer_board.return_board()
        user_board = copy.deepcopy(board)
        cnt = 0

        directions = {
            "1": [(-1, 0), (-2, 0), (-3, 0), (-1, -1), (-1, -2), (-1, 1), (-1, 2), (-3, -1), (-3, 1)],
            "2": [(1, 0), (2, 0), (3, 0), (1, -1), (1, -2), (1, 1), (1, 2), (3, -1), (3, 1)],
            "3": [(0, -1), (0, -2), (0, -3), (-1, -1), (-2, -1), (1, -1), (2, -1), (-1, -3), (1, -3)],
            "4": [(0, 1), (0, 2), (0, 3), (-1, 1), (-2, 1), (1, 1), (2, 1), (-1, 3), (1, 3)]
        }

        if orientation in directions:
            for dx, dy in directions[orientation]:
                user_board[probable_x + dx][probable_y + dy] = 5

        for x in range(1, 11):
            for y in range(1, 11):
                if user_board[x][y] == 2:
                    if 4 <= x <= 10 and 3 <= y <= 8:
                        if all((user_board[x - i][y] == 1 or user_board[x - i][y] == 4) for i in range(1, 4)) and \
                                all((user_board[x - 1][y + j] == 1 or user_board[x - 1][y + j] == 4) for j in
                                    range(-2, 3) if j != 0) and \
                                all((user_board[x - 3][y + j] == 1 or user_board[x - 3][y + j] == 4) for j in [-1, 1]):
                            for i in range(1, 4):
                                user_board[x - i][y] = 5
                            for j in range(-2, 3):
                                if j != 0:
                                    user_board[x - 1][y + j] = 5
                            user_board[x - 3][y - 1] = user_board[x - 3][y + 1] = 5

                    if 1 <= x <= 7 and 3 <= y <= 8:
                        if all((user_board[x + i][y] == 1 or user_board[x + i][y] == 4) for i in range(1, 4)) and \
                                all((user_board[x + 1][y + j] == 1 or user_board[x + 1][y + j] == 4) for j in
                                    range(-2, 3) if j != 0) and \
                                all((user_board[x + 3][y + j] == 1 or user_board[x + 3][y + j] == 4) for j in [-1, 1]):
                            for i in range(1, 4):
                                user_board[x + i][y] = 5
                            for j in range(-2, 3):
                                if j != 0:
                                    user_board[x + 1][y + j] = 5
                            user_board[x + 3][y - 1] = user_board[x + 3][y + 1] = 5

                    if 3 <= x <= 8 and 4 <= y <= 10:
                        if all((user_board[x][y - i] == 1 or user_board[x][y - i] == 4) for i in range(1, 4)) and \
                                all((user_board[x - i][y - 1] == 1 or user_board[x - i][y - 1] == 4) for i in
                                    range(1, 3)) and \
                                all((user_board[x + i][y - 1] == 1 or user_board[x + i][y - 1] == 4) for i in
                                    range(1, 3)) and \
                                all([
                                    (user_board[x - 1][y - 3] == 1 or user_board[x - 1][y - 3] == 4),
                                    (user_board[x + 1][y - 3] == 1 or user_board[x + 1][y - 3] == 4)
                                ]):
                            for i in range(1, 4):
                                user_board[x][y - i] = 5
                            for i in range(1, 3):
                                user_board[x - i][y - 1] = user_board[x + i][y - 1] = 5
                            user_board[x - 1][y - 3] = user_board[x + 1][y - 3] = 5

                    if 3 <= x <= 8 and 1 <= y <= 8:
                        if all((user_board[x][y + i] == 1 or user_board[x][y + i] == 4) for i in range(1, 4)) and \
                                all((user_board[x - i][y + 1] == 1 or user_board[x - i][y + 1] == 4) for i in
                                    range(1, 3)) and \
                                all((user_board[x + i][y + 1] == 1 or user_board[x + i][y + 1] == 4) for i in
                                    range(1, 3)) and \
                                all([
                                    (user_board[x - 1][y + 3] == 1 or user_board[x - 1][y + 3] == 4),
                                    (user_board[x + 1][y + 3] == 1 or user_board[x + 1][y + 3] == 4)
                                ]):
                            for i in range(1, 4):
                                user_board[x][y + i] = 5
                            for i in range(1, 3):
                                user_board[x - i][y + 1] = user_board[x + i][y + 1] = 5
                            user_board[x - 1][y + 3] = user_board[x + 1][y + 3] = 5

                    user_board[x][y] = 5

        for x in range(1, 11):
            for y in range(1, 11):
                if user_board[x][y] == 5:
                    cnt += 1

        if cnt == 30:
            return True
        else:
            return False

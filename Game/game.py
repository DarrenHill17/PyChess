import numpy as np

class Board():
    NORMAL_BOARD = [['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR'],
                    ['WP'] * 8,
                    ['**'] * 8,
                    ['**'] * 8,
                    ['**'] * 8,
                    ['**'] * 8,
                    ['BP'] * 8,
                    ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR']]

    def __init__(self) -> None:
        self.board = self.NORMAL_BOARD

    def get_piece(self, file: int, rank: int):
        return self.board[rank-1][file-1]
    
    def print_board(self, view: int) -> str:
        if view == 0: # White POV
            return str(np.flipud(np.array(self.board)))
        return str(np.fliplr(np.array(self.board)))
        # return str(self.board)

b = Board()
print(b.print_board(1))
print(b.get_piece(4, 1))

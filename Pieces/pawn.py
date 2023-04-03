from piece import Piece

class Pawn(Piece):
    has_moved = False

    def __init__(self, color) -> None:
        Piece.__init__(self, color)

    def is_legal(self, start_position, end_position) -> bool:
        if not self.has_moved:
            pass
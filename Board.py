# functions
# display
# move
# selected
from Player import Player
import chess

class Board:

    def __init__(self):
        self.p1 = Player("White")
        self.p2 = Player("Black")
        board = chess.Board()
        self.board = board
        pass
    
    def display_players(self):
        self.p1.display()
        self.p2.display()   

    def display_board(self):
        print(self.board)

    def current_player(self):
        if self.board.turn:
            return "White"
        else:
            return "Black"

    def move(self, move_str):
        if self.check_self_move(move_str):
            return
        move = chess.Move.from_uci(move_str)
        if move not in self.board.legal_moves:
            print("Invalid move")
            return
        if self.board.turn:
            self.p1.move(self.board, move)
        else:
            self.p2.move(self.board, move)
        
        result = self.check_status()
        print(move)

    def check_status(self):
        if self.board.is_checkmate():
            print("Checkmate")
        elif self.board.is_stalemate():
            print("Stalemate")
        elif self.board.is_insufficient_material():
            print("Insufficient material")
        elif self.board.is_seventyfive_moves():
            print("Seventy five moves")
        elif self.board.is_fivefold_repetition():
            print("Fivefold repetition")
        elif self.board.is_check():
            print("Check")
        elif self.board.is_game_over():
            print("Game over")
        else:
            print("Game in progress")
            return 1
        return 0
    
    def check_self_move(self, move):
        if move[0:2] == move[2:4]:
            print("Invalid move, self move")
            return True
        return False
        
    def piece_at(self, square):
        return self.board.piece_at(square)
    
    def get_squares(self):
        return chess.SQUARES
    

# def main():
#     b = Board()
#     print("Welcome to Chess")
#     b.display_players()
#     b.display_board()
#     while True:
#         print("Enter your move for", b.current_player())
#         move = input()
#         is_self_move = b.check_self_move(move)
#         if is_self_move:
#             continue
#         else:
#             b.move(move)
#         b.display_board()

# if __name__ == "__main__":
#     main()
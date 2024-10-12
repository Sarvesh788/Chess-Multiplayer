import pygame
import sys
from Player import Player

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8 
SQUARE_SIZE = WIDTH // COLS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
p1 = Player("white")
p2 = Player("black")

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Board with Pieces")

pieces_black = {
    "b_king": pygame.image.load("chess_maestro_bw/bk.png").convert_alpha(),
    "b_queen": pygame.image.load("chess_maestro_bw/bq.png").convert_alpha(),
    "b_bishop": pygame.image.load("chess_maestro_bw/bb.png").convert_alpha(),
    "b_knight": pygame.image.load("chess_maestro_bw/bn.png").convert_alpha(),
    "b_rook": pygame.image.load("chess_maestro_bw/br.png").convert_alpha(),
    "b_pawn": pygame.image.load("chess_maestro_bw/bp.png").convert_alpha(),
}

pieces_white = {
    "w_king": pygame.image.load("chess_maestro_bw/wk.png").convert_alpha(),
    "w_queen": pygame.image.load("chess_maestro_bw/wq.png").convert_alpha(),
    "w_bishop": pygame.image.load("chess_maestro_bw/wb.png").convert_alpha(),
    "w_knight": pygame.image.load("chess_maestro_bw/wn.png").convert_alpha(),
    "w_rook": pygame.image.load("chess_maestro_bw/wr.png").convert_alpha(),
    "w_pawn": pygame.image.load("chess_maestro_bw/wp.png").convert_alpha(),
}


for key in pieces_white:
    pieces_white[key] = pygame.transform.scale(pieces_white[key], (SQUARE_SIZE, SQUARE_SIZE))

for key in pieces_black:
    pieces_black[key] = pygame.transform.scale(pieces_black[key], (SQUARE_SIZE, SQUARE_SIZE))

piece_positions = {
    "b_king": p2.get_king_pos(), 
    "b_queen": p2.get_queen_pos(),
    "w_king": p1.get_king_pos(),
    "w_queen": p1.get_queen_pos(),
    "b_bishop": p2.get_bishop_pos(),
    "b_knight": p2.get_knight_pos(),
    "b_rook": p2.get_rook_pos(),
    "w_bishop": p1.get_bishop_pos(),
    "w_knight": p1.get_knight_pos(),
    "w_rook": p1.get_rook_pos(),
    "b_pawn": p2.get_pawn_pos(),
    "w_pawn": p1.get_pawn_pos()
}

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    for piece, positions in piece_positions.items():
        if isinstance(positions, list):
            for pos in positions:
                col, row = pos
                if piece.startswith("w_"):
                    screen.blit(pieces_white[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))
                elif piece.startswith("b_"):
                    screen.blit(pieces_black[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))
        else:
            col, row = positions
            if piece.startswith("w_"):
                screen.blit(pieces_white[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))
            elif piece.startswith("b_"):
                screen.blit(pieces_black[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))


def move_piece(piece, new_col, new_row, index):
    print(piece, new_col, new_row, index)
    if index is None:
        piece_positions[piece] = (new_col, new_row)
    else:
        piece_positions[piece][index] = (new_col, new_row)

def main():
    selected_piece = None  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = mouse_x // SQUARE_SIZE
                row = mouse_y // SQUARE_SIZE

                for piece in piece_positions.items():
                    if isinstance(piece[1], list):
                        for pos in piece[1]:
                            if pos == (col, row):
                                selected_piece = piece[0]
                                index = piece[1].index(pos)
                    else:
                        if piece[1] == (col, row):
                            selected_piece = piece[0]
                            index = None
                        

            elif event.type == pygame.MOUSEBUTTONUP and selected_piece:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                new_col = mouse_x // SQUARE_SIZE
                new_row = mouse_y // SQUARE_SIZE
                move_piece(selected_piece, new_col, new_row, index)
                selected_piece = None

        draw_board()
        draw_pieces()
        pygame.display.flip()

if __name__ == "__main__":
    main()


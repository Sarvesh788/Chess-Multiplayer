import pygame
import chess
from Board import Board

# Initialize Pygame and the chess board
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess Game with Mouse Interaction")

# Constants
SQUARE_SIZE = 100
PIECE_SIZE = SQUARE_SIZE // 2
FPS = 30

# Load piece images (using PNG files)
piece_images = {}
piece_types = ['p', 'r', 'n', 'b', 'q', 'k']
for color in ['w', 'b']:  # 'w' for white, 'b' for black
    for piece in piece_types:
        image_file = f'alpha/{color}{piece}.svg'  # Load PNG images
        image = pygame.image.load(image_file)
        scaled_image = pygame.transform.smoothscale(image, (SQUARE_SIZE // 1.5, SQUARE_SIZE // 1.5))
        piece_images[color + piece] = scaled_image

board = Board()

# Draw the chessboard
def draw_board():
    colors = [pygame.Color("#f6ffe3"), pygame.Color("#81b64c")]
    for rank in range(8):
        for file in range(8):
            color = colors[(rank + file) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(file * SQUARE_SIZE, rank * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Draw the chess pieces
def draw_pieces(board):
    for square in board.get_squares():
        piece = board.piece_at(square)
        if piece:
            piece_image = piece_images[f"{'w' if piece.color == True else 'b'}{piece.symbol().lower()}"]
            row, col = divmod(square, 8)
            x = col * SQUARE_SIZE + (SQUARE_SIZE - PIECE_SIZE) // 2
            y = (7 - row) * SQUARE_SIZE + (SQUARE_SIZE - PIECE_SIZE) // 2
            screen.blit(piece_image, pygame.Rect(x, y, PIECE_SIZE, PIECE_SIZE))

def get_square_under_mouse(pos):
    x, y = pos
    row = 7 - (y // SQUARE_SIZE)
    col = x // SQUARE_SIZE
    return chess.square(col, row)

def main():
    clock = pygame.time.Clock()
    selected_square = None
    running = True
    while running:
        draw_board()
        draw_pieces(board)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                selected_square = get_square_under_mouse(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if selected_square is not None:
                    target_square = get_square_under_mouse(event.pos)
                    move = chess.Move(selected_square, target_square)
                    print(move)
                    board.move(move.uci())
                    selected_square = None
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()

from time import time
from math import log2
from chess import pgn, Board
from chessutil import get_pgn_games
import sys

def decode(pgn_string: str, output_file_path: str):
    start_time = time()
    total_move_count = 0
    games = get_pgn_games(pgn_string)
    
    with open(output_file_path, "w") as output_file:
        output_file.write("")
    
    output_file = open(output_file_path, "ab")
    output_data = ""
    
    for game in games:
        chess_board = Board()
        game_moves = list(game.mainline_moves())
        total_move_count += len(game_moves)
        
        for move in game_moves:
            legal_move_ucis = [lm.uci() for lm in list(chess_board.generate_legal_moves())]
            move_binary = bin(legal_move_ucis.index(move.uci()))[2:]
            
            max_binary_length = int(log2(len(legal_move_ucis)))
            move_binary = move_binary.zfill(max_binary_length)
            chess_board.push_uci(move.uci())
            output_data += move_binary
            
            if len(output_data) % 8 == 0:
                output_file.write(bytes([int(output_data[i*8:i*8+8], 2) for i in range(len(output_data)//8)]))
                output_data = ""
    
    print(f"Decoded data has been written to {output_file_path}")

def run_decoder():
    if len(sys.argv) != 3:
        print("Usage: python run_decoder.py <input_pgn_file> <output_file>")
        sys.exit(1)
    
    input_pgn_file = sys.argv[1]
    output_file_path = sys.argv[2]
    
    try:
        with open(input_pgn_file, 'r') as f:
            pgn_string = f.read()
        decode(pgn_string, output_file_path)
    except FileNotFoundError:
        print(f"Error: File '{input_pgn_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_decoder()
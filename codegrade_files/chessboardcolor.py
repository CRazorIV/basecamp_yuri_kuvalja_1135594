# the color of a square depends on the combination of its file (letter) and rank (number).
# formula: file_index + rank_index = total = color.

user_chess_position = input("Enter the chess position: ")

chess_position_filename = user_chess_position[0]   
chess_position_number = user_chess_position[1]      

file_index = "abcdefgh".index(chess_position_filename.lower()) 
rank_index = int(chess_position_number) - 1                  

total = file_index + rank_index

if total % 2 == 0:
    color = "Black"
else:
    color = "White"

print(f"{color}")
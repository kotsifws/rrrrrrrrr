import random


def play_games(rows, columns):
    # points
    white = 0
    black = 0
    for loop in range(100):
        # select random positions for pieces
        bl_knight = (random.randint(0, rows - 1), random.randint(0, columns - 1))
        w_tower = (random.randint(0, rows - 1), random.randint(0, columns - 1))
        while bl_knight == w_tower:
            w_tower = (random.randint(0, rows - 1), random.randint(0, columns - 1))
        # Calculate points
        # tower gets a point
        # if the knight is in the same row or column as the tower
        if w_tower[0] == bl_knight[0] or w_tower[1] == bl_knight[1]:
            white += 1
        # knight gets a point
        # if the tower is in the same diagonal as the knight
        if abs(w_tower[0] - bl_knight[0]) == abs(w_tower[1] - bl_knight[1]):
            black += 1
    # print point totals
    print("Total Points White: ", white)
    print("Total Points Black: ", black)


print("Chessboard size: 7x8")
play_games(7, 8)
print("Chessboard size: 7x8")
play_games(8, 8)

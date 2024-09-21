# Program to create a theater seating arrangement and assign reserved seats

theater_seating = [['N' for _ in range(5)] for _ in range(5)]

reserved_seats = [(1, 1), (1, 2), (2, 4), (3, 1), (4, 3),(0,0)]

for seat in reserved_seats:
    row, col = seat
    theater_seating[row][col] = 'R'

print("Theater Seating Arrangement:")
for row in theater_seating:
    print(" ".join(seat for seat in row))

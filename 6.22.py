#Alexander Ho
#1677933


first_a = int(input())
first_b = int(input())
first_sol = int(input())
second_a = int(input())
second_b = int(input())
second_sol = int(input())

check = False
for x in range(-10, 10, 1):
    for y in range(-10, 10, 1):
        if ((first_a * x + first_b * y == first_sol) and (second_a * x + second_b * y == second_sol)):
            check = True
            print(x, y)

if (check == False):
    print('No solution')
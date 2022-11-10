from solver import solve_quadratic
x = int(input("Enter the a,b,c values:\n"))
y = int(input())
z = int(input())
answer = solve_quadratic(x, y, z)
print(answer)
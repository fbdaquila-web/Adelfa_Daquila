# =============== #
# [ IMPORT & Context / P1 ] #
# --------------- #
import math

print("Hello, User. \nThis is an algorithm made to compute the length of a triangle's hypotenuse when given the other two sides' lengths.")

# ============== #
# [ INPUT / P3 ] #
# -------------- #
side_a_length = float(input("Enter the length of one of the two sides (a): "))
side_b_length = float(input("Enter the length of the other of the two sides (b): "))

# ================ #
# [ PROCESS / P4 ] #
# ---------------- #
# Formula for the length of a triangle's hypotenuse, adapted into python code.
hypotenuse_length = float(math.sqrt(pow(side_a_length, 2) + pow(side_b_length, 2)))

# =============== #
# [ OUTPUT / P5 ] #
# --------------- #
print(f"The length of the triangle's hypotenuse is {hypotenuse_length:.3g} units.")
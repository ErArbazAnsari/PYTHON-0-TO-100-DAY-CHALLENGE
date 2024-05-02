# Operators in Python
# Operators in Python are the special symbols that perform arithmetic or logical computations. The value that the operator operates on is called the operand.

# Arithmetic Operators
x = 10
y = 3

addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y
modulus = x % y
exponentiation = x**y
floor_division = (
    x // y
)  # Floor division is division that results into whole number adjusted to the left in the number line. Example of floor division is 3//2 = 1. The division of 3 by 2 is 1.5. So the floor division of 3 by 2 is 1.

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)
print("Floor Division:", floor_division)

# Comparison Operators
a = 5
b = 10

print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print("a == b:", a == b)
print("a != b:", a != b)

# Logical Operators
p = True
q = False

print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

# Assignment Operators
x = 5
x += 3
print("x:", x)

# Bitwise Operators
a = 10
b = 7

bitwise_and = (a & b)  # Bitwise AND operator sets each bit to 1 if both bits are 1. Otherwise, it sets the bit to 0. For example, 10 & 7 = 2 because the binary representation of 10 is 1010 and the binary representation of 7 is 0111. So, the binary representation of 2 is 0010.
bitwise_or = a | b
bitwise_xor = a ^ b
bitwise_not = ~a # Bitwise NOT operator inverts all the bits. For example, ~10 = -11 because the binary representation of 10 is 1010. So, the binary representation of -11 is 0101.
left_shift = a << 2 # Bitwise left shift operator shifts the bits to the left by the specified number of positions. For example, 10 << 2 = 40 because the binary representation of 10 is 1010. So, the binary representation of 40 is 101000.
right_shift = a >> 2

print("Bitwise AND:", bitwise_and)
print("Bitwise OR:", bitwise_or)
print("Bitwise XOR:", bitwise_xor)
print("Bitwise NOT:", bitwise_not)
print("Left Shift:", left_shift)
print("Right Shift:", right_shift)

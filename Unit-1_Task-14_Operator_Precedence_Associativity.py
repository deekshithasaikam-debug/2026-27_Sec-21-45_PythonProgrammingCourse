# Operator Precedence and Associativity

# Operator Precedence
result1 = 10 + 5 * 2
result2 = (10 + 5) * 2

print("Operator Precedence:")
print("10 + 5 * 2 =", result1)
print("(10 + 5) * 2 =", result2)

# Operator Associativity
result3 = 20 - 5 - 3
result4 = 20 / 5 / 2

print("\nOperator Associativity:")
print("20 - 5 - 3 =", result3)
print("20 / 5 / 2 =", result4)

# Right-to-left associativity of exponentiation
result5 = 2 ** 3 ** 2

print("\nExponentiation Associativity:")
print("2 ** 3 ** 2 =", result5)
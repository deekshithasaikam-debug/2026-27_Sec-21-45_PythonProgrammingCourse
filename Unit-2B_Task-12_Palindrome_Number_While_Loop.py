n = int(input("Enter a number: "))
original_n = n
reverse = 0
while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10
if reverse == original_n:
    print(f"{original_n} is a palindrome.")
else:
    print(f"{original_n} is not a palindrome.")
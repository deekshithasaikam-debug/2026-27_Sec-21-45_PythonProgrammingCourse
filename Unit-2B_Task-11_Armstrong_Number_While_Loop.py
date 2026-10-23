n = int(input("Enter a number: "))
original_n = n
sum_of_cubes = 0
while n > 0:
    digit = n % 10
    sum_of_cubes += digit ** 3
    n //= 10
if sum_of_cubes == original_n:
    print(f"{original_n} is an Armstrong number.")
else:
    print(f"{original_n} is not an Armstrong number.")
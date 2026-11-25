# Example solution: print_details with **kwargs
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Krishna", age=26, city="Guntur")
import sys


def add(a,b):
    return a + b


def multiply(a, b):
    return a * b


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <num1> <num2>")
        sys.exit(1)

    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    sum_result = add(num1, num2)
    product_result = multiply(num1, num2)
    print(f"The sum of {num1} and {num2} is {sum_result}")
    print(f"The product of {num1} and {num2} is {product_result}")
    

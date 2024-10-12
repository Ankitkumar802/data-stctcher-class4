def binary_to_decimal(binary):
    decimal = 0
    binary = binary[::-1]  # Reverse the binary string to handle powers of 2 easily

    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += 2 ** i
    
    return decimal


def decimal_to_binary(decimal):
    binary = ""
    
    if decimal == 0:
        return "0"
    
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2

    return binary


def main():
    print("Choose conversion type:")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        binary = input("Enter a binary number: ")
        decimal = binary_to_decimal(binary)
        print(f"Decimal equivalent of binary {binary} is: {decimal}")
    
    elif choice == '2':
        decimal = int(input("Enter a decimal number: "))
        binary = decimal_to_binary(decimal)
        print(f"Binary equivalent of decimal {decimal} is: {binary}")
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

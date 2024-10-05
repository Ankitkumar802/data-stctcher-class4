
while True:
    number = int(input("Input number: "))
    s = 0
    temp = number


    while temp != 0:
        digit = temp % 10
        s = s + digit ** 3
        temp = temp // 10  

    if number == s:
        print(number, "is an Armstrong number")
    else:
        print(number, "is not an Armstrong number")

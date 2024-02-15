def isprime(num):
    if num <= 0:
        print("you have enter negative values or Zero. They are not prime")

    elif num==1:
        print(f'{num} is not prime')

    else:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1

        if count == 2:
            print(f"The {num} is prime")
        else:
            print(f"The {num} is not prime")


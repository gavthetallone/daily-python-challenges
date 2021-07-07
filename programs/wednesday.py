def evendigits(user_input):
    numbers_list = user_input.split()

    num1 = int(numbers_list[0])
    num2 = int(numbers_list[1])
    
    number_string = ""

    for count in range(num1, num2+1):
        if count % 2 == 0:
            if count > 9:
                temp = [int(digit) for digit in str(count)]
                if int(temp[0]) % 2 == 0 and int(temp[1]) % 2 == 0:
                    number_string += (str(count) + ", ")
            else:
                number_string += (str(count) + ", ")
        else:
            continue
    return number_string

if __name__ == "__main__":  
    print(evendigits(input("Please enter two integers: ")))
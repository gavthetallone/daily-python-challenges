print("### THE FIBONACCI SEQUENCE ###\n")

def fibonacci(number):
    n = int(number)                     #converting user input string into integer
    fib_list = [0]*(n+1)                #creating a list of zeros, of size n+1

    count = 0
    for count in range(0, n+1):         #looping through list and storing fibonacci sequence
        if count == 0:
            fib_list[count] = 0
        elif count == 1:
            fib_list[count] = 1
        elif count > 1:
            fib_list[count] = fib_list[count-1] + fib_list[count-2]     #fibonacci formula

    return(f"\n\tf(n) = {fib_list[n]}\n")           #returning value in list at position 'n'
                                                    #formatting output to include new lines/tabs etc.
                                                    
if __name__ == "__main__":
    print(fibonacci(input("Please enter an integer value. \n\nFor n = ")))     #calling fibonacci function and taking user input
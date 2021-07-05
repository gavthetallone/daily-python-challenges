print("Please enter a random set of words. For example, 'hello world and practice makes perfect and hello world again'")
user_input = str(input("\n: "))       #taking user input

input_split = user_input.split()      #splitting input and placing str values into a list

set_inputs = set(input_split)         #converting list into a set to remove repeating values
sorted_inputs = sorted(set_inputs)    #sorted into alphanumeric order

count = 0
answer = ""

for count in range(0,len(sorted_inputs)):
    answer += (sorted_inputs[count] + " ")    #storing and concatenating the set values into a string
    count += 1

print("\n:", answer)
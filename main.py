# -- ABPL(Array Based Programming Language) --
array = [0]
index = 0
def evaluate(command):
    global array
    global index
    if command[0] == "A":
        array[index] += int(command[1:])
    elif command[0] == "S":
        array[index] -= int(command[1:])
    elif command == "PUSH":
        array.append(0)
    elif command[0] == "R":
        del array[int(command[1:])]
    elif command == "CHARACTER":
        print(chr(array[index]))
    elif command == "DEBUG":
        print(f"Array: {array}\nIndex: {index}\nCurrent value at Index: {array[index]}")
    elif command == "FORWARD":
        index += 1
    elif command == "BACKWARD":
        index -= 1
file_path = 'program.abpl'
with open(file_path, 'r') as file:
    words = file.read().split()
for word in words:
    evaluate(word)
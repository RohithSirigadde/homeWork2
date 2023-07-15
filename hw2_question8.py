enterfile = input("Enter the file name: ")
file = open(enterfile, 'r')
line_count = 0
for line in file:
    line_count = line_count + 1
print("The number of lines in this text file is", linecount)
line_number = 0
while True:
    num = int(input("Please enter a line number or press 0 to exit: "))
if num >=1 and num <= line_count:
    file = open(enterfile, 'r')
    for lines in file:
        line_number = line_number + 1
        if line_number == num:
            print(lines)
else:
    if num == 0:
        print("Thanks for using the program")
        break

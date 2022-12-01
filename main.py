f = open("input_day_1.txt", "r")
calories_list = []
for line in f:
    if line != '\n':
        calories_list.append(int(line.strip()))
    else:
        calories_list.append(line)
f.close()

max = 0
sum=0
for i in range(len(calories_list)):
    if type(calories_list[i]) == int:
        sum+=calories_list[i]
    else:
        if sum > max:
            max = sum
        sum = 0   

print(calories_list[-1])
print(max)


f = open("input_day_1.txt", "r")
calories_list = []
for line in f:
    if line != '\n':
        calories_list.append(int(line.strip()))
    else:
        calories_list.append(line)
f.close()


sum=0
max_list = [0,0,0]
for i in range(len(calories_list)):
    if type(calories_list[i]) == int:
        sum+=calories_list[i]
        
    if calories_list[i] == '\n' or i == (len(calories_list)-1):
        if sum > max_list[0]:
            max_list[2]=max_list[1]
            max_list[1] = max_list[0]
            max_list[0] = sum
        elif sum > max_list[1]:
            max_list[2]=max_list[1]
            max_list[1] = sum
        elif sum > max_list[2]:
            max_list[2] = sum
        sum = 0   

total_sum = 0
for num in max_list:
    total_sum += num

print(total_sum)



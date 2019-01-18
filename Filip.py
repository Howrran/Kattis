num_one, num_two = map(int,input().split(' '))
num1 = str(num_one)
num2 = str(num_two)
num1 = num1[::-1]
num2 = num2[::-1]
num_one = int(num1)
num_two = int(num2)

if num_one > num_two:
    print(num_one)
else:
    print(num_two)

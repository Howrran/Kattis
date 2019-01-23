money, k = map(int,input().split())
price_list = list(map(int,input().split()))
price_list.sort()
counter = 0

while(len(price_list) > 0):
    if money >= price_list[0]:
        money -= price_list[0]
        counter += 1
        price_list.pop(0)
    else:
        break

print(counter)

n = int(input())
first_orders = list(input() for i in range(n))
second_orders = list(input() for i in range(n))
cnt = 0
forward_car_dict = dict()
after_car_dict = dict()

for i in range(1,n):
    for j in range(i):
        if first_orders[i] not in forward_car_dict:
            forward_car_dict[first_orders[i]] = [first_orders[j]]
        else:
            forward_car_dict[first_orders[i]].append(first_orders[j])

for i in range(n):
    if i == 0:
        after_car_dict[second_orders[i]] = []
    for j in range(i):
        if second_orders[i] not in after_car_dict:
            after_car_dict[second_orders[i]] = [second_orders[j]]
        else:
            after_car_dict[second_orders[i]].append(second_orders[j])

for k,v in after_car_dict.items():
    if k not in forward_car_dict:
        continue
    forwards = forward_car_dict[k]
    for i in forwards:
        if i not in v:
            cnt += 1
            break
print(cnt)
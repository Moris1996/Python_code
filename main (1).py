import random


def func(min_value, max_value, amount):
    i = 0
    lst=[]
    while i < amount:
        lst += [random.randint(min_value, max_value)]
        i += 1

    return lst


print("please enter min value : ")
min_value = input()
print("please enter max value : ")
max_value = input()
while int(min_value) > int(max_value):
    print("Error : min value cant be bigger then max value")
    print("please enter min value : ")
    min_value = input()
    print("please enter max value : ")
    max_value = input()

print("please enter amount : ")
amount = input()

print(func(int(min_value), int(max_value), int(amount)))




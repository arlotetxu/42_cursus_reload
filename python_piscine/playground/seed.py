import random

my_list = [1, 3, 5, 3, 4, 8, 9, 0]

random.seed(12)


for i in range(10):
    choice = random.choice(my_list)
    print(choice)


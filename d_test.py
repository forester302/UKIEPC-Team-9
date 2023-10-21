import random

test_bounds = (1000000//3)*3
print(test_bounds)
n_list = []
for i in range(500):
    n_list.append(random.randint(1, test_bounds+1))
print(sum(n_list))
f_n_list = []
for n in n_list:
    f_n_list.append(1)
    f_n_list.append(n)
    f_n_list.append(n+1)
print(len(f_n_list))
with open("out", "w") as f:
    for n in f_n_list:
        print(n, file=f, end=" ")

    
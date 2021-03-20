# Task 2

import pickle

with open('task2', 'rb') as file:
    _sum = pickle.loads(file.read())
    total_sum = sum(_sum) / len(_sum)
    print(total_sum)

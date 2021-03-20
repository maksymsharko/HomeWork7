# Task №1(page 1)

dict_task_1_1 = {}

with open("task1.txt") as file:
    syntax = file.readlines()
    for string in range(len(syntax)):
        syntax[string] = syntax[string].replace("\n", "")
    dict_task_1_1 = {syntax[string]: syntax[string + 1] for string in range(0, len(syntax), 2)}
    print(dict_task_1_1)


# Task №1(page 2)

task_1_2 = ''

del syntax[0: len(syntax): 2]
for string in range(len(syntax)):
    task_1_2 = task_1_2 + syntax[string]

with open("task1.txt", "w") as file:
    file.writelines(task_1_2)
print(task_1_2)
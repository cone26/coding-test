from collections import Counter
tasks = ["A","A","A","B","B","B"]
n = 2
counter = Counter(tasks)
for task,i in counter.most_common(n+1):
    print(task,i)
    counter.subtract()


print(4 % 5)
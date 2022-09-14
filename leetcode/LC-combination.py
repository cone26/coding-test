import itertools
# dfs


def combine(n,k):
    results =[]
    def dfs(elements, start, k):
        if k == 0 : 
            results.append(elements[:])
            return
        for i in range(start,n+1):
            elements.append(i)
            print(f'i = {i}, elements = {elements}, start = {start}, k = {k},results = {results}')
            dfs(elements,i+1,k-1)
            elements.pop()

    dfs([],1,k)
    return results

answer  = combine(4,2)
print(answer)
# itertools
print(itertools.combinations(range(1,n+1,),k))
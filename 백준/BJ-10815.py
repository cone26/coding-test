# 숫자 카드
n = int(input())
# 1.binary search로 찾기 위해서 검색할 list를 오름차순으로 정렬해준다.
lst1 = sorted(list(map(int,input().split()))) 
m = int(input())
lst2 = list(map(int,input().split()))

# 2. binary search 함수
def binarySearch(lst,start,end,i):
    # 2-1 답이 마지막 숫자일 경우도 있어서 start랑 end가 같을 경우까지 허용해야함
    while start <= end :
        # 2-2 mid = 검색 포인터 / 포인터를 이동하며 해당 숫자를 탐색한다.
        mid = (start+end) //2
        # 2-3 탐색 과정/ 검색 대상 리스트가 정렬되어 있기 때문에 반씩 잘라가며 검색할 수 있다.
        if lst[mid] == i : return 1
        elif lst[mid] < i : start = mid+1
        else : end = mid - 1
    # 만약 while문 조건에서 벗어난다면 => 검색할 대상이 존재하지 않음. 0을 return
    return 0
# 3. 존재하는지 확일할 List를 돌며 함수를 실행시킨다.
for i in lst2 :
    answer = binarySearch(lst1,0,n-1,i)
    print(answer,end=' ')

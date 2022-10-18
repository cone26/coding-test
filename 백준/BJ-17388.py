# 와글와글 숭고한
S,K,H = map(int,input().split())
dic = {
    S : "Soongsil",
    K : 'Korea',
    H : 'Hanyang'
}
if S + K + H < 100 :
    print(dic[min(S,K,H)])
else : print('OK')
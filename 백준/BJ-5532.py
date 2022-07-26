# 방학 숙제
# input l :방학 일수, b:수학 풀어야하는 페이지 수 , a:국어 풀어야하는 페이지,c:국어 최대 풀이 페이지,d:수학 최대 풀이 페이지
vacation=[]
for _ in range(5): vacation.append(int(input()))
[days, m_page, k_page, m_limit, k_limit] = vacation
while True :
    m_page -= m_limit; k_page -= k_limit
    days -= 1
    if m_page <= 0 and k_page <= 0: break
print(days)
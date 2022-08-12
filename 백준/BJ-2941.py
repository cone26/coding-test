# 크로아티아 알파벳
alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input().rstrip()
for i in alphabet:
    if i in word : word = word.replace(i,'0')
print(len(word))

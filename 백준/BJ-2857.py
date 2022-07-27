# FBI
fbi = []
for j in range(5):
    member = input()
    if 'FBI' in member :
        for i in member : 
            if not(i.isupper()) or not(i.isnumeric()) or i != '-': break
        fbi.append(str(j+1))

print('HE GOT AWAY!') if len(fbi) == 0 else print(' '.join(fbi))
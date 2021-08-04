x = input('ingrese la palabra: ')
n = 0
m = 0
o = 0
p = 0
q = 0
for i in x :
    if i == 'a':
        n = n+1
    elif i == 'e':
        m = m+1
    elif i == 'i':
        o = o+1
    elif i == 'o':
        p = p+1
    elif i == 'u':
        q = q+1

print (f'hay {n} letras a,{m} letras e, {o} letras i,{p} letras o y {q} letras u')
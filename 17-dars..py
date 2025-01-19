# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:14:49 2024

@author: MS1517
"""
"""
ism=input('Ismingizni kiriting: ')
savol=f'Salom, {ism.title()}. Yoshingiz nechchida?'
yosh=input(savol)
yosh=int(yosh)
height=input('Boyingiz nechchi metr? ')
height=float(height)
"""
"""
son=1
while son<=5:
    print(son,end=' ')
    son+=1
    
print('Dastur tugadi')

a=3 
while a<=9 :
    print(a,end=' ')
    a=a+1
"""
"""
print('Kiritilgan sonning kvadratini qaytruvchi dastur.')
savol='Istalgan sonni kiriting'
savol+="(dasturni to'xtatish uchun 'exit' deb yozing):"
qiymat=' '
while qiymat !='exit': 
    qiymat=input(savol)
    if qiymat !='exit':
        print(float(qiymat)**2)
print('Dastur tugadi.')
 """ 
""" 
#Ishora bilan 
print('Kiritilgan sonning kvadratini qaytruvchi dastur.')
savol='Istalgan sonni kiriting'
savol+="(dasturni to'xtatish uchun 'exit' deb yozing):"
ishora=True
while ishora:
    qiymat=input(savol)
    if qiymat =='exit':
        ishora=False
    else:
        print(float(qiymat)**2)
print('Dastur tugadi!')

print('Kiritilgan sonning kvadratini qaytruvchi dastur.')
savol='Istalgan sonni kiriting'
savol+="(dasturni to'xtatish uchun 'exit' deb yozing):"
while True:
    qiymat=input(savol)
    if qiymat =='exit':
        break
    else:
        print(float(qiymat)**2)
print('Dastur tugadi!')
"""
#break 
"""
sonlar=list(range(1,11))
for son in sonlar:
    if son ==5:
        break
    print(f"{son} ning kvadrati {son**2} ga teng")

#continue

sonlar=list(range(1,11))
for son in sonlar:
    if son ==5:
        continue
    print(f"{son} ning kvadrati {son**2} ga teng")

son=0
while son<10:
    son+=1
    if son%2!=0:
        continue
    else:
        print(son)
"""







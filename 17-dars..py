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
# break
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

##### Amaliyot#######

#1.
'''
kitoblar = []  # Kitoblar ro'yxatini yaratam

while True:
    kitob = input("Yaxshi ko'rgan kitobingizni kiriting (yoki 'stop' deb yozing to'xtatish uchun): ")
    kitoblar.append(kitob) 
    if kitob.lower() == 'stop':  # Agar foydalanuvchi 'stop' deb yozsa
        print("Dastur tugadi.")
        break  # Dastur to'xtaydi
       
        
print("\nSiz yaxshi ko'rgan kitoblar:")
for kitob in kitoblar:
    print(f"- {kitob}")
'''
#2.


# Muzeyga chipta narhi foydalanuvchining
# yoshiga bog'liq:
# 7 dan yoshlarga - 2000 so'm,
# 7-18 gacha 3000 so'm,
# 18-65 gacha 10000 so'm,
# 65 dan kattalarga bepul.
# Shunday while tsikl yozingki,
# dastur foydalanuvchi yoshini so'rasin
# va chipta narhini chiqarsin.
# Foydalanuvchi exit yoki quit deb yozganda
# dastur to'xtasin (ikkita shartni ham tekshiring).

savol='Yoshingizni kiriting:'
while True:
    qiymat=input(savol)
    if qiymat=='exit ' or qiymat=='quit':
        break
    yosh=int(qiymat)
    if yosh<7:
        narx=2000
    elif 7<=yosh<18:
        narx=3000
    elif 18<=yosh<65:
        narx=10000
    else:
        narx=0
    if narx==0 :
        print('sizga chipta bepul.')
    else:
        print(f"Sizga bilet {narx} so'm.")
        
        
        













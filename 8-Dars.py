# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:02:13 2024

@author: User
"""

#Aksar holatlarda ro'yxat ichidagi elementlarni alifbo ketma-ketligida tartiblash 
#talab qilinishi mumkin. Buning uchun list uchun maxsus 
#   .sort() metodidan foydalanamiz.

'''cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort(reverse=True)
print(cars)'''

#Ketma-ketligini buzmagan holda ro'yxatni tartiblash talab qilinishi mumkin. 
#Buning uchun    sorted()
# funktsiyasidan foydalanamiz:

'''mexmonlar=['Rustam','Doston','Olim','Avaz','Begzod']
print(sorted(mexmonlar,reverse=True))'''

#Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) talab qilinishi 
#mumkin. Buning uchun  .reverse()  metodidan foydalanamiz.

#mevalar=['olma','bexi','shaftoli','olcha']
#mevalar.reverse()
#print(mevalar)

#Ro'yxatning uzunligi, ya'ni uning ichidagi elementlar sonini aniqlash uchun 
#len()
# funktsiyasidan foydalanamiz:
  
#print(len(mevalar))

#range() FUNKTSIYASI
#Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz 
#mumkin. list() funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz:

#sonlar=list(range(5,15))
#print(sonlar)
#juft_sonlar=list(range(0,20,2))
#toq_sonlar=list(range(1,20,2))
#print('Juft sonlar:',juft_sonlar)
#print('Toq sonlar:',toq_sonlar)
#print(min(juft_sonlar))
#print(max(juft_sonlar))
#print(sum(juft_sonlar))
#mening_mevalarim=mevalar[1:4]
#print(mening_mevalarim)

'''hamkasblar=['Temur','Shagzod','Begzod','Siroj','Sherzod','Adham']
smendoshlar=hamkasblar[:]
smendoshlar.append('Saloh')
smendoshlar.append('Bobur')
smendoshlar.append('Rustam')
print(hamkasblar)
print(smendoshlar)'''

#TUPLES - O'ZGARMAS RO'YXAT

'''hamkasblar=('Temur','Shagzod','Begzod','Siroj','Sherzod','Adham')

print(hamkasblar[-2])
print(hamkasblar[2:])

hamkasblar=list(hamkasblar)

hamkasblar[1]='Farrux'
hamkasblar.append('Qobil')
hamkasblar.remove('Adham')

hamkasblar=tuple(hamkasblar)
print(hamkasblar)'''

#############       AMALIYOT
'''davlatlar=['Ozbekiston','Qozogiston','Tojigiston','Turmaniston','Qirgiziston']
print(davlatlar)
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar,reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)'''
juft_sonlar1200=list(range(120,1201,2))
#print('juft_sonlar: ',juft_sonlar1200)
#print('Juft_sonlar yiindisi: \n>>>',sum(juft_sonlar1200))
#a=max(juft_sonlar1200)
#b=min(juft_sonlar1200)
#print('Eng katta va eng kichkina qiymatlar ayirmasi: ', max(juft_sonlar1200)-min(juft_sonlar1200),'ga teng')
#print('a=',a)
#('b=',b)
#print('Eng katta va eng kichkina qiymatlar ayirmasi:\n>>> a-b=', a-b )
'''print(len(juft_sonlar1200))
sonlar1=juft_sonlar1200[1:21]
sonlar2=juft_sonlar1200[261:281]
sonlar3=juft_sonlar1200[-20:]
print(sonlar1)
print(sonlar2)
print(sonlar3)'''
taomlar=['osh','kabob','mastava','somsa','manti']
nonushta=taomlar[:]
nonushta.remove('osh')
nonushta.remove('kabob')
nonushta.append('qaymoq')
nonushta.append('murobbo')
print(nonushta)
print(taomlar)
#nonushta=tuple(nonushta)
print(nonushta)
nonushta[0] = "qaymoq va non"
print(nonushta)





















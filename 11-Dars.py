# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 02:28:15 2024

@author: User
"""
'''kun=input('Bugun nima kun?\n>>>')
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni.') '''

'''kun=input('Bugun nima kun?\n>>>')
harorat=float(input('Havo harorati qanay?\n>>>'))
if kun.lower()=='yakshanba' and harorat>30:
    print('Cho\'milishga ketdik!')
elif kun.lower()=='yakshanba' and harorat<30:
    print('Uyda dam olamiz!')'''

'''kun=input('Bugun nima kun?\n>>>')
harorat=float(input('Havo harorati qanay?\n>>>'))
if kun.lower()=='shanba' or kun.lower()=='yakshanba' and harorat>30:
    print('Cho\'milishga ketdik!')
elif kun.lower()=='shanba' or kun.lower()=='yakshanba' and harorat<30:
    print('Uyda dam olamiz!')'''

'''narx=15000
choy=True
salat=True
if choy and salat:
    narx=narx+10000
elif choy or salat:
    narx=narx+5000

print(f'Jami {narx} so\'m')'''

'''narx=15000
choy=True
non=True
kampot=True
salat=False
asarti=False

if choy:
    print('Mijoz choy sotib oldi')
    narx=narx+3000
if non:
    print('Mijoz non sotib oldi')
    narx=narx+2000

if salat:
    print('Mijoz salat sotib oldi')
    narx=narx+5000

if kampot:
     print('Mijoz kampot sotib oldi')
     narx=narx+6000  

if asarti:
    print('Mijoz asarti sotib oldi')
    narx=narx+7000

print(f'Jami summa {narx} so\'m')'''

'''menu=['somsa','manti','sho\'rva','osh','shashlik']
ovqat=input('Nima ovqat yeysiz?\n>>>')
if ovqat.lower() in menu:
    print('Buyurtma qabul qilindi.')
else:
    print('Afsuski bizda bunday ovqat yo\'q.')'''

'''menu=['somsa','manti','sho\'rva','osh','shashlik']
ovqat=input('Nima ovqat yeysiz?\n>>>')
if ovqat.lower() not in menu:
    print('Afsuski bizda bunday ovqat yo\'q.')
else:
    print('Buyurtma qabul qilindi.')'''

'''menu=['somsa','manti','sho\'rva','osh','shashlik']
buyurtmalar=['kabob','honim','lagmon','osh','somsa','sho\'rva']

   for taom in buyurtmalar:
      if taom in menu:
        print(f'Menuda {taom} bor')
      else:
         print(f'Kechirasiz ,menuda {taom} yo\'q')'''

# Buyurtmalarda taom bolsa qaysi buyurtmadagi taomlar mentuda borligini chiqaradi.

'''menu=['somsa','manti','sho\'rva','osh','shashlik']
buyurtmalar=['kabob','honim','lagmon','osh','somsa','sho\'rva']
#buyurtmalar=[]    
if buyurtmalar:
     print(f'buyurtmalarda {len(buyurtmalar)} ta zakaz bor')         
else:
     print('Kechirasiz,buyurtmalarda taom yoq') '''

'''for taom in buyurtmalar:
     if taom in menu:
        print(f'Menuda {taom} bor')
     else:
        print(f'Kechirasiz ,menuda {taom} yo\'q')'''

if 11%2:


son = float(input("Juft son kiriting: "))
if son % 2:
    print('Bu son juft emas.')
else:
    print("Rahmat!")

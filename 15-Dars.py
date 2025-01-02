# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 14:17:49 2024

@author: User
"""

talaba_0 = {
    'ism': 'murod olimov',
    'yosh': 20,
    't_yil': 2000
}

'''print(talaba_0['ism'].title())
for kalit, qiymat in talaba_0.items():
    print(f"Kalit:{kalit}")
    print(f"Qiymat:{qiymat}\n")'''

'''telefonlar={
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
for k,q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q} ")'''
    
maxsulotlar={
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000
    }
'''print(maxsulotlar.keys())    
print('Do\'kondagi maxsulotlar:')    
for maxsulot in maxsulotlar.keys():
    print(maxsulot.title())'''    
    
'''print('Do\'kondagi maxsulotlar:')    
for maxsulot in maxsulotlar.keys():
    print(maxsulot.title())'''
    
bozorlik=['anor','uzum','non','baliq']
for maxsulot in maxsulotlar:
    if maxsulot in bozorlik:
        print(f'{maxsulot.title()} {maxsulotlar [maxsulot]} so\'m' )

for buyum in bozorlik:
    if buyum not in maxsulotlar:
        print(f'Iltimos dokonga {buyum} ham olib keling.')

'''print('Do\'konimizdagi maxsulotlar')
for maxsulot in sorted(maxsulotlar):
    print(maxsulot.title())'''
    
'''telefonlar={
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orifi':'nokia 330', 
    'hali': 'galaxy s9' ,
    'rolim':'mi 11 pro',
    'lorif':'nokia 3310', 
    'fali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 310', 
    'gsli':'iphone x',
    'gvali':'galaxy s91',
    'rolim':'mi 11 pro',
    'lorif':'nokia 3310' 
     }
print(telefonlar.values())'''

'''print('Foydalanuvchiar quyidagi telefonlardan foydalanadi:')
for tel in telefonlar.values():
    print(tel)'''

'''print('Foydalanuvchilar quyidagi telefonlardan foydalanadi:')    
for tel in set(telefonlar.values()):
    print(tel)'''

toys={"boll","car","lamp","car","bear"}    
print(toys)    
    
    
    
    
    
    
    
    
    
    
    
    
    

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 09:20:57 2024

@author: User
"""
'''car0={
      'model':'lasetti',
      'rang':'oq',
      'yil':'2018',
      'narx':'13000',
      'km':'50000',
      'karobka':'avtomat'
      }

car1={
      'model':'nexia 3',
      'rang':'qora',
      'yil':'2015',
      'narx':'9000',
      'km':'85000',
      'karobka':'mexani'
      }

car2={
      'model':'gentra',
      'rang':'qizil',
      'yil':'2019',
      'narx':'15000',
      'km':'20000',
      'karobka':'mexania'
      }'''

'''car=car1
print(f'{car['model'].title()},'
      f'{car['rang']} rang,'
      f'{car['yil']}-yil, {car['narx']}$')'''

'''cars=[car0,car1,car2]
for car in cars:
    print(f'{car['model'].title()},'
          f'{car['rang']} rang,'
          f'{car['yil']}-yil, {car['narx']}$')'''
    
'''print(cars[0]['model'])
print(f'{cars[2]['rang']} '
      f'{cars[2]['model']}')'''

'''malibus=[]
for n in range(10):
    new_car={
      'model':'malibu',
      'rang':'None',   #rangi aniqmas
      'yil':2020,
      'narx':'None',
      'km':0,
      'karobka':'avto'
      }
    malibus.append(new_car)'''

"""for malibu in malibus[:3]:
    malibu['rang']='qizil'"""
   

"""for malibu in malibus[3:6]:
    malibu['rang']='qora'"""

'''for malibu in malibus[6:]:
    malibu['rang']='qora'
    malibu['karobka']='mexanik'
for malibu in malibus:
    print(malibu) 
    
for malibu in malibus:
    if malibu['karobka']=='avto':
        malibu['narx']=40000
    else:
        malibu['narx']=35000
for malibu in malibus:
    print(malibu)   '''     
        
'''dasturchilar={
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'marat':['c++','c#']
    }    '''
    
'''for ism,tillar in dasturchilar.items():
    print(f'\n {ism.title()} quyiagi dasturlash tillarini biladi:')
    for til in tillar:
            print(til.upper())'''
    
    
'''for ism,tillar in dasturchilar.items():
    print(f'\n {ism.title()} quyiagi dasturlash tillarini biladi:')
    for til in tillar:
        print(f'{til.upper()} ', end='' )'''
    
hamkasblar={
    'ali':{
        'familya':'aliyev',
        'tyil':2001,
        'malumot':'oliy',
        'tillar':['html','css','js']},
        
    'vali':{
        'familya':'valiyev',
        'tyil':2002,
        'malumot':'orta-maxsus',
        'tillar':['html','python']},
   'hasan':{
        'familya':'aliyev',
        'tyil':1999,
        'malumot':'oliy',
        'tillar':['c#','css','java'] }     
      } 

for ism , info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familya'].title()},"
          f"{info['tyil']}-yilda tug'ilgan."
          f"Ma'lumoti:{info["malumot"]}. \n"
          "Quyidagi dasturlash tillarini biladi:" )
    
    for til in info['tillar']:
         print(til.upper())
          











   
    
    
    
    
    
    
    
    
    
    


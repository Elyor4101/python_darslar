# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 17:36:06 2024

@author: MS1517
"""
'''
print("Yaqin do'slaringiz ro'yhatini tuzamiz")
ismlar=[ ]
n=1
while True:
    savol=f"{n}-do'slaingiz ismini kiriting:"
    ism=input(savol)
    ismlar.append(ism)
    takrorlash=input("Yana ism kiritasizmi (ha/yo'q)")
    n+=1
    if takrorlash !='ha':
        break

print("Do'stlaringiz ro'yxati:")
for ism in ismlar:
    print(ism.title())
    
'''
'''
print("Do'slaringiz yoshini saqlaymiz")
dostlar={}
ishora=True
while ishora:
    ism=input("Do'stlaringiz ismini kiriting:")
    yosh=input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism]=int(yosh)
    javob=input("yana ma'lumot qo'shasizmi: (ha/yo'q)")
    if javob =="yo'q":
        ishora=False
for ism,yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")
print(dostlar)
'''
'''
cars=['nexia','jentra','gelik','nexia','mers','bmv','nexia']
while 'nexia' in cars:
    cars.remove('nexia')
print(cars)
'''
talabalar=['botir','rustam','nodir','farrux']
baholangan_talabalar={}
while talabalar:
    talaba=talabalar.pop()
    baho=input(f"{talaba.title()}ning bahosini kiriting:")
    print(f"{talaba.title()}  baholandi")
    baholangan_talabalar[talaba]=int(baho)
print(baholangan_talabalar)























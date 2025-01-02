# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:02:13 2024

@author: User
"""

#upper() metodi matndagi har bir harfni katta harfga o'zgartiradi. 
#lower() metodi esa aksincha, har bir harfni kichik harfga o'zgartiradi.
#title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi. 
#capitalize() esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.
#Bu metodlar matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.
#lstrip() — matn boshidagi bo'shliqni,
#rstrip() – matn oxiridagi bo'shliqni,
#strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi
ism='Ahad'
familya='Qayum'
#print(ism,familya)
#print(ism+familya)
#print(ism+' '+ familya)
#ism_sharif=f"{ism} {familya}"
#print(ism_sharif)
#print(f"Salom,menin ismim {ism}. {ism} {familya}!")
#print('Hello world')
#print('Hello \tworld')
#print('Hello \nworld')
#print("Hello \bWorld")
#ism='James'
#familya='Bont'
#ism_sharif=f'{ism} {familya}'
#print(ism_sharif.lower())
#print(ism_sharif.title())
#print(ism_sharif.capitalize())
#ism_sharif="james bond"
#print(ism_sharif.title())
#print(ism_sharif.capitalize())
#meva='  olma  '
#print("men " + meva.lstrip() + " yaxshi koraman")
#print("men " + meva.rstrip() + " yaxshi koraman")
#print("men " + meva.strip() + " yaxshi koraman")
#print("men ".capitalize() + meva.strip() + " yaxshi koraman")

#ism=input("Ismingiz nima?")
#print("Assalomu alaykum, "+ism)
#ism=input("Ismingiz nima?\n>>>")
#print("Assalomu alaykum, "+ism)

#kocha="Bogbon"
#viloyat="Samarqand"

#print(kocha+ " kochasi,"+ mahalla+ " mahallasi,"+ tuman+ " tumani,"+\
      #viloyat+ " viloyati")

#print(kocha+ " kochasi,\n"+ mahalla+ " mahallasi,\n"+ tuman+ " tumani,\n"
     # + viloyat+ " viloyati\n")

#manzil=f"{kocha}  kochasi, {mahalla}  mahallasi, {tuman} tumani, {viloyat} viloyati"
#print(manzil)

#print(manzil.upper())
#print(manzil.lower())
#print(manzil.title())
#print(manzil.capitalize())

"""kvt=20
kvy=kvt**2
print(kvy)
pi=3.14159
radus=10
diametr=2*radus
print("Aylana uzunligi ",pi*diametr)

Aholi_soni=7_559_654_312
print("Yer kurrasida ",Aholi_soni, "ga teng")

x,y,z=10,-7.25,50
print(x,y,z)"""

"""ism='Jobir'
yosh=36
xabar=ism +' '+ str(yosh)+ " yoshda"
print(xabar)
print(type(ism))
print(type(yosh))"""

"""t_yil=int(input("Tug'ilgan yilingizni kiriting: "))
yosh=2024-t_yil
print('Siz '+str(yosh)+ " yoshda ekansiz")"""

"""t_yil=input("Tg'lgan yilingizni kiriting: ")
t_yil=int(t_yil)
yosh=2024-t_yil
print("Siz"+' '+str(yosh)+" yoshda ekansiz")"""

"""son=input("ISTALGAN SONNI KIRITING:\n>>>")
print(type(son))
son=int(son)
kvadrat=son**2
kub=son**3
print(str(son)+" ning kvarati "+str(kvadrat)+" ga teng")
print(str(son)+" ning kubi "+str(kub)+" ga teng")"""

"""yosh=input("Yoshingiz nechchida?\n>>>")
yosh=int(yosh)
t_yil=2024-yosh
print("Siz "+str(t_yil)+" da tug'ilgansiz.")"""

# Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi,
#  ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur

b=float(input("Birinci sonni kiriting: "))
i=float(input("Ikkinchi sonni kiriting: "))
"""y=b+i
a=b-i
k=b*i
t=b/i
print(str(b)+'+'+str(i)+"="+str(y))
print(str(b)+'-'+str(i)+"="+str(a))
print(str(b)+'*'+str(i)+"="+str(k))
print(str(b)+'/'+str(i)+"="+str(t))"""

print( f"{b}+{i}=", b+i)
print( f"{b}-{i}=", b-i)
print( f"{b}*{i}=", b*i)
print( f"{b}/{i}=", b/i)















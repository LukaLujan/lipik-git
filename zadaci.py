#!/usr/bin/env python
# coding: utf-8

# 1. Kreirajte dvije brojčane varijable te ispišite rezultat operatora usporedbe 
# (usporedba jednakosti, nejednakosti, strogo veće, strogo manje, veće ili jednako, manje ili jednako).

# In[1]:


var1 =4
var2 =5
print(var1 ==var2)
print(var1 !=var2)
print(var1 >var2)
print(var1 <var2)
print(var1 >=var2)
print(var1 <=var2)


# 2  Kreirajte dvije varijable i dodijelite im vrijednosti True ili False. 
# Ispišite rezultate logičkih operatora (and, or, not) za dvije prethodno kreirane varijable.

# In[25]:


var1 =True
var2 =True

print(var1==True and var2 ==False )
print(var1 ==True and var2 ==True)
print(var2 ==False or var1 ==False)
print(not var1)


# 4. Napišite program koji će u varijable a i b spremiti dva dvoznamenkasta broja. 
# U varijablu a pohranite zadnju znamenku broja koji se nalazi u varijabli b, a u varijablu b pohranite zadnju znamenku broja koja se nalazi u varijabli a. Ispišite sadržaj varijabli a i b.

# In[60]:


a =str(34)
b =str(25)
ac =a
bc =b
ac=ac.replace(a[1],b[1])
bc=bc.replace(b[1],a[1])
print(ac,bc)


# 5. Omogućite unos 8 racionalnih brojeva te ispišite rezultat po sljedećoj formuli: 
# a + b / c * d**e // f - g % h 
# - komentarima ispišite što se sve događa kroz nekoliko slučajeva upisanih različitih brojeva

# In[74]:


a =(input("unesite 8 brojeva sa razmakom "))
brojevi = a.split()
#brojeve kao veliki string sam odvojio u jednu listu
brojevi =[int(x) for x in brojevi]
#zatim sam pomocu list compehation pretvorio sve brojeve koji su bili string u integers
a,b,c,d,e,f,g,h = tuple(brojevi)
print( a + b / c * d**e // f - g % h)
#obavio sam matematičku funkciju


# 6. Unesi jedan nasumični broj. 
# Ispiši aritmetičku sredinu onoliko brojeva(0-101) koliko je iznosio uneseni nasumični broj.
# Navedeni broj uzmi kao vrijednost opsega kruga te ispiši vrijednost polumjera navedenog kruga.

# In[78]:


a=55
lista =[ x for x in range(0,a)]

sredina = sum(lista)/len(lista)
print(sredina)


# 7. Ispiši vrijednost broja Pi na 4 decimalna mjesta, kvadriraj taj broj te ga podijeli s racionalnim brojem odabranim 
# od strane korisnika (input funkcija) i ispiši rezultat.

# In[84]:


djelitelj =int(input("unesi neki broj "))
import math
PI =round(math.pi,4)
(PI**2)/djelitelj


# 8 Unesi neki nasumični broj kojeg ćeš uzeti kao vrijednost duljine liste u koju se trebaju spremiti vrijednosti od 0 do 1001. 
# 	Ispiši sljedeće vrijednosti na ekran:
# 		a) medijan
# 		b) mod
# 		c) aritmetičku vrijednost
# 		d) sve brojeve koji se u definiranoj listi nalaze ispred vrijednosti koju smo izračunali kao medijan navedene liste
# 		e) sve brojeve koji su manji od vrijednosti koju smo izračunali kao medijan navedene liste 
# 
# 	*Bonus: Napravite novu listu koja sadrži samo vrijednosti koje su za 10% veće ili manje od aritmetičke sredine
# 

# In[102]:


a=65
lista =[ x for x in range(0,a)]
import statistics
print(f"{statistics.mean(lista) } mean")
print(f"{statistics.median(lista) } median")
print(f"{statistics.median(lista) } mod")

lista_2=[]
for x in lista:
    if x > (statistics.mean(lista)*1.1) or x < (statistics.mean(lista)/1.1) :
        lista_2.append(x)
        
print(lista_2)


# 9. Napišite algoritam koji prima nasumičan pozitivni broj manji od 86400 te pretvara taj broj iz sekunda 
# i ispisuje koliko je to točno vrijeme u satima, minutama i sekundama

# In[105]:


n =int(input("upiši neko broj manji od 86 000, i mi ćemo to pretvoriti u sekunde i sate "))
import datetime
  
def convert(n):
    return str(datetime.timedelta(seconds = n))
      
# Driver program

print(convert(n))


# 10. Napišite algoritam koji uzima broj nasumične dužine te ispisuje:
# a) svaku drugu znamenku s tri decimalna mjesta (0,000) 
# b) zaokružen zbroj svih upravo ispisanih znamenki

# In[152]:


import decimal
a=str(1311111111)
lista_dec=[]
len(a)
for i in range(len(a)):
    if i %2 !=0 and i !=0:
        lista_dec.append(decimal.Decimal(format(int(a[i]), '.3f')))




print(sum(lista_dec))


# 11. U varijablu upišite neki proizvoljni niz znakova. Nad varijablom pozovite odgovarajuću funkciju koja će vratiti duljinu upisanoga niza znakova te rezultat spremite u novu varijablu. Ispišite sve znakove do polovice niza. 
# Primjer: ako imamo niz od 15 znakova (abcdefghijklmno), potrebno je ispisati 1., 2., 3., 4., 5., 6., 7. i 8. znak (abcdefgh)

# In[175]:


a ="abcdefghijklmno"

duzina=len(a)

duz_za_iter =int()
if duzina% 2==1:
    duz_za_iter =int(duzina/2 +0.5)
else:
    duz_za_iter =duzina//2
    
string=""
for i in range(duz_za_iter):
    string +=a[i]
print(string)


# In[168]:


duz_za_iter =int()


# In[169]:


duz_za_iter


# In[170]:





# In[ ]:





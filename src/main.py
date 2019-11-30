#Author = Wahyu Saputro R.M.
#NPM = 5170711019
#Prodi = S1 Teknik Elektro / A / UTY
import numpy as np
from Menu import *
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
menu()
#Kasus
kasus1 = np.array(["Sakit_Kepala","Badan_Lemas"]) #Anemia 2
kasus2 = np.array(["Sakit_Kepala","Badan_Lemas","Kedinginan"]) #anemia 3
kasus3 = np.array(["Panas","Bersin","Batuk", "Tenggorokan_Sakit"]) #Bronkitis 4
kasus4 = np.array(["Bersin","Batuk","Tenggorokan_Sakit"]) #Bronkitis 3
kasus5 = np.array(["Panas", "Badan_Lemas","Kedinginan"]) #Demam 3
kasus6 = np.array(["Panas","Sakit_Kepala","Badan_Lemas","Kedinginan"]) #Demam 4
kasus7 = np.array(["Panas", "Sakit_Kepala", "Bersin", "Batuk", "Pilek", "Badan_Lemas","Kedinginan"]) #Flu 7
kasus8 = np.array(["Panas", "Sakit_Kepala", "Bersin", "Pilek", "Badan_Lemas", "Kedinginan", "Tenggorokan_Sakit"]) #Flu 7
kasus9 = np.array(["Panas", "Bersin", "Batuk", "Pilek","Badan_Lemas", "Kedinginan", "Tenggorokan_Sakit"]) #FLU 7
# Masukan Gejala
lst = []
n = int(input("Jumlah data : "))

for i in range (0,n):
	ele = input()
	lst.append(ele)
print(lst)
# pembagi 
cases1 = max(n,2)
cases2 = max(n,3)
cases3 = max(n,4)
cases4 = max(n,3)
cases5 = max(n,3)
cases6 = max(n,4)
cases7 = max(n,7)
cases8 = max(n,7)
cases9 = max(n,7)
# Pembanding
#1
for i in range (0,n):
	if lst[i] == kasus1[0]:
		count1 += 1
	elif lst[i] == kasus1[1]:
		count1 += 1
#2
for i in range (0,n):
	if lst[i] == kasus2[0]:
		count2 += 1
	elif lst[i] == kasus2[1]:
		count2 += 1
	elif lst[i] == kasus2[2]:
		count2 += 1
#3
for i in range (0,n):
	if lst[i] == kasus3[0]:
		count3 += 1
	elif lst[i] == kasus3[1]:
		count3 += 1
	elif lst[i] == kasus3[2]:
		count3 += 1
	elif lst[i] == kasus3[3]:
		count3 += 1
#4
for i in range (0,n):
	if lst[i] == kasus4[0]:
		count4 += 1
	elif lst[i] == kasus4[1]:
		count4 += 1
	elif lst[i] == kasus4[2]:
		count4 += 1
#5
for i in range (0,n):
	if lst[i] == kasus5[0]:
		count5 += 1
	elif lst[i] == kasus5[1]:
		count5 += 1
	elif lst[i] == kasus5[2]:
		count5 += 1
#6
for i in range (0,n):
	if lst[i] == kasus6[0]:
		count6 += 1
	elif lst[i] == kasus6[1]:
		count6 += 1
	elif lst[i] == kasus6[2]:
		count6 += 1
	elif lst[i] == kasus6[3]:
		count6 += 1
#7
for i in range (0,n):
	if lst[i] == kasus7[0]:
		count7 += 1
	elif lst[i] == kasus7[1]:
		count7 += 1
	elif lst[i] == kasus7[2]:
		count7 += 1
	elif lst[i] == kasus7[3]:
		count7 += 1
	elif lst[i] == kasus7[4]:
		count7 += 1
	elif lst[i] == kasus7[5]:
		count7 += 1
	elif lst[i] == kasus7[6]:
		count7 += 1
#8
for i in range (0,n):
	if lst[i] == kasus8[0]:
		count8 += 1
	elif lst[i] == kasus8[1]:
		count8 += 1
	elif lst[i] == kasus8[2]:
		count8 += 1
	elif lst[i] == kasus8[3]:
		count8 += 1
	elif lst[i] == kasus8[4]:
		count8 += 1
	elif lst[i] == kasus8[5]:
		count8 += 1
	elif lst[i] == kasus8[6]:
		count8 += 1
#9
for i in range (0,n):
	if lst[i] == kasus7[0]:
		count9 += 1
	elif lst[i] == kasus9[1]:
		count9 += 1
	elif lst[i] == kasus9[2]:
		count9 += 1
	elif lst[i] == kasus9[3]:
		count9 += 1
	elif lst[i] == kasus9[4]:
		count9 += 1
	elif lst[i] == kasus9[5]:
		count9 += 1
	elif lst[i] == kasus9[6]:
		count9 += 1

#Hasil
persen1 = (count1/cases1)*100
persen2 = (count2/cases2)*100
persen3 = (count3/cases3)*100
persen4 = (count4/cases4)*100
persen5 = (count5/cases5)*100
persen6 = (count6/cases6)*100
persen7 = (count7/cases7)*100
persen8 = (count8/cases8)*100
persen9 = (count9/cases9)*100

print('Anemia    : ',persen1,'%')
print('Anemia    : ',persen2,'%')
print('Bronkitis : ',persen3,'%')
print('Bronkitis : ',persen4,'%')
print('Demam     : ',persen5,'%')
print('Demam     : ',persen6,'%')
print('Flu       : ',persen7,'%')
print('Flu       : ',persen8,'%')
print('Flu       : ',persen9,'%')

hasil = max(persen1,persen2,persen3,persen4,persen5,persen6,persen7,persen8,persen9)
if persen1 == hasil:
	print("Kemungkinan Penyakit Anemia : ",hasil)
elif persen2 == hasil:
	print("Kemungkinan Penyakit Anemia : ",hasil)
elif persen3 == hasil:
	print("Kemungkinan Penyakit Bronkitis : ",hasil)
elif persen4 == hasil:
	print("Kemungkinan Penyakit Bronkitis : ",hasil)
elif persen5 == hasil:
	print("Kemungkinan Penyakit Demam : ",hasil)
elif persen6 == hasil:
	print("Kemungkinan Penyakit Demam : ",hasil)
elif persen7 == hasil:
	print("Kemungkinan Penyakit Flu : ",hasil)
elif persen8 == hasil:
	print("Kemungkinan Penyakit Flu : ",hasil)
elif persen9 == hasil:
	print("Kemungkinan Penyakit Flu : ",hasil)

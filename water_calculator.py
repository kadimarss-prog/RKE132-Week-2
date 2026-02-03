paevanorm = 2000 
klaasi_maht = 250 

klaaside_arv= int(input("Mitu klaasi vett oled juba joonud? ")) 

joodud_kogus = klaaside_arv * klaasi_maht 
protsent = (joodud_kogus / paevanorm) * 100
print (protsent)

if protsent < 50: 
    print("Joo rohkem vett, keha vajab seda!")
elif protsent < 100: 
    print("Tubli, jätka samas vaimus!") 
else: print("Suurepärane, oled oma päevase eesmärgi täitnud!")
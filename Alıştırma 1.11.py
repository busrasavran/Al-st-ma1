
liste=[]


for i in range(1,125):
    kalan1=125%i
    kalan2=200%i
    kalan3=350%i
    if kalan1==kalan2 and kalan2==kalan3:
        liste.append(kalan3)
        bölen=i

print("En büyük kalan", max(liste), "veren", bölen)
print(liste)
        
        
    

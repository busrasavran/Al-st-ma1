toplam_sayı=0

for n in range(100,1000,2):
    n=str(n)
    if n[0]==n[1]:
        toplam_sayı=toplam_sayı+1
    elif n[0]==n[2]:
            toplam_sayı=toplam_sayı+1
    elif n[1]==n[2]:
            toplam_sayı=toplam_sayı+1
print(toplam_sayı)
            
        

        
    
        

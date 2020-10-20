sum=0
for n in range(1,10**4,1): #Sonsuzu nasıl ifade edebileceğimi bilemedim ama büyük bir sayı yazınca pi'nin yaklaşık değerini verdi
    sum+= 1/n**2
    sum=float(sum)

print((6*sum)**(1/2))



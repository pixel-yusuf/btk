#Kullanıcıdan isim, soyisim,telefon numarası alarak bir liste atayınız
bilgiler=[]
ay=input("İsminiz:")
bey=input("Soyisminiz:")
cey=(input("Telefon numaranız:"))
bilgiler.append(ay)
bilgiler.append(bey)
bilgiler.append(cey)
print(bilgiler)
print("----------------")
print("Adı:",bilgiler[0])
print("Soyadı:",bilgiler[1])
print("Telefon Numarası:",bilgiler[2])
print("----------------")
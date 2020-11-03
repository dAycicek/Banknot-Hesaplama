def banknot(sayi):
    ikiyuzluk = (int(para/200))
    ikiyuzcik = ikiyuzluk * 200

    yuzluk = (int((para - ikiyuzcik)/100))
    yuzlukcik = yuzluk * 100

    ellilik = (int((para - ikiyuzcik - yuzlukcik)/50))
    ellilikcik = ellilik * 50

    yirmilik = (int((para - ikiyuzcik - yuzlukcik - ellilikcik)/20))
    yirmilikcik = yirmilik * 20

    onluk = (int((para - ikiyuzcik - yuzlukcik - ellilikcik - yirmilikcik)/10))
    onlukcik = onluk * 10

    beslik = (int((para - ikiyuzcik - yuzlukcik - ellilikcik - yirmilikcik - onlukcik)/5))
    beslikcik = beslik * 5

    birlik = (int((para - ikiyuzcik - yuzlukcik - ellilikcik - yirmilikcik - onlukcik - beslikcik)/1))
    return ikiyuzluk,yuzluk,ellilik,yirmilik,onluk,beslik,birlik

para = input("Para: ")
para = int(para)
ikiyuzluk, yuzluk, ellilik,yirmilik,onluk,beslik,birlik = banknot(para)

print("İki yüzlük sayısı: ",ikiyuzluk)
print("Yüzlük sayısı: ",yuzluk)
print("Ellilik sayısı: ", ellilik)
print("Yirmilik sayısı: ", yirmilik)
print("Onluk sayısı: ", onluk)
print("Beşlik sayısı: ", beslik)
print("Birlik sayısı: ",birlik)

#Deniz yapıyosun kardeşim helal

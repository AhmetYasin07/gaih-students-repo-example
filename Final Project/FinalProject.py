class Cooking():
  name=""
  products = []
  times = []
  def __init__(self, name, products, times):
    pass

class Recipe1(Cooking):
  def __init__(self, name ,products, times):
    super().__init__(name, products, times)
    self.name = name
    self.products = products
    self.times = times
  
  def cookingGuide(self):
    print("*"*10 + f"{self.name}" + "*"*10)
    print(f"\nHazırlama Süresi: {self.times[0]}")
    print(f"Pişme Süresi: {self.times[1]}")
    print("\nMalzemeler:\n ")
    for i in self.products:
      print("     "+i)
    print("\nHazırlanışı: \n ")
    print("""
    Orta boy bir tencerenin içerisine tereyağını koyun.
    
    Rendelenmiş sarımsakları, domates salçasını koyun ve güzelce karıştırın.

    Domatesleri rendeleyin ve üzerine baharatları ekleyerek güzelce karıştırın.

    Domatesleri bir süre bu şekilde pişirerek yoğunlaştırın. Ardından makarnaları ekleyin ve üzerine su gezdirin.

    Kapağını kapatın ve suyunu çekene kadar ortalama 10-12 dakika kadar pişirin. Ardından ocaktan alın ve birkaç dakika dinlendirin.

    Üzerine dilediğiniz malzemeleri ekleyerek servis edin.""")
  
class Recipe2(Cooking):
  def __init__(self, name ,products, times):
    super().__init__(name, products, times)
    self.name = name
    self.products = products
    self.times = times
  def cookingGuide(self):
    print("*"*10 + f"{self.name}" + "*"*10)
    print(f"\nHazırlama Süresi: {self.times[0]}")
    print(f"Pişme Süresi: {self.times[1]}")
    print("\nMalzemeler:\n ")
    for i in self.products:
      print("     "+i)
    print("\nHazırlanışı: \n ")
    print("""
    Orta boy bir tencerenin içerisine tereyağını koyun.
    
    Rendelenmiş sarımsakları, domates salçasını koyun ve güzelce karıştırın.

    Domatesleri rendeleyin ve üzerine baharatları ekleyerek güzelce karıştırın.

    Domatesleri bir süre bu şekilde pişirerek yoğunlaştırın. Ardından makarnaları ekleyin ve üzerine su gezdirin.

    Kapağını kapatın ve suyunu çekene kadar ortalama 10-12 dakika kadar pişirin. Ardından ocaktan alın ve birkaç dakika dinlendirin.

    Üzerine dilediğiniz malzemeleri ekleyerek servis edin.""")

class Recipe3(Cooking):
  def __init__(self, name ,products, times):
    super().__init__(name, products, times)
    self.name = name
    self.products = products
    self.times = times
  def cookingGuide(self):
    print("*"*10 + f"{self.name}" + "*"*10)
    print(f"\nHazırlama Süresi: {self.times[0]}")
    print(f"Pişme Süresi: {self.times[1]}")
    print("\nMalzemeler:\n ")
    for i in self.products:
      print("     "+i)
    print("\nHazırlanışı: \n ")
    print("""
    Kişi sayısına göre azaltıp arttırabileceğiniz oranda sucuğu ince ince dilimleyin.

    Ocağa aldığınız yanmaz yapışmaz tabanlı yağsız tavaya sucuk dilimlerini yerleştirin.

    Aralarda ters çevirerek hafif bir renk alana ve yağını salana kadar sucukları orta ateşte pişirin.

    Kişi sayısına göre arttırabileceğiniz yumurtayı, sarısının dağılmaması için dikkatli bir şekilde bütün olarak sucuk dilimlerinin orta kısmına kırın.

    Yumurta beyazını aralarda dağıtıp, spatulanın ucuyla hafif bir şekilde karıştırarak kısık ateşte pişirin.

    Akı, şeffaf bir renkten beyaza doğru dönen sahanda sucuklu yumurtayı sıcak olarak bekletmeden sevdiklerinizle paylaşın.
    """)

meal1 = Recipe1("Domatesli Makarna", ["Makarna","Tereyağı","Domates salçası","Sarımsak","Domates","Karabiber","Tuz","Ilık su"], ["5dk","20 dk"])

meal2 = Recipe2("Çoban Salata", ["Domates","Biber","Salatalık","Kuru soğan","Maydanoz","Zeytinyağı","Limon suyu","Tuz"], ["20 dk","Pişmesi Gerekmiyor"])

meal3 = Recipe3("Sucuklu Yumurta", ["Sucuk","Yumurta","Tuz"], ["5 dk","5 dk"])

meal1.cookingGuide()
print("\n "*5)
meal2.cookingGuide()
print("\n "*5)
meal3.cookingGuide()

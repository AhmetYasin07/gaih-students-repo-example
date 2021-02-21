class Cooking():
  name=""
  products = []
  times = []
  def __init__(self, name, products, times):
    self.name = name
    self.products = products
    self.times = times
  
  def add(self, product):
    print(f"{product} malzemesini ekleyin.")

  def addTo(self, tool, product):
    print(f"{tool} içerisine {product} koyun. ")

  def mix(self):
    print("Karıştırın.")

  def cook(self, min):
    print(f"{min} pişirin.")

  def serve(self):
    print("Yemek hazır :) Servis edebilirsiniz.")
  
class Recipe1(Cooking):
  def __init__(self, name ,products, times):
    super().__init__(name, products, times)

  def grate(self, product):
    print(f"{product} malzemesini rendeleyin.")
  
  def rest(self,min):
    print(f"Yemeği ocaktan alıp {min} bekleyin.")

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

  def startCooking(self):
    self.addTo("Tencere",self.products[1])
    self.grate(self.products[3])
    self.add(self.products[2])
    self.add("Baharat")
    self.mix()
    self.cook("Bir süre")
    self.add(self.products[0])
    self.add("Su")
    self.cook("10 dk")
    self.rest("bir kaç dakika")
    print("\n "*2)
    self.serve()

    
class Recipe2(Cooking):
  def __init__(self, name ,products, times):
    super().__init__(name, products, times)

  def chopProd(self, product):
    print(f"{product} malzemesini doğrayın.")
  
  def peelProd(self, product):
    print(f"{product} malzemesini soyun. ")

  def cutProd(self, product, shape):
    print(f"{product} malzemesini {shape} şeklinde kesin")

  def notIn(self, product):
    print(f"{product} malzemesini kenara ayırın.")

  def cookingGuide(self):
    print("*"*10 + f"{self.name}" + "*"*10)
    print(f"\nHazırlama Süresi: {self.times[0]}")
    print(f"Pişme Süresi: {self.times[1]}")
    print("\nMalzemeler:\n ")
    for i in self.products:
      print("     "+i)
    print("\nHazırlanışı: \n ")
    print("""
    Çoban salatayı hazırlamak için; sap kısımlarını aldığınız sulu ve orta boy domatesleri ince ince doğrayın.

    Kabuğunu soyduğunuz salatalıkları domateslerle uyumlu olacak şekilde kesin.

    Ortadan ikiye kestiğiniz ve çekirdeklerini çıkardığınız yeşil biberleri yarım ay şeklinde kesin.

    Kuru soğanı küçük parçalar halinde ya da arzuya göre ince piyazlık doğrayın. Maydanozu incecik kıyın.

    Kuru soğan dışında kalan doğranmış tüm malzemeyi salata kabında karıştırın. Servis tabağına aldığınız salata üzerine doğranmış kuru soğanları yerleştirin.

    Salatanın sosu için; zeytinyağı, taze sıkılmış limon suyu ve tuzu küçük bir kapta karıştırdıktan sonra salatanın üzerine gezdirin.

    Sosuyla harmanladığınız salatayı, sulanmaması için bekletmeden servis edin. Her türlü ana yemek yanında sevdiklerinizle paylaşın.
    """)

  def prepareSauce(self):
    self.add(self.products[5])
    self.add(self.products[6])
    self.add(self.products[7])
    self.mix()

  def startCooking(self):
    self.chopProd(self.products[0])
    self.peelProd(self.products[2])
    self.chopProd(self.products[2])
    self.cutProd(self.products[1], "yarım ay")
    self.chopProd(self.products[3])
    self.chopProd(self.products[4])
    self.notIn(self.products[3])
    self.mix()
    self.add(self.products[3])
    self.prepareSauce()
    self.add("Sos")
    print("\n "*2)
    self.serve()

class Recipe3(Cooking):
  def __init__(self, name ,products, times):
    super().__init__(name, products, times)
    
  def sliceProd(self, product):
    print(f"{product} malzemesini dilimleyin ")

  def upturnProd(self, product):
    print(f"{product} malzemesini pişerken ara ara ters çevirin. ")

  def breakProd(self, product):
    print(f"{product} malzemesini kırıp ekleyin. ")

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
  def startCooking(self):
    self.sliceProd(self.products[0])
    self.addTo("Tava", self.products[0])
    self.cook(self.products[0])
    self.upturnProd(self.products[0])
    self.breakProd(self.products[1])
    self.cook("Kısık ateşte")
    self.mix()
    print("\n "*2)
    self.serve()


meal1 = Recipe1("Domatesli Makarna", ["Makarna","Tereyağı","Domates salçası","Sarımsak","Domates","Karabiber","Tuz","Ilık su"], ["5dk","20 dk"])

meal2 = Recipe2("Çoban Salata", ["Domates","Yeşil Biber","Salatalık","Kuru soğan","Maydanoz","Zeytinyağı","Limon suyu","Tuz"], ["20 dk","Pişmesi Gerekmiyor"])

meal3 = Recipe3("Sucuklu Yumurta", ["Sucuk","Yumurta","Tuz"], ["5 dk","5 dk"])

meal1.cookingGuide()
print("\n "*5)
meal2.cookingGuide()
print("\n "*5)
meal3.cookingGuide()
print("\n "*5)

print("1- Domatesli Makarna\n2- Çoban Salata\n3- Sucuklu Yumurta")
print("\n "*2)

Menu = int(input("Pişirmek istediğiniz yemeğin sayısını giriniz: "))
print("\n "*2)

if Menu == 1:
  meal1.startCooking()
elif Menu == 2:
  meal2.startCooking()
elif Menu == 3:
  meal3.startCooking()
else:
  print("Üzgünüz, menüde böyle bir seçenek yok :(")

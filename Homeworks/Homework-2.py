studentNumber = int(input("How many student: "))
# Öğrenci sayısını belirliyoruz. (Ödev için 5 giriyoruz)
a = 0
# Döngüyü sınırlandırmak için bir değişkeni 0'a atıyoruz ve döngü sonuna 1 artırıyoruz.
students = []
grades = []
# Öğrenci bilgilerini tuttuğumuz listeler
while a < studentNumber:
  words = ["Midterm", "Final", "Homework"] 
  students.append(str(input("\nStudent Name: ")))
  # Kullanıcıdan öğrencinin ismini alıp listeye ekliyoruz.
  grade = []
  # döngü içinde geçici olarak öğrencinin 3 notunu bu listede tutuyoruz.
  for i in words:
    grade.append(int(input(f"\n{i}: "))) 
    # Döngü ile kullanıcıdan öğrenciye ait 3 farklı notu alıyoruz ve bunu geçici listeye ekliyoruz.
  totalGrade = 0
  for j in grade:
    totalGrade += j
  grades.append(totalGrade / len(grade))
  # Ortalamayı bulmak için değeri 0 olan bir değişken tanımlayıp geçici not listesi üzerinde gezinerek notları topluyoruz.
  # Notların toplamını geçici listenin uzunluğuna (not sayısına) bölerek ortalamayı buluyoruz ve kalıcı olan grades listesine ekliyoruz.
  a += 1

info = dict(sorted(zip(grades,students)))
# İki listeyi zip ile sözlük haline getirip sıralıyoruz.

info= dict((value, key) for (key,value) in info.items())
# Daha güzel gözükmesi açısından not: "isim" şeklinde olan sözlüğü "isim": not haline çeviriyoruz.

print("\n***************************\n")

for k, v in info.items():
  print(f"{k}: {v} \n")
  # Sözlüğümüz üzerinde gezinerek değerlerimizi yazdırıyoruz.

print("\n**************************")


print(f"Congratulations {students[grades.index(max(grades))]} !!!!!")
# Döngüde bir öğrencinin bilgilerini sırayla listelere eklemiştik bu yüzden öğrencinin adı ve notu farklı listelerde aynı indexte bulunuyor.
# Bunu kullanarak en yüksek notun indexini bulduk ve bu indexteki kişinin en yüksek not alan kişi olduğunu anlayıp tebrik ettik.
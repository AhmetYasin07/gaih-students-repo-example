import random

primeNumbers= []
for i in range(2,101):
  for j in range(2,i):
    if i % j == 0:
      break
  else:
    primeNumbers.append(i)
# Asal sayıları bulup hepsini bir listede topluyoruz.

i=0
a=0
matrisNumbers = [],[],[]
while i<9:
  randomNum = random.choice(primeNumbers)
  # asal sayılardan birini rastgele seçiyoruz.
  if randomNum not in matrisNumbers[0] and randomNum not in matrisNumbers[1] and randomNum not in matrisNumbers[2] :   
    matrisNumbers[a].append(randomNum)
    # eğer seçtiğimiz sayı daha önce seçilmemişse o an bulunduğumuz listeye bu sayıyı ekliyoruz 
  else:
    continue
  # eğer sayı seçilmişse döngüyü burda durdurup başa sarıyoruz.
  
  i += 1
  # i her defasında 1 artacak böylece döngü 9 tur atacak ve 9 sayımız olacak
  if i%3==0:
    # eğer i'nin 3 ile bölümünden kalan 0 ise bu sayı 3ün katıdır yani o an bulunduğunuz listede 3 sayı olmuştur.
    print(matrisNumbers[a])
    a+=1

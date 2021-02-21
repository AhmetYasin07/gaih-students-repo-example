def prime_first(number):
  for j in range(2,number):
    if number % j == 0:
      return None 
  else:
    print(number, "prime_first")


def prime_second(number):
  for j in range(2,number):
    if number % j == 0:
      return None
  else:
    print(number, "prime_second")

for i in range(0,1000):
  if i == 0 or i == 1:
    continue 
  elif i < 500:
    prime_first(i)
  else: 
    prime_second(i)

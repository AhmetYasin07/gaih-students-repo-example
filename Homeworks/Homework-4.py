class Hangman():
    def __init__(self, secret, guess, lives):
        self.secret = str(input("Enter a Secret Word: "))
        self.guess = ""
        self.lives = 10
    def start(self):
        while self.lives > 0:
            # Can 0 olana kadar döngü(oyun) devam edecek
            char_left = 0
            for char in self.secret:
                if char in self.guess:
                    print(char)
                else:
                    print("-")
                    char_left += 1
            # Girilen kelimenin her bir harfi üzerinde geziniyoruz. Eğer tahmin edilmişse yerine yazıyoruz eğer edilememişse - yazıyoruz.
            if char_left == 0:
                print("\nCongratulations !!!")
                break
            # Eğer tahmin edilecek harf kalmamışsa oyunu kazanmış oluyoruz.
            guess = input("\nGuess a Word: ")
            self.guess += guess
            # Kullancıdan bir kelime tahmini alıyoruz ve bunu yukarda tanımladığımız stringimize ekliyoruz.
            if guess not in self.secret:
                self.lives -= 1
                print("\nWrong!")
                print(f"\nYou have {self.lives} left")
                if self.lives == 0:
                    print("\nYou died!")
            # Eğer tahmin edememişsek canımız bir eksiliyor. Eğer canımız 0a düşmüşse oyunu kaybediyoruz.

Hangman = Hangman('', '', '')
Hangman.start()
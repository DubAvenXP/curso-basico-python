import random
import os


def random_word():
    palabras = []
    with open("intermedio/archivos/palabras.txt", "r") as f:
        for line in f:
            palabras.append(line.strip())
    return palabras[random.randint(0, len(palabras) - 1)]


def play_game():
    word = [letter for letter in random_word()]
    word_to_guess = ["_"] * len(word)
    letters_guessed = []

    while word != word_to_guess:
        try:
            os.system("clear")
            print(" ".join(word_to_guess) + "\n")
            print("Letras incorrectas: " + " ".join(letters_guessed))
            letter = input("Ingrese una letra: ")
            
            assert len(letter) == 1, "Solo puede ingresar una letra"
            assert letter.isalpha(), "Solo puede ingresar letras"

            if letter in letters_guessed:
                print(f"La letra {letter} ya fue ingresada")
                continue
            word_to_guess = [letter if word[i] == letter else word_to_guess[i] for i in range(len(word))]
            if letter not in word:
                letters_guessed.append(letter)
                
        except Exception as e:
            continue

    os.system("clear")
    print(" ".join(word_to_guess) + "\n")
    print("Felicitaciones, ganaste!\n")

        
        
        


def run():
    play_game()


if __name__ == '__main__':
    run()
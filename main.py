import random

words = ["яблуко", "персик", "кавун", "слива", "диня"]

rand_word = random.choice(words)

choices_inp = int(input("Введіть кількість спроб: "))

hidden_word = []
choice_count = 1

for i in range(len(rand_word)):
    hidden_word.append("*")
print(''.join(hidden_word))

while ''.join(hidden_word) != rand_word:

    answer = input("Введіть літеру або слово цілком: ").lower()

    if answer == rand_word:
        print(f"Вітаю! Ви вгадали слово: {rand_word}")
        break

    elif len(answer) == 1:
        if answer not in rand_word:
            print("Такої літери немає.")
            if choice_count == choices_inp:
                print("Ви програли")
                print(f"Загадане слово {rand_word}")
                break
            print(''.join(hidden_word))
            choice_count += 1

        for i in range(len(rand_word)):
            if answer == rand_word[i]:
                hidden_word[i] = answer
                if choice_count == choices_inp and ''.join(hidden_word) != rand_word:
                    print("Ви програли")
                    print(f"Загадане слово {rand_word}")
                    break
                print(''.join(hidden_word))
                choice_count += 1

    elif answer != rand_word:
        print("Не вірно.")
        print(''.join(hidden_word))

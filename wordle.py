from random import choice

words5 = ('котик', 'парус', 'носок', 'гроза', 'лавка', 'озеро', 'шапка', 'ручка',
          'кубик', 'шарик', 'сырок', 'город', 'свеча', 'банка', 'стена',
          'ложка', 'вилка', 'комод', 'зубок', 'моряк', 'трава', 'сапог', 'глина',
          'забор', 'конек', 'слава', 'салат', 'ведро', 'крыша', 'доска',
          'носик', 'крыса')

word = choice(words5)
guess = [["_", "_", "_", "_", "_"], set()]

attempt = 1
win = False


while attempt <= 7:
    trues = ""
    print(f"\nПопытка {attempt}")
    user = input("Введите предполагаемое слово: ")
    if len(user) != 5:
        print("Слово должно быть из 5 букв")
        continue
    for i in range(len(user)):
        if user[i] == word[i]:
            guess[0][i] = user[i].upper()
        elif user[i] in word:
            guess[1].add(user[i])
    if user == word:
        print("Вы выиграли!")
        win = True
        break

    attempt += 1
    print(f"Слово: {"".join(guess[0])} ::: Буквы: {"".join(guess[1])}")

if not win:
    print(f"Вы проиграли, был загадано слово - {word}")
input("Нажмите enter для выхода")
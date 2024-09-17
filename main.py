import telebot
from random import choice

token = "7541733490:AAFaLdofgS82L-Pusv48T6OOITnfhoPd5eE"
bot = telebot.TeleBot(token)

words5 = ('котик', 'парус', 'носок', 'гроза', 'лавка', 'озеро', 'шапка', 'ручка',
          'кубик', 'шарик', 'сырок', 'город', 'свеча', 'банка', 'стена',
          'ложка', 'вилка', 'комод', 'зубок', 'моряк', 'трава', 'сапог', 'глина',
          'забор', 'конек', 'слава', 'салат', 'ведро', 'крыша', 'доска',
          'носик', 'крыса')

users = {}


class Game:
    def __init__(self):
        self.word = choice(words5)
        self.guessed = [["_", "_", "_", "_", "_"], set()]
        self.attempts = 7
        self.win = False

    def info(self) -> str:
        if self.win:
            return ("Поздравляем, вы угадали!\n"
                    "Нажмите /start чтобы играть заново")
        elif self.attempts > 0:
            text = (f"{str(self.guessed[0])}\n"
                    f"Известные буквы: {str(self.guessed[1])}\n"
                    f"\n"
                    f"У вас осталось {self.attempts} попыток")
            return text
        else:
            return (f"Извините, у вас закончились попытки.\n"
                    f"Загаданное слово было - {self.word}\n"
                    f"Нажмите /start для повторной игры")

    def write(self, user_word):
        if self.attempts > 0:
            if user_word == self.word:
                self.win = True
                self.guessed[0] = user_word.upper()
            else:
                for i in range(len(self.word)):
                    if user_word[i] == self.word[i]:
                        self.guessed[0][i] = user_word[i].upper()
                    elif user_word[i] in self.word:
                        self.guessed[1].add(user_word[i])
                self.attempts -= 1


@bot.message_handler(commands=["start"])
def start(message):
    print(message)
    users[str(message.chat.id)] = Game()

@bot.message_handler(content_types=["text"])
def answer(message):
    game = users[str(message.chat.id)]
    game.write(message.text)
    bot.send_message(chat_id=message.chat.id, text=game.info())

bot.polling()

# Исправить: при введении слова без /start ошибка
# Убрать лишние скобки в ответе
import telebot
from telebot import types
import random

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на ваш токен
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Главное меню с кнопками
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    # Создаем кнопки для разных категорий команд
    btn1 = types.KeyboardButton('ℹ️ Информация')
    btn2 = types.KeyboardButton('🎮 Развлечения')
    btn3 = types.KeyboardButton('🔧 Утилиты')
    btn4 = types.KeyboardButton('📊 Статистика')
    btn5 = types.KeyboardButton('🎲 Случайное')
    btn6 = types.KeyboardButton('⚙️ Настройки')
    
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    
    bot.send_message(message.chat.id, 
                    "👋 Добро пожаловать! Выберите категорию:",
                    reply_markup=markup)

# Обработка нажатий на кнопки
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'ℹ️ Информация':
        show_info_commands(message)
    elif message.text == '🎮 Развлечения':
        show_entertainment_commands(message)
    elif message.text == '🔧 Утилиты':
        show_utility_commands(message)
    elif message.text == '📊 Статистика':
        show_statistics_commands(message)
    elif message.text == '🎲 Случайное':
        show_random_commands(message)
    elif message.text == '⚙️ Настройки':
        show_settings_commands(message)
    else:
        bot.send_message(message.chat.id, "Используйте кнопки для навигации")

# Команды категории "Информация"
def show_info_commands(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    buttons = [
        types.InlineKeyboardButton('📅 Дата и время', callback_data='date_time'),
        types.InlineKeyboardButton('🌤️ Погода', callback_data='weather'),
        types.InlineKeyboardButton('💱 Курсы валют', callback_data='currency'),
        types.InlineKeyboardButton('📈 Криптовалюты', callback_data='crypto'),
        types.InlineKeyboardButton('📰 Новости', callback_data='news'),
        types.InlineKeyboardButton('🎯 О боте', callback_data='about_bot'),
        types.InlineKeyboardButton('👤 Инфо о пользователе', callback_data='user_info'),
        types.InlineKeyboardButton('🌐 Мой IP', callback_data='my_ip'),
        types.InlineKeyboardButton('📏 Конвертер единиц', callback_data='converter'),
        types.InlineKeyboardButton('🔙 Назад', callback_data='back_main')
    ]
    
    markup.add(*buttons)
    bot.send_message(message.chat.id, "📋 Команды информации:", reply_markup=markup)

# Команды категории "Развлечения"
def show_entertainment_commands(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    buttons = [
        types.InlineKeyboardButton('🎲 Случайное число', callback_data='random_number'),
        types.InlineKeyboardButton('🎯 Случайный выбор', callback_data='random_choice'),
        types.InlineKeyboardButton('📜 Цитата дня', callback_data='quote'),
        types.InlineKeyboardButton('😊 Смайлик', callback_data='smile'),
        types.InlineKeyboardButton('🎭 Шутка', callback_data='joke'),
        types.InlineKeyboardButton('🔮 Магический шар', callback_data='magic_ball'),
        types.InlineKeyboardButton('🎵 Случайная песня', callback_data='random_song'),
        types.InlineKeyboardButton('🎬 Фильм дня', callback_data='movie'),
        types.InlineKeyboardButton('🎮 Мини-игры', callback_data='mini_games'),
        types.InlineKeyboardButton('🔙 Назад', callback_data='back_main')
    ]
    
    markup.add(*buttons)
    bot.send_message(message.chat.id, "🎮 Развлекательные команды:", reply_markup=markup)

# Команды категории "Утилиты"
def show_utility_commands(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    buttons = [
        types.InlineKeyboardButton('⏰ Таймер', callback_data='timer'),
        types.InlineKeyboardButton('📝 Напоминание', callback_data='reminder'),
        types.InlineKeyboardButton('🧮 Калькулятор', callback_data='calculator'),
        types.InlineKeyboardButton('📄 Текст в голос', callback_data='text_to_speech'),
        types.InlineKeyboardButton('🔊 Голос в текст', callback_data='speech_to_text'),
        types.InlineKeyboardButton('📷 QR-код', callback_data='qr_code'),
        types.InlineKeyboardButton('🔐 Генератор паролей', callback_data='password_gen'),
        types.InlineKeyboardButton('📊 Опрос', callback_data='poll'),
        types.InlineKeyboardButton('📁 Архиватор', callback_data='archiver'),
        types.InlineKeyboardButton('🔙 Назад', callback_data='back_main')
    ]
    
    markup.add(*buttons)
    bot.send_message(message.chat.id, "🔧 Утилиты:", reply_markup=markup)

# Команды категории "Статистика"
def show_statistics_commands(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    buttons = [
        types.InlineKeyboardButton('📊 Стата чата', callback_data='chat_stats'),
        types.InlineKeyboardButton('👥 Активность', callback_data='activity'),
        types.InlineKeyboardButton('📈 Графики', callback_data='charts'),
        types.InlineKeyboardButton('🏆 Рейтинги', callback_data='ratings'),
        types.InlineKeyboardButton('📅 История', callback_data='history'),
        types.InlineKeyboardButton('🎯 Прогресс', callback_data='progress'),
        types.InlineKeyboardButton('📋 Отчет', callback_data='report'),
        types.InlineKeyboardButton('🔢 Аналитика', callback_data='analytics'),
        types.InlineKeyboardButton('📉 Тренды', callback_data='trends'),
        types.InlineKeyboardButton('🔙 Назад', callback_data='back_main')
    ]
    
    markup.add(*buttons)
    bot.send_message(message.chat.id, "📊 Статистические команды:", reply_markup=markup)

# Команды категории "Случайное"
def show_random_commands(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    buttons = [
        types.InlineKeyboardButton('🎲 Случайное число', callback_data='rand_num'),
        types.InlineKeyboardButton('🎯 Случайный выбор', callback_data='rand_choice'),
        types.InlineKeyboardButton('🎨 Случайный цвет', callback_data='rand_color'),
        types.InlineKeyboardButton('📖 Случайный факт', callback_data='rand_fact'),
        types.InlineKeyboardButton('🌍 Случайная страна', callback_data='rand_country'),
        types.InlineKeyboardButton('🐾 Случайное животное', callback_data='rand_animal'),
        types.InlineKeyboardButton('🍕 Случайная еда', callback_data='rand_food'),
        types.InlineKeyboardButton('🎵 Случайный артист', callback_data='rand_artist'),
        types.InlineKeyboardButton('📚 Случайная книга', callback_data='rand_book'),
        types.InlineKeyboardButton('🔙 Назад', callback_data='back_main')
    ]
    
    markup.add(*buttons)
    bot.send_message(message.chat.id, "🎲 Случайные команды:", reply_markup=markup)

# Команды категории "Настройки"
def show_settings_commands(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    buttons = [
        types.InlineKeyboardButton('⚙️ Настройки бота', callback_data='bot_settings'),
        types.InlineKeyboardButton('🔔 Уведомления', callback_data='notifications'),
        types.InlineKeyboardButton('🌍 Язык', callback_data='language'),
        types.InlineKeyboardButton('🎨 Тема', callback_data='theme'),
        types.InlineKeyboardButton('📱 Интерфейс', callback_data='interface'),
        types.InlineKeyboardButton('🔒 Конфиденциальность', callback_data='privacy'),
        types.InlineKeyboardButton('📊 Авто-стата', callback_data='auto_stats'),
        types.InlineKeyboardButton('🔄 Сброс настроек', callback_data='reset_settings'),
        types.InlineKeyboardButton('💾 Экспорт данных', callback_data='export_data'),
        types.InlineKeyboardButton('🔙 Назад', callback_data='back_main')
    ]
    
    markup.add(*buttons)
    bot.send_message(message.chat.id, "⚙️ Настройки:", reply_markup=markup)

# Обработка callback-запросов
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            # Информационные команды
            if call.data == 'date_time':
                from datetime import datetime
                now = datetime.now()
                bot.send_message(call.message.chat.id, f"📅 Текущая дата и время:\n{now.strftime('%Y-%m-%d %H:%M:%S')}")
            
            elif call.data == 'weather':
                bot.send_message(call.message.chat.id, "🌤️ Функция погоды будет реализована позже")
            
            elif call.data == 'currency':
                bot.send_message(call.message.chat.id, "💱 Курсы валют:\nUSD: 95.5 RUB\nEUR: 102.3 RUB")
            
            elif call.data == 'crypto':
                bot.send_message(call.message.chat.id, "📈 Криптовалюты:\nBTC: $45,000\nETH: $3,200")
            
            elif call.data == 'news':
                bot.send_message(call.message.chat.id, "📰 Последние новости будут здесь")
            
            elif call.data == 'about_bot':
                bot.send_message(call.message.chat.id, "🤖 Этот бот создан для демонстрации 50 различных команд с кнопками!")
            
            elif call.data == 'user_info':
                user_info = f"👤 Информация о вас:\nID: {call.from_user.id}\nИмя: {call.from_user.first_name}\nUsername: @{call.from_user.username}"
                bot.send_message(call.message.chat.id, user_info)
            
            elif call.data == 'my_ip':
                bot.send_message(call.message.chat.id, "🌐 Ваш IP: 127.0.0.1 (локальный)")
            
            elif call.data == 'converter':
                bot.send_message(call.message.chat.id, "📏 Конвертер единиц:\n1 км = 1000 м\n1 кг = 1000 г")
            
            # Развлекательные команды
            elif call.data == 'random_number':
                num = random.randint(1, 100)
                bot.send_message(call.message.chat.id, f"🎲 Случайное число: {num}")
            
            elif call.data == 'random_choice':
                choices = ["🍎 Яблоко", "🍌 Банан", "🍊 Апельсин", "🍓 Клубника"]
                choice = random.choice(choices)
                bot.send_message(call.message.chat.id, f"🎯 Случайный выбор: {choice}")
            
            elif call.data == 'quote':
                quotes = [
                    "Жизнь - это то, что происходит, пока ты строишь планы.",
                    "Будь тем изменением, которое хочешь видеть в мире.",
                    "Успех - это способность двигаться от неудачи к неудаче, не теряя энтузиазма."
                ]
                bot.send_message(call.message.chat.id, f"📜 Цитата дня:\n{random.choice(quotes)}")
            
            elif call.data == 'smile':
                smiles = ["😊", "😂", "🤔", "😍", "🎉", "🔥", "⭐", "🌈"]
                bot.send_message(call.message.chat.id, f"Ваш смайлик: {random.choice(smiles)}")
            
            elif call.data == 'joke':
                jokes = [
                    "Почему программисты путают Хэллоуин и Рождество? Потому что Oct 31 == Dec 25!",
                    "Какой у программиста любимый напиток? Java!",
                    "Сколько программистов нужно, чтобы вкрутить лампочку? Ни одного, это hardware проблема!"
                ]
                bot.send_message(call.message.chat.id, f"🎭 Шутка:\n{random.choice(jokes)}")
            
            elif call.data == 'magic_ball':
                answers = ["Да", "Нет", "Возможно", "Спроси позже", "Определенно да", "Ни в коем случае"]
                bot.send_message(call.message.chat.id, f"🔮 Магический шар говорит: {random.choice(answers)}")
            
            elif call.data == 'random_song':
                songs = ["Queen - Bohemian Rhapsody", "The Beatles - Hey Jude", "Michael Jackson - Billie Jean"]
                bot.send_message(call.message.chat.id, f"🎵 Случайная песня: {random.choice(songs)}")
            
            elif call.data == 'movie':
                movies = ["Крестный отец", "Форрест Гамп", "Начало", "Побег из Шоушенка"]
                bot.send_message(call.message.chat.id, f"🎬 Фильм дня: {random.choice(movies)}")
            
            elif call.data == 'mini_games':
                markup = types.InlineKeyboardMarkup()
                btn1 = types.InlineKeyboardButton('🎯 Угадай число', callback_data='guess_number')
                btn2 = types.InlineKeyboardButton('✂️ Камень-ножницы-бумага', callback_data='rps_game')
                markup.add(btn1, btn2)
                bot.send_message(call.message.chat.id, "🎮 Выберите игру:", reply_markup=markup)
            
            # Утилиты
            elif call.data == 'timer':
                bot.send_message(call.message.chat.id, "⏰ Функция таймера будет реализована позже")
            
            elif call.data == 'reminder':
                bot.send_message(call.message.chat.id, "📝 Функция напоминаний в разработке")
            
            elif call.data == 'calculator':
                bot.send_message(call.message.chat.id, "🧮 Калькулятор: отправьте математическое выражение")
            
            elif call.data == 'password_gen':
                import string
                password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
                bot.send_message(call.message.chat.id, f"🔐 Сгенерированный пароль: `{password}`", parse_mode='Markdown')
            
            # Возврат в главное меню
            elif call.data == 'back_main':
                send_welcome(call.message)
            
            # Мини-игры
            elif call.data == 'guess_number':
                number = random.randint(1, 10)
                bot.send_message(call.message.chat.id, f"🎯 Я загадал число от 1 до 10. Попробуй угадать!")
            
            elif call.data == 'rps_game':
                markup = types.InlineKeyboardMarkup(row_width=3)
                btn1 = types.InlineKeyboardButton('🪨 Камень', callback_data='rps_rock')
                btn2 = types.InlineKeyboardButton('✂️ Ножницы', callback_data='rps_scissors')
                btn3 = types.InlineKeyboardButton('📄 Бумага', callback_data='rps_paper')
                markup.add(btn1, btn2, btn3)
                bot.send_message(call.message.chat.id, "✂️ Выберите ваш ход:", reply_markup=markup)
            
            # Игра камень-ножницы-бумага
            elif call.data.startswith('rps_'):
                user_choice = call.data.split('_')[1]
                choices = {'rock': '🪨 Камень', 'scissors': '✂️ Ножницы', 'paper': '📄 Бумага'}
                bot_choice = random.choice(list(choices.keys()))
                
                result = ""
                if user_choice == bot_choice:
                    result = "🤝 Ничья!"
                elif (user_choice == 'rock' and bot_choice == 'scissors') or \
                     (user_choice == 'scissors' and bot_choice == 'paper') or \
                     (user_choice == 'paper' and bot_choice == 'rock'):
                    result = "🎉 Вы победили!"
                else:
                    result = "😔 Вы проиграли!"
                
                bot.send_message(call.message.chat.id, 
                               f"Ваш выбор: {choices[user_choice]}\n"
                               f"Мой выбор: {choices[bot_choice]}\n"
                               f"{result}")
            
            # Обработка остальных команд
            else:
                bot.send_message(call.message.chat.id, f"Команда '{call.data}' в разработке 🛠️")
                
    except Exception as e:
        print(f"Ошибка: {e}")

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()

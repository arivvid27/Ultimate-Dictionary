from replit import db
from PyDictionary import PyDictionary
from time import sleep

PyDict = PyDictionary()

while True:
	print('#' * 5,'USER MANUAL', '#' * 5 )
	user = input("""
INSERT = [insert]
KNOW MEANING = [know]
SHOW ALL CREATED WORDS = [show]
DELETE = [delete]
QUIT = [quit]
>>> """)

	if user == 'insert':
		user_input_name = input('What is the name? > ')
		user_input_define = input('What is the definition > ')
		print('Ok')
		print('INSERTING...')
		sleep(3)
		try:
			db[user_input_name] = user_input_define
			print('Success!')
		except Exception:
			print('Oops. There seems to be an error. Please run this on repl.it, or comment below so arivvid27 can fix it.')
	elif user == 'know':
		user_know = input('What word do you want to know the meaning for? > ')
		if user_know in db:
			try:
				value = db[user_know]
				print(value)
			except:
				print('Oops. There seems to be an error. Please comment below so arivvid27 can fix it.')
		elif user_know not in db:
			print(PyDict.meaning(user_know))
		elif user_know not in db or PyDict:
			print('Oops. The word you are looking for does not seem to exist. Please check your spelling, or insert a word of your own.')
	elif user == 'show':
		keys = db.keys()
		for keys in keys:
			print(keys)
		sleep(5)
	elif user == 'delete':
		user_delete = input('What word do you want to delete? > ')
		del db[user_delete]
		print('Deleted')
	elif user == 'quit':
		print('ok!')
		exit()
	else:
		print('I don\'t know that')
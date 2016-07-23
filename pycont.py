import sqlite3
import os
import platform
import re

version = 4.4

#get platform type
platform = platform.system()

# the contacts list
con_list = []
conn = sqlite3.connect("")
def connect():
	global conn;
	conn = sqlite3.connect("contacts.db")

connect()

try:
	conn.execute("CREATE TABLE contacts (name TEXT, number TEXT,address TEXT,email TEXT);")
except sqlite3.OperationalError:
	pass

def isContactInList(name):
	contacts_list()
	if name not in con_list:
		print "there is no contact named",name
	else:
		return True

def help():
	print "*** PyCont contacts manager <powerd by Aleiti Technologies all rights reserved> v {0} ***\
		\ntype a to add a new contact.\
		\ntype \"rm contactName\" to remove contact.\
		\ntype \"ls\" to print out all the contacts.\
		\ntype \"p contactName\" to print out contact information.\
		\ntype \"edit contactName\" to update contact.\
		\ntype \"exit\" to exit.\
		\ntype \"clear\" to clear the screen.\
		\ntype h to see this help list again.".format(version)

def contacts_list():
	cursor = conn.execute("SELECT *  from contacts")
	for column in cursor:
		con_list.append(column[0])
	return con_list

def clear_screen():
	if platform == "Windows":
		os.system('cls')
	elif platform == "Linux":
		os.system("clear")

#program's main loop
def start():
	clear_screen()
	help()
	connect()
	while 1:
		del con_list[:]
		user_input = raw_input();

		if user_input == "a":
			add_contact();
		elif user_input == "exit":
			conn.close()
			if __name__ == '__main__':
				exit()
			else:
				break
		elif user_input == "clear":
			clear_screen()
		elif user_input == "h":
			help()
		elif user_input == "ls":
			print_all();
		elif user_input == "":
			pass
		else :
			args = user_input.split()
			arg_length = len(args)
			if args[0] == "rm":
				if arg_length < 2:
					print "please identity a contact to delete."
				if arg_length is 2:
					if isContactInList(args[1]):
						rm_contact(args[1])
			elif args[0] == "p":
				if arg_length < 2:
					print "please identity a contact to show."
				elif isContactInList(args[1]):
					print_contact(args[1])
			elif args[0] == "edit":
				if arg_length < 2:
					print "please identity a contact to edit."				
				elif isContactInList(args[1]):
					update(args[1])
			else :
				print "unknown command."

def add_contact():
	#keep the contacts list up to date
	contacts_list()
	# get the name and make sure that it is not repeated and it has charcters
	while True:
		name = raw_input("enter contact's name : ")
		if name in con_list:
			print "contact name \"{0}\" is already in use.".format(name)
		if len(name) < 1:
			pass
		else:
			break
	#get number and make sure that it dosn't contain any letters
	while True:
		number = raw_input("number : ")
		if number.isalpha():
			print "enter a vaild number ."
		else:
			break
	address = raw_input("address : ")
	email = raw_input("email : ")
	conn.execute("INSERT INTO contacts (name,number,address,email) VALUES (\"{0}\",\"{1}\",\"{2}\",\"{3}\");"\
		.format(name,number,address,email))
	conn.commit()

def rm_contact(argument):
	conn.execute("DELETE FROM contacts WHERE name IS \"{0}\"".format(argument))
	print "contact {0} deleted successfuly.".format(argument)
	conn.commit()
# print the list of available contacts
def print_all():
	enum_contacts = contacts_list()
	x = 1
	length = len(enum_contacts)
	if length is 0:
		print "sorry there is no contacts yet :("
		return
	while True:
		if x == 1:
			print "**********"
		print enum_contacts[x - 1]
		if x is not length:
			print "----"
		if x is length:
			print "**********"
			break
		x += 1

def print_contact(argument):
	info = conn.execute("SELECT * FROM contacts WHERE name IS \"%s\""% argument)
	for column in info:
		print "\n< {0} >".format(column[0])
		print "number : {0}".format(column[1])
		print "address : {0}".format(column[2])
		print "email : {0}".format(column[3])
		print "***************"

def update(name):
	#keep the contacts list up to date
	contacts_list()
	argument = name
	info = conn.execute("SELECT * FROM contacts WHERE name IS \"%s\""% argument)
	for column in info:
		name = column[0]
		number = column[1]
		address = column[2]
		email = column[3]
	print "press enter to keep it as it is"
	# get the name and make sure that it is not repeated 
	while True:
		new_name = raw_input("name : {0} =====> ".format(name))
		if new_name in con_list:
			print "contact name \"{0}\" is already in use.".format(new_name)
		elif len(new_name) is 0:
			new_name = name
			break
		else:
			break
	#get number and make sure that it dosn't contain any letters
	while True:
		new_number = raw_input("number : {0} =====> ".format(number))
		if new_number.isalpha():
			print "please enter a vaild number ."
		elif len(new_number) is 0:
			new_number = number
			break
		else:
			break
	new_address = raw_input("address : {0} =====> ".format(address))
	if len(new_address) is 0:
		new_address = address
	new_email = raw_input("email : {0} =====> ".format(email))
	if len(new_email) is 0:
		new_email = email
	conn.execute("UPDATE contacts SET name = \"{1}\",number = \"{2}\",address = \"{3}\",email = \"{4}\" WHERE name IS \"{0}\""\
		.format(argument,new_name,new_number,new_address,new_email))
	conn.commit()

#starts the program
if __name__ == '__main__':
	start()
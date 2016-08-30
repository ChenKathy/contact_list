#Architecting a contact list:

#1. How to treat Name?
#2. Categories under name (mobile, email, bday) can be listed as key value pairs

contact = {("Diana", "Banana"): [{"mobile": "415-555-5555"}, {"email": "diana@hack.com"}, {"birthday": "Feb 21"}]}

class Contact(object):
	def __init__(self, first_name, last_name, mobile = "", email = ""):
		self.first_name = first_name
		self.last_name = last_name
		self.mobile = mobile
		self.email = email

	def add_contacts():
		contacts = []

	def send_text(self, text):

		if self.mobile == "":
			print "Please enter a number"

		else:
			text = raw_input("Enter text message")
			print "To:", self.mobile, "-", text


def main():
	contacts = []

	first_name = raw_input("Enter first name").lower()
	last_name = raw_input("Enter last name").lower()
	mobile = raw_input("Enter mobile")
	email = raw_input("Enter email")

	
	contact_firstname = Contact(first_name, last_name, mobile, email)
	contacts.append(contact_firstname)

	for items in contacts:
		print items.__dict__
	
if __name__ == '__main__':
	main()




# def add_contact():
# 	firstname = lower.raw_input("first name: ")
# 	lastname = lower.raw_input("last name: ")
# 	mobile = raw_input("mobile: ")
# 	email = lower.raw_input("email: ")
# 	birthday = raw_input("birthday: ")

# contact[firstname, lastname] = []

# def change_mobile():

# def change_last():
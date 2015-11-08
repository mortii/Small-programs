"""
Checks to see if email-address provided is valid given some constraints:
A valid email address is of the format: username@websitename.extension
Username can only contain letters, digits, dash and underscore.
Website name can have letters and digits. 
Maximum length of the extension is 3. 
"""

import re

# n = int(raw_input())
# email_list = []

# for x in range(n):
#     email = raw_input()
#     email_list.append(email)
    

email = "lara@hackerrank.com"
email2 = "brian-23@hackerrank.com"
email3 = "britts_54@hackerrank.com"
email4 = "britts_54!@hackerrank.com"

email_list = [email, email2, email3, email4]


def check_valid_email(email):
	match = re.search(r"^([\w-]+)@([^\W_]+)\.([a-z]+\Z)", email)
	
	if match:
		username = match.group(1)
		website = match.group(2)
		extension = match.group(3)

		# print "username", username 
		# print "website", website
		# print "extension", extension

		if len(extension) < 4:
			return True
		return False

	return False


valid_email_list = filter(check_valid_email, email_list)
valid_email_list.sort()
print valid_email_list




#Version without complex regex:

"""
import re

# n = int(raw_input())
# email_list = []

# for x in range(n):
# 	email = raw_input()
# 	email_list.append(email)

email = "lara@hackerrank.com"
email2 = "britts_54@hackerrank.com"
email3 = "britts_54!@hackerrank.com"
email_list = [email, email2, email3]


def check_website(website):
	#website can only contain letters and digits
	
	if len(website) < 1:
		return False
		
	for char in list(website):
		if not char.isalnum():
			return False
	return True


def check_username(username):
	#Username can only contain letters, digits, dash and underscore

	if len(username) < 1:
		return False

	for char in list(username):
		match = re.search(r"\w", char) # \w = a letter or digit or underbar [a-zA-Z0-9_]
		if not match:
			return False
	return True


def check_extension(extension):
	# extension has to be longer than 4 letters

	if len(extension) < 4:
		return True
	return False


def check_valid_email(email):
	username_index = email.find("@")
	extension_index = email.find(".")

	if username_index == -1 or extension_index == -1:
		return False

	username = email[:username_index]
	website = email[username_index+1:extension_index]
	extension = email[extension_index+1:]

	if check_extension(extension) and check_username(username) and check_website(website):
		return True
	return False


valid_email_list = filter(check_valid_email, email_list)
valid_email_list.sort()
print valid_email_list
"""
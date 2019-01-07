import os, smtplib, getpass, sys


#  functions
def closeProgram(logMessage):
	print("\nClosing Program")
	sys.exit("[LOG MESSAGE] : " + logMessage)

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #


#  user input
allowed_mail_servers = ["gmail", "g", "yahoo", "y"]

mail_server = input('\n\nMail Server - Gmail(g) / Yahoo(y) ? : ')
print("\n")

mail_server = mail_server.lower()

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #


# configure SMTP server
if mail_server in allowed_mail_servers:
	if mail_server == "g" or mail_server == "gmail":
		mail_server = "gmail"
		port = 587
	elif mail_server == "y" or mail_server == "yahoo":
		mail_server = "yahoo"
		port = 25
	smtp_server = "smtp." + mail_server + ".com"
else:
	print("[ERROR] The entered mail server is not allowed!")
	print("[FIX] Allowed mail servers:")
	for allowed_mail_server in allowed_mail_servers:
		print("    • " + allowed_mail_server) 
	closeProgram("Incorrect user input!")

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

# user input

user_email = input('Enter user email: ')
user_email_password = getpass.getpass('Enter email password: ')
email_recipient = input('Enter the recipient email: ')

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

# setup email variables
email_subject = input('Enter an Email Subject: ') 
email_body = input('Message To Email: ')
email_total_count = int( input('Number of emails copies to send: ') )

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

# send email
try:
    server = smtplib.SMTP(smtp_server, port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user_email, user_email_password)

    for i in range(1, email_total_count + 1):
        # subject = os.urandom(9)
        msg = "From: " + str(user_email) + "\nSubject: " + str(email_subject) + "\n" + str(email_body)
        server.sendmail(user_email, email_recipient, msg)
        print("\rTotal emails sent: %i" % i)
        sys.stdout.flush()
    server.quit()
    print('\n All emails assumingly sent :)!!!')
except KeyboardInterrupt:
	closeProgram("Keyboard Interrupt by user.")
except smtplib.SMTPAuthenticationError:
    closeProgram("The username or password you entered was incorrect.")


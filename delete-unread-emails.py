from imapclient import IMAPClient

my_mail = IMAPClient('imap.gmail.com', ssl=True, port=993)
my_mail.login("Your Email", "Your Password")
total_Emails = my_mail.select_folder('Inbox')

# This shows how many messages are in the inbox
print(f"You have total {total_Emails[b'EXISTS']} messages in your Gmail.")

deleteMessage = my_mail.search('UNSEEN')
my_mail.delete_messages(deleteMessage)

# This shows the number of unread messages that have been deleted
print(f'{len(deleteMessage)} unread messages have been deleted.')

my_mail.logout()
print('Logged out successfully')

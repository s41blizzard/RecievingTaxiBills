import imaplib

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('zard.41@gmail.com', 'Gravity84>>')

mail.select("taxi")
result, data = mail.search(None, '(SINCE "01-OCT-2019" BEFORE "20-DEC-2019")')
ids = data[0]  # data is a list.
id_list = ids.split()  # ids is a space separated string
print(len(id_list))





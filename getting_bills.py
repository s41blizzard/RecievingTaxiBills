import imaplib

mail = imaplib.IMAP4_SSL('imap.mail.ru')
mail.login('s41.blizzard@mail.ru', 'Gravity2558')

mail.select("cabs_reciept")
result, data = mail.search(None, "ALL")
ids = data[0]  # data is a list.
id_list = ids.split()  # ids is a space separated string
latest_email_id = id_list[-1]  # get the latest
print(id_list)

# result, data = mail.fetch(latest_email_id, "(RFC822)")  # fetch the email body (RFC822) for the given ID
#
# raw_email = data[0][1]  # here's the body, which is raw text of the whole email
# # including headers and alternate payloads

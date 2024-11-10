def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    a = 0
    if '@' and ('.com' or '.net' or '.ru') in recipient and '@' and ('.com' or '.net' or '.ru') in sender:
        a = 1
    if a == 0:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
        return
    if (sender == recipient) and a == 1:
        print("Нельзя отправить письмо самому себе!")
        return
    if (str(sender) != 'university.help@gmail.com') and a == 1:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
    elif a == 1:
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)


send_email(str(input()), str(input()), sender=str(input()))
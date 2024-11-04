import hashlib


def checks():
    f = open("Users/users.txt", "r")
    for x in f.readlines():
        data = x.split(":")
        if '\n' in data[4]:
            data[4] = data[4][0:-1]
        print(data)
    f.close()


def create_user(user_name, password, card, cvv, date):
    f = open("Users/users.txt", "r")
    current_data = f.read()
    f.close()
    f = open("Users/users.txt", "w")
    # user_name = input("enter user name: ")
    # password = input("enter password: ")
    # card = input("enter card number: ")
    # cvv = input("enter cvv: ")
    # date = input("enter date: ")
    user = user_name+":"+hashlib.sha256(password.encode()).hexdigest()+":"+hashlib.sha256(card.encode()).hexdigest()+":"+hashlib.sha256(cvv.encode()).hexdigest()+":"+hashlib.sha256(date.encode()).hexdigest()
    current_data = current_data+"\n"+user
    f.write(current_data)
    f.close()

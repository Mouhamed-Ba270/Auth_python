import getpass
database = {"clcoding" : "976729", "pythonclcoding" : "2502"}
username = input("Entrer votre nom d'utilisateur : ")
password = getpass.getpass("Entrer votre mot de passe : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter encore votre mot de passe : ")
        break
print("Connectez avec Success")
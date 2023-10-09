import re

password = input("Lütfen Parolanız giriniz: ")

if len(password) < 10:
    print("Parolanız en fazla 10 karakter uzunluğunda olmalıdır.")
elif not re.search(r"[A-Z]", password):
    print("Parolanız en az bir tane Büyük harf içermelidir.")
elif not re.search(r"[a-z]", password):
    print("Parolanız en az bir tane küçük harf içermelidir.")
elif not re.search(r"[0-9]", password):
    print("Parolanız en az bir tane rakam içermelidir.")
elif not re.search(r"[!@#\$%\^&\*\(\)-_=\+\[\]{}\|;:'\",<>\.?/\\]", password):
    print("Parolanız en az bir adet özel karakter içermelidir.")
else:
    print("Parolanız güçlüdür.")

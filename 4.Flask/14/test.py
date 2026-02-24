import bcrypt

password = "in_password_ro_becasi_nadi"
print(password)
password_byte = password.encode("utf-8")

hashed = bcrypt.hashpw(password_byte, bcrypt.gensalt())
print(hashed)


new_password = "in_password_ro_becasi_bedi"
new_password_byte = new_password.encode("utf-8")


if bcrypt.checkpw(new_password_byte, hashed):
    print("Yes")
else:
    print("No")
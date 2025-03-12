# 1 Lists (indexing, slicing, adding/removing elements)

# users = ["mosha", "coder", "aisha", "abdul"]
# users[0] = "juma"  # edit
# users.append("jesca")  # add
# users.remove("coder")  # remove
# users.sort() # sort
# print(users)


# 2 Tuples

users = ("mosha", "coder", "aisha", "abdul", "sea")

# print(users[2:4]) slice

user = {"name": "John Smith", "email": "john@gmail.com",
        "password": "123", "address": "kigamboni", "city": "dar es salaam"}


# print(
#     f"Hello sir, My name is {user['name']} \n and my account credentials are \n email: {user['email']}, password is"
#     f"{user['password']}, My address is {user['city']}, {user['address']}")

for key, value in user.items():
    print(f"{key}: {value}")

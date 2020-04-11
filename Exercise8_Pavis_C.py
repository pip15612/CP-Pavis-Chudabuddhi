usernameInput = input("username:")
password = input("password:")

if usernameInput == "pavis" and password == "chudabuddhi":
    print("Milk 20THB Press 1")
    print("Banana 15THB Press 2")
    chose = int(input("เลือกสินค้า"))
    if chose == 1:
        many = int(input("How many"))
        milk = int(20)
        print("ราคา", milk * many, "THB")
    elif chose == 2:
        many = int(input("How many"))
        banana = int(15)
        print("ราคา",banana*many,"THB")
else:
    print("Error")

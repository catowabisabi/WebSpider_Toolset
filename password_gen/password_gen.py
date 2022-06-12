#Password Generator 密碼生産器
import random
# 生産一個由字母組成的清單
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# 使用者輸入他們希望的密碼長度與字符組合與數量
print("Welcome to the Password Generator!\n歡迎使用密碼生産器\n")
num_letters = int(input("How many letters would you like in your password?\n請問你希望你的密碼中有多少個英文字母?\n")) 
num_symbols = int(input(f"\nHow many symbols would you like?\n請問你希望你的密碼中有多少個符號?\n"))
num_numbers = int(input(f"\nHow many numbers would you like?\n請問你希望你的密碼中有多少個數字?\n"))


password_list = []

# 分別於字母, 字符, 數字三個清單中隨機提出使用者所設定數量的字母, 字符, 數字, 組成新的字串。
# 我們在這裏使用append, 但我們也可以使用extend
for char in range(1, num_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, num_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, num_numbers + 1):
  password_list += random.choice(numbers)

# 隨機打亂密碼元素清單中的字串
random.shuffle(password_list)

# 打密碼元素清單連結為字串。
password = ""
for char in password_list:
  password += char

print(f"Your password is (你的密碼為) : {password}\n\n\n")
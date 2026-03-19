from constants import SPECIAL_CHARS, NUMERIC_CHARS
from constants import LOWERCASE_LETTER_CHARS, UPPERCASE_LETTER_CHARS
from constants import MIN_LENGTH, MAX_LENGTH
import secrets


def main():

    pwd_length = get_pwd_length()
    pwd_type = get_pwd_type()    
    pwd_gen = generat_pwd(pwd_length, pwd_type)
    print(pwd_gen)


# Prompt user for a password length
def get_pwd_length():
    while True:
        pwd_length = int(input(f"Choose a password length between {MIN_LENGTH} and {MAX_LENGTH}: "))
        if pwd_length >= MIN_LENGTH and pwd_length <= MAX_LENGTH:
            return pwd_length
        else:
            print(f"Error: Invalid input. Input must be a number between {MIN_LENGTH} and {MAX_LENGTH}.")

# Prompt two option: pure random or custom
def get_pwd_type():
    while True:
        pwd_type = input("Random [r] or Custom [c]? ").lower()
        if pwd_type == "r" or pwd_type == "c":
            return pwd_type        
        else: 
            print("Error: Invalid input. Input must be either r or c.")
        
# Generate password based on the pwd_type (custom or random)
def generat_pwd(pwd_length, pwd_type):
    conf_dic = {
        "1": SPECIAL_CHARS,
        "2": NUMERIC_CHARS,
        "3": UPPERCASE_LETTER_CHARS,
        "4": LOWERCASE_LETTER_CHARS
    }

    if pwd_type == "c":
        usr_conf_options = input(
            "Special characters [1]\n"
            "Numeric characters [2]\n"
            "UPPER CASE CHARACTERS [3]\n"
            "lower case characters [4]\n"
            "What characters do you wish to include: "
            )     
        
        custom_pwd_str = ""

        for i in usr_conf_options:
            if i in conf_dic:
                custom_pwd_str += conf_dic[i]
        
        return ''.join(secrets.choice(custom_pwd_str) for i in range(pwd_length))
     

    if pwd_type == "r":
        rand_pwd_str = SPECIAL_CHARS + NUMERIC_CHARS + LOWERCASE_LETTER_CHARS + UPPERCASE_LETTER_CHARS
        return ''.join(secrets.choice(rand_pwd_str) for i in range(pwd_length)) 
        

if __name__ == "__main__":
    main()
from constants import SPECIAL_CHARS, NUMERIC_CHARS
from constants import LOWERCASE_LETTER_CHARS, UPPERCASE_LETTER_CHARS
from constants import MIN_LENGTH, MAX_LENGTH
from ascii_art import ascii_art
from rich.console import Console
import secrets

console = Console()


def main():
    for line in ascii_art:
        console.print(line, style="purple")
    
    pwd_length = get_pwd_length()
    pwd_type = get_pwd_type()    
    
    if pwd_type == "c":
        gened_pwd = generate_custom_pwd(pwd_length)
    elif pwd_type == "r":
        gened_pwd = generate_rand_pwd(pwd_length)

    console.print(f"\n[yellow]your generated password is:[/yellow] [blue]{gened_pwd}")



# Prompt user for a password length
def get_pwd_length():
    while True:
        try:
            pwd_length = int(console.input(f"[yellow]Choose a password length between {MIN_LENGTH} and {MAX_LENGTH}: "))
            if pwd_length >= MIN_LENGTH and pwd_length <= MAX_LENGTH:
                return pwd_length
            else:
                console.print(f"[red]Error: Input must be a number between {MIN_LENGTH} and {MAX_LENGTH}.")
        except ValueError:
            console.print(f"Error: Input must be a number.", style="red")
        
# Prompt two option: pure random or custom
def get_pwd_type():
    while True:
        pwd_type = console.input("\n[yellow]Random (r) or Custom (c)? ").lower()
        if pwd_type == "r" or pwd_type == "c":
            return pwd_type        
        else: 
            console.print("Error: Invalid input. Input must be either r or c.", style="red")
        
# Generate password based on the pwd_type (custom or random)
def generate_custom_pwd(pwd_length):
    # Custom config dictionary
    conf_dic = {
        "1": SPECIAL_CHARS,
        "2": NUMERIC_CHARS,
        "3": UPPERCASE_LETTER_CHARS,
        "4": LOWERCASE_LETTER_CHARS
    }

    # Prompt user for the chars they want
    while True:
        usr_conf_options = console.input(
            "\n[orange1]Special characters (1)\n"
            "Numeric characters (2)\n"
            "UPPER CASE CHARACTERS (3)\n"
            "lower case characters (4)\n"
            "[yellow]What characters do you wish to include: "
            )     
        
        # Create custom string to generate a password
        custom_pwd_str = ""
        for i in usr_conf_options:
            if i in conf_dic:
                custom_pwd_str += conf_dic[i]

        if custom_pwd_str == "":
            console.print("Error: Select at least one valid option", style="red")
        else:
            return ''.join(secrets.choice(custom_pwd_str) for i in range(pwd_length))


def generate_rand_pwd(pwd_length):
    rand_pwd_str = SPECIAL_CHARS + NUMERIC_CHARS + LOWERCASE_LETTER_CHARS + UPPERCASE_LETTER_CHARS
    return ''.join(secrets.choice(rand_pwd_str) for i in range(pwd_length)) 
        

if __name__ == "__main__":
    main()
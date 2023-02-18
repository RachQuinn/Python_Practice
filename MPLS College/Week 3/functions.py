#email = "CONTACT@MINNEAPOLIS.EDU"
# emails are coventionally written in lowercase
# convert email to lowercase, and print it
#print(email.lower())

def convert_number(number_of_megabytes):
    return number_of_megabytes * 100000

def main():
    number_of_mb = float(input("What is the number of megabytes?"))
    converted_number = convert_number(number_of_mb)
    print(f"You have {converted_number}")

main()



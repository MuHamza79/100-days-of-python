x = int(input("Enter a number: "))
#CASE STATEMENT
match x:
    case _ if x<0:
        print("The number is negative")
    case _ if x==0:
        print("The number is zero")
    case _ if x > 0 :
        if x <= 10:
            print("The numbe is b/w 1-10")
        elif x > 10 and x <= 20:
            print("The number is b/w 10-20")
        else:
            print("The number is greater than 20")
    case _:
        print("Something went wrong")
print("The number you entered was",x)


def check_status(code):
    match code:
        case 200:
            return "Success"
        case 404:
            return "Not Found"
        case _:  # This is the default case
            return "Unknown Status Code"

print(check_status(404))  # Output: Not Found
print(check_status(500))  # Output: Unknown Status Code

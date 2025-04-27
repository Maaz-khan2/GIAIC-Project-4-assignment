def main():
    print("Delete this line and write your code here! :)")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

def main():
    dividend : int = int(input("please enter the value is divided"))  
    dividor : int = int(input("Please Enter the value id divided"))  

    quotient: int = dividend // dividor
    remainder: int = dividend % dividor

    print(f"The result of this division is" + str(quotient) "with remainder is" + str(remainder))
    if __name__ == '__main__':
     main()
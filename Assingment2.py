def func():
    while True:
        try:
            num = int(input("Enter a number : "))
            if 10000 >= num >= 0:

                return(num)

            elif num < 0 or num > 10000:
                print("you need number between 0-10000")


        except:
            print("try again ")


print(func())
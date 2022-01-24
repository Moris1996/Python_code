def up_n_down(my_str, num):
    my_new_str = ""
    big_letter = 0
    small_letter = 0
    numbers = 0
    sign = 0

    for i in my_str:
        my_str = input("please enter text :")
        num = int(input("please enter number 1 or 2 :"))
        my_new_str = my_str +(i)
        if num == 1:

            my_str = chr(i) + chr(ord("A")-32)
            big_letter += 1

            return my_new_str

        elif num == 2:
            pass

        else:
            print("enter only 1 or 2 number !")

up_n_down("cvcb",1)
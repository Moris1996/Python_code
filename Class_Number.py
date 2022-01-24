import datetime

class Number:
    def __init__(self):
        self.__numlen = 0
        self.__numarr = []
        self.__datetime = ""

    def __str__(self):
        return str(self.__numarr)

    def get_len(self):
        return self.__numlen

    def get_arr(self):
        return self.__numarr

    def get_datetime(self):
        return self.__datetime

    def set_len(self, num):
        self.__numlen = num

    def set_arr(self, arr):
        self.__numarr = arr

    def set_datetime(self, datetime):
        self.__datetime = datetime


    def addElement(self, num):
        if isinstance(num, int) and num not in self.__numarr:
            self.__numarr.append(num)
            self.__numlen += 1
            self.__datetime = datetime.datetime.now()

        else:
            print("only int and unique num please!")
            return




    def remove(self, num):
        if isinstance(num, int) and num in self.__numarr:
            self.__numarr.remove(num)
            self.__numlen -= 1
        else:
            print("Only int and existing number.")
            return







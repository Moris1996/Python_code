class Students:
    """
    calss of student's , by name, last name, age, grade
    with setters and getters to get info and set new info .
    """

    def __init__(self, name, lname, age, grade):
        self.__firstName = name
        self.__lastName = lname
        self.__age = age
        self.__grade = grade

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__firstName

    def get_lname(self):
        return self.__lastName

    def get_grade(self):
        return self.__grade

    def set_name(self, name):
        self.__firstName = name

    def set_lname(self, lname):
        self.__lastName = lname

    def set_grade(self, grade):
        self.__grade = grade


    def set_age(self, age):
        self.__age = age


    def update_name(self, name):
        if len(name) > 10:
            print("The limit is 10 characters")
        else:
            self.__name = name

    def update_lname(self, lname):
        if len(lname) > 20:
            print("The limit is 20 characters")
        else:
            self.__lname = lname

    def update_grade(self, grade):
        if 0 > self.__grade or self.__grade > 100:
            print("enter number between 0-100 , please . ")
        else:
            self.__grade = grade

    def __str__(self):
        return f"Name: {self.__firstName}\nLast Name: {self.__lastName}\nAge: {self.__age}\nGrade: {self.__grade}"




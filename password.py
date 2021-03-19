class Password:
    def __init__(self):
        self.__password = ""
        self.__message = ""

    def setPassword(self, password):
        self.__password = password

    def __checkOne(self):
        valid = True
        if len(self.__password) >= 8:
            return valid
        else:
            self.__message += "Your password needs to contain at least 8 characters.\n"
            return False

    def __checkTwo(self):
        valid = True
        if self.__password.find("password") == -1:
            return valid
        else:
            self.__message += "Your password cannot contain the word \"password\".\n"
            return False

    def __checkThree(self):
        valid = True
        if not self.__password.endswith("123"):
            return valid
        else:
            self.__message += "Your password cannot end in \"123\".\n"
            return False

    def __checkFour(self):
        valid = True
        digit = 0
        for i in range(len(self.__password)):
            if self.__password[i].isdigit():
                digit += 1
            else:
                pass
        if digit >= 2:
            return valid
        else:
            self.__message += "You need at least two numbers in your password.\n"
            return False

    def __checkFive(self):
        valid = True
        if self.__password.isalnum():
            return valid
        else:
            self.__message += "Your password cannot contain special characters.\n"
            return False

    def getErrorMessage(self):
        return self.__message

    def isValid(self):
        # self.__checkOne()
        # self.__checkTwo()
        # self.__checkThree()
        # self.__checkFour()
        # self.__checkFive()
        counter = 0
        if self.__checkOne():
            counter += 1
        if self.__checkTwo():
            counter += 1
        if self.__checkThree():
            counter += 1
        if self.__checkThree():
            counter += 1
        if self.__checkFour():
            counter += 1
        if self.__checkFive():
            counter += 1

        if counter == 6:
            return True
        else:
            return False



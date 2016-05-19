# class for Member data
class Member:
    # initialize default values
    def __init__(self):
        self.__age = 0
        self.__win_loss = 0
        self.__login = 0
        self.__gender = ''
        self.__income = 0
        self.__status = ''

    def getAge(self):
        return self.__age

    def setAge(self, val):
        self.__age = val

    def getWinLoss(self):
        return self.__win_loss

    def setWinLoss(self, val):
        self.__win_loss = val

    def getLogin(self):
        return self.__login

    def setLogin(self, val):
        self.__login = val

    def getGender(self):
        return self.__gender

    def setGender(self, val):
        self.__gender = val

    def getIncome(self):
        return self.__income

    def setIncome(self, val):
        self.__income = val

    def getStatus(self):
        return self.__status

    def setStatus(self, val):
        self.__status = val
# >> End : Member <<


# class for Rule data
class Rule:
    # initialize default values
    def __init__(self):
        self.__age = 0
        self.__win_loss = 0
        self.__login = 0
        self.__gender = ''
        self.__income = 0
        self.__status = ''
        self.__age_operator = ''
        self.__win_loss_operator = ''
        self.__login_operator = ''
        self.__gender_operator = ''
        self.__income_operator = ''

    def getAge(self):
        return self.__age

    def setAge(self, val):
        self.__age = val

    def getWinLoss(self):
        return self.__win_loss

    def setWinLoss(self, val):
        self.__win_loss = val

    def getLogin(self):
        return self.__login

    def setLogin(self, val):
        self.__login = val

    def getGender(self):
        return self.__gender

    def setGender(self, val):
        self.__gender = val

    def getIncome(self):
        return self.__income

    def setIncome(self, val):
        self.__income = val

    def getStatus(self):
        return self.__status

    def setStatus(self, val):
        self.__status = val

    def getAgeOperator(self):
        return self.__age_operator

    def setAgeOperator(self, val):
        self.__age_operator = val

    def getWinLossOperator(self):
        return self.__win_loss_operator

    def setWinLossOperator(self, val):
        self.__win_loss_operator = val

    def getLoginOperator(self):
        return self.__login_operator

    def setLoginOperator(self, val):
        self.__login_operator = val

    def getGenderOperator(self):
        return self.__gender_operator

    def setGenderOperator(self, val):
        self.__gender_operator = val

    def getIncomeOperator(self):
        return self.__income_operator

    def setIncomeOperator(self, val):
        self.__income_operator = val
# >> End : Rule <<
import model
import util

class RuleController:
    __FILE_HEADER_AMT = 2
    __COL_INDEX_AGE = 0
    __COL_INDEX_WINLOSS = 1
    __COL_INDEX_LOGIN = 2
    __COL_INDEX_GENDER = 3
    __COL_INDEX_INCOME = 4
    __COL_INDEX_STATUS = 5
    __COL_NAMES = {__COL_INDEX_AGE: 'Age'
        , __COL_INDEX_WINLOSS: 'Win-Loss'
        , __COL_INDEX_LOGIN: 'Log-in'
        , __COL_INDEX_GENDER: 'Gender'
        , __COL_INDEX_INCOME: 'Income'
        , __COL_INDEX_STATUS: 'Status'} # column names
    __COL_AMT = len(__COL_NAMES) # amount of column names

    __COND_SEP = ',' # sperator of rule property condition
    __COND_AMT = 2 # amount of factors of rule property condition
    __NO_IMPACT = '-' # no-impact sign
    __GRATER_EQUAL = 'ge'
    __LESS = 'lt'
    __EQUAL = 'e'
    __OPERATORS = {__GRATER_EQUAL: ' >= ', __LESS: ' < ', __EQUAL: ' = '}
    __GENDERS = ['male', 'female']
    __STATUS = ['discontinue', 'continue']

    def readRules(self, ruleFile):
        rules = []

        try:
            file = open(ruleFile, 'r')
            lines = list(file)

            if len(lines) > self.__FILE_HEADER_AMT:
                for i in range(self.__FILE_HEADER_AMT, len(lines)):
                    ruleProp = lines[i].split()

                    try:
                        rule = self.__createRule(ruleProp)
                    except Exception as e:
                        raise Exception("Rule #" + str(i + 1 - self.__FILE_HEADER_AMT) + " : " + str(e))

                    rules.append(rule)

                file.close()
                return rules
            else:
                file.close()
                raise Exception('There is no rule information!')
        except IOError:
            raise Exception(ruleFile + ' does not exist!')

    def __createRule(self, ruleProp):
        if len(ruleProp) == self.__COL_AMT:
            rule = model.Rule()

            age = ruleProp[self.__COL_INDEX_AGE] # get Age at index 0 of Rule Properties
            if age != self.__NO_IMPACT:
                conds = age.split(self.__COND_SEP)
                if len(conds) == self.__COND_AMT:
                    operator = conds[0] # get operator(GE or LT) at index 0
                    if operator.lower() in self.__OPERATORS:
                        rule.setAgeOperator(operator)
                    else:
                        raise Exception('The Operator of Age is not correct!')

                    val = util.parseInt(conds[1]) # get Age value at index 1
                    if type(val) == int:
                        rule.setAge(val)
                    else:
                        raise Exception('Age should be integer!')
                else:
                    raise Exception('Age info is not correct!')
            else:
                rule.setAge(self.__NO_IMPACT)

            win_loss = ruleProp[self.__COL_INDEX_WINLOSS] # get Win-Loss at index 1 of Rule Properties
            if win_loss != self.__NO_IMPACT:
                conds = win_loss.split(self.__COND_SEP)
                if len(conds) == self.__COND_AMT:
                    operator = conds[0] # get operator(GE or LT) at index 0
                    if operator.lower() in self.__OPERATORS:
                        rule.setWinLossOperator(operator)
                    else:
                        raise Exception('The Operator of Win-Loss is not correct!')

                    val = util.parseInt(conds[1]) # get Win-Loss value at index 1
                    if type(val) == int:
                        rule.setWinLoss(val)
                    else:
                        raise Exception('Win-Loss should be integer!')
                else:
                    raise Exception('Win-Loss info is not correct!')
            else:
                rule.setWinLoss(self.__NO_IMPACT)

            login = ruleProp[self.__COL_INDEX_LOGIN] # get Log-in at index 2 of Rule Properties
            if login != self.__NO_IMPACT:
                conds = login.split(self.__COND_SEP)
                if len(conds) == self.__COND_AMT:
                    operator = conds[0] # get operator(GE or LT) at index 0
                    if operator.lower() in self.__OPERATORS:
                        rule.setLoginOperator(operator)
                    else:
                        raise Exception('The Operator of Log-in is not correct!')

                    val = util.parseInt(conds[1]) # get Log-in value at index 1
                    if type(val) == int:
                        rule.setLogin(val)
                    else:
                        raise Exception('Log-in should be integer!')
                else:
                    raise Exception('Log-in info is not correct!')
            else:
                rule.setLogin(self.__NO_IMPACT)

            gender = ruleProp[self.__COL_INDEX_GENDER] # get Gender at index 3 of Rule Properties
            if gender != self.__NO_IMPACT:
                rule.setGenderOperator(self.__EQUAL)

                if gender.lower() in self.__GENDERS:
                    rule.setGender(gender)
                else:
                    raise Exception('Gender should be "Male" or "Female"!')
            else:
                rule.setGender(self.__NO_IMPACT)

            income = ruleProp[self.__COL_INDEX_INCOME] # get Income at index 4 of Rule Properties
            if income != self.__NO_IMPACT:
                conds = income.split(self.__COND_SEP)
                if len(conds) == self.__COND_AMT:
                    operator = conds[0] # get operator(GE or LT) at index 0
                    if operator.lower() in self.__OPERATORS:
                        rule.setIncomeOperator(operator)
                    else:
                        raise Exception('The Operator of Income is not correct!')

                    val = util.parseInt(conds[1]) # get Income value at index 1
                    if type(val) == int:
                        rule.setIncome(val)
                    else:
                        raise Exception('Income should be integer!')
                else:
                    raise Exception('Income info is not correct!')
            else:
                rule.setIncome(self.__NO_IMPACT)

            status = ruleProp[self.__COL_INDEX_STATUS] # get Status at index 5 of Rule Properties
            if status.lower() in self.__STATUS:
                rule.setStatus(status)
            else:
                raise Exception('Status should be "Continue" or "Discontinue"!')

            return rule
        else:
            raise Exception('Rule information is not correct!')

    def __getReadableRule(self, rule):
        conds = []

        if rule.getAge() != self.__NO_IMPACT:
            conds.append(self.__COL_NAMES[self.__COL_INDEX_AGE] + self.__OPERATORS[rule.getAgeOperator().lower()] + str(rule.getAge()))

        if rule.getWinLoss() != self.__NO_IMPACT:
            conds.append(self.__COL_NAMES[self.__COL_INDEX_WINLOSS] + self.__OPERATORS[rule.getWinLossOperator().lower()] + str(rule.getWinLoss()))

        if rule.getLogin() != self.__NO_IMPACT:
            conds.append(self.__COL_NAMES[self.__COL_INDEX_LOGIN] + self.__OPERATORS[rule.getLoginOperator().lower()] + str(rule.getLogin()))

        if rule.getGender() != self.__NO_IMPACT:
            conds.append(self.__COL_NAMES[self.__COL_INDEX_GENDER] + self.__OPERATORS[rule.getGenderOperator().lower()] + str(rule.getGender()))

        if rule.getIncome() != self.__NO_IMPACT:
            conds.append(self.__COL_NAMES[self.__COL_INDEX_INCOME] + self.__OPERATORS[rule.getIncomeOperator().lower()] + str(rule.getIncome()))

        return 'If ' + ' & '.join(conds) + ' --> ' + rule.getStatus()

    def genReadableRules(self, readableRuleFile, rules):
        file = open(readableRuleFile, 'w')

        for i in range(len(rules)):
            readableText = self.__getReadableRule(rules[i])
            file.write('Rule ' + str(i + 1) + ' : ' + readableText + '\n')

        file.close()

    def __matchCondition(self, memberValue, condOperator, condValue):
        if condValue != self.__NO_IMPACT:
            if condOperator.lower() == self.__GRATER_EQUAL:
                if memberValue >= condValue:
                    return True
                else:
                    return False
            elif condOperator.lower() == self.__LESS:
                if memberValue < condValue:
                    return True
                else:
                    return False
            else:
                # check equality between 2 values
                if memberValue == condValue:
                    return True
                else:
                    return False
        else:
            return True

    def matchRules(self, rules, member):
        for rule in rules:
            if (self.__matchCondition(member.getAge(), rule.getAgeOperator(), rule.getAge())) \
                and self.__matchCondition(member.getWinLoss(), rule.getWinLossOperator(), rule.getWinLoss()) \
                and self.__matchCondition(member.getLogin(), rule.getLoginOperator(), rule.getLogin()) \
                and self.__matchCondition(member.getGender(), rule.getGenderOperator(), rule.getGender()) \
                and self.__matchCondition(member.getIncome(), rule.getIncomeOperator(), rule.getIncome()):
                return rule.getStatus()

        return "Non-Match"

class MemberController:
    __FILE_HEADER_AMT = 2
    __COL_INDEX_AGE = 0
    __COL_INDEX_WINLOSS = 1
    __COL_INDEX_LOGIN = 2
    __COL_INDEX_GENDER = 3
    __COL_INDEX_INCOME = 4
    __COL_INDEX_STATUS = 5
    __COL_NAMES = {__COL_INDEX_AGE: 'Age'
        , __COL_INDEX_WINLOSS: 'Win-Loss'
        , __COL_INDEX_LOGIN: 'Log-in'
        , __COL_INDEX_GENDER: 'Gender'
        , __COL_INDEX_INCOME: 'Income'
        , __COL_INDEX_STATUS: 'Status'} # column names
    __COL_AMT = len(__COL_NAMES) # amount of column names

    __GENDERS = ['male', 'female']
    __REPORT_HEADER = __COL_NAMES[__COL_INDEX_AGE] + "\t" + __COL_NAMES[__COL_INDEX_WINLOSS] + "\t" + __COL_NAMES[__COL_INDEX_LOGIN] + "\t" + __COL_NAMES[__COL_INDEX_GENDER] + "\t" + __COL_NAMES[__COL_INDEX_INCOME] + "\t" + __COL_NAMES[__COL_INDEX_STATUS] + "\n------------------------------------------------------\n"
    __REPORT_ITEM_FORMAT = "%s\t%s\t\t%s\t%s\t%s\t%s\n"

    def readMembers(self, memFile):
        members = []

        try:
            file = open(memFile, 'r')
            lines = list(file)

            if len(lines) > self.__FILE_HEADER_AMT:
                for i in range(self.__FILE_HEADER_AMT, len(lines)):
                    memProp = lines[i].split()

                    try:
                        member = self.__createMember(memProp)
                    except Exception as e:
                        raise Exception("Member #" + str(i + 1 - self.__FILE_HEADER_AMT) + " : " + str(e))

                    members.append(member)

                file.close()
                return members
            else:
                file.close()
                raise Exception('There is no member information!')
        except IOError:
            raise Exception(memFile + ' does not exist!')

    def __createMember(self, memProp):
        if len(memProp) == self.__COL_AMT:
            member = model.Member()

            age = util.parseInt(memProp[self.__COL_INDEX_AGE]) # get Age at index 0 of Member Properties
            if type(age) == int:
                member.setAge(age)
            else:
                raise Exception('Age should be integer!')

            win_loss = util.parseInt(memProp[self.__COL_INDEX_WINLOSS]) # get Win-Loss at index 1 of Member Properties
            if type(win_loss) == int:
                member.setWinLoss(win_loss)
            else:
                raise Exception('Win-Loss should be integer!')

            login = util.parseInt(memProp[self.__COL_INDEX_LOGIN]) # get Log-in at index 2 of Member Properties
            if type(login) == int:
                member.setLogin(login)
            else:
                raise Exception('Log-in should be integer!')

            gender = memProp[self.__COL_INDEX_GENDER] # get Gender at index 3 of Member Properties
            if gender.lower() in self.__GENDERS:
                member.setGender(gender)
            else:
                raise Exception('Gender should be "Male" or "Female"!')

            income = util.parseInt(memProp[self.__COL_INDEX_INCOME]) # get Income at index 4 of Member Properties
            if type(income) == int:
                member.setIncome(income)
            else:
                raise Exception('Income should be integer!')

            status = memProp[self.__COL_INDEX_STATUS] # get Gender at index 5 of Member Properties
            member.setStatus(status)

            return member
        else:
            raise Exception('Member information is not correct!')

    def genMemberReport(self, memReportFile, members):
        file = open(memReportFile, 'w')

        # write Header
        file.write(self.__REPORT_HEADER)

        for i in range(len(members)):
            file.write(self.__REPORT_ITEM_FORMAT % (members[i].getAge(), members[i].getWinLoss(), members[i].getLogin(), members[i].getGender(), members[i].getIncome(), members[i].getStatus()))

        file.close()













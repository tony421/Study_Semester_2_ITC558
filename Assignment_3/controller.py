import model #import for Member and Rules models
import util #import for utility functions (eg. parseInt)

# create class for rule-related functions
class RuleController:
    __FILE_HEADER_AMT = 2 # number of headers in a file
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
    __OPERATORS = {__GRATER_EQUAL: ' >= ', __LESS: ' < ', __EQUAL: ' = '} # possible operators
    __GENDERS = ['male', 'female'] # gender info
    __STATUS = ['discontinue', 'continue'] # status info

    # function: read rules from the file
    def readRules(self, ruleFile):
        # the list of rules
        rules = []

        try:
            # open file for read
            file = open(ruleFile, 'r')

            # convert file to list object to get the list of lines
            lines = list(file)

            # number of lines should be more than header lines
            if len(lines) > self.__FILE_HEADER_AMT:
                # loop all rules by skipping header lines
                for i in range(self.__FILE_HEADER_AMT, len(lines)):
                    # split rule properties from the line
                    ruleProp = lines[i].split()

                    try:
                        # create a new rule info
                        rule = self.__createRule(ruleProp)
                    except Exception as e:
                        raise Exception("Rule #" + str(i + 1 - self.__FILE_HEADER_AMT) + " : " + str(e) + ' Please check the information.')

                    # add the rule to the list
                    rules.append(rule)

                # close the file
                file.close()
                return rules
            else:
                file.close()
                raise Exception('There is no rule information! Please check the information.')
        except IOError:
            # inform an error when the file not found
            raise Exception(ruleFile + ' does not exist!')

    def __createRule(self, ruleProp):
        # number of rule properties should be 6
        if len(ruleProp) == self.__COL_AMT:
            # create a new object of Rule
            rule = model.Rule()

            age = ruleProp[self.__COL_INDEX_AGE] # get Age at index 0 of Rule Properties
            if age != self.__NO_IMPACT: # if Age is not no-impact, then
                # split Age conditions by ','
                conds = age.split(self.__COND_SEP)

                # If number of conditions is 2, then
                if len(conds) == self.__COND_AMT:
                    operator = conds[0] # get operator(GE or LT) at index 0
                    if operator.lower() in self.__OPERATORS: # if Age operator is in possible operators, then
                        # set the operator to the property
                        rule.setAgeOperator(operator)
                    else:
                        # else, inform an error
                        raise Exception('The Operator of Age is not correct!')

                    val = util.parseInt(conds[1]) # get Age value at index 1
                    if type(val) == int: # if the Age value is int, then
                        # set the value to the property
                        rule.setAge(val)
                    else:
                        # else, inform an error
                        raise Exception('Age should be integer!')
                else:
                    # else, inform an error
                    raise Exception('Age info is not correct!')
            else:
                # else, set No-Impact to Age prop
                rule.setAge(self.__NO_IMPACT)

            win_loss = ruleProp[self.__COL_INDEX_WINLOSS] # get Win-Loss at index 1 of Rule Properties
            if win_loss != self.__NO_IMPACT: # if Win-Loss is not no-impact, then
                # split Win-Loss conditions by ','
                conds = win_loss.split(self.__COND_SEP)

                # If number of conditions is 2, then
                if len(conds) == self.__COND_AMT:
                    operator = conds[0] # get operator(GE or LT) at index 0
                    if operator.lower() in self.__OPERATORS: # if Win-Liss operator is in possible operators, then
                        # set the operator to the property
                        rule.setWinLossOperator(operator)
                    else:
                        # else, inform an error
                        raise Exception('The Operator of Win-Loss is not correct!')

                    val = util.parseInt(conds[1]) # get Win-Loss value at index 1
                    if type(val) == int: # if the Win-Loss value is int, then
                        # set the value to the property
                        rule.setWinLoss(val)
                    else:
                        # else, inform an error
                        raise Exception('Win-Loss should be integer!')
                else:
                    # else, inform an error
                    raise Exception('Win-Loss info is not correct!')
            else:
                # else, set No-Impact to Win-Loss prop
                rule.setWinLoss(self.__NO_IMPACT)

            login = ruleProp[self.__COL_INDEX_LOGIN] # get Log-in at index 2 of Rule Properties
            if login != self.__NO_IMPACT: # if Log-in is not no-impact, then
                # split Log-in conditions by ','
                conds = login.split(self.__COND_SEP)

                # If number of conditions is 2, then
                if len(conds) == self.__COND_AMT:
                    operator = conds[0] # get operator(GE or LT) at index 0
                    if operator.lower() in self.__OPERATORS: # if Log-in operator is in possible operators, then
                        rule.setLoginOperator(operator) # set the operator to the property
                    else:
                        # else, inform an error
                        raise Exception('The Operator of Log-in is not correct!')

                    val = util.parseInt(conds[1]) # get Log-in value at index 1
                    if type(val) == int: # if the Log-in value is int, then
                        rule.setLogin(val) # set the value to the property
                    else:
                        # else, inform an error
                        raise Exception('Log-in should be integer!')
                else:
                    # else, inform an error
                    raise Exception('Log-in info is not correct!')
            else:
                rule.setLogin(self.__NO_IMPACT) # else, set No-Impact to Log-in prop

            gender = ruleProp[self.__COL_INDEX_GENDER] # get Gender at index 3 of Rule Properties
            if gender != self.__NO_IMPACT: # if Gender is not no-impact, then
                # set the equal operator to the property
                rule.setGenderOperator(self.__EQUAL)

                if gender.lower() in self.__GENDERS: # if Gender value is in possible genders, then
                    rule.setGender(gender) # set the value to the property
                else:
                    # else, inform an error
                    raise Exception('Gender should be "Male" or "Female"!')
            else:
                # else, set No-Impact to Gender prop
                rule.setGender(self.__NO_IMPACT)

            income = ruleProp[self.__COL_INDEX_INCOME] # get Income at index 4 of Rule Properties
            if income != self.__NO_IMPACT: # if Income is not no-impact, then
                conds = income.split(self.__COND_SEP) # split xxx conditions by ','

                # If number of conditions is 2, then
                if len(conds) == self.__COND_AMT:
                    operator = conds[0] # get operator(GE or LT) at index 0
                    if operator.lower() in self.__OPERATORS: # if Income operator is in possible operators, then
                        rule.setIncomeOperator(operator) # set the operator to the property
                    else:
                        # else, inform an error
                        raise Exception('The Operator of Income is not correct!')

                    val = util.parseInt(conds[1]) # get Income value at index 1
                    if type(val) == int: # if the Income value is int, then
                        rule.setIncome(val) # set the value to the property
                    else:
                        # else, inform an error
                        raise Exception('Income should be integer!')
                else:
                    # else, inform an error
                    raise Exception('Income info is not correct!')
            else:
                # else, set No-Impact to Income prop
                rule.setIncome(self.__NO_IMPACT)

            status = ruleProp[self.__COL_INDEX_STATUS] # get Status at index 5 of Rule Properties
            if status.lower() in self.__STATUS: # if Status operator is in possible statuses, then
                rule.setStatus(status) # set the value to the property
            else:
                # else, inform an error
                raise Exception('Status should be "Continue" or "Discontinue"!')

            # return the instance of rule
            return rule
        else:
            raise Exception('Rule information is not correct!')

    # function: generate readable format of rule parameter
    def __getReadableRule(self, rule):
        # the list of rule conditions
        conds = []

        # if Age is not no-impact, then add readable condition to the list
        if rule.getAge() != self.__NO_IMPACT:
            conds.append(self.__COL_NAMES[self.__COL_INDEX_AGE] + self.__OPERATORS[rule.getAgeOperator().lower()] + str(rule.getAge()))

        # if Win-Loss is not no-impact, then add readable condition to the list
        if rule.getWinLoss() != self.__NO_IMPACT:
            conds.append(self.__COL_NAMES[self.__COL_INDEX_WINLOSS] + self.__OPERATORS[rule.getWinLossOperator().lower()] + str(rule.getWinLoss()))

        # if Log-in is not no-impact, then add readable condition to the list
        if rule.getLogin() != self.__NO_IMPACT:
            conds.append(self.__COL_NAMES[self.__COL_INDEX_LOGIN] + self.__OPERATORS[rule.getLoginOperator().lower()] + str(rule.getLogin()))

        # if Gender is not no-impact, then add readable condition to the list
        if rule.getGender() != self.__NO_IMPACT:
            conds.append(self.__COL_NAMES[self.__COL_INDEX_GENDER] + self.__OPERATORS[rule.getGenderOperator().lower()] + str(rule.getGender()))

        # if Income is not no-impact, then add readable condition to the list
        if rule.getIncome() != self.__NO_IMPACT:
            conds.append(self.__COL_NAMES[self.__COL_INDEX_INCOME] + self.__OPERATORS[rule.getIncomeOperator().lower()] + str(rule.getIncome()))

        # join all conditions with ' & ' and indicate the status and the return the value
        return 'If ' + ' & '.join(conds) + ' --> ' + rule.getStatus()

    # function: generate readable rules file
    def genReadableRules(self, readableRuleFile, rules):
        # open the file for write
        file = open(readableRuleFile, 'w')

        # loop all rules
        for i in range(len(rules)):
            try:
                readableText = self.__getReadableRule(rules[i]) # generate readable format of rule
                file.write('Rule ' + str(i + 1) + ' : ' + readableText + '\n') # write the value to the file
            except:
                file.close() # close the file
                # if any error occurs, inform an error
                raise Exception('Could not generate readable rule of Rule #' + str(i + 1))

        # close the file
        file.close()

    # function: match any rule condition with member value
    def __matchCondition(self, memberValue, condOperator, condValue):
        # if the rule condition value is not no-impact, then
        if condValue != self.__NO_IMPACT:
            # if the rule condition operator is grater-than or equal, then check the condition
            if condOperator.lower() == self.__GRATER_EQUAL:
                if memberValue >= condValue:
                    return True
                else:
                    return False
            # if the rule condition operator is less-than, then check the condition
            elif condOperator.lower() == self.__LESS:
                if memberValue < condValue:
                    return True
                else:
                    return False
            # if the rule condition operator is equal, then check the condition
            else:
                if memberValue == condValue:
                    return True
                else:
                    return False
        else:
            # else, return True
            return True

    # function: match all rules with member properties
    def matchRules(self, rules, member):
        # loop all rules
        for rule in rules:
            # check every conditions of the rule with all member properties
            if (self.__matchCondition(member.getAge(), rule.getAgeOperator(), rule.getAge())) \
                and self.__matchCondition(member.getWinLoss(), rule.getWinLossOperator(), rule.getWinLoss()) \
                and self.__matchCondition(member.getLogin(), rule.getLoginOperator(), rule.getLogin()) \
                and self.__matchCondition(member.getGender().lower(), rule.getGenderOperator(), rule.getGender().lower()) \
                and self.__matchCondition(member.getIncome(), rule.getIncomeOperator(), rule.getIncome()):
                # If the match found, return the status of the rule
                return rule.getStatus()

        # There is no any match rule, return "Non-Match"
        return "Non-Match"
# >> End : RuleController <<


#create class for member-related functions
class MemberController:
    __FILE_HEADER_AMT = 2 # number of headers in a file
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

    __GENDERS = ['male', 'female'] # gender info

    # report header
    __REPORT_HEADER = __COL_NAMES[__COL_INDEX_AGE] + "\t" + __COL_NAMES[__COL_INDEX_WINLOSS] + "\t" + __COL_NAMES[__COL_INDEX_LOGIN] + "\t" + __COL_NAMES[__COL_INDEX_GENDER] + "\t" + __COL_NAMES[__COL_INDEX_INCOME] + "\t" + __COL_NAMES[__COL_INDEX_STATUS] + "\n------------------------------------------------------\n"
    __REPORT_ITEM_FORMAT = "%s\t%s\t\t%s\t%s\t%s\t%s\n" # format of report item

    # function: read members from the file
    def readMembers(self, memFile):
        # the list of members
        members = []

        try:
            file = open(memFile, 'r') # open the file for read
            lines = list(file) # convert file to list object to get the list of lines

            if len(lines) > self.__FILE_HEADER_AMT: # number of lines should be more than header lines
                for i in range(self.__FILE_HEADER_AMT, len(lines)): # loop all lines by skipping header lines
                    memProp = lines[i].split() # split all properties from the line

                    try:
                        member = self.__createMember(memProp) # create a new member info
                    except Exception as e:
                        # inform any error occurs when creating the member object
                        raise Exception("Member #" + str(i + 1 - self.__FILE_HEADER_AMT) + " : " + str(e) + ' Please check the information.')

                    members.append(member) # add the instance to the list

                file.close()
                return members # return all members
            else:
                file.close()
                raise Exception('There is no member information! Please check the information.')
        except IOError:
            # inform an error when the file not found
            raise Exception(memFile + ' does not exist!')

    # function: create a new instance of member
    def __createMember(self, memProp):
        # number of member properties should be 6
        if len(memProp) == self.__COL_AMT:
            member = model.Member() # create a new instance of member

            age = util.parseInt(memProp[self.__COL_INDEX_AGE]) # get Age at index 0 of Member Properties
            if type(age) == int: # if Age is int, then
                member.setAge(age) # set the value to the prop
            else:
                raise Exception('Age should be integer!') # inform an error

            win_loss = util.parseInt(memProp[self.__COL_INDEX_WINLOSS]) # get Win-Loss at index 1 of Member Properties
            if type(win_loss) == int: # if Win-Loss is int, then
                member.setWinLoss(win_loss) # set the value to the prop
            else:
                raise Exception('Win-Loss should be integer!') # inform an error

            login = util.parseInt(memProp[self.__COL_INDEX_LOGIN]) # get Log-in at index 2 of Member Properties
            if type(login) == int: # if Log-in is int, then
                member.setLogin(login) # set the value to the prop
            else:
                raise Exception('Log-in should be integer!') # inform an error

            gender = memProp[self.__COL_INDEX_GENDER] # get Gender at index 3 of Member Properties
            if gender.lower() in self.__GENDERS: # if Gender is in the possible genders, then
                member.setGender(gender) # set the value to the prop
            else:
                raise Exception('Gender should be "Male" or "Female"!') # inform an error

            income = util.parseInt(memProp[self.__COL_INDEX_INCOME]) # get Income at index 4 of Member Properties
            if type(income) == int: # if Income is int, then
                member.setIncome(income) # set the value to the prop
            else:
                raise Exception('Income should be integer!') # inform an error

            status = memProp[self.__COL_INDEX_STATUS] # get Gender at index 5 of Member Properties
            member.setStatus(status) # set the value to the prop

            return member # return the instance
        else:
            # else, inform an error
            raise Exception('Member information is not correct!')

    def genMemberReport(self, memReportFile, members):
        file = open(memReportFile, 'w') # open the file for write

        try:
            file.write(self.__REPORT_HEADER) # write the report header

            # loop all members
            for i in range(len(members)):
                # write all member properties in a line
                file.write(self.__REPORT_ITEM_FORMAT % (members[i].getAge(), members[i].getWinLoss(), members[i].getLogin(), members[i].getGender(), members[i].getIncome(), members[i].getStatus()))
        except:
            file.close() # close the file
            # if any error occurs, inform an error
            raise Exception('Could not generate Member Report!')

        file.close() # close the file
# >> End : MemberController <<
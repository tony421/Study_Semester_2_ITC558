# ITC558 - Programming Principles
# Assignment 3
# Thawatchai Jidsodsai (11587622)

# This program is developed for AB Games company
# so that help the company to recognizes the reason why its customers discontinue with it

import model #import for Member and Rules models
import controller # import for Member and Rule functions
import util #import for utility functions (eg. parseInt)

RULE_FILE = 'Rules.txt'
READABLE_RULE_FILE = 'ReadableRules.txt'
MEMBER_FILE = "Members.txt"
MEMBER_REPORT_FILE = "MemberReport.txt"
rules = []
members = []

try:
    ruleController = controller.RuleController() # create RuleController instance
    rules = ruleController.readRules(RULE_FILE) # read logic rules from file
    ruleController.genReadableRules(READABLE_RULE_FILE, rules) # generate ReadableRules file
    # for r in rules:
    #     print("[%s:%s], [%s:%s], [%s:%s], [%s:%s], [%s:%s], %s" % (r.getAgeOperator(), r.getAge(), r.getWinLossOperator(), r.getWinLoss(), r.getLoginOperator(), r.getLogin(), r.getGenderOperator(), r.getGender(), r.getIncomeOperator(), r.getIncome(), r.getStatus()))

    memberController = controller.MemberController() # create MemberController instance
    members = memberController.readMembers(MEMBER_FILE) # read member info from file
    # for mem in members:
    #     print("%s, %s, %s, %s, %s, %s" % (mem.getAge(),  mem.getWinLoss(), mem.getLogin(), mem.getGender(), mem.getIncome(), mem.getStatus()))

    # loop all members for matching with the rules
    for i in range(len(members)):
        try:
            status = ruleController.matchRules(rules, members[i]) # match a member with rules
            members[i].setStatus(status) # set status for a member
        except:
            # if any error occurs while matching rules, inform an error
            raise Exception('Could not match rules with Member #' + str(i + 1))

    memberController.genMemberReport(MEMBER_REPORT_FILE, members) # generate MemberReport file

    print('The program has been executed successfully, please check the result files.')
except Exception as e:
    print("Error => " + str(e))
import model
import controller
import util

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

    # loop all members to match rules
    for member in members:
        status = ruleController.matchRules(rules, member) # match a member with rules
        member.setStatus(status) # set status for a member

    memberController.genMemberReport(MEMBER_REPORT_FILE, members) # generate MemberReport file

    print('The program has been executed successfully, please check the result files.')
except Exception as e:
    print("Error => " + str(e))
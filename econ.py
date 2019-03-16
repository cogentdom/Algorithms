income = 1000
test_scores1 = 607.3 + 3.85*income - 0.0423*(income*income)
print "Test scores:" + str(test_scores1) + " when income is: " + str(income)
income = 11000
test_scores2 = 607.3 + 3.85*income - 0.0423*(income*income)
print "Test scores:" + str(test_scores2) + " when income is: " + str(income)
test_scores1 =test_scores1 * -1
test_scores2 =test_scores2 * -1
percent_diff = 100*(test_scores1 - test_scores2) / ((test_scores1 + test_scores2)/2)
print "Percent Diff is: " + str(percent_diff)

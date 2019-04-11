import sys
import DataSet as ds
import Test


if __name__ == '__main__':
    orig_stdout = sys.stdout
    f = open("Results/results.log", "w")
    sys.stdout = f    # <---------------------------------------------------- comment this line out to print in terminal
    print "###############################"
    print "### BANKNOTE AUTHENTICATION ###"
    print "###############################"
    banknote_auth_dataset = ds.DataSet(filename="DataSets/data_banknote_authentication.txt")
    Test.kFoldCrossValidation(5, banknote_auth_dataset)
    print "################"
    print "### PHISHING ###"
    print "################"
    phishing_websites_dataset = ds.DataSet(filename="DataSets/Training Dataset.arff")
    Test.kFoldCrossValidation(5, phishing_websites_dataset)
    print "################"
    print "#### HTRU 2 ####"
    print "################"
    HTRU_dataset = ds.DataSet(filename="DataSets/HTRU_2.arff")
    Test.kFoldCrossValidation(5, HTRU_dataset)
    sys.stdout = orig_stdout
    f.close()

import sys
import DataSet as ds
import Test


if __name__ == '__main__':
    orig_stdout = sys.stdout
    f = open("Results/results.log", "w")
    sys.stdout = f    # <---------------------------------------------------- comment this line out to print in terminal
    print "###########################"
    print "# BANKNOTE AUTHENTICATION #"
    print "###########################"
    banknote = ds.DataSet(filename="DataSets/data_banknote_authentication.txt")
    Test.kFoldCrossValidation(5, banknote)
    print "###########################"
    print "######### PHISHING ########"
    print "###########################"
    phishing = ds.DataSet(filename="DataSets/phishing.txt")
    Test.kFoldCrossValidation(5, phishing)
    print "###########################"
    print "########## HTRU 2 #########"
    print "###########################"
    HTRUDataSet = ds.DataSet(filename="DataSets/HTRU_2.txt")
    Test.kFoldCrossValidation(5, HTRUDataSet)
    sys.stdout = orig_stdout
    f.close()

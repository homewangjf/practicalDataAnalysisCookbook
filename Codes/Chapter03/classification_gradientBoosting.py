# this is needed to load helper from the parent folder
import sys
sys.path.append('..')

# the rest of the imports
import helper as hlp
import pandas as pd
import sklearn.ensemble as en

@hlp.timeit
def fitGradientBoosting(data):
    '''
        Build a gradient boosting classier
    '''
    # create the classifier object
    gradBoost = en.GradientBoostingClassifier(
        min_samples_split=100, n_estimators=500)

    # fit the data
    return gradBoost.fit(data[0],data[1])

# the file name of the dataset
r_filename = '../../Data/Chapter03/bank_contacts.csv'

# read the data
csv_read = pd.read_csv(r_filename)

# split the data into training and testing
train_x, train_y, \
test_x,  test_y, \
labels = hlp.split_data(
    csv_read, 
    y = 'credit_application',
    x = ['n_duration','n_nr_employed',
        'prev_ctc_outcome_success','n_euribor3m',
        'n_cons_conf_idx','n_age','month_oct',
        'n_cons_price_idx','edu_university_degree','n_pdays',
        'dow_mon','job_student','job_technician',
        'job_housemaid','edu_basic_6y']
)

# train the model
classifier = fitGradientBoosting((train_x, train_y))

# classify the unseen data
predicted = classifier.predict(test_x)

# print out the results
hlp.printModelSummary(test_y, predicted)

# print out the importance of features
for counter, (nm, label) \
    in enumerate(
        zip(labels, classifier.feature_importances_)
    ):
    print("{0}. {1}: {2}".format(counter, nm,label))
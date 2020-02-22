import csv, pandas as pd, numpy as np, sys

def read_csv_file(data_file):
    csvRows = []
    csvFileObj = open(data_file) #reads in data file
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        csvRows.append(row)
    csvFileObj.close()
    return csvRows

data_file = sys.argv[1]
avg_up_to = float(input("please enter a time value to avg up to: "))

column_list = list(map(list, zip(*read_csv_file(data_file))))
del column_list[0]
for column in column_list:
    column[0] = float(column[0])
sorted_column_list = sorted(column_list) #sorts each list member by its time stamp (the number in the list)

print("csv file read, now prepping data frame")

delay_dict = {words[0]:words[1:] for words in sorted_column_list}
data_frame = pd.DataFrame(delay_dict).astype(float)
delete_list = []
avgd_list = []
for label, content in data_frame.items():
    int_list = list(range(1, 102)) #makes a list of numbers between 1 and 101 for the next if statement to compare to 
    if label/10000 in int_list: #looks for label which is multiple of 10000 to then average from with the code below 
        s1 = data_frame.loc[0:, label:(label+1000)].astype(float) 
        mean_absorbtions = s1.mean(axis=1, skipna = True)
        delay_list = list(s1)
        for x in delay_list:
            avgd_list.append(x)
        mean_delay = np.mean(delay_list)
        delete_list.append(mean_delay)
        data_frame[mean_delay] = mean_absorbtions
        data_frame = data_frame.drop(delay_list, axis = 1) # delete columns that have been averaged n.b .drop creates a new object by default hence having to tell it perform on the orginal dataframe
    elif label >= avg_up_to and label not in avgd_list: # puts delays over 22000 and that have not already been removed into the delete list 
            delete_list.append(label)

print("data frame avgd, now prepping avgd csv")
          
sorted_df = data_frame.sort_index(axis=1) # sorts the delay columns in ascending order 
late_time_rmvd_array = sorted_df.drop(delete_list, axis = 1) #removes delays from 22000 onwards based on what has been put in delete list
file_str = data_file.split('.') #writes array to a new csv file with avgd appened to the name 
late_time_rmvd_array.to_csv(file_str[0] + '_avgd' + '.csv')

print("avg done")

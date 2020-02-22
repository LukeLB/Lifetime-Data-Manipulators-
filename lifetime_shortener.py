import os, csv, operator, sys
def remove_latetime(data_file):
	csvRows = []
	csvFileObj = open(data_file)	
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		csvRows.append(row)
	csvFileObj.close()
	column_list = list(map(list, zip(*csvRows)))
	EO_delays = column_list[0]
	del column_list[0]
	for column in column_list:
		column[0] = float(column[0])
	sorted_column_list = sorted(column_list)
	sorted_column_list
	early_list = []
	late_list = []
	early_list.append(EO_delays)
	late_list.append(EO_delays)
	for i in sorted_column_list:
		if int(i[0]) <= 9000:
			early_list.append(i) 
		else:
			late_list.append(i) 
	return_csv_early_list = list(map(list, zip(*early_list)))
	file_str = data_file.split('.')
	print(file_str)
	csvFileObj = open(file_str[0] + '_shortened' + '.csv', 'w', newline='')
	csvWriter = csv.writer(csvFileObj)
	for row in return_csv_early_list:
		csvWriter.writerow(row)
	csvFileObj.close()	
if len(sys.argv) > 1:
	remove_latetime(sys.argv[1])	
else:
	print('You forgot the file name Mahima')

# Lifetime-Data-Manipulators-
Scripts used to manipulate raw data collected off the LIFEtime 100 kHz laser system so it can be imported into KOALA analysis software. 

Two python files are provided lifetime_shortener.py and lifetime_averager.py these can both be used to reduce the file size of raw data retrieved from high repetition rate laser system called LIFEtime based at the Central Laser Facility in the Rutherford Appleton Laboratory. These scripts can be used for any matrix with Pixel vs Time (ns), with the matrix elements being intensities.  

lifetime_shortener.py works by reading the the original csv file, ordering the time axis in ascending order and then removing all time points above 9 us. The script then creates a new csv file named [original_file_name]_shortend.

lifetime_averager.py works on the basis that all data points past 9 us are from the repition rate of the laser and so at every microsecond past 9 us the multiple time points may be averaged to one, thus reducing data points and file size. The script when run will ask for a time point in ns to average up to and will remove the rest of the time points past that. lifetime_averager.py imports the raw data into a pandas data frame from which it orders and then averages all data points in a range at every 1 us data point after 9 us. The script then creates a new csv file named [original_file_name]_avgd

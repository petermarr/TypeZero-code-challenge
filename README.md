This code was written by Peter Marr on 3 May 2017 using Python 2.7.12 on Kubuntu. It was written for the TypeZero internship coding challenge assigned by James Quinn on 2 May 2017.

The program "linreg.py" does simple linear regression on a data set and displays the slope (m) and y-intercept (b) values for the relationship. The user is then prompted for a x-value, for which the model's predicted y-value is computed and displayed. Finally, the user is prompted for a list of x-values separated by commas, all of whose corresponding model y-values are calculated and displayed in a list.

To use the program, run the command:

python linreg.py [file]

where [file] is a text file in the same directory, containing data in a specific format (explained below). The program requires exactly one command line argument, and will exit if this condition is not met. The program will also exit if the file is empty, does not exist, or is malformed.

The data in the read file must have the following formatting: each line contains one ordered pair, in the form "x y", where the values are separated by a space. For example:

1 2

3 4

5 6


This file format was chosen because it is a typical format for data reported by machines or physical systems; data reported slightly differently, perhaps with a comma separating the values, could be quickly reformatted with a find-and-replace function, or the code could be altered to accept different formats or additional information (for example, the time that each trial was taken).

After doing a simple linear regression computation on the data set given, the code will prompt the user to enter one x-value, for which the model's predicted y-value will be calculated and displayed in standard output. If the user's input is malformed, the input will be rejected and the user prompted to try again.

Finally, the user will be prompted to enter a series of x-values in a comma-separated value format, which is printed as a list. The values are expected in the following format:

1,2,3,4

The predicted y-values for each x-value are also calculated and printed as a list. In the future, the code could be modified to accept file names to read, the files containing x-values or x-value lists for which to calculate y-values.

The repository contains a few test text files to use with the program. data.txt contains a few lines of properly-formatted data, for which the model will correctly calculate values for linear regression. badformat1.txt and badformat2.txt are files with bad data formatting, and the program will exit upon encountering bad files. empty.txt is a completely empty text file and will similarly cause the code to exit. 
import sys

# exit if incorrect number of command line arguments

if len(sys.argv) != 2:
    print("Error: expected exactly one command line argument, for file name. Exiting.")
    sys.exit(1)

filename = sys.argv[1]

# read file, exit if file does not exist
try:
    with open(filename) as f:
        text = f.read()
except IOError:
    print("File does not exist, exiting.")
    sys.exit(1)
            
values = text.split("\n")

# exit if file is empty

if len(text) == 0:
    print("Supplied file is empty, exiting.")
    sys.exit(1)

xval = [ ]
yval = [ ]
xmean = 0
ymean = 0

# parse values and prepare xmean and ymean

for i in range(len(values)):
    s = values[i]
    s.strip()
    if len(s) > 0:
        linevalues = s.split()
        if len(linevalues) != 2:
            print("Lines should have exactly two values separated by a space, exiting.")
            sys.exit(1)
        try:
            xval.append(float(linevalues[0]))
            xmean += xval[i]
            yval.append(float(linevalues[1]))
            ymean += yval[i]
        except ValueError:
            print("Data literals malformed, exiting.")
            sys.exit(1)
    
print("List of x-values: " + str(xval))
print("List of y-values: " + str(yval))

# finish calculating means

xmean = float(xmean)/len(xval)
ymean = float(ymean)/len(yval)

print("\nFor the given set of data, the arithmetic mean of x-values is: " + str(xmean))

# do simple linear regression, which is only valid for a dependent
# variable with one explanatory variable; for example, y = m(x) + b,
# where m and b are coefficients to be found.
# for regression of a more complex function, e.g. y = a(x1) + b(x2) + c,
# a different technique would be necessary

# first find m = sum((x_i - xmean)*(y_i - ymean)) / sum(x_i - xmean)^2
# summing from i=1 to n, where i is the trial and n is the number of trials

mnum = 0.0
mdenom = 0.0

for i in range(len(xval)):
    xdiff = xval[i] - xmean
    ydiff = yval[i] - ymean
    mnum += xdiff * ydiff
    mdenom += xdiff * xdiff
    
m = mnum/mdenom

# now find b, b = ymean - m*xmean

b = ymean - m*xmean

# display map of m and b values

print("\nCoefficients found from simple linear regression:\n{m: " + str(m) + "}\n{b: " + str(b) + "}")

# take in user's x value and find model's corresponding y value

while True:
    try:
        userx = input("\nInput a numeric value for the independent variable 'x' to find the corresponding value for the dependent variable 'y': ")

        usery = m*float(userx) + b;
        break
    # if malformed input, except, loop to beginning of 'while', try again
    except SyntaxError:
        print("\nMalformed input, please try again.")
    except TypeError:
        print("\nMalformed input, please try again.")

print("\nThe y-value for the given x-value is: " + str(usery))

# take in user's list of x values and find model's corresponding y values

while True:
    try:
        userxvals = input("\nInput a list of x values as a series of comma-separated values: ")
        break
    # if malformed input, except, loop to beginning of 'while', try again
    except SyntaxError:
        print("\nMalformed CSV input, please try again.")

print("\nx values supplied by user: ")
print(list(userxvals))

useryvals = [ ]

# calculate model's y values for given x

for i in range(len(userxvals)):
    useryvals.append(m*float(userxvals[i]) + b)

print ("\ny values according to model: ")
print(useryvals)

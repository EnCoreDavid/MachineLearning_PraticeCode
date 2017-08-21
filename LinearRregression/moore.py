import re
import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

non_decimal = re.compile(r'[^\d]+')

for line in open('./moore.csv'):
    r = line.split('\t')

    x = int(non_decimal.sub('', r[2].split('[')[0]))
    y = int(non_decimal.sub('', r[1].split('[')[0]))
    X.append(x)
    Y.append(y)

X = np.array(X)
Y = np.array(Y)

plt.scatter(X, Y)
plt.show()

Y = np.log(Y)
plt.scatter(X, Y)
plt.show()

denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean()*X.sum()) / denominator
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y)) /denominator

Yhat = a*X +b

plt.scatter(X, Y)
plt.plot(X, Yhat)
plt.show()

# calculate r-squared
d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print "the r-squared is: ", r2

# log(tc) = a*year1 + b
#  tc = exp(a*year1 + b) = exp(a*year1) * exp(b)
#  2tc = 2 * exp(a*year1) * exp(b) = exp(ln(2)) * exp(a*year1) * exp(b)
#      = exp(b) * exp(a*year1 + ln(2))
# a*year1 + ln(2) = a* year2
#  year2 = year1 + ln(2)/a

print "time to double:", np.log(2)/a, " years"

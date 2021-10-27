import math
#this will include various tools for analyzing data such as average, standard deviation, correlation, and slope of the graph
#average
#takes an array as input and returns the average
def avg(a):
    x = 0
    for element in a:
        x += element
    return(x / len(a))



#finds standard deviation, the average of how much things deviate from the average
def deviation(a):
    av = avg(a)
    variance = 0
    count = len(a)
    sumdif = 0
    for element in a:
        sumdif += (element - av)**2
    variance = sumdif / (count - 1)
    return(math.sqrt(variance))



#calculate the correlation between 2 sets of data
def correlation(a, b):
   xsamplemean = avg(a)
   ysamplemean = avg(b)
   xsampledev = smplstandarddev(a)
   ysampledev = smplstandarddev(b)
   totals = 0
   i = 0

   while i < len(a):
       totals += ((a[i] - xsamplemean) / xsampledev) * ((b[i] - ysamplemean) / ysampledev)
       i += 1
   r = totals / (len(a) - 1)
   return(r) 

def linear(a, b):
    yint = 0
    m = (a[1] - a[0]) / (b[1] - b[0])
    i = 0
    while i < len(a):
        if a[i] == 0:
            yint = b[i]
        i += 1
    return("y = " + str(m) + "x + " + str(yint))

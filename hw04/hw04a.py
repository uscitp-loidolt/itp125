def median(x):
    x_sort = sorted(x)
    if len(x_sort) < 1:
            print "Median doesn't exist"
    elif len(x_sort) % 2 == 1:
            return x_sort[((len(x_sort)+1)/2)-1]
    else:
            return float(sum(x_sort[(len(x_sort)/2)-1:(len(x_sort)/2)+1]))/2.0

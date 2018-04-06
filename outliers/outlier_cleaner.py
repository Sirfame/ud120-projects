#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    dirty_data = []

    ### your code goes here
    for index in range(0, 90): 
        tup = (abs(net_worths[index] - predictions[index]), index)
        dirty_data.append(tup);
    dirty_data.sort();

    outliers = []
    for index in range(81, 90):
        outliers.append(dirty_data[index][1])
    
    print(outliers)
    
    for index in range(0, 90):
        print(index)
        if index not in outliers:
            tup = (ages[index], net_worths[index], abs(predictions[index] - net_worths[index]))
            cleaned_data.append(tup)
        
            
    print(cleaned_data)
    return cleaned_data


import os
import csv

# Path to collect data from the Resources folder
# wrestlingCSV = os.path.join('..', 'Resources', 'WWE-Data-2016.csv')
fileCsv = "budget_data.csv"

# Read in the CSV file
with open(fileCsv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # print(header)

    totalmonths = 0
    profitlosssum = 0
    perioddifferencesum = 0
    i = 0
    greatestIncrease = 0
    greatestDecrease = 0
    

    for row in csvreader:
        totalmonths = totalmonths + 1
        profitlosssum = profitlosssum + int(row[1])
        if(i != 0):
            diferencia = int(row[1]) - int(lastrow[1])
            perioddifferencesum = perioddifferencesum + diferencia

            if(diferencia < greatestDecrease):
                greatestDecrease = diferencia
            
            if(diferencia > greatestIncrease):
                greatestIncrease = diferencia
            
        lastrow = row 
        i = i + 1
    
    promedio = perioddifferencesum / (totalmonths - 1)


    print(totalmonths)
    print(profitlosssum)
    print(perioddifferencesum)
    print(promedio)
    print(greatestDecrease)
    print(greatestIncrease)
    # for row in csvreader:
    
    #     print(row)    
        # If the wrestler's name in a row is equal to that which the user input, run the 'getPercentages()' function
        # if(nameToCheck == row[0]):
        #     getPercentages(row)

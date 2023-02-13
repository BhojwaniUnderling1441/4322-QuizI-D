'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile = open('employee_data.csv','r',newline = '')
reader = csv.reader(infile)
next(reader)

#create an empty dictionary
employee_dict = {}

#use a loop to iterate through the csv file
for row in reader:
    #check if the employee fits the search criteria
    if(row[3] == 'Marketing' and row[4] == 'CSR'):
        name = row[1] + ' ' + row[2]
        current_salary = format(float(row[5]),',.2f')
        new_salary = float(row[5]) * 1.1
        employee_dict[name] = format(new_salary,',.2f')

        print(f"Manager Name: {name} Current Salary: ${current_salary}")

infile.close()

    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout

for key in employee_dict:
    print(f"Manager Name: {key} New Salary: ${employee_dict[key]}")

          
        

        
    

#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# Evan Anderson, 2021-Nov-14, Created File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of dicts to hold data
dicRow = {'intID': 0,'strTitle': '','strArtist': ''}  # blank dictionary key

# Opening Text file
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Defining the ID
objFile = open(strFileName, 'r')
for row in objFile:
    NewRow = row.strip().split(',')
    dicRow = {'intID': NewRow[0],'strTitle': NewRow[1],'strArtist': NewRow[2]}
    lstTbl.append(dicRow)
ID = int(len(lstTbl))
lstTbl = []
objFile.close()

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n[l] Load Inventory from File\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to File\n[x] Exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input

# Exit
    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break

# Load Inventory from file   
    if strChoice == 'l':
        print('\nLoading Inventory from File...')
        objFile = open(strFileName, 'r')
        for row in objFile:
            NewRow = row.strip().split(',')
            dicRow = {'intID': int(NewRow[0]),'strTitle': NewRow[1],'strArtist': NewRow[2]}
            lstTbl.append(dicRow)
            #Clear the values
            dicRow = {'intID': 0,'strTitle': '','strArtist': ''}
        objFile.close()
        
        #Show the results
        print('Items in list now:')
        for row in lstTbl:
            print(row)
        print()
        
# Add CD
    elif strChoice == 'a':
        ID = ID + 1
        dicRow['intID'] = ID
        dicRow['strTitle'] = input('Enter the CD\'s Title: ')
        dicRow['strArtist'] = input('Enter the Artist\'s Name: ')
        lstTbl.append(dicRow)
        #Clear the values
        dicRow = {'intID': 0,'strTitle': '','strArtist': ''}

# Display Current Inventory        
    elif strChoice == 'i':
        print()
        lstTbl
        for row in lstTbl:
                print(row.values())
  
# Delete CD from Inventory            
    elif strChoice == 'd':
        print()
        for row in lstTbl:
            print(row.values())
        IDRemove = int(input('Select which ID # you would like to delete: ')) - 1
        for row in lstTbl:
            if row['intID'] == IDRemove:
                lstTbl.remove(row)
            print(row)

# Save Inventory to File    
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            list_of_values = list(row.values())
            list_of_values = str(list_of_values).replace(', ',',').replace('[','').replace(']','').replace('\'','') + '\n'
            objFile.write(list_of_values)
            list_of_values = ''
        objFile.close()
        print('\nSaved!')
        #Clear table not that info has been exported
        lstTbl = []    
    
    else:
        print('\nPlease choose either l, a, i, d, s or x!')


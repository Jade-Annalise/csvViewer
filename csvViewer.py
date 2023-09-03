#simple csv reader using pandas, numpy and tkinter 

#library imports 
import pandas as pd
import numpy as np
from tkinter import * 

#function to read chosen csv file, convert to numpy array, add array items to list, cont below
#create tkinter windows, and create/place/fill all labels with corresponding variables 
def csvDisplay(): 
    fileName = enterName.get()                  #gets name from entry on first screen and stores as variable 
    csvDF = pd.read_csv(fileName + ".csv")      #uses variable filename to open csv and stores as dataframe
    csvArray = csvDF.to_numpy()                 #converts dataframe to numpy array 
    
    #creates variable and list for later loops 
    x = 0
    cellsList = []
    
    #loops through the dataframe to get its size 
    for each in csvDF: 
        x += 1
    
    #loops through the arrays in the array and appends each variable to the list 
    for each in csvArray:
        for item in each: 
            cellsList.append(item)
    
    #creates and sets size of second tikinter window             
    workbook = Tk()
    workbook.geometry("800x640")
    
    #creates the frame that the sheets will be displayed in 
    sheetWindow = Frame(workbook)
    sheetWindow.pack()
    
    #creates variable for loop, used to place variables correctly 
    i = 0
    
    #loops to place and fill each label in a grid format with the corresponding variable 
    for rows in range(x):
        for cols in range(x): 
            cells = Label(sheetWindow, relief = "sunken", font = "Congenial 12", width = 8, text = cellsList[i])
            i += 1 
            cells.grid(row = rows, column = cols)
    
    #initiates the sheets tkinter window and its frames/widgets                      
    workbook.mainloop()

#creates amnd sets the size of first tkinter window 
screen = Tk()
screen.geometry("800x640")

#creates the frame that the instuctions, entry box and button will be displayed in 
chooseScreen = Frame(screen)
chooseScreen.pack()

#creates and places label to display instructions to user
instruct = Label(chooseScreen, font = "Congenial 14", text = "Welcome to the CSV Viewer!\n Please enter the name of the CSV file you would like to view below: ")
instruct.grid(row = 0, column = 1, columnspan = 4, rowspan = 2)

#creates and places the entry box to take user input
enterName = Entry(chooseScreen, font = "Congenial 11", width = 24, relief = "sunken")
enterName.grid(row = 3, column = 2, columnspan = 2, pady = 16)

#creates and places button to initiate the csvDisplay function 
enterButton = Button(chooseScreen, width = 12, font = "Congenial 10", text = "Enter", relief = "groove", command = csvDisplay)
enterButton.grid(row = 6, column = 2, columnspan = 2, pady = 12)

#initiates first tkinter window and its frames/widgets
screen.mainloop()






        

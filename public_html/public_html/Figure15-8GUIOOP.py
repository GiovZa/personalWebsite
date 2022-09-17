from tkinter import *
class WageCalculator:
    def __init__(self):
        def calcGrossPayClicked(result,hours,payrate):
           result.configure(text=str(float(hours.get())*float(payrate.get())))
        #Create the main window
        self.main_window = Tk()
        #create all widgets
        self.hoursLabel = Label(self.main_window, \
            text = "Enter the number of hours worked:")
        self.hoursEntry = Entry(self.main_window)
        self.payRateLabel = Label(self.main_window, \
            text = "\tEnter the hourly pay rate:")
        self.payRateEntry = Entry(self.main_window)
        self.resultLabel = Label(self.main_window, \
            text = "\t\tThe gross pay is:")
        self.resultAmount = Label(self.main_window, \
            text=" ") # no output to start
        self.calcButton=Button(self.main_window,text= "Calculate Gross Pay",fg="red",\
            command=lambda: calcGrossPayClicked(self.resultAmount,\
                                        self.hoursEntry,self.payRateEntry))
        self.exitButton=Button(self.main_window,text= "Exit",width=15,bg="red",\
            command=self.main_window.destroy) 
        #layout screen
        self.hoursLabel.grid(row=0,column=0,pady=5) 
        self.hoursEntry.grid(row=0,column=1,padx=5) 
        self.payRateLabel.grid(row=1,column=0)
        self.payRateEntry.grid(row=1,column=1)
        self.resultLabel.grid(row=2,column=0)
        self.resultAmount.grid(row=2,column=1)
        self.calcButton.grid(row=3,column=0,pady=10)
        self.exitButton.grid(row=3,column=1)
        mainloop()

my_gui = WageCalculator()

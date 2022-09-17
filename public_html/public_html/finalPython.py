from tkinter import *
def main():
    def readPayFile(empHoursArray):
        counter = 0
        fileName = "PayrollHours.txt"
        mainFile= open(fileName, "r")
        record = mainFile.readline()
        while record != "":
            empHoursArray[counter] = int(record)
            record = mainFile.readline()
            counter = counter +1
        return (counter)
    def computePay(empHoursArray, recCount, empPayArray):
        for i in range(0, recCount):
            if empHoursArray[i] <= 40:
                empPayArray[i] = empHoursArray[i] * 10
            if empHoursArray[i] > 40:
                overtimeHours = empHoursArray[i] - 40
                overtimePay = overtimeHours *15
                empPayArray[i] = 10 * (empHoursArray[i] - overtimeHours)
                empPayArray[i] = overtimePay + empPayArray[i]
        return (empPayArray)
    employeeHrs = [0]*10
    employeePay = [0]*10
    numberOfRecs = readPayFile(employeeHrs)
    getMoney = computePay(employeeHrs, numberOfRecs, employeePay)
    for i in range(0, 9):
        if employeePay[i] > 0:
            print("employee", i + 1)
            print(employeePay[i])
    def getPayFunction(answer, employeeID):
        output = int(employeeID.get())
        solution= employeePay[output - 1]
        answer.configure(text= str(solution))
    main_window = Tk()
    infoLabel = Label(main_window, text="Enter emplyee ID to find pay for:")
    employeeID = Entry(main_window)
    answer = Label(main_window, text="")
    getPayButton= Button(main_window, text="get pay",\
        command=lambda: getPayFunction(answer, employeeID))
    quitButton=Button(main_window,text="quit",command= main_window.destroy)
    infoLabel.grid(row=0,column=0)
    employeeID.grid(row=0,column=1)
    getPayButton.grid(row=1,column=0)
    quitButton.grid(row=1,column=1)
    answer.grid(row=0,column=3)
main()

from tkinter import *

def calcAreaButtonClicked(outputLabel,length,width):
    validInput=True
    try:
        l=int(length.get())
        #length.configure(bg="white")
        length.configure(bg="white")
    except:
        length.configure(bg="red")
        outputLabel.configure(text=" ")
        validInput=False
    try:
        w=int(width.get())
        width.configure(bg="white")
    except:
        width.configure(bg="red")
        outputLabel.configure(text=" ")
        validInput=False
    if validInput:
        outputLabel.configure(text= str(l*w),bg="white")
                
#main
main_window = Tk() #main_window is GUI window – close, closes all widgets
lengthLabel=Label(main_window, text="Enter Rec length:").grid(row=0,column=0)
widthLabel=Label(main_window, text="Enter Rec width:").grid(row=1,column=0)
length = Entry(main_window)
width = Entry(main_window)
length.grid(row=0, column=1)
width.grid(row=1, column=1)
answerLabel = Label(main_window,text="         answer is:") #what about ouput?
answerLabel.grid(row=2,column=0)
answer = Label(main_window,text=" ") #what about ouput?
answer.grid(row=2,column=1,sticky="W") #LEFT JUSTIFY
btn=Button(main_window,text= "Calculate Area",\
command=lambda: calcAreaButtonClicked(answer,length,width))
btn.grid(row=3,column=1)
quitBtn=Button(main_window,text="Quit",command=main_window.destroy) 
quitBtn.grid(row=4,column=3) #above method call no ()
## make some rows wider to give sapace - standard row about 20 pixels
main_window.grid_rowconfigure(0, minsize=30)
main_window.grid_columnconfigure(0, minsize=140)
main_window.mainloop( )

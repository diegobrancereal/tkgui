from tkinter import *
from tkinter.messagebox import *
from datetime import *
from PIL import ImageTk, Image, ImageOps
def registerACamperWindow():
    #Basics
    newWin = Toplevel()
    main2 = Frame(newWin)
    newWin.geometry("750x600")
    newWin.maxsize(width=750, height=600)
    newWin.minsize(width=750, height=600)

    #GRIDDING
    first_frame = LabelFrame(main2, text="Camper's personal information", relief="sunken")


    first_name = Label(first_frame, text="First name")
    first_name_entry_var = StringVar()
    first_name_entry = Entry(first_frame, width=30)

    last_name = Label(first_frame, text="Last name")
    last_name_entry_var = StringVar()
    last_name_entry = Entry(first_frame, width=30)

    sex_label = Label(first_frame)
    main2.grid(padx=50, pady=50)

    #First frame 
    first_frame.grid(row=1, column=1, padx=30, pady=30, ipadx=30, ipady=30)

    first_name.grid(row=1, column=1)
    first_name_entry.grid(row=1, column=2)

    last_name.grid(row=1, column=3, sticky=E)
    last_name_entry.grid(row=1, column=4, sticky=E)
    newWin.grab_set()

    newWin.mainloop()
    

    
    
    
def findACamperWindow():
    newWin = Toplevel()
    
    newWin.grab_set()



    newWin.mainloop()

def callback():
    
    if askokcancel("Quit", "Do you really wish to quit the program?"):
        root.destroy()
    

#MAIN
#All global list variables
global dateForCamper
Camper = ["Hendrick", "Louie", "Gob"]

root = Tk()
mainframe = Frame(root)
root.geometry("750x600")
root.title("Jegg's & Bill's camping registry")
root.protocol("WM_DELETE_WINDOW", callback)


#Images

#Left arrow Image
left_raw = Image.open('left-arrow.png')#Could have opened it another way but this works well too I guess
resized_left = left_raw.resize((32, 30))#Resizes theimage
left_arrow_image = ImageTk.PhotoImage(resized_left) #Display's the image

#Right arrow Image
flipped_left = ImageOps.mirror(resized_left) # Flips the image
right_arrow_image = ImageTk.PhotoImage(flipped_left)



#Buttons 
register_a_camper_button = Button(mainframe, text="Register a camper", width=20, height=3, command=registerACamperWindow)

find_a_camper_button = Button(mainframe, text="Find a camper", width=20, height=3)

see_list_of_activities_button = Button(mainframe, text="See list of activites", width=20, height=3)

see_more_button = Button(mainframe, text="see more", width=20, height=3)




# Calendar ---------------------------------------------

calendar_frame = LabelFrame(mainframe, width=40, relief="solid")


# Date button

left_arrow_button = Button(calendar_frame, text="Yesterday", image=left_arrow_image)
date_label = Label(calendar_frame, text="DATE HERE")
right_arrow_button = Button(calendar_frame, text="Next day", image=right_arrow_image)

#List of all registered campers
listOfAllPToday = StringVar()
listOfAllPToday.set(Camper)

schedule_list_box = Listbox(calendar_frame, listvariable=listOfAllPToday, selectmode=SINGLE, width=55, font="Arial 10", height=20)









#GRID the widgets
#root.maxsize(width=850, height=650)
#root.minsize(width=650, height=450)
mainframe.grid(padx=50, pady=50)

#MAIN GRID

#Buttons(IPADX AND IPADY COULD BE USED FOR SIZING)
register_a_camper_button.grid(row=1, column=1, sticky=W)

find_a_camper_button.grid(row=4, column=1, sticky=W)

see_list_of_activities_button.grid(row=5, column=1, sticky=W)

see_more_button.grid(row=6, column=2)
#Calendarframe
calendar_frame.grid(row=1, column=2, rowspan=5, padx=90, sticky=W)

#Label
left_arrow_button.grid(row=1, column=1, sticky=W, ipadx=20, ipady=10)
date_label.grid(row=1, column=2, ipadx=60, ipady=10)
right_arrow_button.grid(row=1, column=3, sticky=E, ipadx=20, ipady=10)

schedule_list_box.grid(row=2, column=1, columnspan=3)
root.mainloop()


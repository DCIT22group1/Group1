from tkinter import *


def info():
    print("Successfully Enrolled!")
    name_info = entry_name.get()
    age_info = entry_age.get()
    address_info = entry_address.get()
    birth_info = entry_birth.get()
    gender_info = entry_gender.get()
    contact_info = entry_contact.get()
    email_info = entry_email.get()
    year_info = entry_year.get()
    units_info = entry_units.get()
    course_info = entry_course.get()

    if name_info and age_info and address_info and birth_info and gender_info and contact_info and email_info and year_info and units_info and course_info != "":
        Label(text="Required Information Acquired!", fg="green", font="arial 11 bold").place(x=835, y=430)
        file = open(name_info + ".txt", "w")
        file.write("Name:            " + name_info + "\n")
        file.write("Age:             " + age_info + "\n")
        file.write("Address:         " + address_info + "\n")
        file.write("Birthday:        " + birth_info + "\n")
        file.write("Gender:          " + gender_info + "\n")
        file.write("Contact Number:  " + contact_info + "\n")
        file.write("Email Address:   " + email_info + "\n")
        file.write("Course:          " + course_info + "\n")
        file.write("Year Level:      " + year_info + "\n")
        file.write("Number of Units: " + units_info + "\n")
        file.close()

        Label(text=name_info, fg="black", font="arial 11 bold").place(x=560, y=44)
        Label(text=course_info, fg="black", font="arial 11 bold").place(x=925, y=44)
        Label(text=year_info, fg="black", font="arial 11 bold").place(x=1155, y=44)
    else:
        Label(text="All infromation must be filled up", fg="red", font="poppins 11 bold").place(x=835, y=430)


def fee():
    if entry_year.get() == 1:
        Label(text="Tuition Fee:", fg="green", font="poppins 11 bold").place(x=835, y=430)


# bg_color = "#27445C"
# frame_back = "9B870C"
# frame_forward = "#008000"

root = Tk()
root.title("Enrollment Form")
root.geometry("800x500+250+100")
bg_color = "#006400"
root.config(bg=bg_color)
c = Canvas(root, bg="gray16", height=200, width=200)
filename = PhotoImage(file="C:\\Users\\Joseph\\Documents\\Testing tktinter\\test2.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()

Label(text="Student Name", font="verdana 16").place(x=60, y=180)
Label(text="Age", font="verdana 16").place(x=60, y=230)
Label(text="Address", font="verdana 16").place(x=60, y=280)
Label(text="Date of Birth", font="verdana 16").place(x=60, y=330)
Label(text="Gender", font="verdana 16").place(x=60, y=380)
Label(text="Contact Number", font="verdana 16").place(x=60, y=430)
Label(text="Email Address", font="verdana 16").place(x=60, y=480)
Label(text="Year Level", font="verdana 16").place(x=700, y=180)
Label(text="No. of Units", font="verdana 16").place(x=700, y=230)
Label(text="Course", font="verdana 16").place(x=700, y=280)

# Personal Information Input
entry_name = StringVar()
entry_age = StringVar()
entry_address = StringVar()
entry_birth = StringVar()
entry_gender = StringVar()
entry_contact = StringVar()
entry_year = StringVar()
entry_units = StringVar()
entry_course = StringVar()
entry_email = StringVar()

entry_name = Entry(root, textvariable=entry_name, width=35, bd=5, font=26)
entry_age = Entry(root, textvariable=entry_age, width=35, bd=5, font=26)
entry_address = Entry(root, textvariable=entry_address, width=35, bd=5, font=26)
entry_birth = Entry(root, textvariable=entry_birth, width=35, bd=5, font=26)
entry_gender = Entry(root, textvariable=entry_gender, width=35, bd=5, font=26)
entry_contact = Entry(root, textvariable=entry_contact, width=35, bd=5, font=26)
entry_email = Entry(root, textvariable=entry_email, width=35, bd=5, font=26)
entry_year = Entry(root, textvariable=entry_year, width=35, bd=5, font=26)
entry_units = Entry(root, textvariable=entry_units, width=35, bd=5, font=26)
entry_course = Entry(root, textvariable=entry_course, width=35, bd=5, font=26)

entry_name.place(x=245, y=180)
entry_age.place(x=245, y=230)
entry_address.place(x=245, y=280)
entry_birth.place(x=245, y=330)
entry_gender.place(x=245, y=380)
entry_contact.place(x=245, y=430)
entry_email.place(x=245, y=480)
entry_year.place(x=835, y=180)
entry_units.place(x=835, y=230)
entry_course.place(x=835, y=280)

# Button
check_value = IntVar()
check_button = Checkbutton(text="Remember me", font="verdana 11", variable=check_value)
check_button.place(x=835, y=330)

Button(text="Enroll", font="verdana 12 bold", width=20, height=2, command=info).place(x=835, y=380)

root.mainloop()

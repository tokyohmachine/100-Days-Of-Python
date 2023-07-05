from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=100, pady=100)


def converted():
    miles = float(miles_entry.get())
    km = miles * 1.689
    km_label.config(text=f"{km}")


# entry miles
miles_entry = Entry(width=15)
print(miles_entry.get())
miles_entry.grid(column=1, row=0)

# label is equal to km
label = Label(text="Miles")
label.grid(column=2, row=0)  # in the center


equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
equal_label.grid(column=0, row=1)


km_label = Label(text="0")
km_label.grid(column=1, row=1)


kmi_label = Label(text="km", font=("Arial", 12, "bold"))
kmi_label.grid(column=2, row=1)


# button
button = Button(text="Calculate", command=converted)
button.grid(column=1, row=2)

window.mainloop()
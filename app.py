import tkinter as tk

def show_output():
    number = int(number_input.get())

    if number ==0:
        output_label.configure(text='1-12เท่านั้น')
        return

    output =''
    for i in range (1,13):
        output += str(number) + 'x' + str(i)
        output += '=' + str(number * i) + '\n'

    output_label.configure(text=output)

window=tk.Tk()
window.title('สูครคูรแม่1-12')
window.minsize(width=400, height=400)

titel_label = tk.Label(master=window,text='สูตรคูณ')
titel_label.pack()

number_input = tk.Entry(master=window)
number_input.pack()

go_button = tk.Button(
    master=window, text='ได้แก่',
    command=show_output
)
go_button.pack()

output_label = tk.Label(master=window)
output_label.pack()

window.mainloop()

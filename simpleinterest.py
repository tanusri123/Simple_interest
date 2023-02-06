from tkinter import * 

window = Tk()

window.title('Simple Interest')
window.geometry("380x400")
window.configure(bg = 'cyan')

def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = p*r*t/100
    interest = round(i,2)

    Showlabel.destroy()

message_label = Label[result_frame, text = "Interest on Rs,"+str(p]+"at rate of interest"+str[r)+"for "+str[t)+"years is Rs"+str(Interest),bg = "grey",width = 55,font = ("Calibri",12)""]
message_label.place[x=20,y = 40]
message_label.pack()

result_frame = LabelFrame(window,text = "Result",bg = "grey",font = ("Calibri",12))
result_frame.pack(padx = 20,pady = 20)
result_frame.place(x=20, = 300)

Showlabel = Label(result_frame,text ="Your result will be displayed here",bg = "grey",font = ("Calibri",12),width = 55 )
Showlabel.place(x = 20,y = 20)
Showlabel.pack()

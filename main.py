from  tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_best_server()
    down = str(round(sp.download()/(10**6),3))+"Mbps"
    up = str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x600")
sp.config(background="#008cff")

# # =============================================================
name_label = Label(sp, text="Made By: Waleed Ahmed Khan", font=("Times New Roman", 16, "bold"), bg="#008cff", fg="White")
name_label.place(x=50, y=10,height=50,width=380 )  # Made by
# # =============================================================

lab = Label(sp,text="Internet Speed Test", font=("Aerial",26,"bold"),bg="#008cff", fg="White")
lab.place(x=50,y=50,height=50,width=380)

lab = Label(sp,text="Download Speed", font=("Aerial",26),bg="#008cff", fg="White")
lab.place(x=50,y=130,height=50,width=380)

lab_down = Label(sp,text="00", font=("Aerial",26,"bold"),fg="Black")
lab_down.place(x=50,y=200,height=50,width=380)

lab = Label(sp,text="Upload Speed", font=("Aerial",26),bg="#008cff", fg="White")
lab.place(x=50,y=290,height=50,width=380)

lab_up = Label(sp,text="00", font=("Aerial",26,"bold"),fg="Black")
lab_up.place(x=50,y=360,height=50,width=380)

button = Button(sp,text="Check Speed", font=("Aerial",18,"bold"),bg="#008cff",fg="White",relief=RAISED, command=speedcheck)
button.place(x=50,y=460,height=50,width=380)

sp.mainloop()
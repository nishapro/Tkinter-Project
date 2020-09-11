from tkinter import *
import wikipedia
root=Tk()
def get_me():
    entry_value=entry.get()
    answer.delete(1.0,END)
    try:
        answer_value=wikipedia.summary(entry_value)
        answer.insert(INSERT,answer_value)
    except:
        answer.insert(INSERT,"please check your input or your internet connection")
        
topframe=Frame(root)
entry=Entry(topframe)
button=Button(topframe,text="search",command=get_me)
entry.pack()
button.pack()
topframe.pack(side=TOP)
bottomframe=Frame(root)
scroll=Scrollbar(bottomframe)
scroll.pack(side=RIGHT,fill=Y)
answer=Text(bottomframe,width=30,height=10,yscrollcommand=scroll.set,wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()
bottomframe.pack()
root.mainloop()



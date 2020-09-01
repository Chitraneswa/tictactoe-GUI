from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("Tic Tac Toe")
root.configure(background='#E9967A')
Tops=Frame(root,bg='blue',pady=2,width=550,height=100,relief=RIDGE)
Tops.grid(row=0,column=0)
lblTitle=Label(Tops,font=('arial',50,'bold'),text='Tic Tac Toe game',bd=21,bg='#E9967A',fg='Cornsilk',justify=CENTER)
lblTitle.grid(row=0,column=0)
MainFrame=Frame(root,bg='#808000',bd=10,width=550,height=600)
MainFrame.grid(row=1,column=0)
LeftFrame=Frame(MainFrame,bg='#FFFF00',bd=10,pady=2,padx=10,width=450,height=500,relief=RIDGE)
LeftFrame.pack(side=LEFT)
RightFrame=Frame(MainFrame,bg='#FFFF00',bd=10,pady=2,padx=10,width=100,height=500,relief=RIDGE)
RightFrame.pack(side=RIGHT)
RightFrame1=Frame(RightFrame,bg='#BC8F8F',bd=10,pady=2,padx=10,width=100,height=200,relief=RIDGE)#ridge for the outline
RightFrame1.grid(row=0,column=0)
RightFrame2=Frame(RightFrame,bg='#BC8F8F',bd=10,pady=2,padx=10,width=100,height=200,relief=RIDGE)
RightFrame2.grid(row=1,column=0)

PlayerX=IntVar()
PlayerO=IntVar()
PlayerX.set(0)
PlayerO.set(0)
buttons=StringVar()
click=True

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scorekeeper()

def scorekeeper():
    if(button1['text']=="X" and button2["text"]=="X" and button3["text"]=="X"):
        button1.configure(background ="powder blue")
        button2.configure(background ="powder blue")
        button3.configure(background ="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "U won a game")
    if (button4['text'] == "X" and button5["text"] == "X" and button6["text"] == "X"):
        button4.configure(background="powder blue")
        button5.configure(background="powder blue")
        button6.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "U won a game")
    if (button3['text'] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        button3.configure(background="powder blue")
        button5.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "U won a game")
    if (button7['text'] == "X" and button8["text"] == "X" and button9["text"] == "X"):
        button7.configure(background="powder blue")
        button8.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "U won a game")
    if (button1['text'] == "X" and button5["text"] == "X" and button9["text"] == "X"):
        button1.configure(background="powder blue")
        button5.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "U won a game")
    if (button1['text'] == "X" and button4["text"] == "X" and button7["text"] == "X"):
        button1.configure(background="powder blue")
        button4.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "U won a game")
    if (button2['text'] == "X" and button5["text"] == "X" and button8["text"] == "X"):
        button2.configure(background="powder blue")
        button5.configure(background="powder blue")
        button8.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "U won a game")
    if (button3['text'] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        button3.configure(background="powder blue")
        button6.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "U won a game")
    if (button1['text'] == "O" and button2["text"] == "O" and button3["text"] == "O"):
        button1.configure(background="powder blue")
        button2.configure(background="powder blue")
        button3.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "U won a game")
    if (button4['text'] == "O" and button5["text"] == "O" and button6["text"] == "O"):
        button4.configure(background="powder blue")
        button5.configure(background="powder blue")
        button6.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "U won a game")
    if (button3['text'] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        button3.configure(background="powder blue")
        button5.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "U won a game")
    if (button7['text'] == "O" and button8["text"] == "O" and button9["text"] == "O"):
        button7.configure(background="powder blue")
        button8.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "U won a game")
    if (button1['text'] == "O" and button5["text"] == "O" and button9["text"] == "O"):
        button1.configure(background="powder blue")
        button5.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "U won a game")
    if (button1['text'] == "O" and button4["text"] == "O" and button7["text"] == "O"):
        button1.configure(background="powder blue")
        button4.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "U won a game")
    if (button2['text'] == "O" and button5["text"] == "O" and button8["text"] == "O"):
        button2.configure(background="powder blue")
        button5.configure(background="powder blue")
        button8.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "U won a game")
    if (button3['text'] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        button3.configure(background="powder blue")
        button6.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "U won a game")
    if button1['text'] == "X" or button1['text'] == "O" :
        if button2['text'] == "X" or button2['text'] == "O":
            if button3['text'] == "X" or button3['text'] == "O":
                if button4['text'] == "X" or button4['text'] == "O":
                    if button5['text'] == "X" or button5['text'] == "O":
                        if button6['text'] == "X" or button6['text'] == "O":
                            if button7['text'] == "X" or button7['text'] == "O":
                                if button8['text'] == "X" or button8['text'] == "O":
                                    if button9['text'] == "X" or button9['text'] == "O":
                                        tkinter.messagebox.showinfo("Game Over", "Reset to play again")




def reset():
    button1['text'] = " "
    button2['text'] = " "
    button3['text'] = " "
    button4['text'] = " "
    button5['text'] = " "
    button6['text'] = " "
    button7['text'] = " "
    button8['text'] = " "
    button9['text'] = " "

    button1.configure(background ="#FFA07A")
    button2.configure(background ="#FFA07A")
    button3.configure(background ="#FFA07A")
    button4.configure(background ="#FFA07A")
    button5.configure(background ="#FFA07A")
    button6.configure(background ="#FFA07A")
    button7.configure(background ="#FFA07A")
    button8.configure(background ="#FFA07A")
    button9.configure(background ="#FFA07A")
def NewGame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)

lblPlayerX=Label(RightFrame1,font=('arial',40,'bold'),text="Player X:",bg='#ADFF2F',pady=2,padx=2)
lblPlayerX.grid(row=0,column=0)
textPlayerX=Entry(RightFrame1,font=('arial',40,'bold'),bd=2,fg="black",textvariable=PlayerX,width=14,justify=LEFT).grid(row=0,column=1)

lblPlayerO=Label(RightFrame1,font=('arial',40,'bold'),text="Player O:",padx=2,pady=2,bg="#ADFF2F")
lblPlayerO.grid(row=1,column=0)
textPlayerO=Entry(RightFrame1,font=('arial',40,'bold'),bd=2,fg="black",textvariable=PlayerO,width=14,justify=LEFT).grid(row=1,column=1)

btnReset=Button(RightFrame2,text="Reset",font=('Times 26 bold'),height=3,width=20, command=reset)
btnReset.grid(row=0,column=0)
btnNewgame=Button(RightFrame2,text="New Game",font=('Times 26 bold'),height=3,width=20, command=NewGame)
btnNewgame.grid(row=1,column=0)


button1=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='#FFA07A',command=lambda:checker(button1))
button1.grid(row=1,column=0)
button2=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='#FFA07A',command=lambda:checker(button2))
button2.grid(row=1,column=1)
button3=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='#FFA07A',command=lambda:checker(button3))
button3.grid(row=1,column=2)
button4=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='#FFA07A',command=lambda:checker(button4))
button4.grid(row=2,column=0)
button5=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='#FFA07A',command=lambda:checker(button5))
button5.grid(row=2,column=1)
button6=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='#FFA07A',command=lambda:checker(button6))
button6.grid(row=2,column=2)
button7=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='#FFA07A',command=lambda:checker(button7))
button7.grid(row=3,column=0)
button8=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='#FFA07A',command=lambda:checker(button8))
button8.grid(row=3,column=1)
button9=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='#FFA07A',command=lambda:checker(button9))
button9.grid(row=3,column=2)



root.mainloop()
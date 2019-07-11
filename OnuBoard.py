from tkinter import*

def playagainscrpt():
    playagain = ('y')
    
window = Tk ()
window .title ('Onu')

player1cards = {
    'Player Name' : 'Player 1'
}

Label (window, text=player1cards, width=30, height=10) .grid(row=1, column=0)

carPick = Text(window, height=1, width=4 )
Button (window, text='Take a card', width=10, command=playagainscrpt) .grid(row=2, column=0)

window.mainloop()


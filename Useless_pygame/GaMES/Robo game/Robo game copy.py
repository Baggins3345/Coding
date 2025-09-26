from tkinter import *

root = Tk()
root.title("Robocalyps: The Game")
root.minsize(1500, 1000)
root.config(bg="black")

# Declare global variables
start = None
play = None
B1 = None
Or = None
B2 = None
GG = None
run = None

def Menu_Screen():
    global start, play, B1, Or, B2 # Declare them as global

    start = Label(text="Robocalyps: The Game!", bg="black", fg="white", font="Arial 50")
    start.place(x=400, y=100)

    play = Label(text="Would you like to play?", bg="black", fg="white", font="Arial 15")
    play.place(x=500, y=300)

    B1 = Button(text="Yes", bg="black", fg="white", font="Arial 15", command=Play_Screen)
    B1.place(x=730, y=300)

    Or = Label(text="or", bg="black", fg="white", font="Arial 15")
    Or.place(x=795, y=300)

    B2 = Button(text="No", bg="black", fg="white", font="Arial 15", command=Exit_Button)
    B2.place(x=830, y=300)

def Game_Over():
    global GG, B1, B2
    GG = Label(text="You're brain has been graciously accepted by the OSBDMF. Would you like to try again?", bg="red", fg="white", font="Arial 20")
    GG.pack()

    B1 = Button(text="Yes", bg="red", fg="white", font="Arial 30", command=Play_Screen2)
    B1.pack()
    B2 = Button(text="No", bg="red", fg="white", font="Arial 30", command=Exit_Button)
    B2.pack()

def Exit_Button():
    exit()


def Play_Screen():
    # Access the global variables
    global start, play, B1, Or, B2

    # Close the Menu_Screen
    start.destroy()
    play.destroy()
    B1.destroy()
    Or.destroy()
    B2.destroy()

    # Create the Play_Screen
    Welcome = Label(text="Welcome to Robocalyps: The Game!\n\n\n In this short game you are a lone scavenger of a post-apocalyptic wasteland overtaken by Robots,\n otherwise known as the 'Oil sucking brain dead MotherF****', or OSBDMF for short.\n\n You are on a mission to find supplies for your group. You stumble upon a town succumbed to nature.\n You're in luck however, there is a pharmacy!", bg="black", fg="white", font="Arial 10")
    Welcome.place(x=10, y=10)

    Q1 = Label(text="Do you... ",bg="black", fg="white", font="Arial 10")
    Q1.place(x=20,y=150)
    A1 = Button(text="Go in",bg="black", fg="white", font="Arial 10", command=Con)
    A1.place(x=20,y=170)
    A1 = Button(text="Run away",bg="black", fg="white", font="Arial 10", command=Run)
    A1.place(x=70,y=170)

def Play_Screen2():
    # Access the global variables
    global GG, B1, B2, run

    # Close the Menu_Screen
    GG.destroy()
    B1.destroy()
    B2.destroy()
    run.destroy()

    # Create the Play_Screen
    Welcome = Label(text="Welcome to Robocalyps: The Game!\n\n\n In this short game you are a lone scavenger of a post-apocalyptic wasteland overtaken by Robots,\n otherwise known as the 'Oil sucking brain dead MotherF****', or OSBDMF for short.\n\n You are on a mission to find supplies for your group. You stumble upon a town succumbed to nature.\n You're in luck however, there is a pharmacy!", bg="black", fg="white", font="Arial 10")
    Welcome.place(x=10, y=10)

    Q1 = Label(text="Do you... ",bg="black", fg="white", font="Arial 10")
    Q1.place(x=20,y=150)
    A1 = Button(text="Go in",bg="black", fg="white", font="Arial 10", command=Con)
    A1.place(x=20,y=170)
    A1 = Button(text="Run away",bg="black", fg="white", font="Arial 10", command=Run)
    A1.place(x=70,y=170)
    
def Run():
    global run
    run = Label(text="You feel a sense of urgent discomfort and decide it better to run away. Amidst your scrambl, you see a patrolling Robot a little too late and he sees you!",bg="red", fg="black", font="Arial 15")
    run.place(x=100,y=200)
    Game_Over()

def Con():
    In_Pharmacy = Label(text="You go in. The door creeks lowly as you venture further and it closes behind you.\nYou find yourself in a nature stricken pharmacy painted by dust covered sun-rays.\nOn your right there is a 'U' shaped desk that takes up most the room. As you look to the other side of the room,\nvending machines come upon your vision and you end seeing the counter blocking off the medicine cabinets.\n\nWhere do you go?",bg="black", fg="white", font="Arial 10")
    In_Pharmacy.place(x=20,y=230)
    A1 = Button(text="Desk",bg="black", fg="white", font="Arial 10", command=Desk)
    A1.place(x=20,y=330)
    A2 = Button(text="Vending Machines",bg="black", fg="white", font="Arial 10", command=Vending)
    A2.place(x=100,y=330)
    A3 = Button(text="Cabinets",bg="black", fg="white", font="Arial 10", command=Cabinets)
    A3.place(x=300,y=330)

def Desk():
    desk = Label(text="You make your way across the room to the 'U' shaped desk. As you search you come across some items:\nOld Money, Sissors, and a Key",bg="black", fg="white", font="Arial 10")
    desk.place(x=20,y=380)
    A2 = Button(text="Vending Machines",bg="black", fg="white", font="Arial 10", command=Vending)
    A2.place(x=100,y=420)
    A3 = Button(text="Cabinets",bg="black", fg="white", font="Arial 10", command=Cabinets)
    A3.place(x=300,y=420)

def Vending():
    vending = Label(text="You make your way across the room to the Vending machine. As you search through the broken glass you come across some items:\nA 'Chonky Chocolate Bar', and a 'Cokie Cola'",bg="black", fg="white", font="Arial 10")
    vending.place(x=20,y=480)
    A3 = Button(text="Cabinets",bg="black", fg="white", font="Arial 10",command=Cabinets)
    A3.place(x=300,y=520)



def Cabinets():
    Cab = Label(text="You make your way across the room to the Cabinets. As you get closer you hear a noise. A rustling of rusty metal on metal.\nYou smell the distinct sent of oil and smoke",bg="black", fg="white", font="Arial 10")
    Cab.place(x=20,y=560)
    Q1 = Label(text="Do you... ",bg="black", fg="white", font="Arial 10")
    Q1.place(x=20,y=580)
    A1 = Button(text="Open the door leading to this smell? and sound",bg="black", fg="white", font="Arial 10", command=Behind_Counter)
    A1.place(x=20,y=610)
    A1 = Button(text="Run away",bg="black", fg="white", font="Arial 10", command=Run)
    A1.place(x=20,y=640)

def Behind_Counter():
    Cab = Label(text="You open the door that leads to the Cabinets. the smell intensifies, you think to yourself\nthat this might be your last moments. Who knows what is behind this door?\nAs the door swings open, there upon the ground lies still a robot.\nOil leaking out of its frame, and electricity moving slowly around it, you step forward slowly",bg="black", fg="white", font="Arial 10")
    Cab.place(x=800,y=10)
    A1 = Button(text="Move towards the wretched machine",bg="black", fg="white", font="Arial 10", command=Talk_kill)
    A1.place(x=800,y=100)
    A1 = Button(text="Make your way to the cabinets",bg="black", fg="white", font="Arial 10", command=Win)
    A1.place(x=1100,y=100)

def Win():
    win = Label(text="You did it, you made it past the dreadful OSBDMF\nand got the supplies you needed!\nHowever this is just the beginning of your survival. Good Job!", bg="white", fg="black", font="Arial 30")
    win.place(x=100, y=300)
    
def Talk_kill():
    closer =Label(text="You make your way to the machine, not caring for the consequences", bg="black", fg="white", font="Arial 10")
    closer.place(x=800, y=140)
    A1 = Button(text="Talk to it",bg="black", fg="white", font="Arial 10", command=Talk)
    A1.place(x=800,y=170)
    A1 = Button(text="Move to kill it",bg="black", fg="white", font="Arial 10", command=Win)
    A1.place(x=900,y=170)

def Talk():
    talk =Label(text="What do you say to this ugly beast of a machine loser, probably that it sucks and that it should die right?", bg="black", fg="white", font="Arial 10")
    talk.place(x=800, y=210)
    A1 = Button(text="You are ugly, and should die! And Kick it",bg="black", fg="white", font="Arial 10", command=Win)
    A1.place(x=800,y=240)
    A1 = Button(text="Are you alright?",bg="black", fg="white", font="Arial 10", command=Alright)
    A1.place(x=1050,y=240)


def Alright():
    Tak = Label(text="Y-you're talking to it, c'mon, lets just move on... oh it's talking back.\nThrough oil drentched coughs it says slowly 'You *DING* who are you? *BEEP*",bg="black", fg="white", font="Arial 10")
    Tak.place(x=800, y=270)
    Tak1 = Label(text="I guess, what do you say?",bg="black", fg="white", font="Arial 10")
    Tak1.place(x=800, y=310)
    A1 = Button(text="Kick it",bg="black", fg="white", font="Arial 10", command=Win)
    A1.place(x=800,y=350)
    A1 = Button(text="You're Mom",bg="black", fg="white", font="Arial 10", command=Win)
    A1.place(x=860,y=350)
    A1 = Button(text="I'm just a scanvenger looking for supplies\nto bring back to my camp",bg="black", fg="white", font="Arial 10", command=Continue_talking)
    A1.place(x=950,y=350)

def Continue_talking():
    love = Label(text="The lifeless machine seems to look you over once and says,\n'there is a key behind the counter on the other side of the room,\nuse it to open the door behind me, you'll understand after.'\nAfter the robot finishes his machine frame looses all movment and he seems to power down. What do you do?",bg="black", fg="white", font="Arial 10")
    love.place(x=800, y=420)
    A1 = Button(text="Get the key",bg="black", fg="white", font="Arial 10", command=Key_Good_Ending)
    A1.place(x=800,y=500)
    A1 = Button(text="Move to kill it",bg="black", fg="white", font="Arial 10", command=Win)
    A1.place(x=900,y=500)

def Key_Good_Ending():
    Good_Ending = Label(text="You make your way across the room to the 'U' shaped desk. As you search you come across some items:\nOld Money, Sissors, and a Key",bg="black", fg="white", font="Arial 10")
    Good_Ending.place(x=800,y=550)
    A1 = Button(text="Open the door",bg="black", fg="white", font="Arial 10", command=Key_Good_Ending1)
    A1.place(x=800,y=600)
    A2 = Button(text="leave with the supplies you came for",bg="black", fg="white", font="Arial 10", command=Win)
    A2.place(x=900,y=600)

def Key_Good_Ending1():
    Good_Ending = Label(text="You open the door to a small closet.\nIn the middle of the closet is a bassinet with a corpse\n on either side and a sleeping baby in the bassinet\nThere is a note that tells you about how this saved this baby from other robots.\nYou take the baby and the supplies with you. Good job soldier!\nYou are the hero in this story ", bg="white", fg="black", font="Arial 30")
    Good_Ending.place(x=50, y=300)


Menu_Screen()
X = Button(text="Exit", bg="white", fg="black", font="Arial 15", command=Exit_Button)
X.place(x=1300, y=700)

root.mainloop()
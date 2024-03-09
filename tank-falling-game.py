#   CONTROL: W - A - S - D
#   SHOOT: spacebar

import random
from tkinter import *
from threading import *

master = Tk()
master.title("Tank Falling Game")
master.iconbitmap("favicon.ico")

sirka = 500
vyska = 640
background_color = "lightsteelblue"

stav_hry = True
Tx = 75
Ty = 590
go = 10 #posun

# --- funkcie ---

#KRESLENIE
def nakresli_tank():
    global Ttelo, Tveza, Tpas1, Tpas2, baseline, strela1, p1, p2, p3, p4, p5, p6, xP, yP, stav_hry, game_over_title, bonuspoint
    
    Tfarba = "darkgreen"
    TfarbaB = "green"

    Pfarba = "grey"
    PfarbaB = "brown"

    xP = 550
    yP = 20

    baseline = plocha.create_rectangle(10, 510, 490, 525, fill="darkred", outline="#E12723")
    strela1 = plocha.create_rectangle(xP,yP-10,xP+10,yP, fill="black", outline="black", tags="strela")

    Ttelo = plocha.create_rectangle(Tx-25,Ty-25, Tx+25, Ty+25, fill=Tfarba, outline=TfarbaB, tags="tank")
    Tveza = plocha.create_rectangle(Tx-2.5,Ty-50, Tx+2.5, Ty, fill=Tfarba, outline=TfarbaB, tags="tank")
    Tpas1 = plocha.create_rectangle(Tx-30,Ty-30, Tx-25, Ty+30, fill=Tfarba, outline=TfarbaB, tags="tank")     #lavy
    Tpas2 = plocha.create_rectangle(Tx+25,Ty-30, Tx+30, Ty+30, fill=Tfarba, outline=TfarbaB, tags="tank")     #pravy

    #vytvor prekazky prvykrat
    p1 = plocha.create_rectangle(xP,yP,xP+10,yP+10, fill=Pfarba, outline=PfarbaB, width=5)
    p2 = plocha.create_rectangle(xP,yP+10,xP+10,yP+20, fill=Pfarba, outline=PfarbaB, width=5)
    p3 = plocha.create_rectangle(xP,yP+20,xP+10,yP+30, fill=Pfarba, outline=PfarbaB, width=5)
    p4 = plocha.create_rectangle(xP,yP+30,xP+10,yP+40, fill=Pfarba, outline=PfarbaB, width=5)
    p5 = plocha.create_rectangle(xP,yP+40,xP+10,yP+50, fill=Pfarba, outline=PfarbaB, width=5)
    p6 = plocha.create_rectangle(xP,yP+50,xP+10,yP+60, fill=Pfarba, outline=PfarbaB, width=5)

    game_over_title = plocha.create_text(xP, yP, text="", font="impact 60", fill="black")
    bonuspoint = plocha.create_oval(xP,yP+60,xP+20,yP+80, fill="gold", outline="darkorange", width=5)


#POHYB TANKU
def goVpravoT(event):
    global Tx, Ty
    if Tx < sirka and Tx > 0:
        Tx += go
    elif Tx >= sirka:
        Tx = 1
    plocha.coords(Ttelo, Tx-25,Ty-25, Tx+25, Ty+25)
    plocha.coords(Tveza, Tx-2.5,Ty-50, Tx+2.5, Ty)
    plocha.coords(Tpas1, Tx-30,Ty-30, Tx-25, Ty+30)
    plocha.coords(Tpas2, Tx+25,Ty-30, Tx+30, Ty+30)
    plocha.update()

def goVlavoT(event):
    global Tx, Ty
    if Tx < sirka and Tx > 0:
        Tx -= go
    elif Tx <= 0:
        Tx = sirka-1
    plocha.coords(Ttelo, Tx-25,Ty-25, Tx+25, Ty+25)
    plocha.coords(Tveza, Tx-2.5,Ty-50, Tx+2.5, Ty)
    plocha.coords(Tpas1, Tx-30,Ty-30, Tx-25, Ty+30)
    plocha.coords(Tpas2, Tx+25,Ty-30, Tx+30, Ty+30)
    plocha.update()

def check_prekazky():
    global Tx, Ty
    #podmienky pre okraje
    if Tx+50 > sirka:
            Tx = Tx-go
    if Tx-50 < 0:
            Tx = Tx+go

def game_over():
    global stav_hry, game_over_title
    stav_hry = False
    plocha.itemconfig(game_over_title, text="GAME OVER!")
    plocha.coords(game_over_title, 250, 260)
    play_again.configure(state="normal")

    plocha.bind_all("<Return>", hratznova)

def hratznova(*args):
    global activeP, prekazkaMove, skore, stav_hry, Tx, Ty, casB, casBlimit
    stav_hry = True
    activeP = [0,0,0,0,0,0]
    prekazkaMove = 0.1
    skore = 0

    casB = (random.randint(1000,3000))    #1000 = 3 sekundy cca
    casBlimit = 0

    play_again.configure(state="disabled")
    
    if game_over_title in plocha.find_overlapping(0,0,500,vyska):
        plocha.itemconfig(game_over_title, text="")
        plocha.coords(game_over_title, xP, yP)

    Tx = 75
    Ty = 590
    
    #resetni strelu
    plocha.coords(strela1, xP,yP-10,xP+10,yP)

    #resetni tank
    plocha.coords(Ttelo, Tx-25,Ty-25, Tx+25, Ty+25)
    plocha.coords(Tveza, Tx-2.5,Ty-50, Tx+2.5, Ty)
    plocha.coords(Tpas1, Tx-30,Ty-30, Tx-25, Ty+30)
    plocha.coords(Tpas2, Tx+25,Ty-30, Tx+30, Ty+30)

    #resetni prekazky
    plocha.coords(p1, xP,yP,xP+10,yP+10)
    plocha.coords(p2, xP,yP+10,xP+10,yP+20)
    plocha.coords(p3, xP,yP+20,xP+10,yP+30)
    plocha.coords(p4, xP,yP+30,xP+10,yP+40)
    plocha.coords(p5, xP,yP+40,xP+10,yP+50)
    plocha.coords(p6, xP,yP+50,xP+10,yP+60)
    
    plocha.itemconfig(p1, tags="")
    plocha.itemconfig(p2, tags="")
    plocha.itemconfig(p3, tags="")
    plocha.itemconfig(p4, tags="")
    plocha.itemconfig(p5, tags="")
    plocha.itemconfig(p6, tags="")

    plocha.update()

    strely_prekazky()


activeP = [0,0,0,0,0,0]
prekazkaMove = 0.1      #na zaciatku
skore = 0

casB = (random.randint(1000,3000))    #1000 = 3 sekundy cca
casBlimit = 0

def strely_prekazky():
    def nakresli_strelu(event):
        global strela1
        if stav_hry == True:
            plocha.coords(strela1, Tx-2.5,Ty-63, Tx+2.5, Ty-51)
            plocha.update()

    def nakresli_prekazku():
        global casP, p1, p2, p3, p4, p5, p6, casB
        Pfarba = "grey"
        PfarbaB = "brown"

        casVar = 0.8
        casP = casVar*1000

        grid = [70,130,190,250,310,370,430]
        if activeP[0] == 0:
            P1x = random.choice(grid)
            plocha.coords(p1,P1x,-50,P1x+50,0)
            plocha.itemconfig(p1, tags="prekazka")
            activeP[0] = 1
        elif activeP[1] == 0:
            P2x = random.choice(grid)
            plocha.coords(p2,P2x,-50,P2x+50,0)
            plocha.itemconfig(p2, tags="prekazka")
            activeP[1] = 1
        elif activeP[2] == 0:
            P3x = random.choice(grid)
            plocha.coords(p3,P3x,-50,P3x+50,0)
            plocha.itemconfig(p3, tags="prekazka")
            activeP[2] = 1
        elif activeP[3] == 0:
            P4x = random.choice(grid)
            plocha.coords(p4,P4x,-50,P4x+50,0)
            plocha.itemconfig(p4, tags="prekazka")
            activeP[3] = 1
        elif activeP[4] == 0:
            P5x = random.choice(grid)
            plocha.coords(p5,P5x,-50,P5x+50,0)
            plocha.itemconfig(p5, tags="prekazka")
            activeP[4] = 1
        elif activeP[5] == 0:
            P6x = random.choice(grid)
            plocha.coords(p6,P6x,-50,P6x+50,0)
            plocha.itemconfig(p6, tags="prekazka")
            activeP[5] = 1

    #POHYB PREKAZKY (padanie)
    def pohybovanie():
        global casP, prekazkaMove, skore, stav_hry, casB, casBlimit
        if stav_hry == True:
            #---PREKAZKA---
            if casP == 0:
                prekazkaMove = prekazkaMove+0.005    #zvysovanie narocnosti
                nakresli_prekazku()

            #---BONUSPOINT---
            TteloCoords = plocha.coords(Ttelo)
            if casB == 0 and bonuspoint not in plocha.find_overlapping(0,0,500,vyska):
                xB = random.randint(10,490)
                while xB in range(int(TteloCoords[0])-30,int(TteloCoords[2])+30):
                    xB = random.randint(10,490)
                plocha.coords(bonuspoint, xB, 580, xB+20, 600)
                casBlimit = 1000

            elif bonuspoint in plocha.find_overlapping(0,0,500,vyska):
                Tteloverlaps = plocha.find_overlapping(TteloCoords[0],TteloCoords[1],TteloCoords[2],TteloCoords[3])
                if int(14) in Tteloverlaps:
                    plocha.coords(bonuspoint, xP,yP+60,xP+20,yP+80)
                    casB = (random.randint(3000,5000))    #1000 = 3 sekundy cca
                    skore = skore+150
                    scoreLabel.config(fg="orange")
                elif casBlimit == 0:
                    plocha.coords(bonuspoint, xP,yP+60,xP+20,yP+80)
                    casB = (random.randint(3000,5000))    #1000 = 3 sekundy cca

            #---STRELA POHYB---
            if strela1 in plocha.find_overlapping(0,0,500,vyska):                               #ak sa strela nachadza v canvas
                plocha.move(strela1, 0, -1)
                plocha.update()                                                                 #musi byt aj na tomto mieste
                
                strelaCoords = plocha.coords(strela1)

                #---KONTAKT STRELY S VRCHOM---
                if (strelaCoords[1]) <= 0:
                    plocha.coords(strela1, xP,yP-10,xP+10,yP)                                   #nech sa vrati do bocnej tabulky
                    plocha.update()

                #---KONTAKT STRELY S PREKAZKOU---
                strelaOverlaps = plocha.find_overlapping(strelaCoords[0],strelaCoords[1],strelaCoords[2],strelaCoords[3])
                for i in strelaOverlaps:
                    if i not in [1,2,3,4,5,6]:
                        plocha.coords(i, xP,yP+(10*(int(i)-6)),xP+10,yP+(10*(int(i)-5)))        #nech sa vrati do bocnej tabulky
                        #plocha.coords(strela1, xP,yP-10,xP+10,yP)                               #nech zmyzne strela
                        plocha.itemconfig(i, tags="")                                           #nech s nou teraz nehybe
                        activeP[i-7] = 0                                                        #nech je znovu k dispozicii
                        scoreLabel.config(fg="darkred")
                        skore = skore+50
                        plocha.update()

            #---KONTAKT PREKAZKY S BASELINE---
            baselineOverlaps = plocha.find_overlapping(10, 515, 490, 525)
            for i in baselineOverlaps:
                if i not in [1,2]:
                    game_over()



            scoreLabel.configure(text="0"*(5-(len(str(skore))))+str(skore))
            casP = casP-1

            if casB > 0:
                casB = casB-1
            if casBlimit != 0:
                casBlimit = casBlimit-1
            plocha.move("prekazka",0,prekazkaMove)
            plocha.update()
            plocha.after(1,pohybovanie)
            
            
    plocha.bind_all("<space>", nakresli_strelu)
    nakresli_prekazku()
    pohybovanie()

# --- hlavny kod ---

scoreLabel = Label(master, text="00000", font="impact 40", fg="darkred", bg=None)
exit_button = Button(master, text="EXIT", font="impact 14", fg="black", cursor="tcross", command=master.quit)
play_again = Button(master, text="PLAY AGAIN", font="impact 14", fg="black", cursor="tcross", command=hratznova, state="disabled")
plocha = Canvas(master, width=sirka, height=vyska, bg=background_color)

scoreLabel.grid(row=1,column=0, columnspan=2)
exit_button.grid(row=0,column=1, sticky="we")
play_again.grid(row=0,column=0, sticky="we")
plocha.grid(row=2,column=0, columnspan=2)

strely_prekazkyThread = Thread(target=strely_prekazky)
strely_prekazkyThread.start()

nakresli_tank()

plocha.bind_all("<d>", goVpravoT)
plocha.bind_all("<D>", goVpravoT)
plocha.bind_all("<a>", goVlavoT)
plocha.bind_all("<A>", goVlavoT)


master.mainloop()
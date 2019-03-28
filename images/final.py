#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Auteur : Elio Saboureau / Clément Denève / Margot Prel
Sujet : Ce programme permet ade faire du traitement sur une image
"""

### Imports ###
from tkinter import *
import PIL.Image
import PIL.ImageTk 
from tkinter.filedialog import *
from tkinter.font import *
import matplotlib.pyplot as plt

image = PIL.Image.open("NB.png")
chemin = ""

nbP = False
sepiaP = False
grisP = False
negatP = False
colP = False

degradeImg = PIL.Image.open("couleurs.png")

color = "#000000"

rayon = 10
seuilL = 20
seuilC = 20
seuilS = 20

### Fonctions globales ###

# Mise à jour de l'image via pinceau
def updateP(event):
    global cadre
    photo = PIL.ImageTk.PhotoImage(image) 
    largeur, hauteur = image.size
    cadre = Canvas(f,height=hauteur ,width=largeur) 
    cadre.create_image(largeur/2,hauteur/2, image=photo)
    cadre.bind("<B1-Motion>", testP)
    cadre.bind("<ButtonRelease>", updateP)
    cadre.grid(row=1, column=0)
    f.mainloop()

# Mise à jour pour le reste
def update():
    global cadre
    photo = PIL.ImageTk.PhotoImage(image) 
    largeur, hauteur = image.size
    cadre.destroy()
    cadre = Canvas(f,height=hauteur ,width=largeur) 
    cadre.create_image(largeur/2,hauteur/2, image=photo)
    cadre.bind("<B1-Motion>", testP)
    cadre.bind("<ButtonRelease>", updateP)
    cadre.grid(row=1, column=0)
    f.mainloop()

# Retrait de tous les changements
def reset():
    global image
    global chemin
    image = PIL.Image.open(chemin)
    update()

# Options des seuils
def optionS():
    global seuilL1
    global seuilC1
    global seuilS1

    fseuil = Tk()

    Label(fseuil, text = "Luminosité").grid(row = 0, column = 0)
    Label(fseuil, text = "Contraste").grid(row = 1, column = 0)
    Label(fseuil, text = "Saturation").grid(row = 2, column = 0)

    scaleL = Scale(fseuil, variable = seuilL1, orient = HORIZONTAL).grid(row = 0, column = 1)
    scaleC = Scale(fseuil, variable = seuilC1, orient = HORIZONTAL).grid(row = 1, column = 1)
    scaleS = Scale(fseuil, variable = seuilS1, orient = HORIZONTAL).grid(row = 2, column = 1)

    fseuil.mainloop()

def optionR():
    print(1)

# Choix du pinceau
def choixP():
    sf = Toplevel()

    sf.title("Choix pinceau")

    x,y = degradeImg.size

    frame = Frame(sf)

    Button(frame, border = 0, image = nbIMG, command = nbChoix).grid(row = 0, column = 0)
    Button(frame, border = 0, image = sepiaIMG, command = sepiaChoix).grid(row = 0, column = 1)
    Button(frame, border = 0, image = grisIMG, command = grisChoix).grid(row = 0, column = 2)

    frame.grid(row = 0, column = 0)

    degrade = Canvas(sf, height = x, width = y)
    degrade.create_image(x/2, y/2, image = degradeImgC)
    degrade.bind("<ButtonRelease>", choixCol)
    degrade.grid(row = 1, column = 0)

    #coul = Canvas(sf, height = 100, width = 100, bg = color).grid(row = 0, column = 3)

    sf.mainloop()

def updtCoul():
    global coul
    coul = Canvas(sf, height = 100, width = 100, bg = color).grid(row = 0, column = 3)

    sf.mainloop()

def choixCol(event):
    global colP, nbP, sepiaP, grisP, negatP,color

    x,y = event.x,event.y
    px = degradeImg.load()

    color = px[x,y]
    #color = rgb_to_hex(color)

    colP = True
    nbP = False
    sepiaP = False
    grisP = False
    negatP = False

    #updtCoul()

def nbChoix():
    global colP, nbP, sepiaP, grisP, negatP

    colP = False
    nbP = True
    sepiaP = False
    grisP = False
    negatP = False

def sepiaChoix():
    global colP, nbP, sepiaP, grisP, negatP

    colP = False
    nbP = False
    sepiaP = True
    grisP = False
    negatP = False

def grisChoix():
    global colP, nbP, sepiaP, grisP, negatP

    colP = False
    nbP = False
    sepiaP = False
    grisP = True
    negatP = False

def negatChoix():
    global colP, nbP, sepiaP, grisP, negatP

    colP = False
    nbP = False
    sepiaP = False
    grisP = False
    negatP = True

def rienChoix():
    global colP, nbP, sepiaP, grisP, negatP

    colP = False
    nbP = False
    sepiaP = False
    grisP = False
    negatP = False


# Test du pinceau
def testP(event):
    x,y = event.x,event.y

    if nbP == True:
        nbPinceau(x,y)
    elif sepiaP == True:
        sepiaPinceau(x,y)
    elif grisP == True:
        grisPinceau(x,y)
    elif negatP == True:
        negatPinceau(x,y)
    elif colP == True:
        colPinceau(x,y)
    else:
        print(1)

# Ouverture d'un fichier
def ouvrir():
    global image
    global chemin
    chemin = askopenfilename(title="Ouvrir une image", filetypes=[('all files','.*')])#('png files','.png'),
    image = PIL.Image.open(chemin)
    imageReset = PIL.Image.open(chemin)
    update()

# Sauvegarde du fichier
def save():
    image.save("sauvegarde.png", "PNG")


# Ouverture de la fenêtre d'aide
def aide():
    print(1)

# Conversion rgb vers hex
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


### Fonction des filtres ###

# Filtre noir et blanc
def nbF():
    global image
    seuil = 128
    x,y = image.size
    px = image.load()

    for i in range(x):
        for j in range(y):
            if (px[i,j][0]+px[i,j][1]+px[i,j][2])/3 > seuil:
                px[i,j] = (255,255,255)
            else:
                px[i,j] = (0,0,0)

    update()

# Filtre sépia
def sepiaF():
    print(1)

# Filtre nuances de gris
def ngF():
    global image
    x,y = image.size
    px = image.load()

    for i in range(0,x):
        for j in range(0,y):
            gris = int(round(0.299*px[i,j][0]+0.587*px[i,j][1]+0.114*px[i,j][2]))
            px[i,j] = (gris,gris,gris)

    update()

# Filtre négatif
def negatF():
    global image
    x,y = image.size
    px = image.load()

    for i in range(0,x):
        for j in range(0,y):
            px[i,j] = (255-(px[i,j][0]) , 255-(px[i,j][1]) , 255-(px[i,j][2]))

    update()

# Filtre flou
def flouF():
    global image
    x,y = image.size
    pix = image.load()

    for i in range(1,x-1,2):
        for j in range(1,y-1,2):
            a = (pix[i,j][0]+pix[i+1,j][0]+pix[i,j+1][0]+pix[i,j-1][0]+pix[i,j+1][0])//5
            b = (pix[i,j][1]+pix[i-1,j][1]+pix[i+1,j][1]+pix[i,j-1][1]+pix[i,j+1][1])//5
            c = (pix[i,j][2]+pix[i-1,j][2]+pix[i+1,j][2]+pix[i,j-1][2]+pix[i,j+1][2])//5
            pix[i,j] = a,b,c
            pix[i+1,j] = a,b,c
            pix[i,j+1] = a,b,c
            pix[i+1,j+1] = a,b,c   
    update()



### Filtre graduels ###

# Saturation
def satP():
    global image
    x,y = image.size
    px = image.load()

    for i in range(x):
        for j in range(y):
            if px[i,j][0] >= px[i,j][1] and px[i,j][0] >= px[i,j][2]:
                px[i,j] = (px[i,j][0] + seuilS, px[i,j][1] , px[i,j][2])
            elif px[i,j][1] >= px[i,j][0] and px[i,j][1] >= px[i,j][2]:
                px[i,j] = (px[i,j][0], px[i,j][1] + seuilS, px[i,j][2])
            elif px[i,j][2] >= px[i,j][1] and px[i,j][2] >= px[i,j][0]:
                px[i,j] = (px[i,j][0] , px[i,j][1] , px[i,j][2] + seuilS)
    update()


def satM():
    global image
    x,y = image.size
    px = image.load()

    for i in range(x):
        for j in range(y):
            if px[i,j][0] >= px[i,j][1] and px[i,j][0] >= px[i,j][2]:
                px[i,j] = (px[i,j][0] - seuilS, px[i,j][1] , px[i,j][2])
            elif px[i,j][1] >= px[i,j][0] and px[i,j][1] >= px[i,j][2]:
                px[i,j] = (px[i,j][0], px[i,j][1] - seuilS, px[i,j][2])
            elif px[i,j][2] >= px[i,j][1] and px[i,j][2] >= px[i,j][0]:
                px[i,j] = (px[i,j][0] , px[i,j][1] , px[i,j][2] - seuilS)
    update()


# Contraste
def contP():
    global image
    x,y = image.size
    px = image.load()

    for i in range(x):
        for j in range(y):
            if (px[i,j][0]+px[i,j][1]+px[i,j][2])/3 <= 128:
                px[i,j] = px[i,j][0]-seuilC,px[i,j][1]-seuilC,px[i,j][2]-seuilC
            else:
                px[i,j] = px[i,j][0]+seuilC,px[i,j][1]+seuilC,px[i,j][2]+seuilC
    update()

def contM():
    global image
    x,y = image.size
    px = image.load()

    for i in range(x):
        for j in range(y):
            if (px[i,j][0]+px[i,j][1]+px[i,j][2])/3 >= 128:
                px[i,j] = px[i,j][0]-seuilC,px[i,j][1]-seuilC,px[i,j][2]-seuilC
            else:
                px[i,j] = px[i,j][0]+seuilC,px[i,j][1]+seuilC,px[i,j][2]+seuilC
    update()

# Luminosité
def lumiP():
    global image

    x,y = image.size
    px = image.load()

    for i in range(x):
        for j in range(y):
            px[i,j] = px[i,j][0]+seuilL,px[i,j][1]+seuilL,px[i,j][2]+seuilL

    update()

def lumiM():
    global image
    x,y = image.size
    px = image.load()

    for i in range(x):
        for j in range(y):
            px[i,j] = px[i,j][0]-seuilL,px[i,j][1]-seuilL,px[i,j][2]-seuilL

    update()

### Division ###

def division():
    global image

    x,y = image.size

    if (x%2 == 1):
        x = x-1
    
    if (y%2 == 1):
        y = y-1
    
    limite_x = x/2
    limite_y = y/2
    im = PIL.Image.new("RGB", (x,y))
    p = im.load()
    pix = image.load()

    for i in range(0,x):
        for j in range(0,y):
            if (i%2 == 0):
                k1 = i/2
                if (j%2 == 0):
                    k2 = j/2
                    p[k1,k2] = (pix[i,j][0],pix[i,j][1],pix[i,j][2])
                else:
                    k2 = (j-1)/2
                    p[k1,limite_y+k2] = (pix[i,j][0],pix[i,j][1],pix[i,j][2])
            else:
                k1 = (i-1)/2
                if (j%2 == 0):
                    k2 = j/2
                    p[limite_x+k1,k2] = (pix[i,j][0],pix[i,j][1],pix[i,j][2])
                else:
                    k2 = (j-1)/2
                    p[limite_x+k1,limite_y+k2] = (pix[i,j][0],pix[i,j][1],pix[i,j][2])
    image = im
    update()

### Histogrammes ###

# Histogramme banal
def histo():
    x,y = image.size
    ordo = []
    px = image.load()

    for i in range(x):
        for j in range(y):
            pixel = (px[i,j][0]+px[i,j][1]+px[i,j][2])/3
            ordo.append(pixel)
            
    plt.hist(ordo, range = (0,256), bins = 256)
    plt.show()

# Histogramme couleurs
def histoRVB():
    x,y = image.size
    r = []
    v = []
    b = []
    px = image.load()

    for i in range(x):
        for j in range(y):
            r.append(px[i,j][0])
            v.append(px[i,j][1])
            b.append(px[i,j][2])

    plt.hist(r, range = (0,256), bins = 256, color='red')
    plt.hist(v, range = (0,256), bins = 256, color='green')
    plt.hist(b, range = (0,256), bins = 256, color='blue')
    plt.show()

### Pinceaux ###

# Pinceau noir et blanc
def nbPinceau(x,y):
    global image
    seuil = 128
    px = image.load()

    for i in range(-rayon,rayon):
        for j in range(-rayon,rayon):
            if abs(i)+abs(j) <= rayon+6:
                if (px[x+i,y+j][0]+px[x+i,y+j][1]+px[x+i,y+j][2])/3 > seuil:
                    px[x+i,y+j] = (255,255,255)
                else:
                    px[x+i,y+j] = (0,0,0)
# Pinceau sépia
def sepiaPinceau(x,y):
    print(20)

# Pinceau nuances de gris
def grisPinceau(x,y):
    global image
    px = image.load()

    for i in range(-rayon,rayon):
        for j in range(-rayon,rayon):
            if abs(i)+abs(j) <= rayon+6:
                gris = int(round(0.299*px[x+i,y+j][0]+0.587*px[x+i,y+j][1]+0.114*px[x+i,y+j][2]))
                px[x+i,y+j] = (gris,gris,gris)

# Pinceau négatif
def negatPinceau(x,y):
    global image
    pix = image.load()

    for i in range(-rayon,rayon):
        for j in range(-rayon,rayon):
            if abs(i)+abs(j) <= rayon+6:
                R = 255-(pix[x+i,y+j][0])
                V = 255-(pix[x+i,y+j][1])
                B = 255-(pix[x+i,y+j][2])
                pix[x+i,y+j] = (R,V,B)

# Pinceau des couleurs
def colPinceau(x,y):
    global image
    px = image.load()

    for i in range(-rayon,rayon):
        for j in range(-rayon,rayon):
            if abs(i)+abs(j) <= rayon+6:
                px[x+i,y+j] = color

### Miroir symétrie et compagnie ###

# Miroir

def mirV():
    global image
    x,y=image.size
    m=(x/2)-(x%2)
    m=int(m)
    px=image.load()

    for i in range(0,m):
        for j in range(0,y):
            mem=px[x-i-1,j]
            px[x-i-1,j]=px[i,j]
            px[i,j]=mem

    update()

def mirH():
    global image
    x,y=image.size
    n=(y/2)-(y%2)
    n=int(n)
    px=image.load()

    for i in range(0,x):
        for j in range(0,n):
            mem=px[i,y-j-1]
            px[i,y-j-1]=px[i,j]
            px[i,j]=mem

    update()

# Symétries

def symV():
    global image
    x,y= image.size
    pix=image.load()

    for i in range(0,x):
        for j in range(0,y):
            pix[i,j]=pix[i,y-j-1]
            pix[i,j]=pix[x-i-1,j]

    update()


def symH():
    global image
    x,y=image.size
    pix=image.load()

    for i in range(0,x):
        for j in range(0,y):
            pix[i,j]=pix[x-i-1,j]
            pix[i,j]=pix[i,y-j-1]
    
    update()


### Programme principal ###

# Définition de l'interface graphique

f = Tk()

f.title("Editeur d'image")


## Barre de menu
barreM = Menu(f, relief = FLAT, bg = "#f7f7f7", fg = "#727272", activebackground = "#2a8eff", activeborderwidth = 0, border = 0, activeforeground = "#f7f7f7")

police = Font(size = 10)

fichier = Menu(barreM, tearoff = 0, relief = FLAT, bg = "#f7f7f7", fg = "#727272", activebackground = "#2a8eff", activeborderwidth = 0, border = 0, activeforeground = "#f7f7f7")
fichier.add_command(label = "Ouvrir", command = ouvrir, font = police)
fichier.add_command(label = "Sauvegarder", command = save, font = police)
fichier.add_command(label = "Quitter", command = f.destroy, font = police)
barreM.add_cascade(label = "Fichier", menu = fichier, font = police)

edit = Menu(barreM, tearoff = 0, relief = FLAT, bg = "#f7f7f7", fg = "#727272", activebackground = "#2a8eff", activeborderwidth = 0, border = 0, activeforeground = "#f7f7f7")
edit.add_command(label = "Nettoyer", command = reset, font = police)
edit.add_command(label = "Noir et blanc", command = nbF, font = police)
edit.add_command(label = "Sépia", command = sepiaF, font = police)
edit.add_command(label = "Nuances de gris", command = ngF, font = police)
edit.add_command(label = "Négatif", command = negatF, font = police)
edit.add_command(label = "Flou", command = flouF, font = police)
barreM.add_cascade(label = "Edition", menu = edit, font = police)

param = Menu(barreM, tearoff = 0, relief = FLAT, bg = "#f7f7f7", fg = "#727272", activebackground = "#2a8eff", activeborderwidth = 0, border = 0, activeforeground = "#f7f7f7")
param.add_command(label = "Rayon", command = optionR, font = police)
param.add_command(label = "Seuils", command = optionS, font = police)
barreM.add_cascade(label = "Paramètres", menu = param, font = police)

sym = Menu(barreM, tearoff = 0, relief = FLAT, bg = "#f7f7f7", fg = "#727272", activebackground = "#2a8eff", activeborderwidth = 0, border = 0, activeforeground = "#f7f7f7")
sym.add_command(label = "Symétrie verticale", command = symV, font = police)
sym.add_command(label = "Symétrie horizontale", command = symH, font = police)
sym.add_command(label = "Miroir vertical", command = mirV, font = police)
sym.add_command(label = "Miroir horizontal", command = mirH, font = police)

barreM.add_cascade(label = "Symétries", menu = sym, font = police)

aide =  Menu(barreM, tearoff = 0, relief = FLAT, bg = "#f7f7f7", fg = "#727272", activebackground = "#2a8eff", activeborderwidth = 0, border = 0, activeforeground = "#f7f7f7")
aide.add_command(label = "Comment s'en servir", command = aide, font = police)
barreM.add_cascade(label = "Aide", menu = aide, font = police)

f.config(menu = barreM)

## Boutons d'actions
barreB = Frame(f, bg = "#d9d9d9")

cM = PhotoImage(file="C-.png")
cP = PhotoImage(file="C+.png")

lM = PhotoImage(file="L-.png")
lP = PhotoImage(file="L+.png")

sM = PhotoImage(file="S-.png")
sP = PhotoImage(file="S+.png")

pin = PhotoImage(file="pin.png")

nbIMG = PhotoImage(file="NB.png")
negaIMG = PhotoImage(file="nega.png")
grisIMG = PhotoImage(file="gris.png")
sepiaIMG = PhotoImage(file="sepia.png")

div = PhotoImage(file="div.png")

histoIMG = PhotoImage(file="histo.png")
historvbIMG = PhotoImage(file="historgb.png")

Button(barreB, border = 0, image = sP, command = satP).grid(row = 0, column = 0)
Button(barreB, border = 0, image = sM, command = satM).grid(row = 0, column = 1)

Canvas(barreB, width = 10, height = 10, bg = "#d9d9d9", highlightbackground = "#d9d9d9").grid(row = 0, column = 2)

Button(barreB, border = 0, image = cP, command = contP).grid(row = 0, column = 3)
Button(barreB, border = 0, image = cM, command = contM).grid(row = 0, column = 4)

Canvas(barreB, width = 10, height = 10, bg = "#d9d9d9", highlightbackground = "#d9d9d9").grid(row = 0, column = 5)

Button(barreB, border = 0, image = lP, command = lumiP).grid(row = 0, column = 6)
Button(barreB, border = 0, image = lM, command = lumiM).grid(row = 0, column = 7)

Canvas(barreB, width = 10, height = 10, bg = "#d9d9d9", highlightbackground = "#d9d9d9").grid(row = 0, column = 8)

Button(barreB, border = 0, image = pin, command = choixP).grid(row = 0, column = 9)

Canvas(barreB, width = 10, height = 10, bg = "#d9d9d9", highlightbackground = "#d9d9d9").grid(row = 0, column = 10)

Button(barreB, border = 0, image = nbIMG, command = nbF).grid(row = 0, column = 11)
Button(barreB, border = 0, image = sepiaIMG, command = sepiaF).grid(row = 0, column = 12)
Button(barreB, border = 0, image = grisIMG, command = ngF).grid(row = 0, column = 13)
Button(barreB, border = 0, image = negaIMG, command = negatF).grid(row = 0, column = 14)

Canvas(barreB, width = 10, height = 10, bg = "#d9d9d9", highlightbackground = "#d9d9d9").grid(row = 0, column = 15)

Button(barreB, border = 0, image = histoIMG, command = histo, highlightcolor = "#d9d9d9").grid(row = 0, column = 16)
Button(barreB, border = 0, image = historvbIMG, command = histoRVB).grid(row = 0, column = 17)

Canvas(barreB, width = 10, height = 10, bg = "#d9d9d9", highlightbackground = "#d9d9d9").grid(row = 0, column = 18)

Button(barreB, border = 0, image = div, command = division).grid(row = 0, column = 19)

Canvas(barreB, width = 10, height = 10, bg = "#d9d9d9", highlightbackground = "#d9d9d9").grid(row = 0, column = 18)

Button(barreB, border = 0, image = nbIMG, command = nbF).grid(row = 0, column = 11)
Button(barreB, border = 0, image = sepiaIMG, command = sepiaF).grid(row = 0, column = 12)
Button(barreB, border = 0, image = grisIMG, command = ngF).grid(row = 0, column = 13)
Button(barreB, border = 0, image = negaIMG, command = negatF).grid(row = 0, column = 14)

barreB.grid(row = 0, column = 0)

cadre = Canvas(f)
cadre.grid(row = 1, column = 0)

degradeImgC = PhotoImage(file="couleurs.png")

f.mainloop()
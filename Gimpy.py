#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
#Logiciel de traitement d'image sous python 3.x en POO
#GUI : tkinter
#Traitement d'image : Pillow alias PIL
#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o Importations o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
from tkinter import *
import PIL.Image
import PIL.ImageTk 
from tkinter.filedialog import *
from tkinter.font import *
import matplotlib.pyplot as plt

#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o Classe de réglage du rayon pinceauo-o-o-o-o-o-o-o-o-o-o-o-o-o
class BrushRadius():
    def __init__(self, master):
        self.master = master
        self.toplevel = Toplevel(master)
        self.screenWidth = master.winfo_screenwidth()
        self.screenHeight = master.winfo_screenheight()
        self.toplevel.title('Rayon du pinceau')
        self.toplevel.geometry('300x650+{}+{}'.format(int(self.screenWidth*(0.75)),50))
        self.toplevel.rowconfigure(0, weight=1)
        self.toplevel.columnconfigure(0, weight=1)
        self.displayElements()

    def displayElements(self):
        self.mainFrame = Frame(self.toplevel, bg='lightblue')
        self.mainFrame.grid(row=0, column=0, sticky='nsew', padx=3, pady=3)
        self.mainFrame.rowconfigure(0, weight=1)
        self.mainFrame.columnconfigure(0, weight=1)


        self.scrollbarRadius = Scrollbar(self.mainFrame, orient='horizontal',command=self.functionUpdateRadius)
        self.scrollbarRadius.grid(row=0, column=0, sticky='new', padx=5, pady=10)

    def functionUpdateRadius(self,a,b):
        print(b)
        self.master.radius = int(100*b)






#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o Classe Pinceau o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
class Brush():
    def __init__(self, master):
        self.master = master
        self.toplevel = Toplevel(master)
        self.toplevel.title('Pinceau')
        self.toplevel.geometry('300x650+0+50')
        self.displayTopLevel()
        self.cadrePinceau.bind("<Button-1>", self.functionGetColor)
        self.Choix = '' 

    #Affichage de la fenêtre
    def displayTopLevel(self):
        #Configuration du toplevel
        self.toplevel.columnconfigure(0, weight=1)
        self.toplevel.rowconfigure(0, weight=1)

        #Creation frame principal
        self.mainFrame = Frame(self.toplevel, bg='white')
        self.mainFrame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=2)
        self.mainFrame.rowconfigure(1, weight=1)
        self.mainFrame.rowconfigure(2, weight=8)

        #Importations des images
        self.imageNoirBlanc = PIL.ImageTk.PhotoImage(file="images/NB.png")
        self.imageNegatif = PIL.ImageTk.PhotoImage(file="images/nega.png")
        self.imageGris = PIL.ImageTk.PhotoImage(file="images/gris.png")
        self.imageSepia = PIL.ImageTk.PhotoImage(file="images/sepia.png")
        self.imageDivision = PIL.ImageTk.PhotoImage(file="images/div.png")
        self.imageHisto = PIL.ImageTk.PhotoImage(file="images/histo.png")
        self.imageHistoCouleur = PIL.ImageTk.PhotoImage(file="images/historgb.png")
        self.imageContrastLess = PIL.ImageTk.PhotoImage(file="images/C-.png")
        self.imageContrastMore = PIL.ImageTk.PhotoImage(file="images/C+.png")
        self.imageLuminositeMoins = PIL.ImageTk.PhotoImage(file="images/L-.png")
        self.imageLuminositePlus = PIL.ImageTk.PhotoImage(file="images/L+.png")
        self.imageSaturationMoins = PIL.ImageTk.PhotoImage(file="images/S-.png")
        self.imageSaturationPlus = PIL.ImageTk.PhotoImage(file="images/S+.png")
        self.imagePinceau = PIL.ImageTk.PhotoImage(file="images/options1.png")
        self.imageFlou = PIL.ImageTk.PhotoImage(file="images/flou.png")
        self.imageDegradeCouleur = PIL.ImageTk.PhotoImage(file="images/couleurs2.png")
        self.imageDegradeCouleurOpen = PIL.Image.open("images/couleurs4bis.png")

        #Creation du frame des boutons
        self.frameButtons = Frame(self.mainFrame, bg='#18C7B0')
        self.frameButtons.grid(row=0, column=0, padx=3, pady=3, sticky='nsew')
        self.frameButtons.rowconfigure(1, weight=1)
        self.frameButtons.rowconfigure(2, weight=1)
        self.frameButtons.columnconfigure(1, weight=1)
        self.frameButtons.columnconfigure(2, weight=1)
        self.frameButtons.columnconfigure(3, weight=1)
        self.frameButtons.columnconfigure(4, weight=1)
        self.frameButtons.columnconfigure(5, weight=1)
        self.frameButtons.columnconfigure(6, weight=1)

        #Création des boutons
        self.B1 = Button(self.frameButtons, border=0, image=self.imageContrastMore, command=self.contrastMore)
        self.B2 = Button(self.frameButtons, border=0, image=self.imageContrastLess, command=self.contrastLess)
        self.B3 = Button(self.frameButtons, border=0, image=self.imageLuminositePlus, command=self.brightnessMore)
        self.B4 = Button(self.frameButtons, border=0, image=self.imageLuminositeMoins, command=self.brightnessLess)   
        self.B5 = Button(self.frameButtons, border=0, image=self.imageSaturationPlus, command=self.saturationMore)
        self.B6 = Button(self.frameButtons, border=0, image=self.imageSaturationMoins, command=self.saturationLess)
        self.B1b = Button(self.frameButtons, border=0, image=self.imageNoirBlanc)
        self.B2b = Button(self.frameButtons, border=0, image=self.imageSepia)
        self.B3b = Button(self.frameButtons, border=0, image=self.imageNegatif)
        self.B4b = Button(self.frameButtons, border=0, image=self.imageFlou)   
        self.B5b = Button(self.frameButtons, border=0, image=self.imageGris)
        self.B6b = Button(self.frameButtons, border=0, image=self.imagePinceau, command=self.callBrushRadius)

        #Sauvegarde pour le bug
        self.B1.image = self.imageContrastMore
        self.B2.image = self.imageContrastLess
        self.B3.image = self.imageLuminositePlus
        self.B4.image = self.imageLuminositeMoins
        self.B5.image = self.imageSaturationPlus
        self.B6.image = self.imageSaturationMoins
        self.B1b.image = self.imageNoirBlanc
        self.B2b.image = self.imageSepia
        self.B3b.image = self.imageNegatif
        self.B4b.image = self.imageFlou
        self.B5b.image = self.imageGris
        self.B6b.image = self.imagePinceau

        self.B1.grid(row = 0, column = 1,padx = 4,pady = 4)
        self.B2.grid(row = 0, column = 2,padx = 4,pady = 4)
        self.B3.grid(row = 0, column = 3,padx = 4,pady = 4)
        self.B4.grid(row = 0, column = 4,padx = 4,pady = 4)
        self.B5.grid(row = 0, column = 5,padx = 4,pady = 4)
        self.B6.grid(row = 0, column = 6,padx = 4,pady = 4)
        self.B1b.grid(row = 1, column = 1,padx = 4,pady = 4)
        self.B2b.grid(row = 1, column = 2,padx = 4,pady = 4)
        self.B3b.grid(row = 1, column = 3,padx = 4,pady = 4)
        self.B4b.grid(row = 1, column = 4,padx = 4,pady = 4)
        self.B5b.grid(row = 1, column = 5,padx = 4,pady = 4)
        self.B6b.grid(row = 1, column = 6,padx = 4,pady = 4)

        #Creation du canvas image couleur
        self.photoCouleur = PIL.ImageTk.PhotoImage(self.imageDegradeCouleurOpen)
        self.imageWidth, self.imageHeight = self.imageDegradeCouleurOpen.size
        self.cadrePinceau = Canvas(self.mainFrame, height=self.imageHeight+5, width=self.imageWidth+5, cursor='cross')
        self.cadrePinceau.grid(row=2, column=0, sticky='new')
        self.cadrePinceau.create_image(self.imageWidth/2,self.imageHeight/2,image=self.photoCouleur)
        self.cadrePinceau.image = self.photoCouleur

        #Creation frame avec la couleur actuelle
        self.frameColor = Label(self.mainFrame, text='Choisissez votre couleur', bg='grey')
        self.frameColor.grid(row=1, column=0, sticky='nsew')

    #Fonctions disponibles
    def functionGetColor(self,event):
        #Sauvegarde de la position du click
        self.click = ((event.x,event.y))
        #Chargement de l'image pour récupérer la couleur
        px = self.imageDegradeCouleurOpen.load()
        #Enregistrement des composantes de couleur du pixel x,y
        r,g,b = px[event.x,event.y][0],px[event.x,event.y][1],px[event.x,event.y][2]
        #Conversion en code hexadecimal
        rgbCode1 = '#%02x%02x%02x%02x' % px[event.x,event.y]
        #On enlève les deux derniers caractères
        self.rgbCode=rgbCode1[0:-2]
        self.Choix = 'Color' 
        self.Color = ((r,g,b))
        #Update de la couleur
        self.functionUpdateColor()
    def functionUpdateColor(self):
        self.frameColor.destroy()
        self.frameColor = Frame(self.mainFrame, height=25, bg=self.rgbCode)
        self.frameColor.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    #Commande des boutons
    def contrastMore(self):
        self.Choix = 'contrastMore'
    def contrastLess(self):
        self.Choix = 'contrastLess'
    def brightnessMore(self):
        self.Choix = 'brightnessMore'
    def brightnessLess(self):
        self.Choix = 'brightnessLess'
    def saturationMore(self):
        self.Choix = 'saturationMore'
    def saturationLess(self):
        self.Choix = 'saturationLess'

    def callBrushRadius(self):
        self.brushRadiusWindow = BrushRadius(self.master)
        self.Radius = self.brushRadiusWindow.Radius










#o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o Fenêtre principale o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
class MainApplication():
    def __init__(self, master):
        #Attributs
        self.saturationThreshold = 20
        self.contrastThreshold = 20
        self.brightnessThreshold = 20
        self.brushRadius = 10
        self.stop = False
        self.clickCount = 0
        self.radius = 15
        self.screenWidth = master.winfo_screenwidth()
        self.screenHeight = master.winfo_screenheight()

        #Création de la fenêtre
        self.master = master
        self.master.columnconfigure(0, weight = 1)
        self.master.rowconfigure(0,  minsize = 42)
        self.master.rowconfigure(1, weight = 5)

        #Affichage des éléments
        self.displayMenu()
        self.displayButtons()
        self.displayCadre()

        #Gestion des évènements
        self.cadre.bind("<Button-1>", self.brushEvent)
        self.cadre.bind("<Motion>", self.functionMousePosition)


    #Méthodes d'affichage de la fenêtre tkinter

    def displayMenu(self):
    
        #Barre de menu globale
        menuBar = Menu(self.master, relief = FLAT, bg = "#f7f7f7", fg = "#727272", activebackground = "#2a8eff", activeborderwidth = 0, border = 0, activeforeground = "#f7f7f7")
        police = Font(size = 10)
        
        #Création des onglets
        fichier = Menu(menuBar, tearoff=0, relief=FLAT, bg="#f7f7f7", fg="#727272", activebackground="#2a8eff", activeborderwidth = 0, border = 0, activeforeground = "#f7f7f7")
        edition = Menu(menuBar, tearoff=0, relief=FLAT, bg="#f7f7f7", fg="#727272", activebackground="#2a8eff", activeborderwidth = 0, border = 0, activeforeground = "#f7f7f7")
        paramet = Menu(menuBar, tearoff=0, relief=FLAT, bg="#f7f7f7", fg="#727272", activebackground="#2a8eff", activeborderwidth = 0, border = 0, activeforeground = "#f7f7f7")
        symetry = Menu(menuBar, tearoff=0, relief=FLAT, bg="#f7f7f7", fg="#727272", activebackground="#2a8eff", activeborderwidth = 0, border = 0, activeforeground = "#f7f7f7")
        aidmenu = Menu(menuBar, tearoff=0, relief=FLAT, bg="#f7f7f7", fg="#727272", activebackground="#2a8eff", activeborderwidth = 0, border = 0, activeforeground = "#f7f7f7")
        
        #Création des sous menus
        #Fichier
        fichier.add_command(label="Ouvrir", font = police,command = self.functionOpenImage)
        fichier.add_command(label="Sauvegarder",  font = police,command = self.functionSaveImage)
        fichier.add_command(label="Quitter", command = self.master.destroy, font = police)
        #Edition
        edition.add_command(label="Reset", font=police, command=self.functionResetImage)
        edition.add_command(label="Noir et blanc",  font=police, command=self.filterBlackAndWhite)
        edition.add_command(label="Sépia", font=police, command=self.filterSepia)
        edition.add_command(label="Nuances de gris", font=police, command=self.filterGrey)
        edition.add_command(label="Négatif", font=police, command=self.filterNegative)
        edition.add_command(label="Flou", font=police, command=self.filterBlurry)
        edition.add_command(label="Theo", font=police, command=self.filterTheo)
        #Paramètres
        paramet.add_command(label = "Rayon",  font = police)
        paramet.add_command(label = "Seuils",  font = police)
        #Symétries
        symetry.add_command(label = "Symétrie verticale",font = police, command = self.filterVerticalSymetry)
        symetry.add_command(label = "Symétrie horizontale",  font = police,command = self.filterHorizontalSymetry)
        symetry.add_command(label = "Miroir vertical",  font = police,command = self.filterVerticalMiror)
        symetry.add_command(label = "Miroir horizontal",  font = police,command = self.filterHorizontalMiror)
        #Aide
        aidmenu.add_command(label = "Aide",  font = police, command = self.functionHelp)
        
        
        #Création des menus défilants
        menuBar.add_cascade(label = "Fichier", menu = fichier, font = police)
        menuBar.add_cascade(label = "Edition", menu = edition, font = police)
        menuBar.add_cascade(label = "Paramètres", menu = paramet, font = police)
        menuBar.add_cascade(label = "Symétries", menu = symetry, font = police)
        menuBar.add_cascade(label = "Aide", menu = aidmenu, font = police)
        
        #Ajout du menu
        self.master.config(menu = menuBar)
    def displayButtons(self):
        ## Définition des boutons

        #Importations des images
        self.imageNoirBlanc = PIL.ImageTk.PhotoImage(file="images/NB.png")
        self.imageNegatif = PIL.ImageTk.PhotoImage(file="images/nega.png")
        self.imageGris = PIL.ImageTk.PhotoImage(file="images/gris.png")
        self.imageSepia = PIL.ImageTk.PhotoImage(file="images/sepia.png")
        self.imageDivision = PIL.ImageTk.PhotoImage(file="images/div.png")
        self.imageHisto = PIL.ImageTk.PhotoImage(file="images/histo.png")
        self.imageHistoCouleur = PIL.ImageTk.PhotoImage(file="images/historgb.png")
        self.imageContrastLess = PIL.ImageTk.PhotoImage(file="images/C-.png")
        self.imageContrastMore = PIL.ImageTk.PhotoImage(file="images/C+.png")
        self.imageLuminositeMoins = PIL.ImageTk.PhotoImage(file="images/L-.png")
        self.imageLuminositePlus = PIL.ImageTk.PhotoImage(file="images/L+.png")
        self.imageSaturationMoins = PIL.ImageTk.PhotoImage(file="images/S-.png")
        self.imageSaturationPlus = PIL.ImageTk.PhotoImage(file="images/S+.png")
        self.imagePinceau = PIL.ImageTk.PhotoImage(file="images/pin.png")
        self.imageFlou = PIL.ImageTk.PhotoImage(file="images/flou.png")
        self.imageDegradeCouleur = PIL.ImageTk.PhotoImage(file="images/couleurs2.png")
        self.imageDegradeCouleurOpen = PIL.Image.open("images/couleurs2.png")


        #Création du frame contenant les boutons
        buttonsFrame = Frame(self.master, bg='#18C7B0')
        #'#d9f9d9'
        buttonsFrame.grid(row=0, column=0, padx=3, pady=3)
        buttonsFrame.columnconfigure(1, weight=1)
        buttonsFrame.columnconfigure(2, weight=1)
        buttonsFrame.columnconfigure(3, weight=1)
        buttonsFrame.columnconfigure(4, weight=1)
        buttonsFrame.columnconfigure(5, weight=1)
        buttonsFrame.columnconfigure(6, weight=1)
        buttonsFrame.columnconfigure(7, weight=1)
        buttonsFrame.columnconfigure(8, weight=1)
        buttonsFrame.columnconfigure(9, weight=1)
        buttonsFrame.columnconfigure(10, weight=1)
        buttonsFrame.columnconfigure(11, weight=1)
        buttonsFrame.columnconfigure(12, weight=1)
        buttonsFrame.columnconfigure(13, weight=1)
        buttonsFrame.columnconfigure(14, weight=1)
        buttonsFrame.columnconfigure(15, weight=1)

        #Création des boutons
        self.B1  = Button(buttonsFrame, border=0, image=self.imageContrastMore, command=self.filterContrastMore)
        self.B2  = Button(buttonsFrame, border=0, image=self.imageContrastLess, command=self.filterContrastLess)
        self.B3  = Button(buttonsFrame, border=0, image=self.imageLuminositePlus, command=self.filterBrightnessMore)
        self.B4  = Button(buttonsFrame, border=0, image=self.imageLuminositeMoins, command=self.filterBrightnessLess)   
        self.B5  = Button(buttonsFrame, border=0, image=self.imageSaturationPlus, command=self.filterSaturationMore)
        self.B6  = Button(buttonsFrame, border=0, image=self.imageSaturationMoins, command=self.filterSaturationLess)
        self.B7  = Button(buttonsFrame, border=0, image=self.imageNoirBlanc, command=self.filterBlackAndWhite)
        self.B8  = Button(buttonsFrame, border=0, image=self.imageNegatif, command=self.filterNegative)
        self.B9  = Button(buttonsFrame, border=0, image=self.imageSepia, command=self.filterSepia)
        self.B10 = Button(buttonsFrame, border=0, image=self.imageGris, command=self.filterGrey)
        self.B11 = Button(buttonsFrame, border=0, image=self.imageDivision, command=self.filterDivideImage)
        self.B12 = Button(buttonsFrame, border=0, image=self.imageHisto, command=self.filterHistogram)
        self.B13 = Button(buttonsFrame, border=0, image=self.imageHistoCouleur, command=self.filterHistogramColor)
        self.B14 = Button(buttonsFrame, border=0, image=self.imagePinceau, command=self.brushPanel)
        self.B15 = Button(buttonsFrame, border=0, image=self.imageFlou, command=self.filterBlurry)

        #Sauvegarde des images (bug PIL)
        self.B1.image = self.imageContrastMore
        self.B2.image = self.imageContrastLess
        self.B3.image = self.imageLuminositePlus
        self.B4.image = self.imageLuminositeMoins
        self.B5.image = self.imageSaturationPlus
        self.B6.image = self.imageSaturationMoins
        self.B7.image = self.imageNoirBlanc
        self.B8.image = self.imageNegatif
        self.B9.image = self.imageSepia
        self.B10.image = self.imageGris
        self.B11.image = self.imageDivision
        self.B12.image = self.imageHisto
        self.B13.image = self.imageHistoCouleur
        self.B14.image = self.imagePinceau
        self.B15.image = self.imageFlou
        
        #Placement des boutons dans la grille
        self.B1.grid(row=0, column=1, padx=4, pady=4)
        self.B2.grid(row=0, column=2, padx=4, pady=4)
        self.B3.grid(row=0, column=3, padx=4, pady=4)
        self.B4.grid(row=0, column=4, padx=4, pady=4)
        self.B5.grid(row=0, column=5, padx=4, pady=4)
        self.B6.grid(row=0, column=6, padx=4, pady=4)
        self.B7.grid(row=0, column=7, padx=4, pady=4)
        self.B8.grid(row=0, column=8, padx=4, pady=4)
        self.B9.grid(row=0, column=9, padx=4, pady=4)
        self.B10.grid(row=0, column=10, padx=4, pady=4)
        self.B11.grid(row=0, column=11, padx=4, pady=4)
        self.B12.grid(row=0, column=12, padx=4, pady=4)
        self.B13.grid(row=0, column=13, padx=4, pady=4)
        self.B14.grid(row=0, column=14, padx=4, pady=4)
        self.B15.grid(row=0, column=15, padx=4, pady=4)
    def displayCadre(self):
        #Création du cadre image
        self.cadre = Canvas(self.master)
        self.cadre.grid(row=1, column=0)
        

    #Fonctions de l'application
    def functionOpenImage(self):
        #Ouverture de l'image avec le chemin indiqué
        self.chemin = askopenfilename(title="Ouvrir une image", filetypes=[('all files','.*')])#('png files','.png'),
        self.image = PIL.Image.open(self.chemin)
        #Sauvegarde de l'image pour la fonction reset
        self.imageSaved = PIL.Image.open(self.chemin)
        #Mise à jour de l'image affichée
        self.functionUpdateImage()
    def functionUpdateImage(self):
        self.photo = PIL.ImageTk.PhotoImage(self.image)
        self.photo.image = self.image
        self.imageWidth, self.imageHeight = self.image.size
        self.cadre.destroy()
        self.cadre = Canvas(self.master,height=self.imageHeight+5 ,width=self.imageWidth+5) 
        self.cadre.create_image(self.imageWidth/2,self.imageHeight/2,image=self.photo)
        self.cadre.grid(row=1, column=0)
        self.cadre.bind("<Button-1>", self.brushEvent)
        self.cadre.bind("<Motion>", self.functionMousePosition)
    def functionSaveImage(self):


        self.image.save("sauvegarde.png", "PNG")
    def functionHelp(self):
        #Fonction qui affiche l'aide utilisateur du logiciel
        print("Affichage de l'aide")
    def functionResetImage(self):
        self.image = PIL.Image.open(self.chemin)
        self.functionUpdateImage()
    def functionMousePosition(self,event):
        self.x = event.x
        self.y = event.y

        

    #Filtres disponibles
    def filterBlackAndWhite(self):
        seuil = 128
        x,y = self.image.size



        px = self.image.load()
        for i in range(x):
            for j in range(y):
                if (px[i,j][0]+px[i,j][1]+px[i,j][2])/3 > seuil:
                    px[i,j] = (255,255,255)
                else:
                    px[i,j] = (0,0,0)
        self.functionUpdateImage()
    def filterNegative(self):
        x,y = self.image.size
        px = self.image.load()
        for i in range(0,x):
            for j in range(0,y):
                px[i,j] = (255-(px[i,j][0]) , 255-(px[i,j][1]) , 255-(px[i,j][2]))
        self.functionUpdateImage()
    def filterGrey(self):
        x,y = self.image.size
        px = self.image.load()
        for i in range(0,x):
            for j in range(0,y):
                gris = int(round(0.299*px[i,j][0]+0.587*px[i,j][1]+0.114*px[i,j][2]))
                px[i,j] = (gris,gris,gris)
        self.functionUpdateImage()
    def filterBlurry(self):
        x,y = self.image.size
        pix = self.image.load()
        for i in range(1,x-1,2):
            for j in range(1,y-1,2):
                a = (pix[i,j][0]+pix[i+1,j][0]+pix[i,j+1][0]+pix[i,j-1][0]+pix[i,j+1][0])//5
                b = (pix[i,j][1]+pix[i-1,j][1]+pix[i+1,j][1]+pix[i,j-1][1]+pix[i,j+1][1])//5
                c = (pix[i,j][2]+pix[i-1,j][2]+pix[i+1,j][2]+pix[i,j-1][2]+pix[i,j+1][2])//5
                pix[i,j] = a,b,c
                pix[i+1,j] = a,b,c
                pix[i,j+1] = a,b,c
                pix[i+1,j+1] = a,b,c   
        self.functionUpdateImage()
    def filterDivideImage(self):
        x,y = self.image.size
        if (x%2 == 1):
            x = x-1
        if (y%2 == 1):
            y = y-1
        limite_x = x/2
        limite_y = y/2
        im = PIL.Image.new("RGB", (x,y))
        p = im.load()
        pix = self.image.load()
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
        self.image = im
        self.functionUpdateImage()
    def filterSepia(self):
        x,y = self.image.size
        px = self.image.load()
        for i in range(0,x):
            for j in range(0,y):
                red = px[i,j][0]*0.393 + px[i,j][1]*0.769 + px[i,j][2]*0.189
                green = px[i,j][0]*0.349 + px[i,j][1]*0.686 + px[i,j][2]*0.168
                blue = px[i,j][0]*0.272 + px[i,j][1]*0.534 + px[i,j][2]*0.131
                px[i,j] = (int(red) , int(green) , int(blue))
        self.functionUpdateImage()
    def filterHistogram(self):
        x,y = self.image.size
        ordo = []
        px = self.image.load()
        for i in range(x):
            for j in range(y):
                pixel = (px[i,j][0]+px[i,j][1]+px[i,j][2])/3
                ordo.append(pixel)
        plt.hist(ordo, range = (0,256), bins = 256)
        plt.show()
    def filterHistogramColor(self):
        x,y = self.image.size
        r = []
        v = []
        b = []
        px = self.image.load()
        for i in range(x):
            for j in range(y):
                r.append(px[i,j][0])
                v.append(px[i,j][1])
                b.append(px[i,j][2])
        plt.hist(r, range=(0,256), bins=256, color='red')
        plt.hist(v, range=(0,256), bins=256, color='green')
        plt.hist(b, range=(0,256), bins=256, color='blue')
        plt.show()
    def filterVerticalMiror(self):
        x,y=self.image.size
        m=(x/2)-(x%2)
        m=int(m)
        px=self.image.load()
        for i in range(0,m):
            for j in range(0,y):
                mem=px[x-i-1,j]
                px[x-i-1,j]=px[i,j]
                px[i,j]=mem
        self.functionUpdateImage()
    def filterHorizontalMiror(self):
        x,y=self.image.size
        n=(y/2)-(y%2)
        n=int(n)
        px=self.image.load()
        for i in range(0,x):
            for j in range(0,n):
                mem=px[i,y-j-1]
                px[i,y-j-1]=px[i,j]
                px[i,j]=mem
        self.functionUpdateImage()
    def filterVerticalSymetry(self):
        x,y=self.image.size
        pix=self.image.load()
        for i in range(0,x):
            for j in range(0,y):
                pix[i,j]=pix[i,y-j-1]
                pix[i,j]=pix[x-i-1,j]
        self.functionUpdateImage()
    def filterHorizontalSymetry(self):
        x,y=self.image.size
        pix=self.image.load()
        for i in range(0,x):
            for j in range(0,y):
                pix[i,j]=pix[x-i-1,j]
                pix[i,j]=pix[i,y-j-1]
        self.functionUpdateImage()
    def filterSaturationMore(self):
        x,y = self.image.size
        px = self.image.load()
        for i in range(x):
            for j in range(y):
                if px[i,j][0] >= px[i,j][1] and px[i,j][0] >= px[i,j][2]:
                    px[i,j] = (px[i,j][0] + self.saturationThreshold, px[i,j][1] , px[i,j][2])
                elif px[i,j][1] >= px[i,j][0] and px[i,j][1] >= px[i,j][2]:
                    px[i,j] = (px[i,j][0], px[i,j][1] + self.saturationThreshold, px[i,j][2])
                elif px[i,j][2] >= px[i,j][1] and px[i,j][2] >= px[i,j][0]:
                    px[i,j] = (px[i,j][0] , px[i,j][1] , px[i,j][2] + self.saturationThreshold)
        self.functionUpdateImage()
    def filterSaturationLess(self):
        x,y = self.image.size
        px = self.image.load()
        for i in range(x):
            for j in range(y):
                if px[i,j][0] >= px[i,j][1] and px[i,j][0] >= px[i,j][2]:
                    px[i,j] = (px[i,j][0] - self.saturationThreshold, px[i,j][1] , px[i,j][2])
                elif px[i,j][1] >= px[i,j][0] and px[i,j][1] >= px[i,j][2]:
                    px[i,j] = (px[i,j][0], px[i,j][1] - self.saturationThreshold, px[i,j][2])
                elif px[i,j][2] >= px[i,j][1] and px[i,j][2] >= px[i,j][0]:
                    px[i,j] = (px[i,j][0] , px[i,j][1] , px[i,j][2] - self.saturationThreshold)
        self.functionUpdateImage()
    def filterBrightnessMore(self):
        x,y = self.image.size
        px = self.image.load()
        for i in range(x):
            for j in range(y):
                px[i,j] = px[i,j][0]+self.brightnessThreshold,px[i,j][1]+self.brightnessThreshold,px[i,j][2]+self.brightnessThreshold
        self.functionUpdateImage()
    def filterBrightnessLess(self):
        x,y = self.image.size
        px = self.image.load()
        for i in range(x):
            for j in range(y):
                px[i,j] = px[i,j][0]-self.brightnessThreshold,px[i,j][1]-self.brightnessThreshold,px[i,j][2]-self.brightnessThreshold
        self.functionUpdateImage()
    def filterContrastMore(self):
        x,y = self.image.size
        px = self.image.load()
        for i in range(x):
            for j in range(y):
                if (px[i,j][0]+px[i,j][1]+px[i,j][2])/3 <= 128:
                    px[i,j] = px[i,j][0]-self.contrastThreshold,px[i,j][1]-self.contrastThreshold,px[i,j][2]-self.contrastThreshold
                else:
                    px[i,j] = px[i,j][0]+self.contrastThreshold,px[i,j][1]+self.contrastThreshold,px[i,j][2]+self.contrastThreshold
        self.functionUpdateImage()
    def filterContrastLess(self):
        x,y = self.image.size
        px = self.image.load()
        for i in range(x):
            for j in range(y):
                if (px[i,j][0]+px[i,j][1]+px[i,j][2])/3 >= 128:
                    px[i,j] = px[i,j][0]-self.contrastThreshold,px[i,j][1]-self.contrastThreshold,px[i,j][2]-self.contrastThreshold
                else:
                    px[i,j] = px[i,j][0]+self.contrastThreshold,px[i,j][1]+self.contrastThreshold,px[i,j][2]+self.contrastThreshold
        self.functionUpdateImage()
    def filterTheo(self):
        x,y = self.image.size
        px = self.image.load()
        px1 = self.imageSaved.load()
        for i in range(51,x-21):
            for j in range(32,y-50):
                if px[i,j][2] >= 90 and px[i,j][1] < 200 and px[i,j][0] < 200:
                    px[i,j] = (223,0,37)
                elif px[i,j][0] > 120 and px[i,j][2] > 120 and px[i,j][1] < 200:
                    px[i,j] = (217,250,5)
                elif px[i,j][0] >= 80 and px[i,j][1] < 200 and px[i,j][2] < 200:
                    px[i,j] = (26,11,233)
        for i in range(365,x):
            for j in range(0,y-194):
                px[i,j] = px1[i,j]
     

        self.functionUpdateImage()
                # if px[i,j][2] >= 90 and px[i,j][1] < 200 and px[i,j][0] < 200:
                #     px[i,j] = (223,0,37)

                    #px[i,j] = (26,11,233)



    #Pinceau
    def brushPanel(self):
        #Création de l'instance brushWindow
        self.brushWindow = Brush(self.master)
    def brushEvent(self,event):
        #Incrémentation du compteur de click
        self.clickCount +=1
        print(self.brushWindow.Choix)

        #Pinceau en mode Couleur
        if self.brushWindow.Choix == 'Color' and self.clickCount%2 == 1 :
            self.stop = False
            self.brushDrawColor()
        if self.brushWindow.Choix == 'Color' and self.clickCount%2 == 0 :
            self.stop = True

        #Pinceau en mode luminosité plus
        if self.brushWindow.Choix == 'brightnessMore' and self.clickCount%2 == 1 :
            self.stop = False
            self.brushBrightnessMore()
        if self.brushWindow.Choix == 'brightnessMore' and self.clickCount%2 == 0 :
            self.stop = True

        #Pinceau en mode luminosité moins
        if self.brushWindow.Choix == 'brightnessLess' and self.clickCount%2 == 1 :
            self.stop = False
            self.brushBrightnessLess()
        if self.brushWindow.Choix == 'brightnessLess' and self.clickCount%2 == 0 :
            self.stop = True

        #Pinceau en mode Saturation plus
        if self.brushWindow.Choix == 'saturationMore' and self.clickCount%2 == 1 :
            self.stop = False
            self.brushSaturationMore()
        if self.brushWindow.Choix == 'saturationMore' and self.clickCount%2 == 0 :
            self.stop = True

        #Pinceau en mode Saturation moins
        if self.brushWindow.Choix == 'saturationLess' and self.clickCount%2 == 1 :
            self.stop = False
            self.brushSaturationLess()
        if self.brushWindow.Choix == 'saturationLess' and self.clickCount%2 == 0 :
            self.stop = True

        #Pinceau en mode Contraste plus
        if self.brushWindow.Choix == 'contrastMore' and self.clickCount%2 == 1 :
            self.stop = False
            self.brushContrastMore()
        if self.brushWindow.Choix == 'contrastMore' and self.clickCount%2 == 0 :
            self.stop = True

        #Pinceau en mode Contraste moins
        if self.brushWindow.Choix == 'contrastLess' and self.clickCount%2 == 1 :
            self.stop = False
            self.brushContrastLess()
        if self.brushWindow.Choix == 'contrastLess' and self.clickCount%2 == 0 :
            self.stop = True
    def brushDrawColor(self):
        x,y = self.image.size
        r,g,b = self.brushWindow.Color
        px = self.image.load()

        if self.x-self.radius >=0 and self.y-self.radius >=0 and self.x+self.radius <= x and self.y+self.radius <= y:
            for i in range(self.x-self.radius, self.x+self.radius):
                for j in range(self.y-self.radius,self.y+self.radius):
                    if ((i-self.x)**2)+((j-self.y)**2) <= self.radius**2:
                        px[i,j] = (r,g,b)
        elif self.x-self.radius >=0 and self.y-self.radius >=0 and self.x+self.radius <= x and self.y+self.radius > y:
            for i in range(self.x-self.radius, self.x+self.radius):
                for j in range(self.y-self.radius,y):
                    if ((i-self.x)**2)+((j-self.y)**2) <= self.radius**2:
                        px[i,j] = (r,g,b)
        elif self.x-self.radius >=0 and self.y-self.radius >=0 and self.x+self.radius > x and self.y+self.radius <= y:
            for i in range(self.x-self.radius, x):
                for j in range(self.y-self.radius,self.y+self.radius):
                    if ((i-self.x)**2)+((j-self.y)**2) <= self.radius**2:
                        px[i,j] = (r,g,b)
        elif self.x-self.radius >=0 and self.y-self.radius <0 and self.x+self.radius <= x and self.y+self.radius <= y:
            for i in range(self.x-self.radius, self.x+self.radius):
                for j in range(0,self.y+self.radius):
                    if ((i-self.x)**2)+((j-self.y)**2) <= self.radius**2:
                        px[i,j] = (r,g,b)
        elif self.x-self.radius <0 and self.y-self.radius >=0 and self.x+self.radius <= x and self.y+self.radius <= y:
            for i in range(0, self.x+self.radius):
                for j in range(self.y-self.radius,self.y+self.radius):
                    if ((i-self.x)**2)+((j-self.y)**2) <= self.radius**2:
                        px[i,j] = (r,g,b)

        self.functionUpdateImage()
        if self.stop == False:
           self.master.after(50,self.brushDrawColor)       
    def brushBrightnessMore(self):

        x,y = self.image.size
        px = self.image.load()
        
        if self.x-self.radius >=0 and self.y-self.radius >=0 and self.x+self.radius <= x and self.y+self.radius <= y:
            for i in range(self.x-self.radius, self.x+self.radius):
                for j in range(self.y-self.radius,self.y+self.radius):
                    px[i,j] = px[i,j][0]+self.brightnessThreshold,px[i,j][1]+self.brightnessThreshold,px[i,j][2]+self.brightnessThreshold
        elif self.x-self.radius >=0 and self.y-self.radius >=0 and self.x+self.radius <= x and self.y+self.radius > y:
            for i in range(self.x-self.radius, self.x+self.radius):
                for j in range(self.y-self.radius,y):
                    px[i,j] = px[i,j][0]+self.brightnessThreshold,px[i,j][1]+self.brightnessThreshold,px[i,j][2]+self.brightnessThreshold
        elif self.x-self.radius >=0 and self.y-self.radius >=0 and self.x+self.radius > x and self.y+self.radius <= y:
            for i in range(self.x-self.radius, x):
                for j in range(self.y-self.radius,self.y+self.radius):
                    px[i,j] = px[i,j][0]+self.brightnessThreshold,px[i,j][1]+self.brightnessThreshold,px[i,j][2]+self.brightnessThreshold
        elif self.x-self.radius >=0 and self.y-self.radius <0 and self.x+self.radius <= x and self.y+self.radius <= y:
            for i in range(self.x-self.radius, self.x+self.radius):
                for j in range(0,self.y+self.radius):
                    px[i,j] = px[i,j][0]+self.brightnessThreshold,px[i,j][1]+self.brightnessThreshold,px[i,j][2]+self.brightnessThreshold
        elif self.x-self.radius <0 and self.y-self.radius >=0 and self.x+self.radius <= x and self.y+self.radius <= y:
            for i in range(0, self.x+self.radius):
                for j in range(self.y-self.radius,self.y+self.radius):
                    px[i,j] = px[i,j][0]+self.brightnessThreshold,px[i,j][1]+self.brightnessThreshold,px[i,j][2]+self.brightnessThreshold
        
        self.functionUpdateImage()
        if self.stop == False:
           self.master.after(50,self.brushBrightnessMore)   
    ###A COMPLETER ###
    def brushBrightnessLess(self):

        pass   
    def brushContrastMore(self):

        pass    
    def brushContrastLess(self):

        pass    
    def brushSaturationMore(self):

        pass  
    def brushSaturationLess(self):

        pass  

        









#Programme principal
def main():
    root = Tk()
    root.title("Logiciel de traitement d'image")
    root.wm_state('zoomed')
    MainApplication(root)
    root.mainloop()
if __name__ == "__main__":
    main()
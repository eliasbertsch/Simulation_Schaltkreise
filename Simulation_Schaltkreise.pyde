from Schaltkreise import Serie, Parallel
from Bauteile import Lampe
mode = 1                                 #Standartmodus Hauptmenü (bei Start und durch Taste anwählbar)

def setup():
    size(1000, 1000)                       #Fenstergrösse          
    background(255, 255, 255)            #Hintergrundfarbe Weiss
    fill(0,0,0)
    textSize(20)                         #Schriftgrösse
    myFont = createFont("Georgia", 20);  #Schriftart
    textFont(myFont);

def draw():
    global mode
    strokeWeight(10)                     #Liniendicke
    if mode == 1:                        #wenn Modus =1
        background(255, 255, 255)        #Darstellungsfunktionen
        fill(0,0,0)

        text(u" Mit diesem Programm kannst du Schaltkreisschemas ausprobieren.\n \n Interessant wird es allerdings erst, wenn in den Schaltkreisen etwas schief geht.\n Mit den Tasten 4 und 5 kannst du ausprobieren was passiert, wenn eine der Leuchten beschädigt ist. \n Drücke um zurück in dieses Menü zu gelangen die Taste 1.", 20, 30)    #Benutzeranleitungen

        text(u"Drücke Taste 2 für die Serienschaltung.", 20, 290)
        text(u"Drücke Taste 3 für die Paralleschaltung.", 520, 290)
        text(u"Drücke Taste 4 für die beschädigte Serieschaltung.", 20, 650)
        text(u"Drücke Taste 5 für die beschädigte Paralellschaltung.", 520, 650)
        bild1 = loadImage("Serienschaltung.jpg")                                           #Bild laden
        image(bild1, 10, 300, 400, 300)                                                  #Bildeigenschaften
        bild2 = loadImage("Parallelschaltung.jpg")
        image(bild2, 510, 300, 400, 300)
        line (0, 200, 1000, 200)
        line (500, 200, 500, 1000)

    if mode == 2:   
        background(255, 255, 255)                                                          #Darstellungsfunktionen
        fill(0,0,0)
        text(u" Halte die Maus gedrückt, um dem Schaltkreis eine Stromquelle hinzuzufügen.", 50, 420)              #Benutzeranleitungen
        text(u" Drücke Taste 1, um zum Menu zurückzukehren. \n Drücke die Taste 2 um die Paralellschaltung auszuprobieren. \n Drücke die Taste 4 um die Serienschaltung mit einer beschädigten Leuchte auszuprobieren \n Drücke die Taste 5 um die Paralellschaltung mit einer beschädigten Leuchte auszuprobieren", 50, 460)                      #Serienschaltung durch Modus 2 mit Taste 2 anwählbar)
        Serie()
        
    if mode == 3:                                                                  #Parallelschaltung durch Modus 3 mit Taste 3 anwählbar)
        background(255, 255, 255)                                                  #Darstellungsfunktionen
        fill(0,0,0)
        text(u" Halte die Maus gedrückt, um dem Schaltkreis eine Stromquelle hinzuzufügen.", 50, 420)              #Benutzeranleitungen
        text(u" Drücke Taste 1, um zum Menu zurückzukehren. \n Drücke die Taste 2 um die Paralellschaltung auszuprobieren. \n Drücke die Taste 4 um die Serienschaltung mit einer beschädigten Leuchte auszuprobieren \n Drücke die Taste 5 um die Paralellschaltung mit einer beschädigten Leuchte auszuprobieren", 50, 460)                      #Serienschaltung durch Modus 2 mit Taste 2 anwählbar)
        Parallel()
        
    if mode == 4:
        background(255, 255, 255)                                                          #Darstellungsfunktionen
        fill(0,0,0)
        text(u" Nun ist die Lampe ganz rechts beschädigt (schwarz bedeutet kaputt),\n dies bedeutet für die Serienschaltung, dass der gesamte Stromkreis beschädigt ist. \n Wenn du die Maus gedrückt hältst, siehst du, dass trotz der Stromquelle keine Leuchte erhellt.", 50, 420)
        text(u" Drücke Taste 1, um zum Menu zurückzukehren. \n Drücke die Taste 2 um die Paralellschaltung auszuprobieren. \n Drücke die Taste 4 um die Serienschaltung mit einer beschädigten Leuchte auszuprobieren \n Drücke die Taste 5 um die Paralellschaltung mit einer beschädigten Leuchte auszuprobieren", 50, 540)                      #Serienschaltung durch Modus 2 mit Taste 2 anwählbar)
        Serie()
        fill(0,0,0)
        circle (600, 100, 100)
        fill (255, 255, 255)
        Lampe(200, 100)
        Lampe(400, 100)
        
    if mode == 5:
        background(255, 255, 255)                                                #Darstellungsfunktionen
        fill(0,0,0)
        text(u" Nun ist die Lampe ganz rechts beschädigt (schwarz bedeutet kaputt),\n dies bedeutet für die Parallelschaltung, dass die anderen Leuchten weiterscheinen. \n Wenn du die Maus gedrückt hältst, siehst du, dass die ganzen Leuchten immernoch erhellen.", 50, 420)
        text(u" Drücke Taste 1, um zum Menu zurückzukehren. \n Drücke die Taste 2 um die Paralellschaltung auszuprobieren. \n Drücke die Taste 4 um die Serienschaltung mit einer beschädigten Leuchte auszuprobieren \n Drücke die Taste 5 um die Paralellschaltung mit einer beschädigten Leuchte auszuprobieren", 50, 540)                      #Serienschaltung durch Modus 2 mit Taste 2 anwählbar)
        Parallel()
        fill(0,0,0)
        circle(700,190,100)
    
    if (keyPressed):                                    #Tastenfunktionen mit Zuweisung zu den entsprechenden Modi
        if (key == '1' or key == '+'):                  #Hauptmenü
            mode = 1
        if (key == '2' or key == '"' or key == '@'):    #Serienschaltung
            mode = 2
        if (key == '3' or key == '*' or key == '#' ):   #Parallelschaltung
            mode = 3
        if (key == '4' or key == 'Ç' or key == 'ç' ):
            mode = 4
        if (key== '5' or key =='%' or key == '['):
            mode= 5
        
        
        
    
    
    
    

    

    

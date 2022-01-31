from Schaltkreise import Serie
mode = 1                                 #Standartmodus Hauptmenü (bei Start und durch Taste anwählbar)

def setup():
    size(800, 600)                       #Fenstergrösse          
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
        line (0, 90, 800, 90)
        line (400, 90, 400, 600)
        text(u"Mit diesem Programm kannst du Schaltkreisschemas ausprobieren.", 20, 30)    #Benutzeranleitungen
        text(u"Drücke für dieses Menu die Taste 1.", 20, 60) 
        text(u"Drücke Taste 2 für die Serienschaltung.", 20, 140)
        text(u"Drücke Taste 3 für die Paralleschaltung.", 420, 140)
        bild1 = loadImage("Serienschaltung.jpg")                                           #Bild laden
        image(bild1, 10, 167, 375.5, 180)                                                  #Bildeigenschaften
        bild2 = loadImage("Parallelschaltung.jpg")
        image(bild2, 407, 190, 390, 159.5)
        

        
    if mode == 2:   
        background(255, 255, 255)                                                          #Darstellungsfunktionen
        fill(0,0,0)
        text(u"Drcke die Maus, um den Schaltkreis auszuprobieren.", 50, 420)              #Benutzeranleitungen
        text(u"Drcke Taste 1, um zum Menu zurckzukehren.", 50, 460)                                                                       #Serienschaltung durch Modus 2 mit Taste 2 anwählbar)
        Serie()
        
        
    if mode == 3:                                                                  #Parallelschaltung durch Modus 3 mit Taste 3 anwählbar)
        background(255, 255, 255)                                                  #Darstellungsfunktionen
        fill(0,0,0)
        text(u"Drücke die Maus, um den Schaltkreis auszuprobieren.", 50, 420)      #Benutzeranleitungen
        text(u"Drücke Taste 1, um zum Menu zurückzukehren.", 50, 460)
        Parallel()

    if (keyPressed):                                    #Tastenfunktionen mit Zuweisung zu den entsprechenden Modi
        if (key == '1' or key == '+'):                  #Hauptmenü
            mode = 1
        if (key == '2' or key == '"' or key == '@'):    #Serienschaltung
            mode = 2
        if (key == '3' or key == '*' or key == '#' ):   #Parallelschaltung
            mode = 3
        
        
        
        
    
    
    
    

    

    

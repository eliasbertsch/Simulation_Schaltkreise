
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
        

        
    if mode == 2:                                                                          #Serienschaltung durch Modus 2 mit Taste 2 anwählbar)
        background(255, 255, 255)                                                          #Darstellungsfunktionen
        fill(0,0,0)
        text(u"Drücke die Maus, um den Schaltkreis auszuprobieren.", 50, 420)              #Benutzeranleitungen
        text(u"Drücke Taste 1, um zum Menu zurückzukehren.", 50, 460)
        if mousePressed == True:                  #Interaktion: wenn Maus gedrückt
            fill(250, 255, 0)                     #Lampen werden gelb gefüllt, Bild eines geladenen Akkus erscheint        
            circle (200, 100, 100)
            circle (400, 100, 100)
            circle (600, 100, 100)
            bild1 = loadImage("Batterie_Voll.png")
            image(bild1, 270, 290, 60, 20)
           
        else:                                     #Zustand, wenn Maus nicht gedrückt ist
            fill(255,255,255)                     #Lampen werden weiss gefüllt, Bild eines entladenen Akkus erscheint
            circle (200, 100, 100)
            circle (400, 100, 100)
            circle (600, 100, 100)
            bild = loadImage("Batterie_Leer.png")
            image(bild, 270, 290, 60, 20)
        

    
        line (50, 100, 150, 100)
        circle (200, 100, 100)
        line(165, 65, 235, 135)
        line(165, 135, 235, 65)

        line (250, 100, 350, 100)
        circle (400, 100, 100)
        line(365, 65, 435, 135)
        line(365, 135, 435, 65)

        line(450, 100, 550, 100)
        circle(600, 100, 100)
        line (565, 65, 635, 135)
        line (565, 135, 635, 65)
    
        line (650, 100, 700, 100)
        line (700, 100, 700, 300)
        line (700, 300, 335, 300)
    
        line (265, 300, 50, 300)
        line (50, 300, 50, 100)
        
        
    if mode == 3:                                                                  #Parallelschaltung durch Modus 3 mit Taste 3 anwählbar)
        background(255, 255, 255)                                                  #Darstellungsfunktionen
        fill(0,0,0)
        text(u"Drücke die Maus, um den Schaltkreis auszuprobieren.", 50, 420)      #Benutzeranleitungen
        text(u"Drücke Taste 1, um zum Menu zurückzukehren", 50, 460)
        if mousePressed == True:                       #Interaktion: wenn Maus gedrückt
            fill(255, 255, 0)                          #Lampen werden gelb gefüllt, Bild eines geladenen Akkus erscheint 
            circle (300, 190, 100)
            circle (500, 190, 100)
            circle (700, 190, 100)
            bild1 = loadImage("Batterie_VollR.png")
            image(bild1, 40, 165, 20, 60)
        
        else:                                      #Zustand, wenn Maus nicht gedrückt ist
            fill(255,255,255)                      #Lampen werden weiss gefüllt, Bild eines entladenen Akkus erscheint
            circle (300, 190, 100)
            circle (500, 190, 100)
            circle (700, 190, 100)
        
            bild = loadImage("Batterie_LeerR.png")
            image(bild, 40, 165, 20, 60)
         
        strokeWeight(10)           #Liniendicke
    
        line(50, 100, 700, 100)    #Verbindungslinie oben horizontal
        line(50, 300, 700, 300)    #Verbindungslinie unten horizontal
    
        line (50, 100, 50, 160)    #Verbindungslinie vertikal S1
        line (50, 230, 50, 300)    #Verbindungslinie vertikal S1
    
        line (300, 100, 300, 300)   #Verbindungslinie vertikal 1
        circle (300, 190, 100)     #Lampe 1
        line(265, 155, 335, 225)   #Diagonalbalken
        line(265, 225, 335, 155)   #Diagonalbalken

        line (500, 100, 500, 300)  #Verbindungslinie vertikal 2
        circle (500, 190, 100)     #Lampe 2
        line(465, 155, 535, 225)   #Diagonalbalken
        line(465, 225, 535, 155)   #Diagonalbalken

        line(700, 100, 700, 300)   #Verbindungslinie vertikal 3
        circle(700, 190, 100)      #Lampe 3
        line (665, 155, 735, 225)  #Diagonalbalken
        line (665, 225, 735, 155)  #Diagonalbalken

    if (keyPressed):                                    #Tastenfunktionen mit Zuweisung zu den entsprechenden Modi
        if (key == '1' or key == '+'):                  #Hauptmenü
            mode = 1
        if (key == '2' or key == '"' or key == '@'):    #Serienschaltung
            mode = 2
        if (key == '3' or key == '*' or key == '#' ):   #Parallelschaltung
            mode = 3
        
        
        
        
    
    
    
    

    

    

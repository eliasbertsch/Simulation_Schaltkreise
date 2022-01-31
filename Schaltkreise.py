from Bauteile import Lampe

def Serie():
    if mousePressed == True:                  #Interaktion: wenn Maus gedrckt
        fill(250, 255, 0)                     #Lampen werden gelb gefllt, Bild eines geladenen Akkus erscheint        
        circle (200, 100, 100)
        circle (400, 100, 100)
        circle (600, 100, 100)
        bild1 = loadImage("Batterie_Voll.png")
        image(bild1, 270, 290, 60, 20)
           
    else:                                     #Zustand, wenn Maus nicht gedrckt ist
        fill(255,255,255)                     #Lampen werden weiss gefllt, Bild eines entladenen Akkus erscheint
        circle (200, 100, 100)
        circle (400, 100, 100)
        circle (600, 100, 100)
        bild = loadImage("Batterie_Leer.png")
        image(bild, 270, 290, 60, 20)

    for x in range(200,601,200):
        Lampe(x,100)

    line (50, 100, 150, 100)    #Balken oben horizontal Teil 2 (ganz links)        
    line (250, 100, 350, 100)   #Balken oben horizontal Teil 2 
    line (450, 100, 550, 100)   #Balken oben horizontal Teil 3 
    line (650, 100, 700, 100)   #Balken oben horizontal Teil 4 (ganz rechts)
    line (700, 100, 700, 300)   #Balken vertikal rechts
    line (50, 300, 50, 100)     #Balken vertikal links
    line (700, 300, 335, 300)   #Balken unten horizontal rechts
    line (265, 300, 50, 300)    #Balken unten horizontal links
    save("data/Serienschaltung.jpg")
    
def Parallel():
    if mousePressed == True:                     #Interaktion: wenn Maus gedrckt
        fill(255, 255, 0)                          #Lampen werden gelb gefllt, Bild eines geladenen Akkus erscheint 
        circle (300, 190, 100)
        circle (500, 190, 100)
        circle (700, 190, 100)
        bild1 = loadImage("Batterie_VollR.png")
        image(bild1, 40, 165, 20, 60)
        
    else:                                      #Zustand, wenn Maus nicht gedrckt ist
        fill(255,255,255)                      #Lampen werden weiss gefllt, Bild eines entladenen Akkus erscheint
        circle (300, 190, 100)
        circle (500, 190, 100)
        circle (700, 190, 100)
        
        bild = loadImage("Batterie_LeerR.png")
        image(bild, 40, 165, 20, 60)
    
    for x in range(300,701,200):
        Lampe(x,190)
           
    line(50, 100, 700, 100)    #Verbindungslinie oben horizontal
    line(50, 300, 700, 300)    #Verbindungslinie unten horizontal
    line (50, 100, 50, 160)    #Verbindungslinie vertikal S1
    line (50, 230, 50, 300)    #Verbindungslinie vertikal S1
    line (300, 100, 300, 300)  #Verbindungslinie vertikal 1
    line (500, 100, 500, 300)  #Verbindungslinie vertikal 2
    line(700, 100, 700, 300)   #Verbindungslinie vertikal 3
    save("data/Parallelschaltung.jpg")
    

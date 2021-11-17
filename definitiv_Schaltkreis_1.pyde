mode=1

text("Klicke die Maustaste um den Stromkreis zu schliessen", 20, 30)

    if mousePressed == True:
        fill(250, 128, 0)
        circle (200, 100, 100)
        circle (400, 100, 100)
        circle (600, 100, 100)
        bild1 = loadImage("Batterie_Voll.png")
        image(bild1, 270, 290, 60, 20)
        
    else:
        fill(255,255,255)
        circle (200, 100, 100)
        circle (400, 100, 100)
        circle (600, 100, 100)
        
        bild = loadImage("Batterie_Leer.png")
        image(bild, 270, 290, 60, 20)
         
    strokeWeight(10)
    
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
    line (700, 300, 330, 300)
    
    line (270, 300, 50, 300)
    line (50, 300, 50, 100)
    



    

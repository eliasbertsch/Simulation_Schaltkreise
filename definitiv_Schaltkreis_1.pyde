mode = 1

def setup():
    size(800, 600)
    background(255, 255, 255)
    fill(0,0,0)
def draw():
    global mode
    if mode == 1:
        background(255, 255, 255)
        fill(0,0,0)
        line (0, 60, 800, 60)
        line (400, 60, 400, 600)
        text("Mit diesem Programm kannst du Schaltkreisschemas ausprobieren.", 20, 20)
        text("Druecke fuer dieses Menu die Taste A", 20, 40) 
        text("Druecke B fuer den Schaltkreis 1", 20, 100)
        text("Druecke C fuer den Schaltkreis 2", 420, 100)
        
        
    if mode == 2:
        background(255, 255, 255)
        fill(0,0,0)
        text("Druecke die Maus um den Schaltkreis auszuprobieren", 20, 20)
        text("Druecke A um zum Menu zuruckzukehren", 20, 400)
        if mousePressed == True:
            fill(250, 255, 0)
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
        
        
    if mode == 3:
        background(255, 255, 255)
        fill(0,0,0)
        text("Druecke die Maus um den Schaltkreis auszuprobieren", 20, 20)
        text("Druecke A um zum Menu zuruckzukehren", 20, 40)
        if mousePressed == True:
            fill(255, 255, 0)
            circle(300, 300, 100)
            circle(500, 300, 100)
            circle (700, 300, 100)
            bild1 = loadImage("Batterie_Voll.png")
            image(bild1, 50, 500, 50, 20)
        else:
            fill(255, 255, 255)
            circle(300, 300, 100)
            circle(500, 300, 100)
            circle (700, 300, 100)
            bild = loadImage("Batterie_Leer.png")
            image(bild, 50, 500, 50, 20)
        

        strokeWeight(10)
    
        line (50, 100, 700, 100)
        line (700, 100, 700, 500)
        line (700, 500, 100, 500)
        line (50, 500, 50, 100)
        line (300, 100, 300, 500)
        line (500, 100, 500, 500)
        circle(300, 300, 100)
        circle(500, 300, 100)
        circle (700, 300, 100)
    
        line(265, 265, 335, 335)
        line(265, 335, 335, 265)
        line(465, 265, 535, 335)
        line(465, 335, 535, 265)
        line(665, 265, 735, 335)
        line(665, 335, 735, 265)

    if (keyPressed):
        if (key == 'b' or key == 'B'):
            mode = 2
        if (key == 'a' or key == 'A'):
            mode = 1
        if (key == 'c' or key =='C'):
            mode = 3
        
        
        
        
    
    
    
    

    

    

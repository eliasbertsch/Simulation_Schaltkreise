mode=1

def setup():
    size(800, 800)
    fill(0,0,0)
    #Beschreibungstext
    text("Mit diesem Programm kannst du Schaltkreisschemas ausprobieren.", 20, 20)
    text("Waehle das gewuenschte Schema, in dem du auf das gewuenschte Schema klickst.", 20, 40)
    
#Schaltkreiserstellung und Lampenleuchtfunktion mithilfe einfügen einer vollen Batterie
def draw():
    global mode
    background(255, 255, 255)
    if mode == 1:
        text("Startseite", 100, 100)
        if mouseX <10:
            mode = 2
    if mode == 2:
        text("Zweite Seite", 100, 100)



    
#Flächeneinteilung
#def draw():
    line (0, 60, 800, 60)
    line (400, 60, 400, 800)
    
    text("Mit diesem Programm kannst du Schaltkreisschemas ausprobieren.", 20, 20)

  

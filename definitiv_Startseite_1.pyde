def setup():
    size(800, 800)
    background(255, 255, 230)
    fill(0,0,0)
    text("Mit diesem Programm kannst du Schaltkreisschemas ausprobieren.", 20, 20)
    text("Waehle das gewuenschte Schema, in dem du auf das gewuenschte Schema klickst.", 20, 40)
    
#Flächeneinteilung
def draw():
    line (0, 60, 800, 60)
    line (400, 60, 400, 800)
    
    text("Mit diesem Programm kannst du Schaltkreisschemas ausprobieren.", 20, 20)

from definitiv_Schaltkreis_1 import Schaltkreis_1

from definitiv_Schaltkreis_2 import Schaltkreis_2
    
#Lampen leuchten bei Klick


   
#Lampen löschen bei Release Maustaste    

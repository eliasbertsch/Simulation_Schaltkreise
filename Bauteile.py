def Lampe(LX,LY):                                #Definition der Funktion Lampe, welche an einer beliebigen Kombination aus X- und Y- Werten eingebaut werden kann
    circle(LX,LY,100)                            #Kreis zeichnen mit Durchmesser 100 um den Punkt aus dem gewählten X- und Y- Wert 
    line(LX - 35,LY - 35, LX + 35, LY + 35)      #Diagonale Linie zeichnen abhängig von dem gewählten X- und Y- Wert
    line(LX - 35,LY + 35, LX + 35, LY - 35)      #Diagonale Linie zeichnen abhängig von dem gewählten X- und Y- Wert
    

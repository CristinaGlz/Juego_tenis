"""
>>> juegos()
partidas 3 
Partida1
Score [15-0]
Score [15-15]
Score [30-15]
Score [30-30]
Score [40-30]
Score [deude-deude]
Score [adv-deude]
Score [adv-deude]
Score [---deude]
Score [set-0]
Partida2
Score [15-0]
Score [15-15]
Score [30-15]
Score [30-30]
Score [40-30]
Score [deude-deude]
Score [adv-deude]
Score [adv-deude]
Score [---deude]
Score [set-0]
Partida3
Score [15-0]
Score [15-15]
Score [30-15]
Score [30-30]
Score [40-30]
Score [deude-deude]
Score [adv-deude]
Score [adv-deude]
Score [---deude]
Score [set-0]


"""
partidas=input("cuantas partidas 3 o 5")
def juegos():    
    print"partida{0}".format(partidas) 
    for i in range(partidas):
        print "Partida{0}".format((i+1))
        for j in range(5):
           mostrar_score(anotar(1,j)) 
           mostrar_score(anotar(2,j)) 

def anotar(jugador,otra):
    gano=0
    pierde=0 
    if jugador == 1 and otra==0:
        gano=15
        pierde=0        
    elif jugador == 2 and otra==0:
        gano=15
        pierde=15 
    if jugador == 1 and otra==1:
        gano=30
        pierde=15   
    elif jugador == 2 and otra ==1:
        gano=30
        pierde=30     
    if jugador == 1 and otra==2:
        gano=40
        pierde=30   
    elif jugador == 2 and otra ==2:
        gano="deude"
        pierde="deude"     
    if jugador == 1 and otra==3:
        gano="adv"
        pierde="deude"   
    elif jugador == 2 and otra ==3:
        gano="adv"
        pierde="deude"  
    if jugador == 1 and otra==4:
        gano="--"
        pierde="deude"   
    elif jugador == 2 and otra ==4:
        gano="set"
        pierde="0"          
    return "[{0}-{1}]".format(gano,pierde)

def mostrar_score(partida):
    print "Score {0}".format(partida)
    

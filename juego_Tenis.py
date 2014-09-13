"""
>>> mostrar_score(anotar(1,0))
Score [15-0]
>>> mostrar_score(anotar(2,0))
Score [15-15]
>>> mostrar_score(anotar(1,1))
Score [30-15]
>>> mostrar_score(anotar(2,1))
Score [30-30]
>>> mostrar_score(anotar(1,2))
Score [40-30]
>>> mostrar_score(anotar(2,2))
Score [deude-deude]
>>> mostrar_score(anotar(1,3))
Score [adv-deude]
>>> mostrar_score(anotar(2,3))
Score [adv-deude]
>>> mostrar_score(anotar(1,4))
Score [---deude]
>>> mostrar_score(anotar(2,4))
Score [set-0]
"""


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
    
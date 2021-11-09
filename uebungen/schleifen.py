#from uebungen.tools import is_prime
from uebungen.tools import 

#Beispiel aufsummieren von zahlen
#Geben wird eine zahl n, summiere alle zahlen bis n 
#Beispiel n =5, summe 1+2+3+4+5
def ausummieren(n:int):
    pass



#Zähle von 0 bis 100.
#Wenn die Zahl durch 3 teilbar ist, schreibe "Fizz"
#Wenn die Zahl durch 5 teilbar ist, schreibe "Buzz"
#Wenn die Zahl durch 3 und 5 teilbar ist schreibe "FizzBuzz"
def fiz_buzz():
    pass



#geben wird ein zahl(int) finde die nächst größere Primzahl
#Wenn du lust hast kann du gerne eine Funktion schreiben die prüft ob eine Zahl eine Primzahl ist
#Wenn du nicht weiterkommst benutze die funktion "is_prime()" diese liefert überprüft ob ein Zahl ein Primzahl ist und liefert True oder False zurück
def finde_die_naechste_primzahl(a:int):
    pass


#Definiere eine Zahl von 0-20
#Der User soll durch Eingabe raten können (insgesamt 3x mal), danach hat er verloren
def zahlen_raten(meineZahl:int):
    pass


#Der müde Frosch
#Ein Frosch will eine 2,00m breite Straße überqueren. Leiter schafft er es bei jedem Sprung nur halb soweit wie beim 
#vorherigen. Er beginnt mit einem Meter,der nächste ist 1/2m, danach 1/4 usw. Schafft er es über die Straße gib die Anzahl der Sprünge zurück.
#Wenn nicht -1
def der_muede_frosch()->int:
    sum = 0
    for i in range(0,63):
        sum+= 1/(1<< i)
        if sum > 2.5:
            return i
    return -1



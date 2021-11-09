#Liefere die gegebene Liste in umgekehrter Reihenfolge zurück
#Bonus: Versuch dies ohne die eingebaute .reversed() Funktion zu verwende
def andersum(liste:list)->int:
    pass

#Teile eine gegebenen Liste in drei gleich große Teile
#Und gib eine Liste mit diesen drei Teilbereichen zurück
#Tipps: len() liefert die Länge der Liste
#Eine Liste kann auch aus Listen bestehen
#[:]Teilebereichoperatoren brauchen Integer int()
def drittel(liste:list)->list:
    pass

#Gegeben ist eine Liste aus integer oder float berechne den Durchschnitt
def durchschnitt(liste:list)->float:
    pass


#Der Median der Messwerte einer Urliste ist derjenige Messwert, 
#der genau „in der Mitte“ steht, wenn man die Messwerte der Größe nach sortiert. 
#Beispielsweise ist für die ungeordnete Urliste 4, 1, 37, 2, 1 der Messwert 2 der Median, 
# der zentrale Wert in der geordneten Urliste 1, 1, 2, 4, 37. 
def median(liste:list)->float:
    pass


# [].sort(), sorted([]) liefern eine aufsteigen sortierte Liste, schreibe eine funktion die die Liste absteigend sortiert
def absteigend_sortiert(liste:list)->float:
    pass


#Gegeben ist eine Liste, entferne alle duplikate,
# so dass jedes Element nur einmal in der Liste vorkommt 
def entferne_duplikate(liste:list)->list:
    pass

#Stell dir eine Halsband mit Buchstaben vor, die Buchstaben können entlang des Bandes verschoben werden.
#Beispiel
#  -F-I-N-J-A-
#Würde man nun das F nehmen und einmal um die Kette herumschieben, käme -I-N-J-A-F-
#Schreibe ein Funktion die überprüft ob ein Halsband gleich dem anderen 
# d.h. nur durch verschieben kommt man auf die gleiche Liste
# -F-I-N-J-A- ist gleich -I-N-J-A-F-
# -F-I-N-J-A- ist gleich -N-J-A-F-I-
#jedoch -F-I-N-J-A- NICHT gleich -A-I-N-J-F- (hier wurde vertauscht)
# und -F-I-N-J-A- NICHT gleich -F-I-J-N-A- (hier wurde vertauscht)
# -F-I-N-J-A- kann durch folgende Liste dargestellt werden ["F","I","N","J","A"]
# Als Hilfestellung, schau dir nochmal die Kapitel über Schleifen und Listen and
#Aufgabe 1.1:
#Wieviele Varianten von -F-I-N-J-A- gibt es für Verschiebung?
#Aufgabe 1.2 Schreibe die Funktionen, dies soll True oder False zurückliefern
finja = ["F","I","N","J","A"]
def ist_gleich_finja(original:list,andere_liste:list)->bool:
    pass

#Beispielaufruf
ist_gleich_finja(finja,["F","N","I","J","A"])##Das sollte False zurückliefern

#Erweitere die Funktion nun das sie allgemeiner ist. Sie sollte für alle möglichen Listen aus Strings funktionieren
#Aufgabe 1.3
#Liefere False zurück wenn eine der Parameter (original, andere_liste)keine Liste ist. 
#Liefere False zurück wenn die Listen nicht gleich lang sind
#Überprüfe deine Funktionen mit einigen Kombinationen.






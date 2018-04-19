###############
Mitschriften EA
###############

Table Of Contents
#################

1. deterministisch in Polynomialzeit
2. inklusive Randomisierte Algorithmen
3. inlusice Hashing und String Matching

Orga
####

Schwerpunkt auf Verstaendniss, Beweise meist kurz gehalten.
Sprechstunde 11:30 - 12:30 OH14 R231

Passwort: EASS18

Klausur 
27.7.
25.9.

Einfuehrung
###########

Graphen (Kurzeinfuehrung)
=========================

G = (V,E) mit V Knoten, E Kanten(endlich)

* Multimenge mit mind. einem (v,w) mehrfach in E
* Kante (v,v) jeisst schleife

gerichtet G=(V,A) vs ungerichtet G(V,E)

Matching
========

Eine Kantenmenge heisst Matching wenn der Schnitt aller Kanten immer leer ist.

Bipartite Graphen
=================

Ein Graph ist Bipartit, wenn Die Knoten in G so aufgeteilt werden koennen, dass
alle Kanten zwischen zwei Knotenmengen verlaufen.

Als Resultat sind alle Kreise von gerader Laenge.

Greedy Heuristik
================

Findet Loesungen, aber keine optimalen.

Matchings sind mindestens halb so gross, wie das Optimale Matching

.. todo::
    38

| 

Matching
########

Maximale Matchings in Graphen
=============================

Sei G=(V,E) ein ungerihterter Graph. Eine Kantenmenge M aus E heisst Matching,
wenn:

.. math::
    e, e' \in M \land e = (u,v), e'=(u',v') \in M
        : \{u,v\} \cap \{u',v'\} = \emptyset

Mit anderen Worten: Jeder Knoten darf hoechstens einer Kante aus M inzident
sein.

Begrifflichkeiten
-----------------

* .. math::
    e \in M \{heisst Matching-Kante\}
* .. math::
    e \not \in M \{heisst freie Kante\}
* .. math::
    v \in V: \{v inzident zu Matching-Kante. heisst Matching Kante\}
* .. math::
    v \in V: \{v heisst inzident zu Matching-Kante. heisst freie Kante\}

Anwendungen von Matching
------------------------

Matching Probleme gehoeren der Klasse der Zuordnungsprobleme an.

Beispiele sind:

* Traveling Salesman Problem
* Chinese Postman Problem
* Maximaler Schnitt in planaren Graphen
* Steganographie (Verstecken geheimer Informationen in Bildern)

Matchings in bipartiten Graphen
===============================

Ein bipartiter Graph ist dadurch definiert, dass seine Knotenmenge in zwei
Untermengen unterteilt werden kann, sodass alle knoten in diesen enthalten sind
und dass nur Kanten zwischen Knoten aus eine Menge zur anderen verlaufen 
koennen.

Ferner folgt daraus, dass ein bipartiter Graph keine ungeraden Kreise enthaelt.

Algorithmen
-----------

Greedy
^^^^^^

.. math:: 
    M := \emptyset\\
    \text{While } \exists e \in E : M \cup e \text{ ist Matching}\\
    \text{do}\\
    M := M \cup e\\
    \text{end}\\
    \text{return }M

Der Nachteil dieses Algorithmus ist, dass er kein Maximales Matching berechnet.

Die Maechtigkeit des Matching laesst sich jedoch ueber folgende Gleichung
beschreiben.

.. math::
    |M_{greedy}| \lgeq |M_{opt}| / 2\\

 Das liegt daran, dass jede Kante eines optimalen Matchings zu einem zum greedy
 Matching inzidenten Knoten inzident ist. Sonst waere das optimale Matching kein
 solches.
 
Aus der Disjunkheit der Matchingkanten folgt dann 

.. math::
    |M_{opt}| \leq |V_{greedy}| = 2 |M_{greedy}|

Matchings im allgemeinen Graphen
================================

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

* 
  .. math::
    e \in M \{heisst Matching-Kante\}
* 
  .. math::
    e \not \in M \{heisst freie Kante\}
* 
  .. math::
    v \in V: \{v inzident zu Matching-Kante. heisst Matching Kante\}
* 
  .. math::
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

Einfacher Matchingalgorithmus
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Der einfache Matching Algorithmus in bipartiten Graphen bedient sich dem Lemma,
dass beweisst, dass fuer einen Graph, der zu einem Matching einen 
M-Verbessernden Pfad enthaelt, das Matching hinsichtlich seiner Maechtigkeit
je iteration um 1 verbessert werden kann.

|

Der M-verbessernde Pfad sei definiert, als ein alternierender Pfad (Matching,
nicht-Matching Kanten abwechselnd) ohne Kreise und mit einer nicht-Matching
Kante zu Beginn und Ende.

Bildet man nun den Symetrischen Schnitt zwischen Matching Kanten und dem Pfad,
so erhaelt man ein neues Matching, dass im Betrag um 1 maechtiger ist, als
das alte. Damit erhaelt man dann auch zu nach einer endlichen Anzahl von 
Iterationen ein optimales Matching.

|

1. initialisiere M leer
2. Berechne den naechsten M-verbessernden Pfad P
3. If (P nicht gefunden) Then return M
4. Else .. math::
    M = M \oplus P\\
5. weiter bei 2

|

Die (worst case) Laufzeit dieses Algorithmus laesst sich wie Folgt berechnen

.. math::

    e = |E|, n = |U \cupplus W|\\
    O(e*n) = O(n*n * n) = O(n^3)

M-alternierende Pfade berechnen/ finden
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Offensichtlich liegt die Schwierigkeit im finden im berechnen/ finden des 
M-alternierenden Pfades.

|

Eine Moeglichkeit dafuer ist es (virtuelle) Quell- und Senkenknoten anzufuegen
und den Graphen so zu richten, dass alle Pfade von der Quelle zur Senke fuehren.

Nun kann eine Breitensuche (nach dem kuerzesten, M-verbessernden Pfad) 
durchgefuehrt werden und der Pfad das Matching Verbessern.

Algorithmus von Hopfield und Karp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Die Graphtraversierung geht nur in O(e). Wir moechten nun aber goressere
Inkrementierungen, als 1 vornehmen. Dies ist etwa dann moeglich, wenn k>1
knotendiskunkte M-Verbessernde Pfade existieren und gleichzeitig "Addiert"
werden.

|

Die Mindestanzahl von Knotendisjunkten Matchings ist gegeben durch die Matchings
M, N mit:

.. math::
    (|N| > |M|) \Rightarrow |N| - |M| \text{ knotendisjunkte M-verbessernde
        Pfade existieren mindestens}\\

|

Wir differenzieren nun zwischen M-verbessernden Pfaden und kuerzesten 
M-verbessernden Pfaden. Sei P ein kuerzester M-verbessernder Pfad und P' ein 
M-verbessernder Pfad, mit .. math::
    P' \in M \oplus P

Dann gilt .. math::
    |P'| \geq |P| + |P \cap P'|


Matchings im allgemeinen Graphen
================================

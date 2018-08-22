################
Mitschriften EDV
################

Table of Contents
#################

* B_Fragen

Skript
######

wichtig:
pipeline 
(...)
farbmodelle
phong modell
shading
projektionsmodelle


Block B
=======

Der Block B beschaeftigt sich mit der Ueberfuehrung einer Szenenbschreibung in
eine bildliche Darstellung.

Daten koennen durch Berechnungen oder Messungen von der Datenquelle erfasst
werden.

Wir untescheiden ferner zwischen 2- und 3d Bilderzeugung

Pipilines
---------

Die Daten durchlaufen einer Pipeline. Diese ist fuer 2D und 3D Modelle
unterschiedlich.

.. _2d_pipe:
2D
^^

1. Transformation
2. Clipping
3. Verrasterung

.. _3d_pipe:
3D
^^

1. Transformation
    + Anwendung einer affinen Abbildung auf die Szene (Szene aus Dreiecken)
2. Beleuchtung
    + Anwendung einer bidirektionelen Shading-Funktion
3. Clipping und Projektion
    + (Clipping) Festlegung einer Sehpyramide, deren Inneres den Teil der Szene 
        definiert
    + Projektion der dreidimensionalen Szene auf eine zweidimensionale Bildebene
4. Sichtbarkeitstrennung
    + Entfernen nicht sichtbarer Teile der Szene
5. Verrasterung
    + Umwandeln der geometrischen Repraesentation in eine Rasterdarstellung

Farben
------

Ein Farbsystem besteht aus drei Grundtoenen, um alle vom Menschen wahrnehmbaren
Farben darzustellen.

CIE
^^^

Commission Internationale de l'Eclairage nutzt drei abstrakte primaerfarben 
X,Y,Z. Y entspricht der Lichtstaerke.

RGB
^^^

Additive darstellung von Farben. Gewichtete Summe von Rot, Gruen, Blau.
p

HSV
^^^
Hue Saturation Value
Hue in [0,360]
Saturation, Value in [0,1]

CMY
^^^

Subtraktives Modell von Cyan, Magenta, Yellow

|

2D Bilderzeugung
----------------

Wir durchlaufen wie bereits bekannt die 2d_pipe_.

Koordinatensysteme
^^^^^^^^^^^^^^^^^^

Wir deferenzieren zwischen lokalen und globalen Koordinatensystemen.

Jedes Objekt selbst hat ein lokales koordinatenssystem, jedes Objekt befindet
sich in einem Raum, dem globalen Koordinatensystem

Transformationen
^^^^^^^^^^^^^^^^

Wir koennen einen punkt anhand einer affinen Abbildung transformieren.
.. math::

    p' = A * p + t

Dabei ist A eine Matrix fuer Skalierung und Rotation, t ein vektor fuer die
Translation.

|

Spezialfaelle fuer die affine Abbildung sind:

Translation: 
.. math::
    E*p + t
Skalierung: 
.. math::
    ((a,0),(0,b)) * p
Rotation:
.. math::
    M_rot * p \\
    \text{wobei } M_rot \text{ die Rotationsmatrix ist.}
Spielgelung: 
.. math::
    E_{mod} * p\\
    \text{waagerecht: } e_{22} = -1\\
    \text{senkrecht: } e_{11} = -1\\
    \text{am Ursprung: } e_{22} = -1 = e_{11}\\
    
Scheerung:
.. math::
    ( E + ((0,s_1),(s_2,0)) ) * p

Transformationsmatrix
^^^^^^^^^^^^^^^^^^^^^

Um alle Transformationen in einer Matrix abdecken zu koennen benutzen wir eine
Transformationsmatrix.

.. math::
    \begin{array}
        a&b&c\\
        d&e&f\\
        g&h&i
    \end{array}

Clipping
^^^^^^^^
Clipping bezeichnet das Abschneiden von Teilen einer Szene die ausserhalb des
definierten Bildbereichs liegen.

* Streckenclipping
    + Algorithmus fuer Clipping
        1. Unterscheide zwischen Punkten, die links/rechts/unterhalb/oberhalb
            vom Bildbereich liegen.
            Entferne alle Kanten, die durch einfache Vergleiche eliminiert 
            werden koennen
        2. Wenn die Kante/ Linie von zwei Punkten durch den Bildbereich geht
            unterteile die Linie in mehrere Linien am Schnittpunkt mit dem 
            Bildbereich

|


Durchfuehrung von Schritt 1:

* Bitmaske fuer die 8 quadranten um den Bildbereich herum 
* Verundung muss 0000 sein

|

Durchfuehrung von Schritt 2:

* Veroderung muss 0000 sein, schnittpunkte dementsprechend waehlen

Verrasterung
^^^^^^^^^^^^

Das Problem, mit dem sich die Verrasterung auseinander setzt ist

Der Algorithmus fuer die Verrasterung betrachtet jeweils die x-punkte/pixel
und rundet die y-punkte/pixel auf den naechsten int/ganzzahligen Wert.

3D-Bilderzeugung
----------------

Transformation
^^^^^^^^^^^^^^

Die Transformationsmatrix bleibt generell gleich, nur das eine weitere
Reihe und spalte hinzugefuegt wird.

Beleuchtung
^^^^^^^^^^^

Das Beleuchtungsmodell von Phong besteht aus:

* Ambienten Anteil
    + sozusagen ein bias-lichtanteil/ indirekte Beleuchtung
* Diffuser Anteil
    + Reflexionen an Materialoberflaeche
    + Gleichmaessige Reflexion in alle Richtungen
* Glaenzender Anteil
    + Gerichtete Reflexion
    + Abhaengig von Betrachtungspunkt

|

Es existieren verschiedene shading Modelle

* Flat Shading
    + keien Interpolation, Mittelwerte Fuellen die Flaechen
* Gouraud Shading
    + Berechnet Farbwerte an den Eckpunkten der Polygone
    + lineare Interpolation, gleichmaessiger
* Phong Shading
    + Material und Normalattribute an den Eckpunkten
    + Interpolation der Normalvektoren der Eckpunkte ueber die Flaeche

|

Textur wird durch eine Rastermatrix vorgegeben

.. _B_Fragen:
Moegliche Pruefungsfragen
=========================

* Allgemeines zu Farben
    + Was sind die aus der VL vorgestellten Farbsysteme?
    + Warum koennen nicht alle fuer den Menschen sichtbaren Farben effizient
      dargestellt werden?
* Allgemeines zur Bilderzeugung
    + 2D/ 3D Pipeline- Ablauf zeichnen.
    + Was ist der Unterschied zwischen 2D/ 3D?
* Transformation
    + Welche Transformationsarten existieren?
    + Was benutzen wir in der VL als Mittel um alle Transformationsarten
      abzudecken?
* Clipping
    + wie wird Clipping durchgefuehrt/ welcher algorithmus?
* Verrasterung
    + wie wird Verrasterung durchgefuehrt/ welcher algorithmus?
* 3D Tansvormation vs 2D Transformation?
* Woraus besteht das vorgestellte 3D-Beleuchtungsmodell?
* Welche arten von Shading existieren, welche ist am besten und warum?


Block C
#######

Dimensionsreduktion
===================


Generell wird das Problem der Datenerfassung und Reduktion dieser Daten auf das
Wesentliche betrachtet. Dabei sollen Unterschiede der Daten immernoch 
ersichtlich bleiben.

|

Ueber die Dimensionsreduktion wird versucht die Richtungen in einem 
hochdimensionalen Raum zu bestimmen, in denne die wesentlichen Strukturen in den
Daten deutlich werden.

Lagrange-Multiplikation
-----------------------

Wir betrachten das Minimierungsproblem von

.. math::
    f(x,y) - \lambda * g(x,y) = \text{min}\\
    g(x,y) = 0\\
    \text{mit den partiellen Ableitungen:}\\
    f_x - \lambda g_x = 0\\
    f_y - \lambda g_y = 0

Dabei gilt f(x,y) = min unter Nebenbedingung g(x,y) = 0

Ausgleichsebenen
----------------

Wir suchen eine Hyperebene e* x = d (e:Koeffizienten Vektor, x:Punkt)

Dabei soll die Summe der quadratischen Abstaende der Punkte zur Hyperebene 
minimal sein.

Optmierungsproblem
------------------

f ist die Summe ueber alle Punmkte mal den Koeffizienten Vektor minus dem 
Schwerpunkt.

g ist der quadratische Betrag des Koeffizienten Vektor.

Hauptachsen
-----------

Projektion
----------

Dimensionsreduktion
-------------------

Singularwertzerlegung
---------------------

Beispiel
========

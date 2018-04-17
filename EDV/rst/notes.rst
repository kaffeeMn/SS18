################
Mitschriften EDV
################

Table of Contents
#################

Besonders Pruefungsrelevant
###########################

* Clipping algorithmus mit bitmasken


Orga
####

R-intro:    Di 24.04. 9-10, 10-11 OH16 R115
UBs:        ab Di 8.5. 9-12 OH16 R115

Skript
######

wichtig:
pipeline 
(...)
farbmodelle
phong modell
shading
projektionsmodelle


.. todo::
    bis Folie 82

Block B
=======

Der Block B beschaeftigt sich mit der Ueberfuehrung einer Szenenbschreibung in
eine bildliche Darstellung.

Daten koennen durch Berechnungen oder Messungen von der Datenquelle erfasst
werden.

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

p^- = A * p + t

Dabei ist A eine Matrix fuer Skalierung und Rotation, t ein vektor fuer die
Translation.

|

Spezialfaelle fuer die affine Abbildung sind:

Translation: E*p + t
Skalierung: ((a,0),(0,b)) * p
Rotation: M_rot * p 
Spielgelung: E_{negative 1 je nach Spiegelung} * p
Scheerung: ( E + ((0,s_1),(s_2,0)) ) * p

.. todo::
    homogene abbildung und erweiterung

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

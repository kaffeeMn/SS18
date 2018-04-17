################
Mitschriften EDV
################

Table of Contents
#################

Besonders Pruefungsrelevant
###########################

* Clipping algorithmus mit bitmasken



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

2D
^^

1. Transformation
2. Clipping
3. Verrasterung

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

Zwweidimensionale Bilderzeugung
-------------------------------

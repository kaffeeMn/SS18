################
Mitschriften EDV
################

Table of Contents
#################

* B_Fragen_
* C_Fragen_
* D_Fragen_
* E_Fragen_
* F_Fragen_
* G_Fragen_
* H_Fragen_
* I_Fragen_

Block B
#######

Der Block B beschaeftigt sich mit der Ueberfuehrung einer Szenenbschreibung in
eine bildliche Darstellung.

Daten koennen durch Berechnungen oder Messungen von der Datenquelle erfasst
werden.

Wir untescheiden ferner zwischen 2- und 3d Bilderzeugung

Pipilines
=========

Die Daten durchlaufen einer Pipeline. Diese ist fuer 2D und 3D Modelle
unterschiedlich.

.. _2d_pipe:

2D
--

1. Transformation
2. Clipping
3. Verrasterung

.. _3d_pipe:

3D
--

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
======

Ein Farbsystem besteht aus drei Grundtoenen, um alle vom Menschen wahrnehmbaren
Farben darzustellen.

CIE
---

Commission Internationale de l'Eclairage nutzt drei abstrakte primaerfarben 
X,Y,Z. Y entspricht der Lichtstaerke.

RGB
---

Additive darstellung von Farben. Gewichtete Summe von Rot, Gruen, Blau.
p

HSV
---

Hue Saturation Value

Hue in [0,360]

Saturation, Value in [0,1]

CMY
---

Subtraktives Modell von Cyan, Magenta, Yellow

|

2D Bilderzeugung
================

Wir durchlaufen wie bereits bekannt die 2d_pipe_.

Koordinatensysteme
------------------

Wir deferenzieren zwischen lokalen und globalen Koordinatensystemen.

Jedes Objekt selbst hat ein lokales koordinatenssystem, jedes Objekt befindet
sich in einem Raum, dem globalen Koordinatensystem

Transformationen
----------------

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
---------------------

Um alle Transformationen in einer Matrix abdecken zu koennen benutzen wir eine
Transformationsmatrix.

.. math::
    \begin{array}
        a&b&c\\
        d&e&f\\
        g&h&i
    \end{array}

Clipping
--------

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
------------

Das Problem, mit dem sich die Verrasterung auseinander setzt ist

Der Algorithmus fuer die Verrasterung betrachtet jeweils die x-punkte/pixel
und rundet die y-punkte/pixel auf den naechsten int/ganzzahligen Wert.

3D-Bilderzeugung
================

Transformation
--------------

Die Transformationsmatrix bleibt generell gleich, nur das eine weitere
Reihe und spalte hinzugefuegt wird.

Beleuchtung
-----------

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

Projektion
----------

* Parrallelprojektion
    + eine Bildebene wird durch einen Bildursprung o und zwei koordinaten u, v 
      definiert
    + Die Parrallelprojektion ist dann bezueglich einer Richtung w parralle
      Projektion der Richtung w auf die Ebene
* perspetivische Projektion
    + zuvor wurden alle Punkte eines Objekts bezueglich einer Richtung w parrallel
      auf die Bildebene projeziert
    + nun wird von einem Augenpunkt aus auf die Ebene Projeziert

Sichtbarkeitsberechnung
-----------------------

* Szenenbasiert
    + Painters Algorithmus/ Binary Space Partitioning
    + erst Sichtbarkeitsberechnung, dann Verrasterung
* Rasterbasiert
    + Tiefenpunktverfahren / Scan-Line / Bereichsunterteilungsverfahren
    + erst Verrasterung, dann Sichtbarkeitsberechnung

.. _B_Fragen:

Moegliche Pruefungsfragen B
===========================

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
* Welche Projektionsverfahren existieren, was ist der fundamentale Unterschied?
* Welche herangehensweisen existieren zur Sichtbarkeitsberechnung?


Block C
#######

Dimensionsreduktion
===================

Hauptachsentransformation
=========================


Generell wird das Problem der Datenerfassung und Reduktion dieser Daten auf das
Wesentliche betrachtet. Dabei sollen Unterschiede der Daten immernoch 
ersichtlich bleiben.

|

Ueber die Dimensionsreduktion wird versucht die Richtungen in einem 
hochdimensionalen Raum zu bestimmen, in denne die wesentlichen Strukturen in den
Daten deutlich werden.

Lagrange-Multiplikatoren
------------------------

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
^^^^^^^^^^^^^^^^^^

f ist die Summe ueber alle Punmkte mal den Koeffizienten Vektor minus dem 
Schwerpunkt.

g ist der quadratische Betrag des Koeffizienten Vektor.

.. math::

    \text{min } f(\ldots) = \Sigma^n_{i=1} (e * a_i - d)^2\\
    \text{, wobei } g(\ldots) = ||e||_2^2 = 1

Dieses Problem kann durch Lagrange Multiplikatoren geloesst werden

Erkenntniss
-----------

Damit eine Hyperebene den quadratischen Abstand zu allen Punkten minimiert, 
muss sie durch den Schwerpunkt dieser Punkte gehen.

Dadurch erhalten wir eine Vereinfacherung des Problems. So koennen wir die 
gegebenen Punkte in den Schwerpunkt verschieben

Dadurch erhalten wir ein neues Verfahren:

1. Verschieben der Punkte, sodass der Schwerpunkt im Ursprung liegt
2. Loesen des Problem fuer den Spezialfall, das die Ausgleichsebene durch den
   Ursprung geht
3. Verschiebe die gefundene Loesung in den Urspruenglichen Schwerpunkt

Kohonenkarten
=============

Eine Kohonenkarte definiert eine Abbildung eines d-dimensionalen Raums auf 
einen k-dimensionalen.
Dabei sollen nachbarschaften moeglichst gut erhalten bleiben.

|

Im Bereich der Datenvisualisierung wird dabei auf k = 2 oder k = 3 reduziert.

Aufbau
------

Die Kohonenkarte besteht aus einem n x m Gitter aus Neuronen. Dabei ist jedem
Neuron ein d-dimensionaler Punkt zugeordnet.

Anlernen
--------

Initialisiert wird die Kohonenkarte durch das zufaellige Zuordnen der 
d-dimensionalen Punkte and die Neuronen.

Die Kohonenkarte wird durch zufaellig gewaehlte Anlerndatenpunkte aus einer
gegebenen Punktmenge angelernt.

Quantisierung
=============

Vektorquantisierung
-------------------

k-Vektorquantisierung
^^^^^^^^^^^^^^^^^^^^^

Auffinden von k Punkten, deren raeumliche Verteiliung denen der Gegebenen
Punkte entspricht.

Exakt k Punkte/ Codewords.

Vektorquantisierung
^^^^^^^^^^^^^^^^^^^

Auffinden von Punkten q, sodass eine disjunkte Zuordnung von maximal p raeumlich
benachbarten Punkten aus der gegebenen Punktmenge zu jedem q existiert.

Unbestimmte Anzahl von Punkten/ Codewords mit je maximal p zugeordneten Punkten.

Aufteilung
^^^^^^^^^^

Eine AUfteilung kann durch Voronoi-Regionen erfolgen

Hyper-Octree-Vektorquantisierung
--------------------------------

Das Bild wird in Quadranten unterteilt. Jeder Quadrant Kann in 4 weitere
Quadranten unterteilt werden, die Kinder des Quadranten werden.
Quadranten werden solange aufgeteilt, bis sie weniger, als p Punkte enthalten.

Median-Schnitt-Vektorquantisierung
----------------------------------

Ein Baum mit maximal 2 Nachfolgern an jedem Knoten.
Aufteilung erfolgt wie beim Hyper-Octree, **ABER** der Schnitt erfolgt im 
Median.

Durch den Median_Schnitt wird eine dichteangepasste Reduktion der gegbenen 
Punktmenge erzielt.

Clustering
==========

Clustering Verfahren sind:

* Partionierende Verfahren
    + Paramter: Anzahl k der CLuster, Distanzfunktion
    + sucht ein flaches Clustering in k Cluster mit minimalen Kosten
* Hierachische Verfahren
    + Paramter: Distanzfunktion fuer Punkte und Cluster
    + bestimmt ein Hierarchie von Clustern
    + mischt jeweils die aehnlichsten CLuster
* Dichtebasierte Verfahren
    + Parameter: minimale Dichte in einem Cluster, Distanzfunktion
    + erweitert Punkte m ohre Nachbarn, bis die Dichte gross genug ist
* Andere
    + Fuzzy, Graph-theoretisch, neuronale Netze

k-Mittelwert-Clustering
-----------------------

Man waehlt zufaellig k Clustermittelpunkte

Fortan wird  fuer alle Objekte:

+ der Abstand jedes Objekts zu jedem Clustermittelpunkt berechnet
+ Jedes Objekt seinem Clustermittelpunkt zugewiesen

Bis sich keine Objektzuordnung mehr aendert, ansonsten wird das Clusterzentrum 
neu berechnet

|

    * Das k-Mittelwert-Clustering kann auch als Verfahren zur 
      k-Vektirquantisierung aufgefasst werden
    * Die resultierenden Cluster koennen stark von der Wahl der initialen 
      Centroide abhaengen
    * Anzahl von Clustern kann auch kleiner als k sein

Moeglichkeiten zur Verbesserung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* mehrere Durchlaeufe mit verschiedenen Starkonfigurationen
* abweichende Masse zur Abstands und Centoidbestimmung
* initiale Centroide sollten moeglichst weit voneinander entfernt sein

.. TODO

Hierarchisches CLustering
-------------------------

Dichtebasiertes Clustering
--------------------------

.. _C_Fragen:

Moegliche Pruefungsfragen C
===========================

* Aufbau einer Kohonenkarte?
* Wie wird eine Kohonenkarte angelernt?
* Warum lohnt es sich eine Kohonenkarte nicht rein randomisiert zu 
  initialisieren
* Worin liegt der Unterschied in der Herangehensweise von Vektorquantisierung
  und k-Vektorquantisierung
* Woraus bildet sich die Voronoi-Region?
* Was ist der Unterschied zwischen Hyper-Octree und Median-Schnitt?
    + Was ist ein Vorteil von Median-Schnitt gegenueber Hyper-Octree
* Wie funktioniert k-Mittelwert-Clustering
* Welche Abstandsmasse existieren im hierarchischen Clustering?
    + wozu werdenn diese benoetigt?
* Was ist eine :math:`\varepsilon`-Umgebung im Kontext des dichtebasierten
  Clustering?
* Nenne je ein Beispiel, indem dichtebasiertes Clustering besonders gut und
  eines, in dem es besonders schlecht Funktioniert


Block D
#######

Graphentheorie
==============

Hypergraph
----------

Bei einem Hypergraph G = (V,E) ist jedes Element von E eine nicht leere
Teilmenge von V ist.

Jede Kante kann also mehrere Anfangs und Endknoten haben.

Zeichenstrategien fuer Graphen
==============================

Es wurden 4 Ansaetze zum Zeichnen von Graphen vorgestellt:

1. Topologie-Form-Metrik
2. Hierarchisch
3. Sichtbarkeit
4. Verfeinerung

Topologie-Form-Metrik
---------------------

Topologie
^^^^^^^^^

Zwei orthogonle Zeichnungen haben gleiche Topologie, wenn sie durch stetige
Deformation ohne VErtauschen bon Facetten ineinander ueberprueft werden koennen

Dazu benutzen wir Planarisierung

* ermitteln des maximalen planaren Untergraphens
* Verbleibende Kanten einfuegen mit moeglichst wenig ueberschneidungen
* Dummy-Knoten an verbleibenden Uebrschneidungen einfuegen

Form
^^^^

Zwei orthogonale Zeichnungen haben gleiche Form, wenn sie:

1. gleiche Topologie haben
2. eine Zeichnung aus der anderen nur durch Laengenaenderungen der 
   Liniensegmente hervorgeht

Dazu benutzen wir Orthogonalisierung

* Knoten ohne Koordinaten
* alle Kanfel sind Winkellisten, zur Festlegung ihrer Knicke
* Das Ziel ist es die Anzahl von Knicken zu minimieren

Metrik
^^^^^^

Zwei othogonale Zeichnungen haben gleiche Metrik, wenn sie:

1. kongruent, bzw. durch Verschieben und Drehen ineinander ueberfuehrt werden
   koennen 

Dazu benutzen wir Kompaktifizierung

* minimiert die Flaeche des Graphen und legt die Kantenknicke fest

Hierachischer Ansatz
--------------------

1. Schichtungsschritt
    * verwandelt einen DAG in einen geschichteten Digraph
        + alle Knoten werden einer Schicht unf alle adjazenten Knoten einer
          Folgeschicht zugeordnet
    * Dummyknoten werden Angefuegt, damit Kanten ueber mehr als eine Schicht
      laufen koennen
2. Schnittreduzierung
    * Minimieren der Anzahl von Kantenschnitten
3. Festlegen der x-Koordinaten
    * ersetze Dummy-Knoten durch Knicke

(Di-)Graphen enthalten Zyklen, dies erschwert das algorithmische Zeichnen des
Graphens.

Wir verwenden den folgenden Ansatz:
1. Entfernen von Zyklen
    * die Richtung einiger Kanten wird invertiert um den Graph azyklisch zu
      machen
    * (greedy Algorithmus fuer minimale Rueckwaertskanten)
2. Hierarchischer Ansatz
3. Kanten wieder umrichten   

Sichtbarkeitsansatz
-------------------

1. Planarisierung, wie bei Topologie-Form-Metrik-Ansatz
2. Sichtbarkeitsschritt
    * jedem Knoten wird ein horizontales Segment zugeordnet
    * jeder Kante wird ein vertikales Segment zugeordnet
        + Kantensegmente haben Anfang und Ende in Knotensegmenten
        + Kantensegmente schneiden einander nicht
3. Ersetzungsschritt
    * ersetzt jedes horizontale Segment durch einen Punkt
    * ersetzt jedes vertikale Segment durch eine Polylinie

Verfeinerungsansatz
-------------------

1. Planarisierung, wie bei Topologie-Form-Metrik-Ansatz
2. Verfeinerung
    * Alle Facetten haben drei Kanten (Triangulierung)
    * Qualitaet des Zeichnens maximaler Graphen haengt in der Regel vom 
      Knotengrad ab
    * Minimierung des maximalen Knotengrades
3. Triangulierungszeichnung
    * "Auslegen" aller Dreiecke
    * entfernen von Dummy-Kanten/Knoten

Schichtenweises Zeichnen allg. gerichteter Graphen
==================================================

Beim Schichtweisen Zeichnen von allgemeinen gerichteten Graphen werden Knoten
auf Schichten angeordnet

Allgorithmus von Sugiyama
-------------------------

1. Entfernen von Zyklen
2. Schichtzuordnung
    + y-Koordinaten der Knoten
3. Kreuzungsreduktion
    + innerhalb der Schichten werden die Knoten so umgeordnet, dass die Anzahl
      von Kreuzungen reduziert ist
4. waagerechte Koordinatenzusweisung
    + x-Koordinaten der Knoten
5. Wiederherstellung der Zyklen

.. TODO wichtig!!!!!!!!!!!

(Binaere) Baeume
================

Einfacher Algorithmus zum Zeichnen
----------------------------------

wir definieren die Funktionen

.. math::
    x : V \rightarrow \mathbb{N}\\
    x(v) = \text{Index von v im Inorder Durchlauf}\\
    y : V \rightarrow \mathbb{N}\\
    y(v) = \text{Abstand von v zur Wurzel}\\

Ueber diese Funktionen erhalten wir die Koordinaten der Knoten

Aestetikkriterien fuer Binaerbaeume
-----------------------------------

1. SchichtenZeichnung, die sich am Abstand zur Wurzel orientiert
2. Linker Kindknoten links und rechter Kindknoten rechts
3. ElternKnoten ist zntriert ueber seinen Kindern
4. Zwei Isomorphe Unterbaeume werden gleich gezeichnet
5. Ein Baum und sein Spiegelbild werden spiegelbildlich gezeichnet

Algorithmus von Reingold und Tilford
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Rekursiv:

* Wenn der Baum nur einen Knoten enthaelt wird dieser gezeichnet
* Sonst:
    1. Wende den Algorithmus auf den linken und den rechten Unterbaum an
    2. Wenn es zwei Kinder gibt, dann:
        + Platziere die beiden erhaltenen Zeichnungen der Unterbaeume 
          in waagerechtem Abstand 2
        + Platziere die Wurzel des Baums eine Stufer darueber und in der 
          Mitte zwischen den Kindern
    3. Sonst:
        + platziere die Wurzel in waagerechtem Abstand 1 vom Kind

|

Erweiterung

* Wenn der Baum nur einen Knoten enthaelt wird dieser gezeichnet
* Sonst:
    1. Wende den Algorithmus auf den linken und den rechten Unterbaum an
    2. Wenn es zwei Kinder gibt, dann:
        + Platziere die beiden erhaltenen Zeichnungen der Unterbaeume 
          in waagerechtem Abstand **1**
        + Platziere die Wurzel des Baums eine Stufer darueber und in der 
          Mitte zwischen den Kindern
        + **falls der Abstand ungerade ist wird der rechte Unterbaum um 1 nach
          rechts geschoben**
    3. Sonst:
        + platziere die Wurzel in waagerechtem Abstand 1 vom Kind

Horizontal-Vertikal Zeichnen
============================

Rekursiv:

* Wenn der Baum nur einen Knoten hat, so wird dieser gezeichnet
* Sonst:
    1. Wende den Algorithmus auf den linken un rechten Unterbaum an
    2. Zeichne den Teilbaum mit der groesseren Anzahl Knoten rechts und den
       Teilbaum mit der kleineren Anzahl KNoten unterhablb der Wurzel

Breite: O(n)

Hoehe: O(log(n))

Zeichnen durch rekurives drehen
===============================

.. math::
    n(G) = |V|\\
    l(v) = \text{linkes Kind}\\
    r(v) = \text{rechtes Kind}\\


1. Fuer jeden Knoten u:
    * vertausche Kinder so, dass n(l(u)) <= n(r(u))
2. Finde den ersten Knoten v, auf dem an weitesten rechts verlaufenden Weg, fuer
   den gilt:
    * :math:`n(r(v)) \leq n - (n log(n))^{1/2} < n(v)`
3. Zeichne die linken Unterbaeume auf dem Weg von der Wurzel nach v mit 
   dem Algorithmus zum horizontal-vertikal Zeichnen
4. Zeichne die Unterbaeume von v rekursiv

Vereinfachen von Polygonzuegen
==============================

min-# Version
-------------

1. Konstruiere einen Graphen G(P,:math:`\varepsilon`), 
   der genau dann eine gerichte Kante
   :math:`p_i, p_j, i<j` enthaelt, wenn die Abweichung der Strecke zwischen
   den Knoten von allen dazwischen liegenden Knoten kleiner als ein Wert
   :math:`\varepsilon` ist.
2. berechen den kuerzesten Weg zwischen dem ersten und letzem Knoten des
   Polygonzugs und geben diesen aus

Fehlermasse
-----------

Messen der Abweichungen zwischen einer Strecke :math:`p_i, p_j`

* Punkt-Steckenabstand
    + maximaler Abstand zwischen einer Strecke und alle dazwischen liegenden
      Punkten
* Punkt Geradenabstand
    + maximale Abstande zwischen der Geraden und allen dazwischen liegenden 
      Punkten
* streckenausgerichtetes Huellenrechteck
    + die Haelfte der Laenge der zur Strecke senkrechten Kanten des
      Rechtecks, das laengs der Strecke ausgrichtet ist
* minimales Huellenrechteck
    + die Haelfte der Laenge der kuerzesten Kante des Rechtecks mit kleinster
      minimaler KAntenlaenge, dass die zwischenliegenden Punkte mit enthaelt

min-e Version
-------------

1. Konstruiere gewichteten gerichteten Graph G(P), der alle gerichtete Kanten 
   enthaelt, welche die maximalen Abweichung der dazwischen liegenden Punkte als
   gewicht haben
2. Finde durch binaere Suche ueber alle auftretenden Gewichte ein minimales
   Gewicht e, sodass ein kuerzester Weg in G(P,e) existiert, der hoechstens
   m Knoten

Douglas Peucker Algorithmus
---------------------------

* Ein Poligonzug P' besteht initial aus dem ersten und letztem Punkt des
  Polygonzugs
* Es wird der Maximale Abstand aller Punkte zur Strecke ausgerechnet
    + Ist dieser groesser als ein vordefiniertes :math:`\varepsilon`
      so wird dieser Punkt in die Strecke mit aufgenommen
      und der Algorithmus links und recht von diesem Punkt ausgefuehrt
    + Sonst terminiert die Rekursion

.. _D_Fragen:

Moegliche Pruefungsfragen D
===========================

* Was ist ein Hypergraph?
* wozu dient Planarisierung und in welchen Algorithmen wird Planarisierung
  benutzt?
    + warum koennen manche Algorithmen auf Planarisierung verzichten?
* erklaere den Algorithmus von Sugiyama
* Weclche Aestethikkriterien werden an das Zeichnen von Baeumen gestellt?
* Was ist anders bei der erweiterten Variante von Reingold/ Tilford?
    + wellcher Nutzen wird daraus gewonnen?
* Nenne 2 weitere Varianten um Graphen moeglichst pltzsparend zu Zeichnen?
    + Was wurde in der VL gesagt, wo das angewendet wird?
* Was ist der Unterschied der min-# und der min-e Variante?
* Wie verwendet Douglas-Peucker Fehlermasse?

BLock E
#######

.. _E_Fragen:

Moegliche Pruefungsfragen E
===========================

* Welche arten von Gittern gibt es?
    + Wozu dienen die Gitter
* Was bedeutet :math:`\alpha`-exponiert?
* Was passiert bei :math:`\alpha = 0`?
* Was ist bei einem Simplex Zellkomplex nicht erlaubt?
* Was sind bekannte Triangulierungsmethoden?
    + Was ist besonders an der Delaunay Triangulierung?
        - Was sind die Eigenschaften einer Delaunay Triangulierung?
        - Was kann man hinsichtlich ener Delaunay Triangulierung sagen
          wenn alle PUnkte aus einem Voronoi-Diagramm kommen?
* Was kann nach dem berechnen eine Trennflaeche fuer Volxelobjekte gemacht
  werden, um das Ergebnis "geschmeidiger"/ besser zu machen?
* Ist die Flaechentrennunf fuer Voxelobjekte immer eindeutig?


BLock F
#######

.. _F_Fragen:

Moegliche Pruefungsfragen F
===========================

* Wie funktioniert das Prozessmodell der Visualisierung?
* Was ist eine Nominal/ Ordinal/ Intervall/ Verhaeltnisskala
* Welche Gliederungsstufen der Farb-Muster-Variablen existieren?
    + Welche dieser Stufen treffen auf Groesse/ Helligkeit/ Muster/ Farbe
      / Richtung und Form zu?
* Wie koennen Merkmale Klassifiziert werden?
* Wie Funktioniert ein Box-Whiskers-Plot?
    + Welche Variationen des Box-Whisker-Plots wurden vorgestellt?

BLock G
#######

.. _G_Fragen:

Moegliche Pruefungsfragen G
===========================

* ?

BLock H
#######

.. _H_Fragen:

Moegliche Pruefungsfragen H
===========================

* ?

BLock I
#######

.. _I_Fragen:

Moegliche Pruefungsfragen I
===========================

* ?

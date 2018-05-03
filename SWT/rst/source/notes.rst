.. todo::
    ...
################
SWT Mitschriften
################

Table Of Contents
#################

Skript
#######

Orga
====

|

Einfuehrung
===========

Ueberblick
----------

SWT umfasst den Teilbereich der Infortmatik, der sich mit:

Planung, Konstruktion, Erstllung, Ueberpruefung, Einfuehrung, Betrieb und
Wartung

beschaeftigt.

Zielsetzung
^^^^^^^^^^^

Anwendungsbereich und -umfeld sind Faktoren fuer die Funktionalitaet einer
Software

Die Nachhaltigkeit einer Software wird sichergestellt, indem eben diese Faktoren
in die Analyse einbezogen werden.

Die Qualitaet wird aus verschiedenen Perspktiven wahrgenommen:
* andere Gewichtung der Merkmale
* andere Moegliche Auspraegungen der Merkmale
* andere Masse zum Beschreiben und Pruefen der Merkmale

Perspektiven sind:
Benutzung, Entwicklung, Administration, Betrieb, Beschaffung, etc.

Ideen der Objektorientierten Softwaregestaltung
------------------------------------------------

Die Arbeitsweise objektorientierter Systeme orientiert sich and der realen Welt.

Bei der Zusammenarbiet von Enitaeten (bzw. Objekten) existieren Regeln, bzw.
objektorientierte Prinzipien:

* Kapselung
    + Jedes Objekt grenzt sich ab
* Lokalitaet
    + Daten und zugehoerige Handlungen sind in einem Objekt zusammen gefasst
* Geheimhaltung
    + Jedes Objekt stellt nach aussen nur notwendige Informationen bereit
* Autonomie
    + Jedes Objekt entscheidet selbt, ueber die von ihm ausgefuehrten Handlungen

Objektorientierte Konzepte in Java
-----------------------------------

Java Bietet sich fuer Objektorientierte Softwareentwicklung an, da es bereits
Classes, Interfaces etc. bereitstellt.

|

UML Klassen- und Paketdiagramme
===============================

* Sammlung graphischer Notationen.
* Jede Notation ist ein Diagramm/ Modell
* Die Notation soll Kommuniaktion unter Entwicklern erleichtern

Zu den Pfeilen:

* gestirchelt: braucht Klasse/ Paket/ Objekt auf das es zeigt
* durchgestrichen mit weissem Kopf: erbt von dem Objekt/ Klasse auf das es zeigt

Paketdiagramme
--------------

Ein Paketdiagramm schafft eine Darstellung auf einer Abstraktionsebene, die es
in JAVA nicht gibt. 

Ein Paketdiagramm enthaelt:
* die Pakete eines Projekts
* die Abhaengigkeit zwischen den Paketen
* (zuordnung von Klassen zu den Paketen)
* (Abhaengigkeit zwischen Klassen)

* gestrichelte Pfeile simbolisieren die nutzung von pakages, classes
  moegliche Stereotypen sind
    + '<<import>>'
    + '<<use>>'
    + '<<bind>>'
        - oft mit implementierungen von generischen KLassen
* durchgezogene Pfeile simbolisieren direkten Zugriff

Klassendiagramme
----------------

Ein Klassendiagramm zeigt:
* Klassen eines Pakets
* Deie Beziehung der Klassen zueinander
* (Bestandteile einzelner Klassen)

Ein Klassendiagramm ermoeglicht es:
* implementierungen zu visualisieren
* Vorgaben fuer
    + Umsetzung in eine Implementierung zu liefern
    + Planung der Implementierung zu liefern
* Daren Operationen und Abhaengigkeiten in objektorientierter Form zu
    visualisieren

Typparameter generischer Klassen werden in einer gestrichelten Box oben rechts
dargestellt.

=========== ===============================
Character   Simbolisiert
=========== ===============================
'+'         public
'-'         privte
'#'         protected
'~'         package(gar kein Zugriffsrecht)
=========== ===============================

Generalisierung/ Spezialisierung
--------------------------------

Zwischen Klasssen:

* Unterklassen zeigen mit einem durchgezogenem Pfeil mit holem Kopf auf ihre 
  Oberklassen
* In Unterklassen werden nur zusaetzliche Attribute und Methoden Aufgefuehrt
* Eine Klasse die von einer anderen abhaengig ist (Parameter/ Methode) zeigt
  auf diese mit eienm gestrichelten Pfeil
* falls abstract mit dem Stereotyp '<<abstract>>' versehen
* Arrays werden mit zusaetzlichen Klammern '[1..n]' versehen fuer die maximale
  Laenge des Arrays

Interfaces:

* ein Interface wird in der bex mit einem zusaetzlichem Stereotyp
  '<<interface>>' versehen
* Eine Klasse, die ein Interface implementiert zeigt mit einem gestrichelten
  ynt

.. 141

Entwurfsmuster
==============

Entwurfsmuster bilden den Einstieg in die Techniken zum Entwerfen zon 
Softwaresystemen

Idee
----

Entwurfsmuster haben das Ziel:

* Gleicharartige Probleme isolieren
* Fuer jedes der gleichartigen Probleme Loesungen erarbeiten

Der daraus entstandene Loesungsansatz wird als Entwurfsmuster bezeichnet

Arten
=====

Die durch das Entwurfsmuster geloesten Probleme koennen in 3 Klassen eingeteilt
werden

1. struktuelle Verbindungen von Klassen und Objekten (Strukturmuster)
2. Interaktion zwischen Objekten (Verhaltensmuster)
3. Erzeugung von Objekten (Erzeugungsmuster)

Klassenbezogen
--------------

Das Klassenbezogene Entwurfsmuster umfasst Klassen und ihre Beziehung auf
Typebene

=================== ======================= =============================
Strukturmuster      Verhaltensmuster        Erzeugungsmuster
=================== ======================= =============================
Klassenadapter      Interpreter             Fabrikmethode
                    Template
=================== ======================= =============================

Objektbezogen
-------------

Das objektbezogene Entwurfsmuster umfasst Objekte und ihre Beziehung bei der
Ausfuehrung.

=================== =======================     =============================
Strukturmuster      Verhaltensmuster            Erzeugungsmuster
=================== =======================     =============================
Objektadabpter      Strategie                   Abstrakte Fabrik
Dekorierer          Mediator                    Singleton
Kompositum          Beobachter                  Erbauer
Fassade             Verantwortlichkeitskette    Prototyp
Bruecke             Kommando
Fliegengewicht      Iterator
Stellvertreter      Erinnerer
                    Zustand
                    Besucher
=================== =======================     =============================

Iterator
========

.. 148

Ein Iterator ermoeglicht den sequentiellen Zugriff auf die Elemente eines
Objektes, ohne dabei die dem Objekt (Aggregat) zugrunde liegende Struktur 
aufzudecken.

Durchlaeufe ueber das Objekt werden von dem zustaendigen Iterator-Objekt 
uebernommen.

Die Anwendung muss Aggregat und Iterator miteinander verbinden

Implementierung
---------------

* Das Aggregat selbst muss eine Schnittstelle implementieren, so dass dann das
  Aggregat als itterierbar gekennzeichnet wird.
* Der Iterator implementiert eine einheitliche Schnittstelle fuer Iteratoren,
  damit alle Iteratoren gleich genutzt werden koennen.
* jedes Aggregat besitzt einen eigenen Iterator, der vom Aggregat bereit
  gestellt wird.
* Der Iterator kann damit bevorzugten Zugriff auf das Aggregat erhalten und so
  eine effiziente Implementierung vornehmen
* Iterator wird auf Anforderung uebergeben

Strategie
=========

.. 173

Eine Strategie ermoeglicht das Festlegen eines Objekts ohne Zugriff aud die 
Implementierung der Klasse des Objekts. Ferenr wird dabei auch nicht das 
Verhalten des Objekts bei der Ausfuehrung veraendert.

|

Dazu kapseln wir das neue Verhalten in eine eigene Strategie-Klasse.
Bei Aenderung des Verhaltens muss lediglich das Strategie Objekt ausgetauscht
werden.

|

Strategien werden also am Objekt gestzt und bei Aufruf einer Methode (apply())
ausgefuehrt

Vergleiche
----------

+-------------------+---------------------------+-------------------------------+
| Entwurfsmuster    | Vorteile                  | Nachteile                     |
+-------------------+---------------------------+-------------------------------+
|                   |                           |                               |
+-------------------+---------------------------+-------------------------------+

Adapter
=======

.. 193

Dekorierer
==========

.. 210

Kompositum
==========

.. 239

Besucher
========

.. 262

Fassade
=======

.. 266

Mediator
========

.. 273

Beobachter
==========

.. 283

Fabrikmethode
=============

.. 309

Singleton
=========

.. 315

Abstrakte Fabrik
================

.. 322

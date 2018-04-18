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
  Pfeil mit holem Kopf auf dieses.

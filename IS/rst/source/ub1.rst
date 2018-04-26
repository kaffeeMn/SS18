################
UB2 Mitschriften
################

A1
==

Erklaerungen
------------

Integritaet:
* Keine doppelten Eintraege (Redundanz)
    + Redundanzen fuehren zu Anomalien
        - Anomalien heisst in unserem Fall mehrfaches Loeschen etc. 
            (Fallunterscheidungen)

Loesungen
---------

* MySQL
    + Ja
* Excel
    + Nein: nicht Parallel, keine Tansaktionsmoeglichkeiten {8, 7}
* LSF
    + Anmeldung
* IBM DB2
    + Ja
* iTunes
    + Anmeldung
* Microsoft SQLServer
    + Ja

A2
==

Loesung
-------

3 Ebenen Schema
^^^^^^^^^^^^^^^

Das DBMS besteht aus den Ebenen:

1. Exteren(s) Schema(ta)
    + SQL : create view
        - Benutzer/ Programme erhalten verschiedene Ansichten auf die DB
2. Semantisches/ Konzeptuelles Schema (Tabellen)
3. Physikalisches Schema

Anfrage Bearbeitung 1->3, Daten Darstellung 3->1

|

Datenunabhaengigkeit:

* Physikalische Datenunabhaengigkeit zwischen 2-3
* Logische Datenunabhaengigkeit zwischen 1-2

A3
==

Erkenntnis:

* Parsen ist recht ineffizient
* Ein richtiges DB-Management System kann effizient suchema
    (kein staendiges Einlesen)

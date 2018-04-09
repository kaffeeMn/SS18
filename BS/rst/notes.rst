####################
Mitschriften BS 2018
####################

Table Of Content
#################

Skript
######

Einfuerhrung
============

Uebersicht des Stoffs
---------------------

* Kontrollflussarbdtraktionen
    + Faeden und Prozesse
* Prozessorzuteilung
* Kooperatione und Konkurrenz von Kontrollfluessen
    + Synchronisation und Verklemmung
* Verwaltung und Virtualisierung des Hauptspeichers
* Ein- und Ausgabe
* Dateisysteme
* IT-Sicherheit
* Multiprozessorsysteme

Vielfalt der Anforderungen
--------------------------

Anforderungen eines Betriebssystems keonnen:

* High Performance Computing (server)
* Sichere Systeme
* Arbeitsplatzsysteme (Desktop-Applications)
* Echtzeitsysteme
* Eingebettete Systeme und automotive Systeme

sein.

Serielle Verarbeitung(1945+)
----------------------------

* Damals wurde noch mittels Lochkarten programiert. Ausgaben geschahen ueber den
    Drucker, Fehleranzeigen ueber Kontrollampen.
* Rechnerzeiten werden durch Papierterminkalender zugeteilt
    + fehlerbehaftet und verschwendet Zeit
* Die Meiste Zeit wurde durch Langsame I/O Geraete verbraucht (Lochkarten und
    Drucker) 
* Erste Software in Form von Programmbibliotheken
    + Binder, Debugger, etc.

Stapelssystem (1955)
--------------------

Ein Stapel von Lochkarten, zur Uebersetzung und Ausfuehrung eines FORTRAN 
Programms.

* Manuelle Betriebseingriffe sollen reduziert werden
* Erste Betriebssysteme "resident monitor" mit
    + Interpretation von Job-Steuerbefehlen
    + Laden und Ausfuehrung von Programmen
    + Geraeteansteuerung

Dabei bleibt ein Monitor dauerhaft im Speeicher waehrend er ein 
Anwendungsprogramm nach dem anderen ausfuehrt.

* Probleme durch fehlerhafte Anwendungen (nicht terminierend etc.)
    + Loesung: Zeitbausteien unterbrechen Prozesse

I/O Flaschenhals
----------------

Geerell ist die CPU schneller, als Kartenleser und Drucker, dadurch wird 
Rechenzeit verschwendet.

Mehrprogrambetrieb/ Threads
----------------------------

################
GTI Mitschriften
################

Table Of Contents
#################

* pingo_
* r_e_
* endliche_automaten_

PINGO-Fragen
############

01-F13
======

a,b,c,d

02-F10
======

b


Skript
######

.. _r_e:

Regulaere Ausdruecke
====================

Einleitung und Beispiele
------------------------

Regulaere Ausdruecke, sind zeichenketten, die Syntaktische Bedingungen erfuellen.

Wir betrachten im folgeneden Methoden, die erkennen ob ein Ausdruck diese Bedin-
gungen erfuellt.

eMail
^^^^^

Eine eMail-Adresse besteht aus einem lokealen Namen, einerm @ und einem Domain
Namen.

lokalName@domanName

Alphabete, Woerter, Sprachen
----------------------------

Eine Zeichenkette, bzw. ein String sei als eine endliche folge von Zeichen 
definiert.

Die Menge der elaubten Zeichenketten nennen wir Alphabet, die Menge von 
Zeichenketten Sprache.

.. math::

    \text{Alphabet } \Sigma \text{ mit Sigma endlich und nicht leer}\\
    \text{Wort } w = \sigma_i ... sigma_{|w|}\\
    \text{das leere Wort: } \epsilon\\
    \Sigma \text{ mit } \Sigma = \{ \sigma_1, ..., \sigma_n \}

Eine Sprache ueber einem Alphabet ist eine endeliche oder unendliche Menge von 
Woertern ueber dem Alphabet.

Der Konkatenationsoperator .. math::
    \dot

verbindet Woerter.

Syntax und Semantik
-------------------

Beschreibungsformalismus
^^^^^^^^^^^^^^^^^^^^^^^^

Zunaechst wir nach einem Beschreibungsformalismus fuer Mail-Adressen gesucht.
Dieser soll:

* moeglichst einfach
* aber genuegend ausdrucksstark sein

Es sollen Label:

* A-Z
* a-z
* 0-9

verwendbar sein

Der lokale Name besteht aus mindestens einem Label

Syntax
^^^^^^

Fuer die Menge an regulaeren Ausdruecken uber Sigma gilt:

1. Zeichen sind Regulaere Ausdruecke
    * die leere Menge ist ein Regulaerer Ausdruck
    * epsilon ist ein regulaerer Ausdruck
    * fuer jedes sigma in Sigma ist sigma ein regulaerer Ausdruck
2. sind alpha und beta regulaere Ausdruecke, so auch
    * (alpha beta)
    * (alpha + beta)
3. Ist alpha ein regulaerer Ausdruck, so auch (alpha*)

 |

Semantik
^^^^^^^^

ist a ein regulaerer Ausdruck, so ist L(a) die Sprache ueber diesen Ausdruck

L(a) ist wie folgt definiert
* L(empty) = empty
* L(epsilon) = {epsilon}
* l(sigma) = {sigma} fuer jedes sigma in Sigma
* mit alpha und beta als regulaere Ausdruecke
    + l((alphabeta)) = L(alpha) o L(beta)
    + L((alpha + beta)) = L(a) u L(beta)
* ist alpha ein reg. Ausdruck, so ist L((alpha*)) = L(alpha)*

Des weiterne heisst eine Sprache L regulaer, wenn es einen regulaeren Ausdruck
alpha gibt mit L = L(alpha)

Beispiele, Erweiterungen und Aequivalenzen
------------------------------------------

die Bindung der Operation ist von stark nach schwach wie folgt geordnet

1. ()
2. *
3. konkatenation
4. +

Abkuerzungen fuer r.e. findet man auf Folie 00-20

Aequivalenzen
^^^^^^^^^^^^^

r.e. alpha und beta sind dann aeuivalent, wenn L(alpha) und L(beta) aequivalent
sind.

.. _endliche_automaten:

Endliche Automaten
==================

Vorab wird sich mit Testalgorithmen fuer regulaere Sprachen beschaeftigt.

Es wird getestet, ob ein Eingabewort w in L ist.

Jede Moegliche Kombination von Variablen wird als Zustand bezeichnet.
Ein System aus endlich vielen Zustaenden und Zustandsuebergaengen heisst
**endliches Transitionssystem**, bzw. **endlicher Automat**.

Ein Automat, der Nur Woerter einer Sprache annimmt entscheidet diese Sprache.

Definition und Parameter
------------------------

Ein Automat A besteht aus:

* *Menge von Zustaenden* Q
* *Eingabealphabet* Sigma
* *Transitionsfunktion* delta : Q x Sigma -> Q
* *Startzustand* s in Q
* *Menge von akzeptierenden Zustaenden* F

A wird denotiert  in der Form:

.. math::

    A = (Q,\Sigma,\delta,s,F)\\

Nicht deterministische endliche Automaten
=========================================

Ziel
----

Wir suchen ein Methode um re in einen Automaten umzuwandeln

Zeichen
^^^^^^^

das Zeichen sigma wird in eine simple Transition uebersetzt

Konkatenationen
^^^^^^^^^^^^^^^

Konkatenationen von Zeichen werden durch aufeinander folgende transitionen 
umgesetzt.

Auswahl (+)
^^^^^^^^^^^

Verundungen werden durch abzweigende Transition, die wieder zum gleichen Zustand
fuehren umgesetzt.


Schleifen (*)
^^^^^^^^^^^^^

Schleifen werden durch transitionen, die wieder zum Anfang der Schleife fuehren
umgesetzt.

Besonderheiten des NFA
----------------------

Der NFA  kann fuer die selbe Eingabe verschiedene Transitionen haben.

Fortan wird die Menge Transitionsrelation mit dreistelligen Tupeln
(start,sigma,end), bei denen mehrere Tupel das selbe start und end mit
verschiedenen sigma haben koennen, angegeben.

Das e-NFA
---------

.. math::
    \delta \subseteq Q x (\Sigma \cup \{\epsilon\}) x Q


################
GTI Mitschriften
################

Table Of Contents
#################

* pingo_
* reg_expr_

PINGO-Fragen
############

00 F13
======

a,b,c,d

Skript
######

.. _reg_expr:

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

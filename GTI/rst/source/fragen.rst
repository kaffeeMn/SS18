Fragen
######

VL
##

generell
========

duerfen Pronleme, Woerter abgekuerzt werden?
Wenn ja: Fuer welche Abkuerzungen ist die Angabe einer Konvention notwendig?

|

Bsp.:

* Turingmaschine durch TM
* Hamiltonkreis durch HK

|

Sind zufallsbasierte Algorithmen und Komplexitaetsklassen KLausurrelevent?
Wenn ja: wie koennte eine aufgabe zu denen aussehen?

Beweis zu TM-DIAG
=================

* Inwiefern war Diagonalisierung ueberhaupt notwendig, der beweis erfolgte doch
  aehnlich zum Beweis von TM-HW durch negation der jeweiligen TM.


Teil D
======

Zeitschranke/ Laufzeit
----------------------

Wenn nach einer Zeitschranke gefragt wird, wie wichtig ist es auf die Funktion

.. math::
    T : \mathbb{N} \rightarrow \mathbb{R}

einzugehen, wenn nach der O-Notation von:
* einem Algorithmus in Pseudocode
* Einer/m TM, GOT0- oder WHILE-Programm
gefragt wird

Probleme
--------

Werden immer die probleme angegeben auf die reduziert werden soll, oder 
    ist da ggf. ein Transfer, bzw. eigenstaendigies auswaehlen, gefordert

ETH/ SETH
---------

Klausurrelevant?
Wenn ja: Wie koennte eine Aufgabe aussehen?

NP, P, NPC
----------

Annahme (i):

.. math::
    P \neq NP

Fragen:

(1):
Ist diese Annahme (ii):
    .. math::
        \text{(i) gilt} \Rightarrow (P \subset NP) 
                                    \land (NPC \subset NP) 
                                    \land (\nexists p \in P: p \in NPC)
schluessig.

(2) Wenn (20 F12):

.. math::
    (P \subset NP) \land (NPC \subset NP) \land (\nexists p \in P: p \in NPC)

gilt, was waere dann ein Problem, dass in NP, aber nicht in NPC liegt.

Stark NP-Vollstaendig
---------------------
20 F17

* "selbst wenn die Größe der vorkommenden Zahlen durch ein Polynom in der Länge 
  der Einga- be beschränkt sind."
    - sind damit Zahlen in unaer-darstellung gemeint?
    - bzw. wie koennen "vorkommende Zahlen" definiert werden.

Uebungen
########

UB7 A1
======

a)
--

* wie asufuehrlich begruenden, dass DPDA mit leerem Keller akzeptiert

b)
--

.. math::
  \{a^n b^n c^n | n \in \mathbb{N}_{0}\} 
  \text{ nicht KF vorraussetzbar oder Beweis noetig?}

A2
==

* Ableitungsbaeume angeben 

    + nicht erklaeren woher die Variabeln abgelesen werden und nur den 
      Baum zeichnen?


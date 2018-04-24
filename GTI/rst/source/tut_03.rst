###########
Tutorium 03
###########

Tutorium zu
###########

Aufgaben
========

PA 3.2
------

a)
^^

aba:

* 1,2,3,3
* 1,2,3,2
* 1,2,4,2
* 1,2,4,3

abbba:

* 1,2,3,3,3
* 1,2,3,3,2
* 1,2,4,4,2
* 1,2,4,4,3

(...)

b)
^^

Widerspruch durch den Potenzmengen Automaten

PA 3.3
------

A
^^

B
^^

.. math::
    \forall i, j \in \{1,2\}, k \in \{0,1,2\}\\
    L^{k}_{i,j}\text{ sei die Menge aller Strings} w \in \Sigma^*
        \text{, fuer die der Automat vom Zustand i in j wechselt nur Zustaende
        an aus } \{1,\dots,k\}\\
    \forall w \in L^{k}_{i,j} : \delta^*(i,w) = j\\
    \forall v \neq \epsilon \in prfx(w) : \delta^*(i,v) \leq k\\

Angewandt auf den Automaten beudet das:

Jede Sprache L^k kann durch einen regulaeren Ausdruck beschrieben werden, L 
selbst wird durch alle Ausdruecke fuer die Akzeptierenden Zustaende Beschrieben.

.. math::
    \alpha_{1,1}^{0} = \epsilon\\
    \alpha_{2,2}^{0} = a\\
    \alpha_{1,2}^{0} = a + b\\
    \alpha_{2,1}^{0} = b\\
    \\
    \alpha_{1,1}^{1} = \alpha_{11}^{0}
        + \alpha_{1,1}^0 (\alpha_{1,1}^0)^* \alpha_{1,1}^0\\
    \alpha_{2,2}^{1} = \\
    \alpha_{1,2}^{1} = \\
    \alpha_{2,1}^{1} = \\
    \\
    \alpha_{1,1}^{2} = \\
    \alpha_{2,2}^{2} = \\
    \alpha_{1,2}^{2} = \\
    \alpha_{2,1}^{2} = \\

UB0 18.4.
#########

* naechste Uebung faellt aus wegen der FVV

Briefkasten 52?

Praesenzblatt
#############

A 1
===

(i) mit der lange des Alphabets durch

.. math::
    | \Sigma | = l

Enthaelt das Alphabet l Zeichen. Folglich existieren

.. math::
    l^n

kombinationen fuer Woerter der Laenge n

|

(ii)

t = n - k + 1

Teilwoerter sind insbesondere dadurch definiert, dass sie zusammenhaengend sind.
Ein Teilwort kann demnach an jedem index anfangen, der nicht groesser n-k+1 ist.

|

(iii)

.. math::
    \Sigma = \{a,b\}\\
    \\
    L_1 = \{\epsilon, a, b\}\\
    l_2 = \{w \in \Sigma^* | |w| \text{ ist gerade}\}\\
    l_3 = \{w \in \Sigma^* | |w| \text{ ist ungerade}\}
    L_1 \dot L_2 = \Sigma = L_1 \dot L_3\\
    L_2 \cap L_3 = \emptyset = L_1 \dot \emptyset

A 2
===

a)

.. math::
    \alpha = (A-Z)^{1,3}-(A-Z)^{1,2} \_
    \beta = (1-9) (0-9)^3 + 0(1-9)^{0,3} + 0^2(1-9)^{0,2} + 0^3(1-9)
    \gamma = \alpha \beta

b) 

.. math::
    \beta = 0 + (1-9)(0-9)^{0,1} + 1(0-9)^{1,2} + 2(0-5)^2\\
    \alpha = \beta . \beta . \beta . \beta\\

c)

.. math::
    \alpha = ((1(\epsilon + 0 + 00 + 000)) + ((\epsilon + 0 + 00 + 000)1))^*

A 3
===

.. math::

    (i)\\
    L_1  = \{ \epsilon \}\\
    L_1^* = \{ \epsilon \} = L_1^+\\
    L_1^* - \{ \epsilon\} \neq L_1^+\\
    \\
    (ii)\\
    L_1 = \{ab,c\}, L_2 = \{a,b,c\}\\
    abc \in L_1^* \cap L_2^*\\
    abc \not \in (L_1 \cap L_2)^*\\
    \\
    (iii)\\
    L_1 = \{a\}, L_2 = \{b\}\\
    ab \in (L_1 \dot L_2)^*\\
    ab \not \in L_1^* \cup L_2^*

###########
Tutorium 01
###########

Tutorium zu Regulaeren Ausdruecken
##################################

Aufgaben
========

PA 1.1
------

a_1:

Regel: beginnend mit 1 endend mit zwei aufeinander folgenden 3en
L = {1w33 | w in Sigma}

a_2:

Regel: enthaelt zwei aufeinander folgende 2en
L = {v22w | v, w in Sigma}

a_3:

Regel: gerade Woerter ueber {1,3}^*
L = {w in {1,3}^* | |w| ist gerade}

a_4:

Regel: Jedes Teilwort hat eine 2 als erstes und letztes Zeichen, wobei
    mindestens zwei 2en vokommen muessen. 

L_help = {2w2 | w in l_help}
L = {w_1, ..., w_n | n in N_0 jedes Teilwort in L_help}

PA 1.2
------

a)

a_0 = (b^*ab^*a)^*b*

b)

a_1 = a_0aa_0

c)

a = a_1ba_1 + a_0ba_0

PA 1.3
------

a_1 = (a+c)^*
a_2 = (b+c)^*((a^*b)^*(b+c)^* + a^*)
    === c^*(a+bc^*+b)^*

problem: aacc
    
a_3 = (b+c+a(a+b)^*c)^*
    === (a+b+c)^*ab^*c(b+c)^* + (b+c)^*

PA 1.4
------

a) a = 0 + (1-9)(0-9)^*

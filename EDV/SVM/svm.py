import numpy as np
import numpy.random as random
from numpy.linalg import norm
from numpy.linalg import solve
from numpy.linalg import matrix_rank as rank
import matplotlib.pyplot as plt
from copy import deepcopy
from cvxopt import matrix
from cvxopt.solvers import qp

N_POINTS_C1 = 50
N_POINTS_C2 = 50
c1_radius = [0, random.randint(low=1,high=49)]
c2_radius = [50, 50-c1_radius[1]]
DATA = [
    np.array([[random.randint(low=0, high=c1_radius[1]) + c1_radius[0]
               for i in range(N_POINTS_C1)],
              [0 for i in range(N_POINTS_C1)]]),
    np.array([[random.randint(low=0, high=c2_radius[1]) + c2_radius[0] 
               for i in range(N_POINTS_C2)], 
              [0 for i in range(N_POINTS_C2)]])
]

def svm_weichert_dual(X, Y, kernel=lambda x1, x2: np.dot(x1,x2), xi=0):
    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)
    N = len(X)

    # max/min Problem:
    # max Sum ai - 1/2 * Sum aiaj yiyj <xi,xj>
    # <=> min 1/2 * Sum aiaj yiyj <xi,xj> - Sum ai

    # <xi,xj>
    #X_ij = np.array(list(map(kernel, X,X)), dtype=float)
    X_ij = np.zeros((N,N), dtype=float)
    for i in range(N):
            for j in range(N):
                X_ij[i,j] = kernel(X[i], X[j])
    # yiyj
    Y_ij = np.outer(Y,Y).astype(float)
    # aiaj yiyj <xi,xj>
    P = matrix(Y_ij * X_ij)

    # - Sum ai
    q = matrix(np.ones(N, dtype=float) * -1.)


    # Constraints:
    # ai >= 0
    G = matrix(np.diag(np.ones(N, dtype=float)) * -1.)
    h = matrix(np.zeros(N, dtype=float))

    # a0*y0 + ... + aNyN = 0
    A = matrix(Y, (1,N))
    b = matrix(0.)


    #solving the quadratic programming problem
    sol = qp(P, q, G, h, A, b)
    alphas = np.ravel(sol['x'])

    # support vektors are those whose alpha values are non zero 
    svs = X[alphas>1e-5]
    svs_y = Y[alphas>1e-5]
    alph = alphas[alphas>1e-5]

    # b = -1/|svs| Sum_k Sum_i aiyi<svsk, xi> 
    b = 0.
    for sv in svs:
        for i,x in enumerate(X):
            b += alphas[i] * Y[i] * kernel(sv,x)
    b *= -1./float(len(svs))

    return alphas, svs, svs_y, b, \
           lambda x: np.sum([alphas[i]*Y[i]*kernel(x, X[i]) for i in range(N)]) + b, \
           lambda x: np.sign(np.sum([alphas[i]*Y[i]*kernel(x, X[i])
                                     for i in range(N)]) + b )


def rotate_around_point(xy, radians, origin=(0, 0)):
    # move to origin
    x,y = xy
    offset_x, offset_y = origin
    adjusted_x = x - offset_x
    adjusted_y = y - offset_y
    # rotate
    cos_rad = np.cos(radians)
    sin_rad = np.sin(radians)
    qx = cos_rad * adjusted_x - sin_rad * adjusted_y
    qy = sin_rad * adjusted_x + cos_rad * adjusted_y

    # move back
    qx += offset_x
    qy += offset_y
    return qx, qy

if __name__ == '__main__':
    # cluster creation via rotation around the centers (0,0) and (50,)
    for j in range(len(DATA[0][0])):
        DATA[0][0][j], DATA[0][1][j] = [
            int(t) for t in rotate_around_point(np.array([DATA[0][0][j], 
                                                          DATA[0][1][j]]),
                                                np.random.rand() *2* np.pi,
                                                (0,0))]
    for j in range(len(DATA[1][0])):
        DATA[1][0][j], DATA[1][1][j] = [
            int(t) for t in rotate_around_point(np.array([DATA[1][0][j], 
                                                          DATA[1][1][j]]),
                                                np.random.rand() *2* np.pi,
                                                (50,0))]
    X,Y = np.concatenate((list(zip(DATA[0][0],DATA[0][1])),
                          list(zip(DATA[1][0],DATA[1][1])))), \
          np.concatenate((np.ones((N_POINTS_C1)), np.ones((N_POINTS_C2))*-1))

    # svm solving the classifaction problem on training data
    alphas, svs, svs_y, b, H, f = svm_weichert_dual(X,Y)#, 
                                                    #kernel=lambda x, y : \
                                                    #        (np.exp(-norm(x-y)
                                                    #         **2) /2))

    # aproximating the hyperplane
    # positively classified sv
    pos = []
    for sv in svs:
        if f(sv) == 1:
            if all([n != 0 for n in [norm(x-sv) for x in pos]]):
                pos.append(sv)
    pos_x = np.sum(pos, axis=0) / len(pos)
    # negatively classified sv
    neg = []
    for sv in svs:
        if f(sv) == -1:
            if all([n != 0 for n in [norm(x-sv) for x in neg]]):
                neg.append(sv)
    neg_x = np.sum(neg, axis=0) / len(neg)

    # mid-point
    s1 = pos_x  + 0.5 * (neg_x - pos_x)
    if np.amin(neg_x - pos_x) <0:
        s1 = neg_x + 0.5 * (pos_x - neg_x)

    if len(pos) == 1 and len(neg) == 1:
        # 2 svs => perpendicular vector
        s2_pos = rotate_around_point(pos_x.tolist(), np.pi/2, s1.tolist())
        s2_neg = rotate_around_point(neg_x.tolist(), np.pi/2, s1.tolist())
        m, n = solve([[s2_pos[0],1],[s2_neg[0],1]],[s2_pos[1],s2_neg[1]])
    else:
        if len(pos) > 1 and len(neg) > 1:
            # two lines => average of the normalized vetors
            n_pos = np.array(pos[0] - pos[-1])
            n_pos /= norm(n_pos)
            n_neg = np.array(neg[0] - neg[-1])
            n_neg /= norm(n_neg)
            n_svs = 0.5 * (n_pos + n_neg)
        # one line => just take that line
        elif len(pos) > 1: 
            n_svs = np.array(pos[0] - pos[-1])
        else:
            n_svs = np.array(neg[0] - neg[-1])
        n_svs  /= norm(n_svs)
        vx = s1 + n_svs
        m, n = solve([[vx[0],1],[s1[0],1]],[vx[1],s1[1]])
    # equation for the plane
    h_plane = lambda x : x * m + n


    # plotting ground trouth
    for x in X:
        if f(x) == 1:
            plt.plot(x[0],x[1], 'bo')
        else:
            plt.plot(x[0],x[1], 'ro')

    # plotting svs
    for x in svs:
        plt.plot(x[0],x[1], 'yo')

    #  plotting the hyperplane
    x = []
    y = []
    for i in range(50):
        if h_plane(i) < 50 and h_plane(i) > -50:
            x.append(i)
            y.append(h_plane(i))
    plt.plot(x,y)
    plt.show()

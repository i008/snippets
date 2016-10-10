def baseline_als(y, lam, p, niter=10):
    """Implements an Asymmetric Least Squares Smoothing
    baseline correction algorithm
    (P. Eilers, H. Boelens 2005)
    """
    L = len(y)
    D = sparse.csc_matrix(np.diff(np.eye(L), 2))
    w = np.ones(L)
    
    for i in xrange(niter):
        W = sparse.spdiags(w, 0, L, L)
        Z = W + lam * D.dot(D.transpose())
        z = spsolve(Z, w*y)
        w = p * (y > z) + (1-p) * (y < z)
        
    return z


# basic lowpass filter
from scipy.signal import firwin, lfilter

numtaps=100 #windowsize
cutoff=0.01 #cutoff freq

f = firwin(numtaps=numptaps, cuttoff=cutoff, window='hamming')
filtered_y = lfilter(f, 1.0, y)


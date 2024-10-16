import numpy as np
import rebound as rb

def get_bin_ae_dumb(sa):
    tmax = sa.tmax
    Ntot = len(sa)
    N95 = int(np.floor(0.9 * Ntot))
    Nout = Ntot-N95
    dist = np.zeros(Nout)
    for i in range(N95,Ntot):
        sim = sa[i]
        p0 =sim.particles[0]
        p1 = sim.particles[-1]
        dist[i-N95] = p1.orbit(primary=p0).d
    q = np.min(dist)
    Q = np.max(dist)
    return qQ_to_ae(q,Q)

def qQ_to_ae(q,Q):
    a = 0.5*(q+Q)
    e = (Q-q)/(q+Q)
    return a,e
if __name__=="__main__":
    import sys
    I = int(sys.argv[1])
    srcdir = "/fs/lustre/cita/hadden/09_stellar_binary_scattering/03_simulations/"
    file_name = srcdir + "s_type_q03_30bd_{}.sa".format(I)
    sa = rb.Simulationarchive(file_name)
    a,e = get_bin_ae_dumb(sa)
    ae_arr=np.array([a,e])
    np.save("./ae_bin_{}",ae_arr)


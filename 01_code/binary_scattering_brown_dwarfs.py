import rebound as rb
import numpy as np
def sim_setup(q_bin,mu_brown_dwarfs,a_brown_dwarfs,e_bin = 0,sigma_i = 0.001):
    m_bin = 1
    m1 = (1-q_bin) * m_bin
    m2 = q_bin * m_bin
    sim = rb.Simulation()
    sim.add(m=m1)
    sim.add(m=m2,a=1)
    bin_com = sim.com()
    for mu,a in zip(mu_brown_dwarfs,a_brown_dwarfs):
        inc= np.random.rayleigh(sigma_i)
        Omega = np.random.uniform(-np.pi,np.pi)
        sim.add(m=mu,a=a,inc = inc,Omega=Omega,primary = bin_com)
    sim.move_to_com()
    return sim
    
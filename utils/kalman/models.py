import numpy as np

class CWPA2D:
    # Continuous Wiener Process Acceleration in 2D

    def __init__(self, dt=1.0, q=2e-2, r=10.0):
        dt2 = dt * dt / 2.0
        dt3 = dt * dt2 / 6.0
        dt4 = dt * dt3 / 8.0
        dt5 = dt * dt4 / 20.0

        self.A = np.asarray([
            [1.0, 0.0, dt, 0.0, dt2, 0.0],
            [0.0, 1.0, 0.0, dt, 0.0, dt2],
            [0.0, 0.0, 1.0, 0.0, dt, 0.0],
            [0.0, 0.0, 0.0, 1.0, 0.0, dt],
            [0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
        ])
        self.Q = q * np.asarray([
            [dt5, 0.0, dt4, 0.0, dt3, 0.0],
            [0.0, dt5, 0.0, dt4, 0.0, dt3],
            [dt4, 0.0, dt3, 0.0, dt2, 0.0],
            [0.0, dt4, 0.0, dt3, 0.0, dt2],
            [dt3, 0.0, dt2, 0.0, dt, 0.0],
            [0.0, dt3, 0.0, dt2, 0.0, dt]
        ])
        self.R = r * np.eye(2)
        self.H = np.asarray([
            [1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0]
        ])
        self.T = np.eye(6)

class Brownian2D:

    def __init__(self, dt=1.0, q=2e-2, r=10.0):

        self.A = np.eye(2)
        self.Q = q * dt * np.eye(2)
        self.R = r * np.eye(2)
        self.H = np.eye(2)
        self.T = np.asarray([
            [1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0]
        ])
from mpi4py import MPI
import numpy as np
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 100

s = random.randint(1, 100)

matrix = np.random.rand(s, s)

comm.send(matrix, dest=(rank+1)%size)
data = comm.recv(source=(rank-1)%size)
print(f"my rank is {rank} and recieve a matrix of shape{data.shape}")

'''if rank == 0:
    A = np.random.rand(random.randint(1, N), N)
    for proc in range(1,size):
        comm.send(A, dest=proc, tag=11)
    Arecv = A
else:
    Arecv = comm.recv(source=0, tag=11)
    print(f" --> process {rank} received a matrix of shape {Arecv.shape}")
'''

np.savez(f"A_{rank}_{size}.npz", A=data)

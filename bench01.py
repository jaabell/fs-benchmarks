from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print(f"Hi from process {rank} of {size}.")

N = 100

if rank == 0:
    A = np.random.rand(N, N)  # , dtype=np.double)
    for proc in range(1, size):
        comm.send(A, dest=proc, tag=11)
    Arecv = A
else:
    Arecv = comm.recv(source=0, tag=11)
    print(f" --> process {rank} received a matrix of shape {Arecv.shape}")

np.savez(f"A_{rank}_{size}.npz", A=Arecv)

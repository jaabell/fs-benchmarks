from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# access mode
a_mode = MPI.MODE_WRONLY | MPI.MODE_CREATE

file_handle = MPI.File.Open(comm, 'test.log', a_mode)

buffer = np.empty(10, dtype=int)
buffer[:] = rank
offset = rank*buffer.nbytes
file_handle.Set_size(1024**2)
file_handle.Write_at_all(offset, buffer)

file_handle.Sync()
file_handle.Close()

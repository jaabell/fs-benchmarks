import time
import subprocess

start_time = time.time()

command = "mpirun -np 6 python3 bench_scatter.py"

subprocess.Popen(command, shell=True).wait()

print ("Total time: %s seconds" % (time.time() - start_time))
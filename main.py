import time
import subprocess

start_time = time.time()

command = "mpiexec -np 6 python bench_01.py"

subprocess.Popen(command, shell=True).wait()

print("Total time: %s seconds" % (time.time() - start_time))
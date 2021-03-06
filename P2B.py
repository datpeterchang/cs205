import numpy as np
import multiprocessing as mp
import time
import matplotlib.pyplot as plt

# Sleep for t seconds
def burnTime(t):
	time.sleep(t)

#for parallel computing
def parallel(processes, jobs, wait_time):
	start=time.time()
	pool = mp.Pool(processes);
	result = pool.map(burnTime(wait_time), range(jobs))
	return time.time()-start
	
#for serial computing:
def serial(jobs, wait_time):
	start = time.time()
	for i in range(0,jobs):
		burnTime(wait_time)
	return time.time()-start

# Main
if __name__ == '__main__':
	N = 16 # The number of jobs
	P = 4  # The number of processes

	# A thread pool of P processes
	pool = mp.Pool(P)

  # Use a variety of wait times
	ratio = []
	wait_time = [10**(-6),10**(-5),10**(-4),10**(-3),10**(-2),10**(-1),1]

	for t in wait_time:
		# Compute jobs serially and in parallel		
		# Use time.time() to compute the elapsed time for each
		serialTime = serial(N,t);
		parallelTime = parallel(P,N,t);

		# Compute the ratio of these times
		ratio.append(serialTime/parallelTime)

	# Plot the results
	plt.plot(wait_time, ratio, '-ob')
	plt.xscale('log')
	plt.xlabel('Wait Time (sec)')
	plt.ylabel('Serial Time (sec) / Parallel Time (sec)')
	plt.title('Speedup versus function time')
	plt.show()

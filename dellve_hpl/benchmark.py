
import dellve
import os
import subprocess as sp
HPL_DIR = '/opt/hpl-2.1_cuda-6.5_gcc-4.4.7_ompi-1.6.5_mkl_ext_pkg_v1'
HPL_CMD = 'mpirun -n 2 --bind-to none run_linpack_10_core_per_gpu_0_2'

class HPL(dellve.Benchmark): 
    name = 'HPL'

    def routine(self):
        p = sp.Popen(HPL_CMD.split(), cwd=HPL_DIR, stdout=sp.PIPE)
        
        try:
            our, err = p.communicate()
        except dellve.BenchmarkInterrupt:
            p.terminate()
        else:
            self.progress = 100


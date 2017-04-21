
import dellve
import psutil

# TODO: de-hardcode this...
HPL_DIR = '/opt/hpl-2.1_cuda-6.5_gcc-4.4.7_ompi-1.6.5_mkl_ext_pkg_v1'
HPL_CMD = 'mpirun -n 2 --bind-to none run_linpack_10_core_per_gpu_0_2'

import re

class HPL(dellve.Benchmark):

    name = 'HPL'

    def routine(self):
        mpi_process = psutil.Popen(HPL_CMD.split(), cwd=HPL_DIR,
                                   stdout=psutil.subprocess.PIPE)

        def printf(s):
            print  s

        try:
            pattern = re.compile('(Prog=.*\%)')

            for stdout_line in iter(mpi_process.stdout.readline, ""):
                print stdout_line

                groups = pattern.findall(stdout_line)
                if len(groups) == 1:
                    progress = groups[0].replace('Prog= ', '').replace('%', '')
                    self.progress = int(float(progress.strip()))

        except dellve.BenchmarkInterrupt:
            print 'Stopping HPL...'
            for mpi_child_process in mpi_process.children():
                mpi_child_process.kill()
                print 'Killed HPL process %d' % mpi_child_process.pid
            mpi_process.kill()
            print 'Killed MPI process %d' % mpi_process.pid
        else:
            self.progress = 100
        finally:
            mpi_process.stdout.close()


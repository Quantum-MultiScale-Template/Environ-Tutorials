#!/bin/bash

mpirun -np 4 pw.x -environ < C6H6.scf.in > scf.out
mpirun -np 4 turbo_lanczos.x -environ  < C6H6.tddfpt.in > tddfpt.out
mpirun -np 4 turbo_spectrum.x -environ < C6H6.tddfpt_pp.in > spectrum.out

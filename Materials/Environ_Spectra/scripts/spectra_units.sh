#/bin/bash
#This will just provide you with a file that has the two columns you are interested in plotting
awk 'NR >1 {print $2, $4}' C6H6.plot_chi.dat > C6H6.plot_S.dat

#Converts from Ry to eV
awk '{print ($1*13.6), $2}' C6H6.plot_S.dat > plot.$i.eV.dat

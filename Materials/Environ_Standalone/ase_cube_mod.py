# Modified from ASE v3.26.0b1
# Modified 07/12/2025
# ASE is licensed under GNU LGPLv2.1
# Copyright 2025, ASE-developers

import time

import numpy as np

from ase.atoms import Atoms
from ase.io import read
from ase.units import Bohr

def write_cube(file_obj, atoms, data=None, origin=None, comment=None):
    """Function to write a cube file.

    file_obj: str or file object
        File to which output is written.
    atoms: Atoms
        The Atoms object specifying the atomic configuration.
    data : 3-dim numpy array, optional (default = None)
        Array containing volumetric data as e.g. electronic density
    origin : 3-tuple
        Origin of the volumetric data (units: Angstrom)
    comment : str, optional (default = None)
        Comment for the first line of the cube file.
    """

    if data is None:
        data = np.ones((2, 2, 2))
    data = np.asarray(data)

    if data.dtype == complex:
        data = np.abs(data)

    if comment is None:
        comment = "Cube file from ASE, written on " + time.strftime("%c")
    else:
        comment = comment.strip()
    file_obj.write(comment)

    file_obj.write("\nOUTER LOOP: X, MIDDLE LOOP: Y, INNER LOOP: Z\n")

    if origin is None:
        origin = np.zeros(3)
    else:
        origin = np.asarray(origin) / Bohr

    file_obj.write(
        "{:5}{:12.6f}{:12.6f}{:12.6f}\n".format(
            len(atoms), *origin))

    for i in range(3):
        n = data.shape[i]
        d = atoms.cell[i] / n / Bohr
        file_obj.write("{:5}{:12.6f}{:12.6f}{:12.6f}\n".format(n, *d))

    positions = atoms.positions / Bohr
    numbers = atoms.numbers
    charges = atoms.get_initial_charges()
    for Z, q, (x, y, z) in zip(numbers, charges, positions):
        file_obj.write(
            "{:5}{:12.6f}{:12.6f}{:12.6f}{:12.6f}\n".format(
                Z, q, x, y, z)
        )

    data.tofile(file_obj, sep="\n", format="%e")

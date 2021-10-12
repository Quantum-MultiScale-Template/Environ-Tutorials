# Environ Examples

    Example QE+Environ runs

example01: pw.x

    Calculation of total solvation free energy of an isolated molecule
    including electrostatic/cavitation/PV contributions. The solvation
    cavity is defined according to the revised-SCCS.

example02: pw.x

    Same as example01, but the solvation cavity is constructed from
    atomic-centered interlocking spheres ("soft-spheres").

example03: pw.x

    Use of different periodic boundary correction schemes for charged
    isolated systems in vacuum and in solution: Martyna-Tuckerman or
    Point-Counter-Charge (parabolic).

example07: pw.x

    Use of the solvent-aware interface to prevent the dielectric to
    penetrate regions that should remain solvent-free.

competition: pw.x

    Who can find the compound with the largest solvation free energy?

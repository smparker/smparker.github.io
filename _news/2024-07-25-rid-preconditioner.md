---
layout: post
title: "Converge TDDFT in 5 iterations with the rid preconditioner"
date: 2024-07-25
---
John's paper introducing the "rid" preconditioner for TDDFT is now
available online in _The Journal of Chemical Physics_.
This paper is the culmination of two intertwined threads in John's research:
1) the use of semiempirical preconditioners to accelerate the convergence of
ab initio TDDFT calculations; and 2) the development of the TDDFT-ris
model for fast and accurate simulations of spectra.
Using the rid preconditioner, TDDFT excitation energies are converged
in about 5 iterations _on average_, which is about a factor of 3 faster
than using the conventional (diagonal) preconditioner.
Even more, this speedup is obtained _without any loss of accuracy_.
The full paper is titled
["Converging TDDFT calculations in 5 iterations with minimal auxiliary preconditioning"](https://doi.org/10.1021/acs.jctc.4c00577).

---
layout: post
title: "Numerically Stable Resonating Hartree-Fock"
date: 2025-03-12
---
One of the challenges in simulating photochemical reactions is that
there are essentially no electronic structure methods that are
accurate, efficient, and robust enough to be applied to a wide variety of systems.
Enter Resonating Hartree-Fock (ResHF), which is a promising solution to this
conundrum because it provides balanced accuracy for different types of excited states,
and has mean-field scaling. However, the original ResHF method is not numerically stable.
In a new paper, Ericka solves this problem by reformulating the ResHF equations
in terms of the matrix adjugate.
With this approach, ResHF becomes fully numerically stable, and can thus be applied
to a wider variety of systems than has been possible previously.

This paper was published in the Journal of Chemical Physics,
["Numerically Stable Resonating Hartree-Fock"](https://dx.doi.org/10.1063/5.0246790).

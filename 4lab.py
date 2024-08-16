# Jasmin Duishebaeva
# 08.15.2024

# Problem 4: Calculate an approximation for pi and compare it with math.pi.

import math

# Simple approximation of Pi using Leibniz formula for Pi
approx_pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13)
print("Approximated Pi:", approx_pi)
print("math.pi:", math.pi)

#!/usr/bin/env python3
"""
Habitable Zone Calculator based on Kopparapu et al. (2013)
Calculates conservative and optimistic habitable zone boundaries for a star.
"""

import sys
import math

def calculate_hz_fluxes(teff):
    """
    Calculate the stellar flux (relative to solar constant) at the four HZ boundaries.
    
    Parameters
    ----------
    teff : float
        Stellar effective temperature in Kelvin.
    
    Returns
    -------
    dict
        Dictionary with keys:
        - 'inner_conservative': flux for runaway greenhouse limit
        - 'outer_conservative': flux for maximum greenhouse limit
        - 'inner_optimistic': flux for early Venus limit
        - 'outer_optimistic': flux for early Mars limit
    """
    # Temperature offset from solar effective temperature (5780 K)
    T = teff - 5780.0
    
    # Coefficients from Kopparapu et al. (2013), Table 2
    # Format: (S_eff_sun, a, b, c, d)
    # Inner conservative (runaway greenhouse)
    ic = (1.107, 1.332e-4, 1.58e-8, -8.308e-12, -1.931e-15)
    # Outer conservative (maximum greenhouse)
    oc = (0.356, 6.171e-5, 1.698e-9, -3.198e-12, -5.575e-16)
    # Inner optimistic (early Venus)
    io = (1.776, 1.433e-4, 2.58e-9, -1.621e-12, -5.087e-17)
    # Outer optimistic (early Mars)
    oo = (0.320, 5.547e-5, 1.526e-9, -2.874e-12, -5.011e-16)
    
    boundaries = {
        'inner_conservative': ic,
        'outer_conservative': oc,
        'inner_optimistic': io,
        'outer_optimistic': oo
    }
    
    fluxes = {}
    for name, (s_sun, a, b, c, d) in boundaries.items():
        s_eff = s_sun + a*T + b*T**2 + c*T**3 + d*T**4
        fluxes[name] = s_eff
    
    return fluxes


def calculate_hz_distances(luminosity, teff):
    """
    Calculate habitable zone distances in AU.
    
    Parameters
    ----------
    luminosity : float
        Stellar luminosity in solar luminosities.
    teff : float
        Stellar effective temperature in Kelvin.
    
    Returns
    -------
    dict
        Dictionary with distances (AU) for each boundary.
    """
    fluxes = calculate_hz_fluxes(teff)
    distances = {}
    for name, flux in fluxes.items():
        # distance = sqrt(L / S_eff)
        if flux <= 0.0:
            raise ValueError(f"Flux for {name} is non-positive, cannot compute distance.")
        distance = math.sqrt(luminosity / flux)
        distances[name] = distance
    return distances


def main():
    if len(sys.argv) != 3:
        print("Usage: python calculate_hz.py <temperature_K> <luminosity_Lsun>")
        print("Example: python calculate_hz.py 5800 1.0")
        sys.exit(1)
    
    try:
        teff = float(sys.argv[1])
        luminosity = float(sys.argv[2])
    except ValueError:
        print("Error: temperature and luminosity must be numeric.")
        sys.exit(1)
    
    if teff <= 0:
        print("Error: temperature must be positive.")
        sys.exit(1)
    if luminosity <= 0:
        print("Error: luminosity must be positive.")
        sys.exit(1)
    
    try:
        distances = calculate_hz_distances(luminosity, teff)
    except ValueError as e:
        print(f"Calculation error: {e}")
        sys.exit(1)
    
    print(f"Habitable Zone Boundaries for star with Teff = {teff} K, L = {luminosity} L_sun")
    print("=" * 60)
    print(f"Conservative HZ (Runaway Greenhouse): {distances['inner_conservative']:.4f} AU")
    print(f"Conservative HZ (Maximum Greenhouse): {distances['outer_conservative']:.4f} AU")
    print(f"Optimistic HZ (Early Venus): {distances['inner_optimistic']:.4f} AU")
    print(f"Optimistic HZ (Early Mars): {distances['outer_optimistic']:.4f} AU")
    print()
    print("Note: Distances are in Astronomical Units (AU).")


if __name__ == "__main__":
    main()
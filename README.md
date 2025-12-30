# Habitable Zone Calculator

A Python tool to calculate conservative and optimistic habitable zone boundaries for exoplanet host stars, based on the stellar flux-dependent coefficients from Kopparapu et al. (2013).

## Purpose

This tool is designed for quick screening of exoplanet habitability. Given a star's effective temperature (in Kelvin) and luminosity (in solar luminosities), it computes the inner and outer edges of both the conservative habitable zone (runaway greenhouse and maximum greenhouse limits) and the optimistic habitable zone (early Venus and early Mars analogs). Output distances are provided in Astronomical Units (AU).

## Installation

Clone this repository:

```bash
git clone https://github.com/z-teckson/habitable-zone-calculator.git
cd habitable-zone-calculator
```

No external dependencies are required beyond Python 3 and the standard library.

## Usage

Run the script from the command line:

```bash
python calculate_hz.py <temperature_K> <luminosity_Lsun>
```

### Example

For a Sun‑like star (Teff = 5780 K, L = 1.0 L⊙):

```bash
python calculate_hz.py 5780 1.0
```

Output:

```
Habitable Zone Boundaries for star with Teff = 5780.0 K, L = 1.0 L_sun
====================================================================
Conservative HZ (Runaway Greenhouse): 0.9518 AU
Conservative HZ (Maximum Greenhouse): 1.6771 AU
Optimistic HZ (Early Venus): 0.7505 AU
Optimistic HZ (Early Mars): 1.7678 AU
```

## Methodology

The calculation follows the time‑independent habitable‑zone model described in:

- Kopparapu, R. K., et al. 2013, ApJ, 765, 131. *“Habitable Zones Around Main‑Sequence Stars: New Estimates.”*

For each boundary (runaway greenhouse, maximum greenhouse, early Venus, early Mars) the stellar flux relative to the solar constant, *S_eff*, is expressed as a fourth‑order polynomial in the temperature offset *T* = *T_eff* – 5780 K. The coefficients are taken from Table 2 of the paper. The orbital distance (in AU) is then obtained from

*d* = √( *L* / *S_eff* ),

where *L* is the stellar luminosity in solar units.

## Contributing

Issues, suggestions, and pull requests are welcome. Please open an issue first to discuss any major changes.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## References

- Kopparapu, R. K., et al. 2013, ApJ, 765, 131. [doi:10.1088/0004-637X/765/2/131](https://doi.org/10.1088/0004-637X/765/2/131)
# Nerdalize CO2 calculator

Nerdalize is building a different cloud. Rather than putting thousands of servers into a datacenter, we're distributing them over homes. There, homeowners make good use of the residual heat: to heat their home in winter and their shower water in summer.

This Python script calculates the amount of CO2 saved per year by Nerdalize. It takes an amount of households as input. The script outputs two things:
1) Total CO2 savings in kilograms and how many traveling kilometers this corresponds to for different ways of transportation.
2) An image showing how many airplane trips you could make for the different trips specified in `flights.csv`.

## Usage

```python co2_calc.py <no-of-households> [output-folder]```

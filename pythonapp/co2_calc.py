import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from transport import Transport

output_folder = '/output'

if len(sys.argv) < 2:
    print('Please specify the number of households: co2_calc.py <no-of-households>')
    sys.exit(1)

if len(sys.argv) == 3:
    output_folder = sys.argv[2]

def km_to_world(km):
    return km / 40000

households = int(sys.argv[1])
co2_tonnes = households * 3
co2_kg = co2_tonnes * 1000
transport = Transport(co2_kg)

# Print traveling kilometers per transport type.
print("For {} households, Nerdalize reduces CO2 emissions by {} tonnes per year.".format(households, co2_tonnes))
print("")
print("This is equivalent to (per person):")
tmpl = "- {:,.0f} Kilometers by {}, equivalent to {:.1f} times around the 🌍"
print(tmpl.format(transport.car(), "🚗", km_to_world(transport.car())))
print(tmpl.format(transport.train(), "🚆", km_to_world(transport.train())))
print(tmpl.format(transport.airplane(), "✈️ ", km_to_world(transport.airplane())))

# Read input file and plot amount of trips that could be made for amount of households.
input_file = "flights.csv"
flights = np.genfromtxt(input_file, delimiter=';', names=True, dtype=None)
x = []
y = []
for flight in flights:
    x.append(str(flight['flight'], encoding='utf-8') )
    y.append(transport.airplane() / float(flight['distance']))

x_num = np.arange(len(x))
nerdalize_orange = '#EB4824'
nerdalize_gray = '#F2F2F2'

plt.style.use('ggplot')
plt.rcParams['axes.facecolor'] = nerdalize_gray
rects = plt.bar(x_num, y, color=nerdalize_orange)
plt.xticks(np.arange(len(x)),x)
plt.xlabel('Flights')
plt.ylabel('Number of trips')
plt.title('The amount of trips you can make by ✈️ per year, for {} households.'.format(households))
plt.savefig(output_folder + '/flights.png', bbox_inches='tight')

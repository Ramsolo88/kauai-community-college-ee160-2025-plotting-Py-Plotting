#  AramsPyPlotting will show some basic uses of loops under differing circumstances.
#     Created by Aram Asman
#        Creation Date: 05/09/2025
#        Last Edit: 04/14/2025

import numpy
import matplotlib.pyplot
import time

# Defining 3 x value array's
x_100 = numpy.linspace(-0.1, 0.1, 100)
x_10000 = numpy.linspace(-0.1, 0.1, 10000)
x_1000000 = numpy.linspace(-0.1, 0.1, 1000000)

# Defining 3 y value array's
y_100 = x_100**2 * numpy.cos(10 / x_100)
y_10000 = x_10000**2 * numpy.cos(10 / x_10000)
y_1000000 = x_1000000**2 * numpy.cos(10 / x_1000000)

# Plotting the 10,000 point graph,
matplotlib.pyplot.figure()
matplotlib.pyplot.plot(x_10000, y_10000, c='purple', label = "10,000 points")
matplotlib.pyplot.title(r"$y = x^2 \cos\left(\dfrac{10}{x}\right)$")
matplotlib.pyplot.xlabel("x")
matplotlib.pyplot.xlim(-0.05,0.05)
matplotlib.pyplot.ylabel("y")
matplotlib.pyplot.ylim(-0.0025,0.0025)
matplotlib.pyplot.legend()
matplotlib.pyplot.grid(True)
matplotlib.pyplot.show()

# Measuring the time to calculate the 1,000,000 point plot,
start_time = time.time()
matplotlib.pyplot.figure()
matplotlib.pyplot.scatter(x_1000000, y_1000000, s=0.1)
matplotlib.pyplot.close()
end_time = time.time()

print(f"\nTime to plot 1,000,000 points: {end_time - start_time:.2f} seconds")
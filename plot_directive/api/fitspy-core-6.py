import numpy as np
import matplotlib.pyplot as plt
from fitspy.core.models_bichromatic import pseudovoigt_ka12
from fitspy.core.models_bichromatic import MODE, WAVELENGTH_RATIO, AMPLITUDE_RATIO

x = np.linspace(68, 71, 2000)
y = pseudovoigt_ka12(x, ampli=100, fwhm=.2, x0=69.14, alpha=0.5, cathode='Cu')
plt.figure()
plt.grid()
plt.plot(x, y)
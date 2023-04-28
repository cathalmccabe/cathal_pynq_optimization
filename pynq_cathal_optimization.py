# PYNQ Cathal optimiation
from pynq import Overlay

ol = Overlay("2023-04-28-13_10_cathal_optimization.bit")

cathal_parameter = ol.read()

# Cathal optimization function:
result = ol.cathal_optimization()

print(result)

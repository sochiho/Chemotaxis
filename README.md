# Chemotaxis

A simulation of 'Chemotaxis', a modified random walk used by some bacteria to find food sources. Chemotaxis is a 'run and tumble' process in which bacteria is either moving on a constant bearing and speed, or it is tumbling. A tumble lasts for a fixed time, and no motion occurs. After a tumble, the bacteria travels at a constant speed along a new random bearing. 

In this simulation, the walk is on a 2-d surface where an energy source exists at a density specified by the function f(x, y) = 4000 - (x^2 + y^2) measured in microns.

The bacteria modifies its random walk to so it moves towards a food source by relating the probability of a tumble occuring to the rate of change of the energy field so that it is less likely to tumble when travelling in a direction which increases the energy density. The model for making the half-life (in seconds) of a run event proportional to the temporal energy gradient seen by the bacteria is: t_half = 1 + k * df/dt where k is a constant defining the sensitivity of the bacteria. 

The rate of change of the energy field is sampled constantly by the bacterium during its random walk. This is achieve by sampling the current energy density, f(x,y), at every point to build a record of f(x,y) against time  to determine the gradient. 


The bacterium is assumed to move at a constant speed of 2 microns/sec with a sensitivity, k, of 0.2. Tumble events are assummed to last for 0.1 seconds. The simulation from a specified position is over a series of equally spaced timesteps covering 100 seconds. 

The output shows:

- a 2D greyscale plot with 20 different bacteria tracks overlaid in the top left graph.

- The top right graph shows a simplified trajectory with marks an only the first ad last points

- The bottom graph shows the mean displacement of the bacteria against time. One line for the Mean Squared Displacement from the bacteria's origin and one for the Mean Squared Displacement from the location of maximum energy.   

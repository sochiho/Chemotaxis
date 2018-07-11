from __future__ import division

USER = 'CHIHO SO'
USER_ID = 'xbwl44'

import numpy
import matplotlib.pyplot as pyplot
import time
import matplotlib.cm
import pylab
import random

# Parameters
x0, y0 = 20, 40 # microns
k = 0.2
V = 2 # microns per second
dt = 0.1
timebase = numpy.arange(0, 100, dt)
r = numpy.array((x0, y0))

def energy_density(r):
    '''This function simulates the sugar energy source specified by the function'''
    x, y = r
    f = 4000 - (x**2 + y**2)
    return f

def velocity(a):
    '''This function is for the velocities in the x and y plane'''
    Vx = V * numpy.cos(a)
    Vy = V * numpy.sin(a)
    
    return numpy.array((Vx, Vy))

def position(r):
    '''This function returns the positions of the bacteria''' 
    x, y = r
    a = random.random() * 2 * numpy.pi
    
    position = numpy.zeros((len(timebase), 2))
    shift = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(len(timebase)):

        position[i] = r
        
        eNew = energy_density(r)
        shift.append(eNew)
        shift = shift[-10:]
        df = shift[-1] - shift[0]

        t_half = 1 + k * df
        if t_half < 0.1: t_half = 0.1

        tau = t_half/ numpy.log(2)
        
        p = numpy.exp(-dt/ tau)

        if random.random() < p:
            '''move at speed * dt'''
            r = r + velocity(a) * dt
            
        else:
            a = random.random() * 2 * numpy.pi

    return position

def MSD(r):
    '''This function calculates the mean square displacement of bacteria
against time from the origin and location of max energy'''
    x, y = r
    
    s_d_f_initial = numpy.zeros((20,1000))
    # Squared displacement from initial
    s_d_f_origin = numpy.zeros((20,1000))
    # Squared displacement form origin
    

    for i in range(20):

        x_data = position([20, 40])[:,0]
        y_data = position([20, 40])[:,1]
        s_d_f_initial[i] = ((20-x_data)**2+(40-y_data)**2)
        s_d_f_origin[i] = (x_data**2+y_data**2)

    MSD_i = numpy.average(s_d_f_initial, axis=0)
    MSD_f = numpy.average(s_d_f_origin, axis=0)       

        
    return MSD_i, MSD_f
       
y_axis = numpy.arange(0, 50, 0.1)
x_axis = numpy.arange(0, 40, 0.1)

dat = numpy.zeros((len(y_axis), len(x_axis)))

for iy, y in enumerate(y_axis):
    for ix, x in enumerate(x_axis):
        dat[iy, ix] = energy_density((x, y))

pyplot.subplot(221)        
for i in range(20):

    position_list = position([20, 40])

    x = position_list[: ,0]
    y = position_list[: ,1]
    
    pyplot.subplot(221)
    pyplot.plot(x,y)
    
    x0, y0 = 20, 40
    x_f, y_f = x[-1], y[-1]
    x_TR = x0, x_f
    y_TR = y0, y_f
    pyplot.subplot(222)
    pyplot.plot(x_TR, y_TR, marker='o')
    
    

MSD_i, MSD_f = MSD([20, 40])

pyplot.xlabel('x /microns')
pyplot.ylabel('y /microns')
pyplot.title('Inital and final bacteria position')
pyplot.tight_layout()

pyplot.subplot(221)
im = pyplot.imshow(dat, extent = (-20, 40, -20, 50),
                   origin = 'lower', cmap = matplotlib.cm.gray,
                   aspect = 'auto')
pyplot.colorbar(im, orientation = 'vertical', label = 'energy density')
pyplot.xlabel('x /microns')
pyplot.ylabel('y /microns')
pyplot.title('Bacteria trajectory')
pyplot.tight_layout()

pyplot.subplot(212)
pyplot.plot(timebase, MSD_i, label = 'from origin', color = 'blue')
pyplot.plot(timebase, MSD_f, label = 'from Max energy', color = 'green')
pyplot.title('Mean Squared diplacement')
pyplot.xlabel('Time')
pyplot.ylabel('MSD')
pyplot.legend(loc= 'lower right')              
pyplot.tight_layout()
pyplot.show()
    


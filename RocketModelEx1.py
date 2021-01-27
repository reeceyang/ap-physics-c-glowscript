from vpython import *
#GlowScript 2.9 VPython

# constants

# variables
m0 = 4000 + 8800 # kg - initial mass of the rocket
m = m0 # kg - mass of the rocket
fuelrate = 129.4 # kg/s - rate at which the rocket burns fuel
thrust # N - thrust force produced by rocket
v = 0 # m/s - velocity of the rocket
a  # m/s^2 - acceleration of the rocket
v_exhaust = 2050 # m/s - exhaust velocity of the rocket
x = 0 # m - current position of the rocket
t = 0 # s - time
dt = 0.01 # s - change in time

window1=graph(height=200, xtitle='Time (s)', ytitle = 'Altitude (m)')  #create the first plot window
pos_plot = gcurve(color=color.red) #specify plotting in the window above
window2 = graph(height=200, xtitle='Time(s)', ytitle= 'Velocity (m/s)')  #create second plot window
vel_plot = gcurve(color=color.blue)  #specify plotting in window above
window3 = graph(height=200, xtitle='Time(s)', ytitle= 'Acceleration (m/s)')  #create third plot window
acc_plot = gcurve(color=color.blue)  #specify plotting in window above

#loop while the rocket still has fuel
while m > 4000:
    # calculate thrust
    thrust = v_exhaust * (fuelrate * dt) / dt
    
    #calculate acceleration
    a = thrust / m
    
    #calculate velocity and position
    v += a * dt
    x += v * dt
    
    #plot the position, velocity, and acceleration
    pos_plot.plot(t, x)
    vel_plot.plot(t, v)
    acc_plot.plot(t, a)
    
    #update the mass of the rocket and the time
    m -= fuelrate * dt
    t += dt
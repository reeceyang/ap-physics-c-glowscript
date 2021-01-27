from vpython import *
#GlowScript 2.9 VPython

# constants
G = 6.674 / (10**11) # Nm^2/kg^2 - gravitational constant
r = 6.3781 * (10**6) # m - approximate radius of the earth
m_earth = 5.9722 * (10**24) # kg - approximate mass of the earth

# variables
m0 = 4000 + 8800 # kg
m = m0 # kg
fuelrate = 129.4 # kg/s
thrust # N
v = 0 # m/s
a # m/s^2
Fnet # N - net force
Fg # N - force of gravity
v_exhaust = 2050 # m/s
x = 0
t = 0 # s
dt = 0.01 # s

window1=graph(height=200, xtitle='Time (s)', ytitle = 'Altitude (m)')  #create the first plot window
pos_plot = gcurve(color=color.red) #specify plotting in the window above
window2 = graph(height=200, xtitle='Time(s)', ytitle= 'Velocity (m/s)')  #create second plot window
vel_plot = gcurve(color=color.blue)  #specify plotting in window above
window3 = graph(height=200, xtitle='Time(s)', ytitle= 'Acceleration (m/s)')  #create third plot window
acc_plot = gcurve(color=color.blue)  #specify plotting in window above

while x >= 0:
    if m > 4000:
        thrust = v_exhaust * (fuelrate * dt) / dt
    else:
        thrust = 0
    
    #calculate the force of gravity using Newton's law of universal gravitation
    Fg = G * m_earth * m / ((r + x) * (r + x))
    
    Fnet = thrust - Fg
    a = Fnet / m
    v += a * dt
    x += v * dt
    
    pos_plot.plot(t, x)
    vel_plot.plot(t, v)
    acc_plot.plot(t, a)
    
    if m > 4000:
        m -= fuelrate * dt
    t += dt
from vpython import *
#GlowScript 2.9 VPython

# constants
g = 9.8 # m/s - acceleration of gravity

# variables
m0 = 4000 + 8800 # kg
m = m0
fuelrate = 129.4 # kg/s
thrust # N
v = 0 # m/s
a # m/s^2
f # N - net force
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

#loop while the rocket is above the ground (position is greater than 0)
while x >= 0:
    # calculate thrust if there is fuel remaining, otherwise set thrust to 0
    if m > 4000:
        thrust = v_exhaust * (fuelrate * dt) / dt
    else:
        thrust = 0
    
    # caculate net force and acceleration
    f = thrust - m * g
    a = f / m
    
    v += a * dt
    x += v * dt
    
    pos_plot.plot(t, x)
    vel_plot.plot(t, v)
    acc_plot.plot(t, a)
    
    # decrease mass of rocket only if fuel is remaining
    if m > 4000:
        m -= fuelrate * dt
    t += dt
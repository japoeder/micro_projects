# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 14:16:05 2021

@author: jonathan
"""

# Set t, dt, and G parameters for simulation
#t = 50000 # total time of simulation
t = 157788000 # total time of simulation
dt = 25000.0 # time delta
G = 6.67E-11

# Create lists for each planetary body
earth = [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24]
mars = [2.2790e+11, 0.0000e+00, 0.0000e+00, 2.4100e+04, 6.4190e+23]
mercury = [5.7900e+10, 0.0000e+00, 0.0000e+00, 4.7900e+04, 3.3020e+23]
sun = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]
venus = [1.0820e+11, 0.0000e+00, 0.0000e+00, 3.5000e+04, 4.8690e+24]

# Create nested list for looping later
nBodies = [earth, mars, mercury, sun, venus]

# Build function to run calculations
print()
def runCalcs(aBody, bBody, tStep, time):
    
    # Break out coordinates for initial r calculation
    pAx = aBody[0]
    pAy = aBody[1]
    pBx = bBody[0]
    pBy = bBody[1]
        
    # Do the same for initial velocities and mass
    vAx = aBody[2]
    vAy = aBody[3]
    aMass = aBody[4]
    bMass = bBody[4]

    # Set counter for while loop
    t_total = 0
    
    # Begin while loop simulation
    while t_total < time:
        
        # Calculate Euclidian distance
        r = ((pBx-pAx)**2 + (pBy-pAy)**2)**(1/2)
        
        # Calculate the total force F
        # Start with the case where r == 0 to avoid divide by 0 error
        if r == 0:
            F = 0
            Fx = 0
            Fy = 0
        
        # Calculate for cases where r != 0
        else:
            # Calc total force F
            F = G * ((aMass * bMass) / r**2)    
            
            # Calculate individual force components
            Fx = F * ((pBx - pAx) / r)
            Fy = F * ((pBy - pAy) / r)

        # In the following calcs, 'A' corresponds to the first body, and 'B' the 2nd.
        # Calculate acceleration in x and y direction
        aAx = Fx / aMass
        aAy = Fy / aMass    
        
        # Calculate velocity in x and y direction
        vAx = vAx + aAx * tStep
        vAy = vAy + aAy * tStep 

        # Calculate updated positions
        pAx = pAx + vAx * tStep
        pAy = pAy + vAy * tStep 
        
        # Update loop counter
        t_total += tStep
        
    # Add results to a dictionary so can be easily printed
    res = {'mX':"{:.4e}".format(aBody[4])
        , 'mY':"{:.4e}".format(bBody[4])
        , 'r':"{:.4e}".format(r)
        , 'F':"{:.4e}".format(F)
        , 'Fx':"{:.4e}".format(Fx)
        , 'Fy':"{:.4e}".format(Fy)
        , 'aAx':"{:.4e}".format(aAx)
        , 'aAy':"{:.4e}".format(aAy)
        , 'vAx':"{:.4e}".format(vAx)
        , 'vAy':"{:.4e}".format(vAy)
        , 'pAx':"{:.4e}".format(pAx)
        , 'pAy':"{:.4e}".format(pAy)
        }

    # Print the final results for a given body / sun combo
    print(res['pAx'], res['pAy'], res['vAx'], res['vAy'], res['mX'])

for n in nBodies:
    runCalcs(n, sun, dt, t)
#pip install matplotlib, pip install pylab
from pylab import *
print("Make a half-life graph over isotopes. Write only numbers if marked with '[n]'.")

#Variables
i = input("What isotope? ")
isotop = i.capitalize() 
t = input("What form of time (day, minute, year...)? ")
tidsenhet = t.capitalize()

halv = float(input("What is the half-life [n]? "))
me = (input("What form of mass (Atoms, Kg...)? "))
mass_enhet = me.capitalize()

mass = float(input("How much mass [n]? "))
tider = int(input("How many half-lives [n]? "))


tid = [0]
N = [mass]

for i in range (1, tider+1):             
    tid.append(halv*i)   
    mass_igjen = N[i-1]*(0.5)
    N.append(mass_igjen) 

scatter(tid, N) 
plot(tid, N)
xlabel(tidsenhet) 
ylabel(mass_enhet + " av " + isotop) 
grid() 
show() 

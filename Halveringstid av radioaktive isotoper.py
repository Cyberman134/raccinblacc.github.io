#pip install matplotlib, pip install pylab (i terminalen)
from pylab import *
print("Her kan du lage en graf over halveringstid av radioaktive isotoper. Skriv kun nummer i spørsmål markert med '[n]'.")

#Variabler
i = input("Hvilke isotop? ")
isotop = i.capitalize() #Capitalise gjør første bokstav til stor bokstav

t = input("Hva er tidsenheten (Dag, Minutter, År...)? ")
tidsenhet = t.capitalize()

halv = float(input("Hva er halveringstiden [n]? "))
me = (input("Hvilke masseenhet (Atomkjerner, Kg...)? "))
mass_enhet = me.capitalize()

mass = float(input("Hvor mye masse [n]? "))
tider = int(input("Hvor mange halveringstider har du lyst på [n]? "))


#Lager lister
tid = [0]
N = [mass]

for i in range (1, tider+1):             
    tid.append(halv*i)    # Legger til halveringstid i listen tid (h_tid, 2*h_tid, 3*h_tid, ...)
    
    # Beregner antall kjerner igjen (halvparten av forrige antall kjerner)
    mass_igjen = N[i-1]*(0.5)
    
    # Legger til antall kjerner igjen i listen N
    N.append(mass_igjen) 

scatter(tid, N) # scatter() fungerer som plot(), men lager punkter i stedet for en sammenhengende linje
plot(tid, N)
xlabel(tidsenhet) # Skriver på tittel langs førsteaksen
ylabel(mass_enhet + " av " + isotop) # Skriver på tittel langs andreaksen
grid() # Tegner inn et rutenett
show() # Viser grafen

# a program that calculates velocity
def velocity():
    displacement=int(input("Input The Displacement: "))
    time=int(input("Input The Time: "))
    velocity=displacement/time
    print("The Velocity Is: ",velocity)
    return velocity
# a program that calculates acceleration
def acceleration():
    velocity=int(input("Input The Velocity: "))
    time=int(input("Input The Time: "))
    acceleration=velocity/time
    print("The Acceleration Is: ",acceleration)
    return acceleration
# a program that calculates force
def force():
    mass=int(input("Input The Mass: "))
    acceleration=int(input("Input The Acceleration: "))
    force=mass*acceleration
    print("The Force Is: ",force)
    return force
# a program that calculates momentum
def momentum():
    mass=int(input("Input The Mass: "))
    velocity=int(input("Input The Velocity: "))
    momentum=mass*velocity
    print("The Momentum Is: ",momentum)
    return momentum
# a program that calculates energy
def energy():
    mass=int(input("Input The Mass: "))
    velocity=int(input("Input The Velocity: "))
    energy=mass*velocity**2
    print("The Energy Is: ",energy)
    return energy
# a program that calculates power
def power():
    work=int(input("Input The Work: "))
    time=int(input("Input The Time: "))
    power=work/time
    print("The Power Is: ",power)
    return power
# a program that calculates work
def work():
    force=int(input("Input The Force: "))
    distance=int(input("Input The Distance: "))
    work=force*distance
    print("The Work Is: ",work)
    return work
# a program that calculates pressure
def pressure():
    force=int(input("Input The Force: "))
    area=int(input("Input The Area: "))
    pressure=force/area
    print("The Pressure Is: ",pressure)
    return pressure
# a program that calculates density
def density():
    mass=int(input("Input The Mass: "))
    volume=int(input("Input The Volume: "))
    density=mass/volume
    print("The Density Is: ",density)
    return density
# a program that calculates frequency
def frequency():
    period=int(input("Input The Period: "))
    frequency=1/period
    print("The Frequency Is: ",frequency)
    return frequency
# a program that calculates period
def period():
    frequency=int(input("Input The Frequency: "))
    period=1/frequency
    print("The Period Is: ",period)
    return period
# a program that calculates wavelength
def wavelength():
    frequency=int(input("Input The Frequency: "))
    wavelength=3*10**8/frequency
    print("The Wavelength Is: ",wavelength)
    return wavelength
# a program that calculates speed
def speed():
    distance=int(input("Input The Distance: "))
    time=int(input("Input The Time: "))
    speed=distance/time
    print("The Speed Is: ",speed)
    return speed
# a program that calculates current
def current():
    charge=int(input("Input The Charge: "))
    time=int(input("Input The Time: "))
    current=charge/time
    print("The Current Is: ",current)
    return current
# a program that calculates resistance
def resistance():
    voltage=int(input("Input The Voltage: "))
    current=int(input("Input The Current: "))
    resistance=voltage/current
    print("The Resistance Is: ",resistance)
    return resistance
# a program that calculates voltage
def voltage():
    current=int(input("Input The Current: "))
    resistance=int(input("Input The Resistance: "))
    voltage=current*resistance
    print("The Voltage Is: ",voltage)
    return voltage
# a program that calculates capacitance
def capacitance():
    charge=int(input("Input The Charge: "))
    voltage=int(input("Input The Voltage: "))
    capacitance=charge/voltage
    print("The Capacitance Is: ",capacitance)
    return capacitance
# a program that calculates displacement
def displacement():
    velocity=int(input("Input The Velocity: "))
    time=int(input("Input The Time: "))
    displacement=velocity*time
    print("The Displacement Is: ",displacement)
    return displacement
# a program that calculates mass
def mass():
    density=int(input("Input The Density: "))
    volume=int(input("Input The Volume: "))
    mass=density*volume
    print("The Mass Is: ",mass)
    return
# a program that calculates volume
def volume():
    mass=int(input("Input The Mass: "))
    density=int(input("Input The Density: "))
    volume=mass/density
    print("The Volume Is: ",volume)
    return volume
# a program that calculates charge
def charge():
    current=int(input("Input The Current: "))
    time=int(input("Input The Time: "))
    charge=current*time
    print("The Charge Is: ",charge)
    return charge
# a program that calculates area
def area():
    length=int(input("Input The Length: "))
    width=int(input("Input The Width: "))
    area=length*width
    print("The Area Is: ",area)
    return area

def main():
    print("welcm to the physics calculator")
    choice=int(input("1. velocity | 2. acceleration | 3. force \n 4. momentum | 5. energy | 6. power \n 7. work | 8. pressure | 9. density \n 10. frequency | 11. period | 12. wavelength \n 13. speed | 14. current | 15. resistance \n 16. voltage | 17. capacitance | 18. displacement \n 19. mass | 20. volume | 21. charge \n 22. area\n Enter Your Choice: "))

    if choice==1:
        velocity()
    elif choice==2:
        acceleration()
    elif choice==3:
        force()
    elif choice==4:
        momentum()
    elif choice==5:
        energy()
    elif choice==6:
        power()
    elif choice==7:
        work()
    elif choice==8:
        pressure()
    elif choice==9:
        density()
    elif choice==10:
        frequency()
    elif choice==11:
        period()
    elif choice==12:
        wavelength()
    elif choice==13:
        speed()
    elif choice==14:
        current()
    elif choice==15:
        resistance()
    elif choice==16:
        voltage()
    elif choice==17:
        capacitance()
    elif choice==18:
        displacement()
    elif choice==19:
        mass()
    elif choice==20:
        volume()
    elif choice==21:
        charge()
    elif choice==22:
        area()
    else:
        print("invalid choice")
main()
def again():
    print("would you like to run the programme again?")
    yesorno=input("y/n")
    if yesorno=="y":
        main()
    elif yesorno=="n":
        print("thanks for using the programme")


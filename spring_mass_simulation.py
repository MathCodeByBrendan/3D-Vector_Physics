def s():
    # Get spring constant
    while True:
        try:
            k = float(input("Enter k (N/m): "))
            if k <= 0:
                print("k must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a number.")

    g = 9.81
    system = []

    # get masses, calculate displacement
    while True:
        mass_str = input("Enter mass, else press enter to exit: ").strip()
        if not mass_str:
            break

        try:
            mass = float(mass_str)
            if mass <= 0:
                print("Mass must be gretaer than 0")
                continue

        except ValueError:
            print("Mass must be a number greater than 0, eg: 1234.34. Enter as number.")
            continue

        system.append((mass, mass * g / k))
    print(f"The displacements of the masses hanging from the spring with spring coefficient = {k} pulled down by gravity:")
    print("Mass (kg)     Stretch(m)")
    print("--------     -----------")
    for mass, stretch in system:
        print(f'{mass: 8.2f}    {stretch: 11.4f}')
    
s()
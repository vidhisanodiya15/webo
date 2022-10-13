Harsh = int(input("age of first person"))
vidhi = int(input(" age of second person"))
vedant = int(input("age of third person"))
vedika = int(input("age of fourth person"))

if Harsh>vidhi:
    print("vidhi is youngest")

if vidhi>vedant:
    print("vedant is youngest")

if vedant<Harsh:
    print("vedant is youngest")

if vedika<vedant:
    print("vedika is youngest")

if vedika<vidhi:
    print("vidhi is oldest")


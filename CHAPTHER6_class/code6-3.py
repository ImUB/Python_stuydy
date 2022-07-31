class Diva:
    version = "v3"

    def __init__(self, name = "Diva"):
        self.name = name

diva1 = Diva()
diva2 = Diva("Miku")
diva3 = Diva("Hana")

def print_diva_info(diva):
    print("====")
    print("Name: ", diva.name)
    print("Version: ", diva.version)

Diva.version = "v4"

print_diva_info(diva1)
print_diva_info(diva2)
print_diva_info(diva3)

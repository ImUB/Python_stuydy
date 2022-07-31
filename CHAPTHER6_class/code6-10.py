class Diva:
    version = "v3"

    def __init__(self, name = "Diva"):
        self.name = name
    def song(self, title="song"):
        print(self.name + " sing the",title)
    def medley(self):
        self.song()
        self.song("second song")
        self.song("third song")

class Miku(Diva):
    def __init__(self, module="class uniform"):
        self.module = module
        super().__init__("miku")
    def dance(self):
        print("Dancing!")

hatsune_miku = Miku()
print(hatsune_miku.module)
print(hatsune_miku.version)
print(hatsune_miku.name)
hatsune_miku.dance()
hatsune_miku.song("Hello")

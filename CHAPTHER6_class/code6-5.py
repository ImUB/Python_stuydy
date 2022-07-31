class Diva:
    version = "v3"

    def __init__(self, name = "Diva"):
        self.name = name
    def song(self, title="song"):
        print(self.name + " sing the ", title)
    def medley(self):
        self.song()
        self.song("second song")
        self.song("third song")

voice_diva = Diva("Hana")
voice_diva.song()
voice_diva.song("World is Mine")
voice_diva.medley()

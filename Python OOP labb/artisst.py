
class Artist:
    def __init__(self, name):
        self._name=name
        self.albums=[]

        

    def addAlbum(self, album):
        self.albums.append(album)
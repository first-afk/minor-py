class Cinema:
    def __init__(self, room, popcorn, name) -> None:
        self.room = room
        self._snack = popcorn
        self.__owner = name
        

    def getOwner(self):
        print(self.__owner)

date = Cinema(34, 'butter', 'Esther')
# date.getOwner()
# print(date.room)            

                   
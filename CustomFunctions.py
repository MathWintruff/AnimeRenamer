class AnimeEpisode:
    
    def __init__(self, Name):
        self.rawName = Name
        self.treatedName = str()
        self.finalName = str()
        self.seasonNumber = str()
        self.episodeNumber = str()
        GetAditionalInfoByRawName(self)
    
    def GetAditionalInfoByRawName(self):
        animeNameTreated = str()
        epNumUntreated = str()
        epNum = str()
        FinalReturn = list()

        for index in range(self.rawName.count("[")):
            bracketsPosition = [self.rawName.index("["), self.rawName.index("]")]
            self.rawName = self.rawName[:bracketsPosition[0]] + self.rawName[bracketsPosition[1]+1:]
        for index in range(self.rawName.count("(")):
            bracketsPosition = [self.rawName.index("("), self.rawName.index(")")]
            self.rawName = self.rawName[:bracketsPosition[0]] + self.rawName[bracketsPosition[1]+1:]
            
        animeNameTreated = animeNameTreated.join(self.rawName)
        self.treatedName = animeNameTreated.strip()

        if " " in animeNameTreated:
            animeNameTreated =  animeNameTreated.split()
        else:
            animeNameTreated =  animeNameTreated.split("_")

        epNumUntreated = list(animeNameTreated[-1])
        
        for letter in epNumUntreated:
            if letter in "0123456789":
                epNum += letter

        self.episodeNumber = epNum
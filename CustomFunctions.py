class AnimeEpisode:
    
    def __init__(self, Name):
        self.rawName = Name
        self.treatedName = str()
        self.finalName = str()
        self.seasonNumber = str()
        self.episodeNumber = str()
        self.GetAditionalInfoByRawName()
    
    def GetAditionalInfoByRawName(self):
        animeNameTreated = str()
        epNumUntreated = str()
        epNum = str()
        FinalReturn = list()
        rawName = self.rawName

        for index in range(rawName.count("[")):
            bracketsPosition = [rawName.index("["), rawName.index("]")]
            rawName = rawName[:bracketsPosition[0]] + rawName[bracketsPosition[1]+1:]
        for index in range(rawName.count("(")):
            bracketsPosition = [rawName.index("("), rawName.index(")")]
            rawName = rawName[:bracketsPosition[0]] + rawName[bracketsPosition[1]+1:]

        animeNameTreated = animeNameTreated.join(rawName)
        self.treatedName = animeNameTreated.strip()

        if " " in animeNameTreated:
            animeNameTreated =  animeNameTreated.split()
        else:
            animeNameTreated =  animeNameTreated.split("_")

        epNumUntreated = list(animeNameTreated[-1])

        if 'E' in epNumUntreated:
            epNum = epNum.join(epNumUntreated[epNumUntreated.index('E')+1:])
        else:
            epNum = epNum.join(epNumUntreated)

        self.episodeNumber = epNum
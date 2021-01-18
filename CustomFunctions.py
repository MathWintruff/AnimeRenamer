class AnimeEpisodeClass:
    
    def __init__(self, animeName, seasonStr, rawName, episodePath):
        self.animeName = animeName
        self.seasonStr = seasonStr
        self.rawName = rawName
        self.path = episodePath
        self.fileFormat = str()
        self.seasonNumber = str()
        self.episodeNumber = str()
        self.finalName = str()

        self.GetAditionalInfo()
    
    def GetAditionalInfo(self):
        #region Declarations
        epNumUntreated = str()
        epNum = str()
        FinalReturn = list()
        rawName = self.rawName
        treatedName = str()
        #endregion

        #region Get File Format
        rawName  = rawName.split(".")
        self.fileFormat = rawName[-1]
        #endregion
        
        #region Treating rawName
        rawName  = " ".join(rawName[:-1])
        for _ in range(rawName.count("[")):
            rawName = rawName[:rawName.index("[")] + rawName[rawName.index("]")+1:]
        for _ in range(rawName.count("(")):
            rawName = rawName[:rawName.index("(")] + rawName[rawName.index(")")+1:]
        animeNameTreated = str().join(rawName)
        if "END" in animeNameTreated:
            animeNameTreated = animeNameTreated.replace("END", "")
        elif "end" in animeNameTreated:
            animeNameTreated = animeNameTreated.replace("end", "")
        elif "End" in animeNameTreated:
            animeNameTreated = animeNameTreated.replace("End", "")
        #endregion
        
        #region Get Episode Number
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
        #endregion

        #region Get Season Number
        self.seasonNumber = self.seasonStr.split()[-1]

        if int(self.seasonNumber) < 10:
            self.seasonNumber = f"0{self.seasonNumber}"
        #endregion

        #region Make Final Name
        self.finalName = f"{self.animeName} S{self.seasonNumber}E{self.episodeNumber}.{self.fileFormat}"
        #endregion

    def PrintAllInfo(self):
        print("\n")
        print(f"O RawName é: {self.rawName}")
        print(f"O seasonStr é: {self.seasonStr}")
        print(f"O animeName é: {self.animeName}")
        print(f"O fileFormat é: {self.fileFormat}")
        print(f"O seasonNumber é: {self.seasonNumber}")
        print(f"O episodeNumber é: {self.episodeNumber}")
        print(f"O finalName é: {self.finalName}")
        print("\n")
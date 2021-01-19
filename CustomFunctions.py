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
        animeNameTreated = animeNameTreated.strip(" ")
        animeNameTreated = animeNameTreated.strip("-")
        animeNameTreated = animeNameTreated.strip("_")
        #endregion
        
        #region Get Season Number
        if "Ova" in self.seasonStr:
            self.seasonNumber = "Ova"
        else:
            if int(self.seasonStr.split()[-1]) < 10:
                self.seasonNumber = f"S0{self.seasonStr.split()[-1]}"
            else:
                self.seasonNumber = f"S{self.seasonStr.split()[-1]}"
        #endregion

        #region Get Episode Number
        if " " in animeNameTreated:
            animeNameTreated =  animeNameTreated.split()
        elif "_" in animeNameTreated:
            animeNameTreated =  animeNameTreated.split("_")
        elif "-" in animeNameTreated:
            animeNameTreated =  animeNameTreated.split("-")

        epNumUntreated = list(animeNameTreated[-1])

        if 'E' in epNumUntreated:
            epNum = epNum.join(epNumUntreated[epNumUntreated.index('E')+1:])
        else:
            epNum = epNum.join(epNumUntreated)
            for char in epNum:
                if char not in "0123456789":
                    epNum = epNum.replace(char, "")

        if "Ova" in self.seasonNumber:
            self.episodeNumber = epNum
        else:
            self.episodeNumber = f"E{epNum}"
        #endregion

        #region Make Final Name
        self.finalName = f"{self.animeName} {self.seasonNumber}{self.episodeNumber}.{self.fileFormat}"
        #endregion

    def PrintAllInfo(self):
        print("\n")
        print(f"the RawName is: {self.rawName}")
        print(f"the animeName is: {self.animeName}")
        print(f"the fileFormat is: {self.fileFormat}")
        print(f"the seasonNumber is: {self.seasonNumber}")
        print(f"the episodeNumber is: {self.episodeNumber}")
        print(f"the seasonStr is: {self.seasonStr}")
        print(f"the finalName is: {self.finalName}")
        print("\n")
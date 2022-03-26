from AnimeEpisodeClass import *
from OtoPy.UsefulTools import *
import os

Logger = OLogger(streamLogging=False, fileLogging=True)
bestLogo =[
 "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
 "@                                                                                                                 @",
 "@         #########       ################         #########         #######        #######        ########       @",
 "@      ###############    ################      ###############      ########      ########       #########       @",
 "@    ###################  ################    ###################    #########    #########       ##########      @",
 "@   ##################### ################   #####################   ######################      ###########      @",
 "@  ########       ########     ######       ########       ########  ######################      ############     @",
 "@ #######           ######     ######      ########          ####### ######################     #############     @",
 "@ #######           #######    ######      #######           ####### ######################     ######  ######    @",
 "@ #######           #######    ######      #######           ####### ######  ######  ######    ######   ######    @",
 "@ ########         #######     ######       #######         ######## ######   ####   ######   ######## ########   @",
 "@  ########       ########     ######       #########      ########  ######          ######   ##################  @",
 "@   #####################      ########   ########################   ######          ######  ###################  @",
 "@    ###################        #################################    ######          ######  #################### @",
 "@      ###############           ##############################      ######          ###### ######         ###### @",
 "@         ########                 ############     ########         ######          ###### ######         ###### @",
 "@                                                                                    ######                       @",
 "@                                                                                    ######                       @",
 "@                                                                                    ######                       @",
 "@                                                                                    ######                       @",
 "@                                                                                                                 @",
 "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
]

for line in bestLogo:
    print(line.replace("@", "%"))
print()

try:
    if "Animes" not in list(os.listdir('.')):
        os.mkdir("Animes")
        Logger.LogWarning("Animes folder created")
except:
    Logger.LogExceptError("An Error has occourred, the traceback of the error is:\n")



allDirectoriesList = os.listdir('./Animes')
seasonDir = list()
AnimeEpisodesList = list()
animeToRename = list()
totalAnimesRenamed = 0

Logger.LogInfo("Starting the Reanaming action")

try:
    GetingAnimesPB = OProgressBar(len(allDirectoriesList), prefix="Getting Animes to rename: ",suffix="Obtained", length=50)
    for i,animeDir in enumerate(allDirectoriesList):
        seasonDir = os.listdir(f'./Animes/{animeDir}')
        GetingAnimesPB.PrintProgress(i+1)
        for season in seasonDir:
            AnimeEpisodesList = os.listdir(f"./Animes/{animeDir}/{season}")
            for animeEpisode in AnimeEpisodesList:
                animeToRename.append(AnimeEpisodeClass(animeDir, season, animeEpisode, f"./Animes/{animeDir}/{season}/"))
    print("All Animes Obtained!\n")

    RenamingAnimesPB = OTimedProgressBar(len(animeToRename), Etc=True, prefix="Renaming Animes: ",suffix="")
    for i,episode in enumerate(animeToRename):
        os.rename(rf"{episode.path}{episode.rawName}",rf"{episode.path}{episode.finalName}")
        Logger.LogInfo(f"The anime:||> {episode.rawName} <|| Was renamed to:||> {episode.finalName} <||")
        RenamingAnimesPB.PrintProgress(i+1)
        totalAnimesRenamed = i+1
    print(f"{totalAnimesRenamed} Anime's Episodes Renamed!")
except:
    Logger.LogExceptError("An Error has occourred, the traceback of the error is:\n")

Logger.LogInfo(f"{totalAnimesRenamed} Anime's Episodes Renamed! Total time to rename was: {RenamingAnimesPB.GetLasElapsedTime()}")

input("Press enter to close!")
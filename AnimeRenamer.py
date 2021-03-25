from CustomFunctions import *
from Logger import *
import os
import traceback
from OtoPy.OtomaTools import *

pb = OProgressBar(100)
pb.PrintProgess(50)
print()
exit()

try:
    if "Animes" not in list(os.listdir('.')):
        os.mkdir("Animes")
        LogAnWarning("Animes folder created")
except:
    LogAnError(f"An Error has occourred, the traceback of the error is:\n{traceback.format_exc()}")



allDirectoriesList = os.listdir('./Animes')
seasonDir = list()
AnimeEpisodesList = list()
animeToRename = list()

LogAnWarning("Starting the Reanaming action")

try:
    for animeDir in allDirectoriesList:
        seasonDir = os.listdir(f'./Animes/{animeDir}')
        for season in seasonDir:
            AnimeEpisodesList = os.listdir(f"./Animes/{animeDir}/{season}")
            for animeEpisode in AnimeEpisodesList:
                animeToRename.append(AnimeEpisodeClass(animeDir, season, animeEpisode, f"./Animes/{animeDir}/{season}/"))

    for episode in animeToRename:
        os.rename(rf"{episode.path}{episode.rawName}",rf"{episode.path}{episode.finalName}")
        LogAnInfo(f"The anime:||> {episode.rawName} <|| Was renamed to:||> {episode.finalName} <||")
except:
    LogAnError(f"An Error has occourred, the traceback of the error is:\n{traceback.format_exc()}")

LogAnWarning("Finalizing the Reanaming action")
from CustomFunctions import *
from Logger import *
import os
import traceback

allDirectoriesList = os.listdir('./Animes')
seasonDir = list()
AnimeEpisodesList = list()
animeToRename = list()

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
    LogAnError(f"\nAn Error has occourred, the traceback of the error is:\n{traceback.format_exc()}\n")
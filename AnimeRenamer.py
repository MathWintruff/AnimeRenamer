from CustomFunctions import *
import os

allDirectoriesList = os.listdir('./Animes')
seasonDir = list()
AnimeEpisodesList = list()
animeToRename = list()

for animeDir in allDirectoriesList:
    seasonDir = os.listdir(f'./Animes/{animeDir}')
    for season in seasonDir:
        AnimeEpisodesList = os.listdir(f"./Animes/{animeDir}/{season}")
        for animeEpisode in AnimeEpisodesList:
            animeToRename.append(AnimeEpisodeClass(animeDir, season, animeEpisode, f"./Animes/{animeDir}/{season}/"))

for episode in animeToRename:
    os.rename(rf"{episode.path}{episode.rawName}",rf"{episode.path}{episode.finalName}")
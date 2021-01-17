from CustomFunctions import *
import os

"""
allDirectoriesList = os.listdir('./Animes')
seasonDirectory = list()
animePath = list()

for dir in allDirectoriesList:
    print(dir)
    seasonDirectory = os.listdir(f'./Animes/{dir}')
    for season in seasonDirectory:
        print(f'>{season}')
        AllanimesPath = os.listdir(f'./Animes/{dir}/{season}')
        for animePath in AllanimesPath:
            FileFormat = animePath.split('.')[-1]
            print(f'>>{animePath}  File Format: {FileFormat}')
"""
    






animeTest = AnimeEpisode("[AnimesTC] Re.Zero kara Hajimeru Isekai Seikatsu 2nd Season - 06 [1080p]")

print(animeTest.rawName)
print(animeTest.treatedName)
print(animeTest.episodeNumber)
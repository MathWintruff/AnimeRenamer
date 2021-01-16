def AnimeEpisodeDiscover(animeName):
    animeNameTreated = str()
    epNumUntreated = str()
    epNum = str()

    for index in range(animeName.count("[")):
        bracketsPosition = [animeName.index("["), animeName.index("]")]
        animeName = animeName[:bracketsPosition[0]] + animeName[bracketsPosition[1]+1:]
    for index in range(animeName.count("(")):
        bracketsPosition = [animeName.index("("), animeName.index(")")]
        animeName = animeName[:bracketsPosition[0]] + animeName[bracketsPosition[1]+1:]
        
    animeNameTreated = animeNameTreated.join(animeName)

    if " " in animeNameTreated:
        animeNameTreated =  animeNameTreated.split()
    else:
        animeNameTreated =  animeNameTreated.split("_")

    epNumUntreated = list(animeNameTreated[-1])
    
    for letter in epNumUntreated:
        if letter in "0123456789":
            epNum += letter

    return epNum
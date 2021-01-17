import os

allDirectoriesList = os.listdir('.')

for dir in allDirectoriesList:

    if '.' in dir:
        print(f'esse dir: {dir} nao e uma pasta')
    else:
        print(dir)
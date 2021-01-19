import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s -- %(message)s", datefmt="%Y-%m-%d|%H:%M:%S")
logTime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

Filelogger = logging.getLogger("MainLogger")
fileHandler = logging.FileHandler(f"./Logs/Log-{logTime}.log")
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
Filelogger.addHandler(fileHandler)

def LogAnInfo(infoMessege):
    Filelogger.info(infoMessege)

def LogAnWarning(WarningMessege):
    Filelogger.warning(WarningMessege)

def LogAnError(errorMessege):
    Filelogger.error(errorMessege)
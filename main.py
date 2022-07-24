import logging, logging_tz
import logging.handlers
import os

import requests

datefmt = '%Y-%m-%d %H:%M:%S%z'
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
formatter = logging_tz.LocalFormatter(fmt='%(asctime)s %(message)s', datefmt=datefmt)
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise


if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    r = requests.get('https://weather.talkpython.fm/api/weather/?city=Raipur&country=IN')
    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
        forcastss = data["weather"]["description"]
        logger.info(f'Weather in Raipur: {temperature}')
        logger.info(f'Forcast in Raipur: {forcastss}')

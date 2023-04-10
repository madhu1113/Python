#
import logging

logging.basicConfig(filename="test4.log", level = logging.INFO, format= '%(levelname)s %(name)s %(asctime)s %(message)s ')
# Whether the things should be logged or not that will be  decided by 'level' which depends on severity number.
try:
    logging.info("I am trying to read a file")
    with open("madhu.txt", "r"):
        logging.open("suucessfuly it has read the file")
except Exception as e:
    logging.critical("This is a situation for us")
    logging.error(e) # This line logs only error in the log file
    logging.exception(e) # This line logs the error with the exception i.e line no., file location etc. in the log file.
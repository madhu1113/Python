# How to get timestamp in log file??
import logging


logging.basicConfig(filename="test2.log", level = logging.DEBUG, format= '%(levelname)s %(name)s %(asctime)s %(message)s ')# Store timestamp also. It will take time from system and message from next line.
logging.info("This is my log with timestamp")
# %(levelname)s --> This gives log level in log fle
# %(name)s --> This gives system name in log fle
# %(asctime)s --> This gives system time in log fle
# %(message)s  --> This gives the messages we write inside logging.info() in log file.

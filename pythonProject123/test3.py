# Real use of logging??
# Understand the hierarchy of logging
import logging

# logging.basicConfig(filename="test3.log", level = logging.DEBUG, format= '%(levelname)s %(name)s %(asctime)s %(message)s ')
# logging.basicConfig(filename="test3.log", level = logging.ERROR) # This won't log anything inside the log file since level is Error
# logging.basicConfig(filename="test3.log", level = logging.CRITICAL) # It won't log anything inside log file since it's level is CRITICAL.
logging.basicConfig(filename="test3.log", level = logging.WARNING) # It will log only Warning, Error and Critical but not debug and info.
# It will log only exception but not info since level is warning whose severity level is 30 and info severity level is 20 so it won't log that.
def divide(a,b) :
    logging.info("The number entered by user is %s and %s", a,b) # Store the user input
    try:
        logging.info("We are into function")
        div = a/b
        logging.info("We have completed s dividion operation")
        logging.info("The result of code is %s", div) # Print the result in log file
        return div
    except Exception as e:
        logging.exception(e)
        print(e)
(divide(3,0))
# How to do logging?? What is the use if logging?
import logging
logging.basicConfig(filename="test.log", level = logging.INFO)
logging.info("This is my first code for logging")
# After execting this code a log file named "test.log" got created
# Now the file is completely empty
# But by including  this code "level = logging.INFO" in 2nd line. logging info will get created inside test.log file.
# we have many types of logging level like warning-->show the warning, debug-->use in case of investigation or diagnosis, info--> In case of generic ingormation, error--> In case of exception,critical--> In case of severe error etc.
# Severity label for different logging levels:- Debug- 10(means least severe), Info - 20, warning- 30, Error-40, Critical - 50(Most severe)
logging.warning(("This will try to load warning messages"))
logging.error("This is an error message")
l = [1,2,3,4,5,6,7,7]

for i in l:
    if i == 2:
        # logging.info(i) # Here 2 will get printed inside log file.
        logging.info(l) # Here kist will get printed.
        logging.warning("this is a warning for a user that they have found out 2 in list ")

logging.shutdown() # It will not log anything after this line.

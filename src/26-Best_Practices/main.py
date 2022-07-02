import logging

"""
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
"""

# try:
#    1/2
# except ZeroDivisionError:
#    logging.warning("Divide by zero error")
# except Exception:
#    logging.critical("Other exception")
# finally:
#    logging.info("Cleaning up...")

try:
   logging.debug('This is a debug message')
except BaseException as err:
   logging.error("Error: %s", err)
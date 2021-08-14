#! python3
# examples of pythonic code

import subprocess, locale
import logging
logging.basicConfig(filename='runningCommandsFromAPython_Program_log_filename.txt',\
                    level=logging.DEBUG,\
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('This is a log message.')

procObj = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE)
outputStr = procObj.stdout.decode(locale.getdefaultlocale()[1])
print(outputStr)
# another way of doing the same thing as above 3 lines
subprocess.run(['ls', '-la'])

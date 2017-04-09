import logging
"""create log file inputting file name,date ,message etc"""
def log_maker(write) :
	logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',
					datefmt='%d/%m/%Y %I:%M:%S %p',
					level=logging.DEBUG,
                    filename='log.txt',
                    filemode='w')
	logging.info(write)

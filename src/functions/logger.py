# Imports
import logging, os, pathlib

FORMAT = logging.Formatter(f'%(asctime)s: %(name)s: %(levelname)s: %(message)s')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(FORMAT)
logger.addHandler(console)

def createLogger(name, level):
	newLogger = logging.getLogger(name)
	logger.setLevel(logging.INFO)
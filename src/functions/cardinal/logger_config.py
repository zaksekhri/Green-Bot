# Imports
import logging, os, pathlib

# Class
class logC:
	"""docstring for logC"""
	def __init__(self, cardinal):
		super(logC, self).__init__()
		self.cardinal = cardinal

	# Global Variables
	basic_format = logging.Formatter(f'%(asctime)s: %(name)s: %(levelname)s: %(message)s')

	# Hard coded and used only once during primary run
	def cardinalLogger(self):
		name = "Cardinal"
		logger = logging.getLogger(name)
		logger.setLevel(logging.INFO)

		logger.addHandler(self.consoleOutput("info"))
		logger.addHandler(self.fileOutput(name, "error"))

		return logger

	def create_Logger(self, name, level, *, outputs):
		"""
		Creates a new logger with the provided args.

		Parameters:
			name:
				The name of the logger
			level:
				The desired logger level
			outputs:
				Where to dump the logs to

		Returns:
			The generated logger object
		"""
		logger = logging.getLogger(f"{name}")
		# level = level.upper()

		lvl = logging.getLevelName(level.upper())
		logger.setLevel(lvl)
		
		# if outputs is not None:
		if outputs != None:
			print("there are outputs")
			for output in outputs:
				print("for item in the list ig")
				if output == "console":
					logger.addHandler(self.consoleOutput(lvl))
				elif output == "file":
					logger.addHandler(self.fileOutput(name, lvl))
				else:
					print("u fucked up")
					self.cardinal.logger.error("Provided outputs are incorrect!")
		else:
			print("consle")
			logger.addHandler(self.consoleOutput(lvl))
		return logger

	## Outputs ----------------------

	# Used to setup log output to a file
	## https://www.w3schools.com/python/python_file_remove.asp -- used to see how to correctly check and remove a file
	def fileOutput(self, name, level):
		"""
		Creates a new logger with the provided args.

		Parameters:
			name:
				The name of the logger
				String
			level:
				The level of output for this output
				String or logging.lvl object

		Returns:
			File log path
		"""
		log_path = pathlib.Path.cwd() / 'logs'
		os.makedirs(log_path, mode=0o750, exist_ok=True)
		file = f"logs\\{name}_log.log"

		if os.path.exists(f"{file}"):  # Checks if the file already exists
			os.remove(f"{file}") # If it does then deletes it
		else:
			pass # if it doesnt exist then it does nothing
		output = logging.FileHandler(f"{file}")

		if isinstance(level, str):
			level = level.upper()
			lvl = logging._nameToLevel.get(level)
			output.setLevel(lvl)
		else:
			output.setLevel(level)
		
		output.setFormatter(self.basic_format)

		# logger.addHandler(file)
		return output

	# Used to setup log output to the console
	## https://stackoverflow.com/a/4843178
	## https://github.com/python/cpython/blob/master/Lib/logging/__init__.py#L98
	def consoleOutput(self, level):
		"""
		Creates a new logger with the provided args.

		Parameters:
			level:
				The level of output for this output
				String or logging.level level

		Returns:
			File log path
		"""
		output = logging.StreamHandler()

		if isinstance(level, str): # Checks if level is a string and configures it to use that lvl
			level = level.upper()
			lvl = logging._nameToLevel.get(level)
			output.setLevel(lvl)
		else:
			output.setLevel(level)

		output.setFormatter(self.basic_format)

		return output
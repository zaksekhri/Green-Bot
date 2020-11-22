#imports
import pygsheets

#class
class gsheets:
	"""Used internally to work with google sheets"""
	def __init__(self):
		# super(gsheets, self).__init__()
		self.gs = pygsheets.authorize(service_file='client_secret.json')
	
	def connect(self, spreadID):
		"""
		Returns a spreadsheet based on the provided id

		Parameters:
		    - spreadid: string, the id for the doc to connect to
		"""
		doc = self.gs.open_by_key(spreadID)
		return doc

	def quickstart(self, spreadID, sheetN):
		"""
		Returns a worksheet from a specific spreadsheet in one easy function.

		Parameters:
		    - spreadid: string, the id for the doc to connect to
		    - sheetN: string, the name of the worksheet to return
		"""
		doc = self.connect(spreadID)
		sheet = doc.worksheet_by_title(f"{sheetN}")
		return sheet
import infected_comp as src
import unittest

class TestInfectedComputers(unittest.TestCase):

	def setUp(self):
		self.testFile = 'testData_antiVirus.csv'
		self.correctResponse = 'AntiVirus_Reports: [\n{"ComputerName": "AAD-AAD77-L.CFS.UOGUELPH.CA", "Definitions Version": "1.163.1756.0", "FirstDetection": "2/1/2013 12:32", "InfectionCount": "11", "LastDetection": "29/07/2013 1:29:03 PM", "LastFullScanDateTimeEnd": "3/7/2012 14:13", "LastFullScanDateTimeStart": "3/7/2012 12:52", "LastQuickScanDateTimeEnd": "", "LastQuickScanDateTimeStart": "", "Remediation Status": "None"},\n]'

	def test_parsing(self):
		jsonResult = src.parseFile(self.testFile)
		self.assertEqual(jsonResult.strip(), self.correctResponse)

if __name__ == '__main__':
	unittest.main()

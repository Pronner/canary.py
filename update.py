## Canary.PY | update ##

class update:

	import CanaryAPI
	from CanaryAPI import updaterModule
	from CanaryAPI import errorhandler

	def main(self):

		CanaryAPI.checkForUpdates()

		CanaryAPI.validation = None

		for updates in updates:

			CanaryAPI.validateUpdates()
	        CanaryAPI.waitForValidation("5")

	        if CanaryAPI.validation = None:

	        	print("No updates were found, continuing build...")
	        	if errorhandler.ErrorFound == true:

	        		CanaryAPI.stopBuild()
	        		CanaryAPI.RunClass("canary.api.errorhandler") # errorhandler is defined in the API, therefore "errorhandler.py" does not exist.
	        	else:

	        		CanaryAPI.continueBuild()
	        else:

	        	print("An update was found, please wait...")
	        	print("Updating your version of canary.py...")

	        	CanaryAPI.updateModule("canary.module.python")
	        	CanaryAPI.updateModule("canary.py.krn86")

	        	CanaryAPI.updateFinish(rule.AfterUpdate, CanaryAPI.continueBuild())

	        	print("Update successful, please wait...")

	        	CanaryAPI.runClass("canary.api.errorhandler")

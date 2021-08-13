import sys, time, os 
from tqdm import tqdm


LegacyDir = os.getenv("HOME") + "/Backups/Legacy"
RetDir = os.getcwd()

if len(sys.argv) > 1:
	if sys.argv[1] == "Backup" and os.path.isdir(LegacyDir):
		print("Starting Upload Process")
		
		if os.path.isdir("/tmp/Legacy"):
			os.chdir("/tmp/Legacy")
			os.system("git pull -q")
			print("Identified Directory")

		else:
			os.system("git clone https://github.com/NxtDaemon/Legacy /tmp/Legacy")
			os.chdir("/tmp/Legacy")
			time.sleep(2)

		
		
		for file in tqdm (os.listdir(LegacyDir), desc="Processing Zips"):
			if not f"{file}.zip" in os.listdir("/tmp/Legacy"):
				os.system(f"zip {file}.zip -r {LegacyDir}/{file} -q -9")
			else: 
				print(f"[*] Detected Duplicate File : {file}")

		os.system("git add . && git commit -m 'Adding challenge backups' && git push -u origin master")

	elif sys.argv[1] != "Backup":
		print("Usage : Python3 LegacyUpload.py <Mode>")
		print("Mode Not Supported")


	elif not os.path.isdir(LegacyDir):
		print("Legacy Directory Cannot be found")

else:
	print("Usage : Python3 LegacyUpload.py <Mode>")
	print("Mode Not Detected")


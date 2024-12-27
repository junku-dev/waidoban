import os
import subprocess
import re
from util import check_whitespace

def get_files(path:str) -> list:
	files: list[str] = []
	f: str = ""
	try:
		if os.path.isdir(path):
			#get all file names in dir
			for f in os.listdir(path):
				
				if not os.path.isfile(path+'/'+f) or not '.pdf' in f:
					continue

				f = format_file_name(path, f)
				files.append(f)
			return files
		
		if os.path.isfile(path):
			file: str = path.split("/")[-1]
			file = format_file_name(path, file)
			files.append(file)
			return files
	except:
		print('bad input:', path, 'does not exits...')
		raise
	
	return

def format_file_name(path:str, file:str) -> str:
	try:
		og_file: str = file
		special: str = '[^a-zA-Z0-9 \n\.]'
		if re.search(special,file) :
			file = re.sub(special, '',file)

		if check_whitespace(file):
				file = file.replace(" ", "")

		if og_file != file:
			cmd = f"mv {path}/'{og_file}' {path}/{file}"
			subprocess.call(cmd, shell=True)
		return file
	except:
		print("error...")
		raise

def cut_pages(path:str, file:str, begin:int, end:int) -> None:
	cmd = f"qpdf {path}/{file} --pages . {begin}-{end} -- --replace-input"
	subprocess.call(cmd, shell=True)
import subprocess

def cut_pages(path:str, file:str, begin:int, end:int) -> None:
	cmd = f"qpdf {path}/{file} --pages . {begin}-{end} -- --replace-input"
	subprocess.call(cmd, shell=True)
import os
import subprocess
from op_ebooks import process_ebooks
from process_files import get_files, cut_pages
from util import get_page_count, cut_page_info

def choose() -> int:
	menu:str = '''
		1. Optimize PDFs - optimize pdfs to reduce file size\n
		2. Cut Pages - make a copy with a specified page range\n
		3. Compress to .rar file - compress pdfs for safe and efficient storage\n
		4. Help
	'''
	print(menu)
	
	sel:int = int(input("select an operation: "))
	return sel

def getPath() -> str:
	path:str = input("\nenter directory or file path: ")
	return os.path.abspath(path)

def app() -> None:
	is_quit:int = 0
	while is_quit == 0:
		files:list = []
		selection:int = choose()
		path = getPath()
		files = get_files(path)
		
		if selection == 1:
			process_ebooks(path, files)
		
		elif selection == 2:
			cut_page_info()
			b: int = int(input("\nstarting page: ")) #start
			e:int = int(input("ending page: ")) #end
			for file in files:
				if e == -1: #-1 - get the last page
					end = get_page_count(path, file)
					print("\nlast page:",end)
					print(f'creating a new file with range: {b}-{end}')
					cut_pages(path, file, b, end)
					print('\ndone.')
				else:
					print(f'\ncreating a new file with range: {b}-{e}')
					cut_pages(path, file, b, e)
					print('done.')
		
		elif selection == 3 or selection == 4:
			print('this feature is WIP lol')
		
		else:
			print("bad input...\ntry again.\n")
			continue
		
		q:str = input("\nquit? (y/n): ")
		
		if q == "y":
			is_quit = 1
			subprocess.call(f'open {path}', shell=True)


if __name__ == "__main__":
	app()
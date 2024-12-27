import subprocess
from util import pdf_setting_info

def process_ebooks(path:str,files:list) -> None:
    try:
        pdf_setting_info()
        size: int = int(input("select compression: "))
        for f in files:
            comp: str = ''
            if size == 1:
                comp = 'screen'

            elif size == 2:
                comp = 'ebook'

            elif size == 3:
                comp = 'prepess'
                
            else:
                print('bad input...')
            
            if not comp:
                print("-dPDFSetting was not set...")
                return

            cmd: str = f"gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/{comp} -dNOPAUSE -dQUIET -dBATCH -dDetectDuplicateImages=true -sOutputFile={path}/comp_{f} {path}/{f}"
            print("\nfile:",f)
            print("running:",cmd)
            subprocess.call(cmd, shell=True)

        print("complete.")
    except:
        print("unexpected error...")
        raise
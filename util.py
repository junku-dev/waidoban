import re
import PyPDF2

def check_whitespace(f:str) -> bool:
    return bool(re.search(r"\s", f))

def create_output_name(path:str, f:str) -> str:
    return f"{path}/compressed_{f}"

# not sure if this will be needed...
# def unlock_pdf(path:str, file:str):
#     cmd = f"qpdf --remove-restrictions -decrypt {path}/'{file}'"
#     print(cmd)

def get_page_count(path:str , file:str) -> int:
    f:str = path + "/" + file
    book = open(f, 'rb')
    pdf = PyPDF2.PdfReader(book)
    return len(pdf.pages)

def cut_page_info() -> None:
    info:str = "info:"
    print("="*100, "\n"+info+"\n" + "-" * len(info), "\nspecify a range of pages. i.e '1-5'",'\nstarting page > 0.\nyou can use "-1" to get the last page if the length is not known.\n' + '='*100)

def pdf_setting_info() -> None:
    print("="*100,"\ncompressions options:\n1. screen - 72dpi images\n2.ebook - 150dpi\n3.prepress - 300dpi\n" + "="*100)
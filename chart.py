import os
from main import get_files, get_path

def do_sort(lst:list) -> list:
    sorted_list:list = sorted(lst)
    return sorted_list

def convert_bytes(b:int) -> str:
    return f"{b/1000000} MB"

def chart_files() -> None:
    path:str = get_path()
    files: list[str] = get_files(path)
    files = do_sort(files)
    chart_data: list[list[str]] = [["~~~Final Results~~~"], ["file name:", "\tfile size:"], []]
    for f in files:
        byte_size:int = os.path.getsize(path + "/" + f)
        row:list[str] = [f, f"\t{convert_bytes(byte_size)}"]
        chart_data.append(row)
    w:int = max(len(data) for row in chart_data for data in row)
    for row in chart_data:
        print("".join(data.ljust(w) for data in row))


if __name__ == "__main__":
    chart_files()
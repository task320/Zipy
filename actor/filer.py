from os import path as os_path
from os import walk
from errorclass.zipyerror import ZipyError
import re

EXTENTION_ZIP = r'.zip'

def get_zip_file_list_path(path):
    if os_path.isdir(path):
        return get_zip_file_list_path_from_dir(path)
    elif os_path.isfile(path):
        return [path]

    raise ZipyError("指定したパスに、ファイル、またはディレクトリが存在しません。")

def get_zip_file_list_path_from_dir(dir_path):
    file_list = []

    for (dir_path, dir_name, files_name) in walk(dir_path):
        for file_name in files_name:
            full_path = os_path.join(dir_path.encode("shift-jis").decode("shift-jis"), file_name.encode("shift-jis").decode("shift-jis"))
            file_list.append(full_path)

    return file_list

def get_zip_file_path(path):
    split_path = []
    split_path = os_path.split(path)
    
    return os_path.join(split_path[0], get_zip_file_name(split_path[1]))

def get_zip_file_name(str):
    return re.sub(r'\.[^.]+$', '', str) + EXTENTION_ZIP


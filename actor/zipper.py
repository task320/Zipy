import subprocess as sr
from errorclass.zipyerror import ZipyError
import actor.filer as filer

def create_zip_file(path, password, level):
    zip_file_path = filer.get_zip_file_path(path)

    compress_to_zip(path, zip_file_path, password)
    
    
def compress_to_zip(dir_path, zip_file_path, password):
    try:
        p = sr.Popen(["zip", "-e", "-r", zip_file_path, dir_path, "-P", password, "-j"],  stdout=sr.PIPE)
        output, err = p.communicate()
        print(output)
    except:
        raise ZipyError("ZIP圧縮に失敗しました。")
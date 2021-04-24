from os import walk, system, mkdir, path, getenv
from collections import defaultdict
from shutil import rmtree, copyfile
import fnmatch

def get_filenames(resultsdir:str) -> dict:
    dirs = []
    for (dirpath, dirnames, filenames) in walk(resultsdir):
        dirs.extend(dirnames)

    dir_to_filenames = defaultdict(list)
    for d in dirs:
        for (dirpath, dirnames, filenames) in walk(f'{resultsdir}/{d}'):
            dir_to_filenames[d].extend(fnmatch.filter(filenames, '*.bzip2'))

    return dir_to_filenames

def create_report_dir(reportsdir:str):
    if path.exists(reportsdir) and path.isdir(reportsdir):
        rmtree(reportsdir)
    mkdir(reportsdir)

def generate_reports(resultsdir:str, reportsdir:str, filenames:dict):
    for key, files in filenames.items():
        for f in files:
            new_dir = f'{reportsdir}/{key}'
            if not path.exists(new_dir):
                mkdir(new_dir)
            copyfile(f'{resultsdir}/{key}/{f}', f'{new_dir}/{f}')
            system(f'bunzip2 {new_dir}/{f}')
            system(f'oscap xccdf generate report {new_dir}/{f}.out > {new_dir}/{f.replace(".xml.bzip2", ".html")}')
            # print(f'oscap xccdf generate report {new_dir}/{f}.out > {new_dir}/{f.replace(".xml.bzip2", ".html")}')

def get_path(relativedir:str) -> str:
    return '/'.join(filter(None, [base_path, relativedir]))

# main
base_path = getenv('BASE_PATH')
reportsdir = get_path('reportsdir')
resultsdir = get_path('resultsdir')
create_report_dir(reportsdir)
generate_reports(resultsdir, reportsdir, get_filenames(resultsdir))

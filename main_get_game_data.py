# python mini project for scripting

# We are going to deal with command line arguments
# copy files or directories
# search files or directories
# os module
# sys module
# subprocess


# go needs to be installed from the link: https://go.dev/ because it's going to be used later in the program...


import os
import json
import shutil
from subprocess import PIPE, run  # to run any terminal command
import sys

from unicodedata import unidata_version

GAME_DIR_PATTERN = "game"
GAME_CODE_EXTENSION = ".go"
GAME_COMPILE_COMMAND = ["go", "build"]

# find the game directory in our folder
""" 
we need to make a command line argument, so that we can make the search dynamic 
eg in terminal: python.exe main_get_game_data /dest_dir /neww_data in order to search any instance of the hello word

And this should be run in cmd  
"""

def find_all_game_paths(source):
    game_paths = []

    for root, dirs, files in os.walk(source): #recursively look into the directories
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)

        break  #for us to do it one time

    return game_paths

def get_name_from_paths(paths, to_strip):
    new_names = []
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_strip, "")
        new_names.append(new_dir_name)

    return new_names


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def copy_and_overwrite(source, dest): #copy source to the destination
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)


def make_json_metadata_file(path, game_dirs):
    data = {
        "gameNames" : game_dirs,

        "numberOfGames" : len(game_dirs)
    }
    with open(path, "w") as file:
        json.dump(data, file)


def compile_game_code(path):
    code_file_name = None
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(GAME_CODE_EXTENSION):
                code_file_name = file
                break

        break

    if code_file_name is None:
        return
    command = GAME_COMPILE_COMMAND + [code_file_name]
    run_command(command, path)

def run_command(command, path):
    cwd = os.getcwd()
    os.chdir(path)

    result = run(command, stdout=PIPE, stdin=PIPE, universal_newlines = True)
    print("compile result", result)

    os.chdir(cwd)







def main(source, target):
    cwd = os.getcwd()  #current working directory (cwd)
    source_path = os.path.join(cwd, source)   # will join the path based on your OS
    target_path = os.path.join(cwd, target)

    game_paths = find_all_game_paths(source_path)
    new_game_dirs = get_name_from_paths(game_paths, "_game")

    create_dir(target_path)


    for src, dest in zip(game_paths, new_game_dirs):  # taking 2 elements from matching arrays and dump it into tuples
        dest_path = os.path.join(target_path, dest)
        copy_and_overwrite(src, dest_path)
        compile_game_code(dest_path)

    json_path = os.path.join(target_path, "metadata.json")

    make_json_metadata_file(json_path, new_game_dirs)

if __name__ == "__main__":
    args = sys.argv
    print(args)
# arguments check, it has to be 3

    if len(args) != 3:
        raise Exception("You must pass a source and target directory - only.")

    source, target = args[1:]
    main(source, target)







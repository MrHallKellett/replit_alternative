from os import listdir, path, getcwd, rename
from config import *
import platform
import ctypes
from importlib.util import spec_from_file_location, module_from_spec
from sys import modules
from db import Database

def hide_file(file_path):
    system_name = platform.system()
    
    if system_name == "Windows":
        # On Windows, use ctypes to set the file's attribute to hidden
        try:
            FILE_ATTRIBUTE_HIDDEN = 0x02
            attrs = ctypes.windll.kernel32.GetFileAttributesW(file_path)
            if attrs == -1:
                raise ctypes.WinError()
            if not attrs & FILE_ATTRIBUTE_HIDDEN:
                ctypes.windll.kernel32.SetFileAttributesW(file_path, attrs | FILE_ATTRIBUTE_HIDDEN)
            #print(f"File '{file_path}' has been hidden successfully on Windows.")
        except Exception as e:
            print(f"Failed to hide file on Windows: {e}")
    
    else:
        # On Unix-like systems, rename the file to start with a dot
        directory, filename = path.split(file_path)
        hidden_file_path = path.join(directory, f".{filename}")
        try:
            rename(file_path, hidden_file_path)
            #print(f"File '{file_path}' has been hidden successfully on {system_name}.")
        except Exception as e:
            print(f"Failed to hide file on {system_name}: {e}")


###############################

def load_module_from_path(path):
    def mod_name(name):
        return "".join(char for char in name if char.isalpha())
    module_name = mod_name(path)
    spec = spec_from_file_location(module_name, path)
    module = module_from_spec(spec)
    modules[module_name] = module
    spec.loader.exec_module(module)
    return module

###############################

def get_students() -> list[str]:
    students = {}
    # iterate student work folder
    for class_group in sorted(listdir(STU_WORK_PATH)):
        if not path.isdir(path.join(STU_WORK_PATH, class_group)):   continue
        print("Found class", class_group)
        this_path = path.join(STU_WORK_PATH, class_group)
        students[class_group] = []
        for student in sorted(listdir(this_path)):
            if not path.isdir(path.join(this_path, student)):   continue
            name = " ".join(student.split(" ")[4:][:-1])
            print("\tFound student", name)
            students[class_group].append((name, path.join(STU_WORK_PATH, class_group, student)))
    return students

###############################

def add_assignments_to_db():
    data = []
    for fn in listdir("assignments"):
        
        if path.isdir(path.join(getcwd(), "assignments", fn)):
            data.append((fn.split()[0], " ".join(fn.split()[1:])))


    
    q = """INSERT INTO assignment VALUES ("{}", "{}")"""
    for id_, ass_name in data:
        
        print(q.format(id_, ass_name))


if __name__ == "__main__":
    add_assignments_to_db()

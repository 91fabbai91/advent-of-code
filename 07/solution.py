import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from aoc_utils import timer_func, logging_func



class File():
    
    def __init__(self, properties: str):
        size, self._name = properties.split(" ")
        self._size = int(size)
    
    @property
    def size(self):
        return self._size

    @property
    def name(self):
        return self._name

class Directory():
    MAX_SIZE = 100000
    def __init__(self, properties: str):
        directory, name = properties.split(" ")
        if directory != 'dir':
            raise ValueError("Directory prefix needs to be dir, but was {directory}")
        self._name = name
        self._child_directories = []
        self._files = []
        self._parent_directory = None
        self._size = 0
        self._smaller_than_max_size = True
    
    def __repr__(self):
        return f"{self._name} {self._size}"


    def is_smaller_than_desired_size(self, desired_size: int):
        return self._size <= desired_size

    def is_bigger_than_desired_size(self, desired_size: int):
        return self._size >= desired_size

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size
    
    def add_size(self, size):
        self._size +=size
        

    @property
    def child_directories(self):
        return self._child_directories

    @property
    def files(self):
        return self._files

    @property
    def parent_directory(self):
        return self._parent_directory
    
    def add_child_directory(self, child_directory):
        child_directory.parent_directory = self
        self._child_directories.append(child_directory)

    def has_child_directories(self):
        return self._child_directories != []

    @parent_directory.setter
    def parent_directory(self, parent_directory):
        if self._parent_directory is not None:
            raise ValueError(f"Parent directory was set before in directory {self.name} was {self.parent_directory}")
        self._parent_directory = parent_directory

    def add_file(self, file: File):
        self._files.append(file)
        self._size +=file.size
        self._parent_directory.add_size(file.size)
        _parent_directory = self._parent_directory
        while _parent_directory.parent_directory is not None:
            _parent_directory.parent_directory.add_size(file.size)
            _parent_directory = _parent_directory.parent_directory
            



def parse_line(actual_directory: Directory, line: str):
    line = line.rstrip()
    if line.startswith("$ ls"):
        return actual_directory
    if line.startswith("$ cd"):
        if line.endswith("/"):
            return Directory("dir /")
        _, _, dir_name = line.split(" ")
        if(dir_name == ".."):
            return actual_directory.parent_directory
        return next(filter(lambda x: x.name == dir_name, actual_directory.child_directories))
    if line.startswith("dir"):
        child_directory = Directory(line)
        actual_directory.add_child_directory(child_directory)
        return actual_directory
    file_ = File(line)
    actual_directory.add_file(file_)
    return actual_directory

def traverse_directory(directory, size_list, size_limit):
    if directory.is_smaller_than_desired_size(size_limit):
        size_list.append(directory.size)
    if directory.has_child_directories():
        for child_directory in directory.child_directories:
            traverse_directory(child_directory, size_list, size_limit)

def traverse_directory_b(directory, size_list, size_limit):
    if directory.is_bigger_than_desired_size(size_limit):
        size_list.append(directory.size)
    if directory.has_child_directories():
        for child_directory in directory.child_directories:
            traverse_directory_b(child_directory, size_list, size_limit)

if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/input.txt",'r') as file: 
        lines = file.readlines()
        directory = None
        for line in lines:
            directory = parse_line(directory, line)
        while directory.parent_directory is not None:
            directory = directory.parent_directory
        blocked_memory = directory.size
        print(f"Outer most dir size {blocked_memory}")
        size_list_a = []
        traverse_directory(directory,size_list_a, 100000)
        print(f"Solution task 1 {sum(size_list_a)}")
        size_list_b = []
        minimum_required_memory= 30000000
        total_memory = 70000000
        traverse_directory_b(directory,size_list_b, minimum_required_memory-(total_memory-blocked_memory))
        print(f"Solution task 2 {min(size_list_b)}")
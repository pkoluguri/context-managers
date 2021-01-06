from contextlib import contextmanager
import os

#using context manager
@contextmanager
def change_dir(destination):
    #try is necissary to catch errors
    try:
        #getting the current word directory
        cwd = os.getcwd()
        #changing the dirctory to the destination
        os.chdir(destination)
        yield
    #after the try: process completes
    finally:
        #chanding the directory to the previous directory
        os.chdir(cwd)
#using chande_dir method
with change_dir("example-dir"):
    #listing the directory here we can do anything like making more files 
    print(os.listdir)
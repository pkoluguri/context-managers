from contextlib import contextmanager

#using context manager
@contextmanager
def open_file(filename,mode):
   #try is necissary to catch errors
   try: 
     #opening the file with the filename and filemode
     f=open(filename,mode)
     #returning the file with yeild
     yield f
    #after the try: process completes
   finally:
     #closing the files
     f.close()

#using the open_file method and using the file
with open_file("file.txt","w") as file:
    file.write("Test")
#checking wether th file is closed
print(file.closed)
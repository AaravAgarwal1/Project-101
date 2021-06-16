import dropbox
import os

from dropbox.files import WriteMode
print("helpo")
print(dropbox.__file__)

class TransferData:
    def __init__(self, access_token): #access_token property of transferDate class
        self.access_token=access_token

    def upload_files(self, file_from, file_to): #2 files- 1. file_from = from where the file should b tranferred 2. file_to- where should the file be transferred
        
        #enumerate local files
        for root,files in os.walk(file_from):
            
            for filename in files:
                #constructing local path
                local_path= os.path.join(root, filename)

                #construct dropbox path
                relative_path= os.path.relpath(local_path, file_from)
                dropbox_path= os.path.join(file_to, relative_path)
        

                dbx= dropbox.Dropbox(self.access_token) 
                #upload the file
                with open(local_path, 'rb') as f: #rb is read in binary mode
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))  #_upload is in built function. we open the file_from as f and then upload that in read mode to file_to (pretty simple

def main():
    access_token="NvjHc0kJ2FMAAAAAAAAAAaPbb47o2l18vYrBQz_X3YA7_f94gN7gyXt6evdU4Q06"
    transferData= TransferData(access_token)

    file_from=  input("Enter the name of the file to be uploaded: ") #/Users/HP/OneDrive/Desktop/whitehatjr Python/abcd.txt"
    file_to= "/project101_fileUploading/abcd.txt"

    transferData.upload_files(file_from, file_to)

if __name__=='__main__':
    main()




import os
import shutil

# The project is to Orgianize your files in folders.
# Place organize_directory.py In the folder where the files needs to be organized and run the code in the terminal.command: 'python organize_directory.py'

current_dir = os.path.dirname(os.path.realpath(__file__))  # The directory where the .py file exists
print('Welcome inorganize.py script -- Happy Clean Folder ! ')
for filename in os.listdir(current_dir):                   # List all files in this directory
    
    if filename.endswith((".png",".jpg",".gif",".jpeg")):  # Loop for all files that ends with images extension
        if not os.path.exists("images"):                   # To pervevent file already exists error
          os.mkdir('Images')                               
        shutil.copy(filename,"Images")                     # Copy all images stored in filename variaple into images directory
        os.remove(filename)
        print('Images Done')

    if filename.endswith((".py",".css",".html",".bash")):  # Loop for all files that ends with codes extension
        
        if not os.path.exists("codes"):                    # To pervevent file already exists erorr
          os.mkdir('codes')
        shutil.copy(filename,"codes")
        os.remove(filename)
        print('Codes Done')
        
    if filename.endswith((".mp4",".wav",".webm")):         # Loop for all files that ends with video extension
        
        if not os.path.exists("Videos"):                   # To pervevent file already exists erorr
          os.mkdir('Videos')
        shutil.copy(filename,"Videos")
        os.remove(filename)
        print('Videos Done')
        
    if filename.endswith((".pdf",".Doc",".txt")):          # Loop for all files that ends with Docs extension
        
        if not os.path.exists("Docs"):                     # To pervevent file already exists erorr
          os.mkdir('Docs')
        shutil.copy(filename,"Docs")
        os.remove(filename)
        print('Docs Done')
        
    if filename.endswith((".dmg",".exe")):                 # Loop for all files that ends with Apps extension
        
        if not os.path.exists("Apps"):                     # To pervevent file already exists erorr
          os.mkdir('Apps')
        shutil.copy(filename,"Apps")
        os.remove(filename)
        print('Apps Done')

print('Done Organizing !!')
import os, sys
import time

# Subdirectory the meme was played under
DIR = 'meme'
HEIGHT = 28

#2345% speedup
def run(frames):

    current_frame = 0

    for frame in frames:
        # Gets every line in the frame
        lines = frame.split('\n')

        for file in os.listdir(DIR):
            # Renames the files, uses the number at the start of the file name to get which line it should be
            # and to keep it in order
            file_num = str(file[:2])
            os.rename(f'{DIR}\{file}',f'{DIR}\{str(file_num)}{lines[int(file_num)+1]}')
        
        # Delay, because windows sadly delays the speed at which the filemanager can refresh file names
        time.sleep(0.7)

        # Prints which frame we are currently on
        print(' Playing:',str(current_frame) + '/' + str(len(frames)), end='\r')
        sys.stdout.flush()
        current_frame += 1
    
    print("Done.",end='\r')

def createFiles():

    for y in range(0,HEIGHT-1):

        if y < 10:
            y = '0' + str(y)

        open(f'{DIR}\\{str(y)}','w')

if __name__ == "__main__":
    
    # Opens raw file, with each ASCII frame inside
    raw = open('raw','r',encoding='utf-8').read()

    # Gets each frame, which is seperated by a comma
    frames = raw.split(',')

    # Creates files, and runs the animation
    createFiles()
    run(frames)
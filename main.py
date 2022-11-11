import os, shutil
from pytube import Playlist, YouTube

def run(pl):
    # insert the downloads destination (optional)
    # e.g. C:\Users\Username\Folder
    filepath = input("Downloads destination (optional): ")
    
    # insert the resolution option (required)
    # type 1 for 360p res and 2 for 1080p res
    resolution = int(input("Resolution 360p (1), 1080p (2): "))
    
    # get linked list of links in the playlist
    links = pl.video_urls
    
    # get each item in the list
    for l in links:
        os.system("cls")
        
        # converts the link to a YouTube object
        yt = YouTube(l)
        
        # takes first stream
        if resolution == 1:
            music = yt.streams.filter(file_extension="mp4", res="360p").first()
        elif resolution == 2:
            music = yt.streams.filter(file_extension="mp4", res="1080p").first()
        else:
            print("invalid option please try again ... ")
            
        default_filename = music.default_filename
        print(default_filename)
        print("Downloading " + default_filename + "...")
        
        # downloads first video stream and rename the first video stream
        music.download()
        default_filename_remove_spaces = default_filename.replace(" ", "")
        try:
            # if its already renamed then pass
            os.rename(default_filename, default_filename_remove_spaces)
        except:
            pass
            
        new_filename_remove_spaces = default_filename.replace(" ", "")
        
        # if exception then create download folder if not exists and store the downloaded audios
        try:
            # if filepath is empty then create download if not exists and store the downloaded audios
            if filepath == "":
                shutil.move(new_filename_remove_spaces, os.path.join(os.path.abspath("./Downloads"), new_filename_remove_spaces))
            else:
                shutil.move(new_filename_remove_spaces, os.path.join(os.path.abspath(filepath), new_filename_remove_spaces))
        except:
            if os.path.exists("./Downloads"):
                shutil.move(new_filename_remove_spaces, os.path.join(os.path.abspath("./Downloads"), new_filename_remove_spaces))
            else:
                os.makedirs("./Downloads")
                shutil.move(new_filename_remove_spaces, os.path.join(os.path.abspath("./Downloads"), new_filename_remove_spaces))
        
    print("Download finished.")

if __name__ == "__main__":
    url = input("Please enter the url of the playlist you wish to download: ")
    pl = Playlist(url)
    run(pl)

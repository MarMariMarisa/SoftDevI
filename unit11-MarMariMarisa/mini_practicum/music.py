class Time:
    __slots__ = ['hours', 'minutes', 'seconds']

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

class Song:
    __slots__ = ['title','artists', 'duration']

    def __init__(self,title,artists,duration):
       self.title = title
       self.artists = artists
       self.duration = duration

class Album:
    __slots__ = ['title','artists',"tracks","run_duration"]

    def __init__(self,title,artists,tracks):
        self.title = title
        self.artists = [artists]
        self.tracks = [tracks]
        hours = 0
        minutes = 0
        seconds = 0
        updating = True
        for track in tracks:
            track.duration.hours += hours
            track.duration.minutes += minutes
            track.duration.seconds += seconds
        while updating == True:
            if minutes >= 60 or seconds >= 60:
                if minutes >= 60:
                    minutes -= 60
                    hours += 1
                if seconds >= 60:
                    seconds -= 60
                    minutes += 1
            else:
                updating = False
        self.run_duration = Time(hours,minutes,seconds)
        
def print_album(album):
    print("Title:",album.title)
    print("Artists:")
    for artist in album.artists:
        print("\t",artist)
    print("Number of albums:", len(album.tracks))
    print("Total run duration:",get_time(album.run_duration))
    for track in album.tracks:
        """
        Im nore sure why the following print line does not work.
        track.title should be pulling the title instead i recieve an error meggage
        """
        print(track.title,"-",[[artist for artist in track.artists]],"-",track.duration)
        

def get_time(time):
    return '{}:{:02}:{:02}'.format(time.hours, time.minutes, time.seconds)

def main():
    song_1 = Song("inarticulation","Rio Romeo",Time(0,2,43))
    song_2 = Song("bet","Rio Romeo",Time(0,4,14))
    song_3 = Song("twice","Rio Romeo",Time(0,3,8))
    album = Album("Good God",["Rio Romeo"],[song_1,song_2,song_3])
    print_album(album)

if __name__ == "__main__":
    main()

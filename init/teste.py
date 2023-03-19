from pytube import  YouTube



YouTube('https://www.youtube.com/watch?v=fdC-3eW-yL8').streams.first().download()

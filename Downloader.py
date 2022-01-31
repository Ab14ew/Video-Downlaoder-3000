import pytube


link = input("url: ")

url = pytube.YouTube(link)
vid = url.streams.get_highest_resolution()
print(vid.title)
vid.download()
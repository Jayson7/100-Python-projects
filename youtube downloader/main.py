
import pytube

link = input("Enter the link: ")

yt = pytube.YouTube(link)

# download video in highest quality
stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first().download()
print("Downloaded", yt.title)
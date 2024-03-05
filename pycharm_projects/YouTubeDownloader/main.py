from pytube import YouTube

url = input("Enter the video url: ")

path = ""

YouTube(url).streams.get_highest_resolution().download(path)

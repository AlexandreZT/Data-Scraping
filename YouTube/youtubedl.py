import os
import re
import bs4
import requests
try:
    from pytube import YouTube
    from pytube import Playlist
except:
    print("Vérifie l'environnement que tu utilise")
    print("as tu essayé : pip install pytube3 ?")    

def video_to_mp3_dl(): # OK
    # https://www.youtube.com/watch?v=DklAU4GNpxA
    ytd = YouTube(input("URL de la vidéo à télécharger : "))
    ytd.streams.filter(only_audio=True).first().download()
    os.rename(ytd.title+".mp4", ytd.title+".mp3")

def video_to_mp4_dl(): # OK
    ytd = YouTube(input("URL de la vidéo à télécharger : "))
    ytd.streams.first().download()
    # https://www.youtube.com/watch?v=DklAU4GNpxA
    # https://www.youtube.com/watch?v=xzVvfOKmFaI
def playlist_to_mp3_dl():
    playlist=[]
    # url=input("Enter the Youtube Playlist URL : ") #Takes the Playlist Link
    url='https://www.youtube.com/watch?v=ynMk2EwRi4Q&list=OLAK5uy_kMJqubo0qbxFrNKEY5Do_LG27bs9fKmmk'
    data= requests.get(url)
    soup=bs4.BeautifulSoup(data.text,'html.parser')
    print(soup.find_all('a'))
    for links in soup.find_all('a'):
        link=links.get('href')
        if (link[0:6]=="/watch" and link[0]!="#"):
            link="https://www.youtube.com"+link
            link=str(link)
            playlist.append(link)

    print(playlist)

def playlist_to_mp4_dl():
    playlist = Playlist("https://www.youtube.com/watch?v=ynMk2EwRi4Q&list=OLAK5uy_kMJqubo0qbxFrNKEY5Do_LG27bs9fKmmk")
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    print("Nombre de vidéo dans la playlist :",len(playlist.video_urls))
    for video in playlist.video_urls:
        try:
            YouTube(video).first().download()
            print("La vidéo", video.title, "a été téléchargé")
        except KeyError as e:
            print(e)
        print(video)
    # print('Number of videos in playlist: %s' % len(pld.video_urls))
    # pld.download()

if __name__ == "__main__":
    choice = eval(input("""
Tappez 1 pour télécharger une video youtube au format mp3
Tappez 2 pour télécharger une video youtube au format mp4
Tappez 3 pour télécharger une playlist youtube au format mp4
Tappez 4 pour télécharger une playlist youtube au format mp4
: """))
    if choice == 1:
        video_to_mp3_dl() 

    elif choice == 2:
        video_to_mp4_dl()

    elif choice == 3:
        # print("Service indisponble pour le moment")
        playlist_to_mp3_dl()

    elif choice == 4:
        # print("Service indisponble pour le moment")
        playlist_to_mp4_dl()

    else: # choice != 1 and choice != 2 and choice != 3 and choice != 4
        print("Je ne comprends pas ta saisie")

import urllib.request
import os

# path = input("donne moi le lien de téléchargement : ")

# urllib.request.urlretrieve(path, 'video_name.mp4')



i = 76
while (i <= 76):
    urllib.request.urlretrieve("http://195.154.102.152/dbs/"+str(i)+".mp4", "DBS E"+str(i)+' VOSTFR.mp4')
    print("+1")
    i+=1

print("finito", i)
# os.system   ('shutdown -s')
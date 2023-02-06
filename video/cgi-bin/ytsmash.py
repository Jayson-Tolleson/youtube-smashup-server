#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# enable debugging
import cgitb
cgitb.enable()
import cgi
import os
import subprocess
from subprocess import Popen, PIPE, STDOUT, run
from pytube import Channel
from youtube_search import YoutubeSearch
import sys
import os

pid = str(os.getpid())

#python programming
searchterms = str(sys.argv[1])
number = int(sys.argv[2])
s1 = str(sys.argv[3])
make = ('cd /var/video && sudo mkdir '+pid)
subprocess.run(make, shell=True, stderr=subprocess.STDOUT)
make1 = ('cd /var/video/'+pid+' && sudo mkdir videos  && sudo mkdir videos2')
subprocess.run(make1, shell=True, stderr=subprocess.STDOUT)
try:
    if s1 := 'general':
     
        #General Search
        videos = []
        videos = YoutubeSearch(searchterms, max_results=number).to_dict()
        #download yt vids
        for v in videos:
            url_suffix = v['url_suffix']
            link = 'https://youtube.com'+(str(url_suffix))
            try: 
                dl = ('cd /var/video/'+pid+'/videos && sudo yt-dlp -f 22 %s')%(link)
                subprocess.call(dl, shell=True, stderr=subprocess.STDOUT)
            except:
                print ('1 dload failed!')
            print ('Download Completed!')
        print ('Download Task Completed!')
except:
    print ('channel')
try:
    if s1 := 'channel':

        #channel search
        c = Channel('https://www.youtube.com/'+searchterms+'/videos')

        #download yt vids
        for url in c.video_urls[:number]:
            link = url
            print (link)
            try: 
                dl = ('cd /var/video/'+pid+'/videos && sudo yt-dlp -f 22 %s')%(link)
                print (dl)
                subprocess.run(dl, shell=True, stderr=subprocess.STDOUT)
            except:
                print ('1 dload failed!')
            print ('Download Completed!')
        print ('Download Task Completed!')
except:
    print('general')

#slice up video
os.chdir('/var/video/'+pid+'/videos')
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = str(count)
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)
list = os.listdir('/var/video/'+pid+'/videos/')
print (list)
f= open("/var/video/"+pid+"/videos2/vidslist.txt","w+")
for l in list:
        cut0 = ('sudo ffmpeg -ss 0:00 -i /var/video/'+pid+'/videos/'+str(l)+' -t 12.0 -c:v copy -c:a copy -y /var/video/'+pid+'/videos2/0-'+str(l))
        subprocess.run(cut0, shell=True, stderr=subprocess.STDOUT)
        f.write("file /var/video/"+pid+"/videos2/0-%s\r\n" % l)
for l in list:
        cut1 = ('sudo ffmpeg -ss 5:00 -i /var/video/'+pid+'/videos/'+str(l)+' -t 12.0 -c:v copy -c:a copy -y /var/video/'+pid+'/videos2/1-'+str(l))
        subprocess.run(cut1, shell=True, stderr=subprocess.STDOUT)
        f.write("file /var/video/"+pid+"/videos2/1-%s\r\n" % l)
for l in list:
        cut2 = ('sudo ffmpeg -ss 10:00 -i /var/video/'+pid+'/videos/'+str(l)+' -t 12.0 -c:v copy -c:a copy -y /var/video/'+pid+'/videos2/2-'+str(l))
        subprocess.run(cut2, shell=True, stderr=subprocess.STDOUT)
        f.write("file /var/video/"+pid+"/videos2/2-%s\r\n" % l)
for l in list:
        cut3 = ('sudo ffmpeg -ss 15:00 -i /var/video/'+pid+'/videos/'+str(l)+' -t 12.0 -c:v copy -c:a copy -y /var/video/'+pid+'/videos2/3-'+str(l))
        subprocess.run(cut3, shell=True, stderr=subprocess.STDOUT)
        f.write("file /var/video/"+pid+"/videos2/3-%s\r\n" % l)

for l in list:
        cut10 = ('sudo ffmpeg -ss 0:30 -i /var/video/'+pid+'/videos/'+str(l)+' -t 12.0 -c:v copy -c:a copy -y /var/video/'+pid+'/videos2/10-'+str(l))
        subprocess.run(cut10, shell=True, stderr=subprocess.STDOUT)
        f.write("file /var/video/"+pid+"/videos2/10-%s\r\n" % l)
for l in list:
        cut11 = ('sudo ffmpeg -ss 5:30 -i /var/video/'+pid+'/videos/'+str(l)+' -t 12.0 -c:v copy -c:a copy -y /var/video/'+pid+'/videos2/11-'+str(l))
        subprocess.run(cut11, shell=True, stderr=subprocess.STDOUT)
        f.write("file /var/video/"+pid+"/videos2/11-%s\r\n" % l)
for l in list:
        cut12 = ('sudo ffmpeg -ss 10:30 -i /var/video/'+pid+'/videos/'+str(l)+' -t 12.0 -c:v copy -c:a copy -y /var/video/'+pid+'/videos2/12-'+str(l))
        subprocess.run(cut12, shell=True, stderr=subprocess.STDOUT)
        f.write("file /var/video/"+pid+"/videos2/12-%s\r\n" % l)
for l in list:
        cut13 = ('sudo ffmpeg -ss 15:30 -i /var/video/'+pid+'/videos/'+str(l)+' -t 12.0 -c:v copy -c:a copy -y /var/video/'+pid+'/videos2/13-'+str(l))
        subprocess.run(cut13, shell=True, stderr=subprocess.STDOUT)
        f.write("file /var/video/"+pid+"/videos2/13-%s\r\n" % l)

for l in list:
        cut20 = ('sudo ffmpeg -ss 1:00 -i /var/video/'+pid+'/videos/'+str(l)+' -t 12.0 -c:v copy -c:a copy -y /var/video/'+pid+'/videos2/20-'+str(l))
        subprocess.run(cut20, shell=True, stderr=subprocess.STDOUT)
        f.write("file /var/video/"+pid+"/videos2/20-%s\r\n" % l)
for l in list:
        cut21 = ('sudo ffmpeg -ss 8:00 -i /var/video/'+pid+'/videos/'+str(l)+' -t 12.0 -c:v copy -c:a copy -y /var/video/'+pid+'/videos2/21-'+str(l))
        subprocess.run(cut21, shell=True, stderr=subprocess.STDOUT)
        f.write("file /var/video/"+pid+"/videos2/21-%s\r\n" % l)
for l in list:
        cut22 = ('sudo ffmpeg -ss 12:00 -i /var/video/'+pid+'/videos/'+str(l)+' -t 12.0 -c:v copy -c:a copy -y /var/video/'+pid+'/videos2/22-'+str(l))
        subprocess.run(cut22, shell=True, stderr=subprocess.STDOUT)
        f.write("file /var/video/"+pid+"/videos2/22-%s\r\n" % l)
for l in list:
        cut23 = ('sudo ffmpeg -ss 18:00 -i /var/video/'+pid+'/videos/'+str(l)+' -t 12.0 -c:v copy -c:a copy -y /var/video/'+pid+'/videos2/23-'+str(l))
        subprocess.run(cut23, shell=True, stderr=subprocess.STDOUT)
        f.write("file /var/video/"+pid+"/videos2/23-%s\r\n" % l)

f.close()
print ('Starting FFMPEG...')
ffmpeg = ('''cd /var/video/'''+pid+'''/videos2/ && sudo ffmpeg -f concat -safe 0 -i vidslist.txt -vf mpdecimate,setpts=N/FRAME_RATE/TB -vcodec libx264 -crf 0 -vsync vfr -y output.mp4 && sudo cp output.mp4 /var/video/movies/'''+str(searchterms).replace(' ',',').replace('/',',')+str(number)+'''.mp4''')
subprocess.run(ffmpeg, shell=True, stderr=subprocess.STDOUT)
remove = ('cd /var/video/ && sudo rm -r '+pid) 
subprocess.run(remove, shell=True, stderr=subprocess.STDOUT)

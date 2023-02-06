YOUTUBE SMASH-UP COMPILER!!!
SERVER
ffmpeg yt-dlp python3 flask pytube youtube_search ....
port: 8000,8080

Instruction:

1. sudo git clone https://github.com/Jayson-Tolleson/youtube-smashup-server.git
2. cd youtube-smashup-server
3. sudo cp -r video /var
3. cd /var/video
4. sudo nano webserver.py and add your cert and key info
5. sudo mkdir movies
6. sudo nohup python3 webserver.py &
7. cd cgi-bin
8. sudo nano console-ytsmash.py add your same cert and key info
9. sudo nohup python3 console-ytsmash.py &

10. go to https://domain_name(.com or .biz):8000/ytsmash

RUN 

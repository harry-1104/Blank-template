clear
sudo docker run --rm \
-it --shm-size=512m -p 6901:6901 \
-e VNC_PW=password kasmweb/kali-rolling-desktop:1.13.0 bash
sudo docker rmi kasmweb/kali-rolling-desktop:1.13.0
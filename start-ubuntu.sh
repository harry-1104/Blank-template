clear
echo "[+] Ubuntu session starting ..."
sudo docker run --name=ubuntu-gnome --rm \
  --tmpfs /run --tmpfs /run/lock --tmpfs /tmp \
  --cgroupns=host --cap-add SYS_BOOT --cap-add SYS_ADMIN \
  -v /sys/fs/cgroup:/sys/fs/cgroup \
  -p 5901:5901 -p 6901:6901 \
  darkdragon001/ubuntu-gnome-vnc
sudo docker rmi darkdragon001/ubuntu-gnome-vnc
clear
echo "[+] Ubuntu session deleted"
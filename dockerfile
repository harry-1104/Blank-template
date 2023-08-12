FROM kalilinux/kali-rolling

RUN apt-get update && apt-get install -y \
    kali-tools-top10 \
    websockify \
    xfce4 \
    xfce4-terminal \
    firefox-esr \
    novnc

# Set the default browser for Xfce
RUN update-alternatives --install /usr/bin/x-www-browser x-www-browser /usr/bin/firefox-esr 100

# Start websockify to proxy the Xfce desktop to a web browser
CMD ["/bin/bash", "-c", "websockify --web /usr/share/novnc/ 0 localhost:5900"]

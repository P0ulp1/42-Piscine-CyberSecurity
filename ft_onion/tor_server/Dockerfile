FROM debian:bookworm

#Install TOR and dependancies
RUN apt update && apt upgrade -y && apt install --yes apt-transport-https gnupg wget bash
COPY ./conf/tor.sources /etc/apt/sources.list.d/tor.sources
RUN wget -qO- https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | gpg --dearmor | tee /usr/share/keyrings/deb.torproject.org-keyring.gpg >/dev/null
RUN apt update && apt install --yes tor deb.torproject.org-keyring nginx less procps systemctl curl sudo

#Configure Nginx and TOR
COPY ./conf/nginx.conf /etc/nginx/nginx.conf
COPY ./conf/torrc /etc/tor/torrc

CMD ["bash", "-c", "\
    service tor start && \
    nginx -g 'daemon off;' & \
    sleep 5 && \
    echo 'Adresse .onion:' && \
    cat /var/lib/tor/ft_onion/hostname && \
    wait"]

#!/bin/bash
service tor start
service ssh start
echo '.onion address: '
cat /var/lib/tor/ft_onion/hostname
nginx -g 'daemon off;'
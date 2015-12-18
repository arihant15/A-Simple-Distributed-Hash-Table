gnome-terminal --window-with-profile=P2P -e "bash -c python\ DIndexServer.py\ -c\ config.json\ -s\ 3340;bash" &
gnome-terminal --window-with-profile=P2P -e "bash -c python\ DIndexServer.py\ -c\ config.json\ -s\ 3341;bash" &
gnome-terminal --window-with-profile=P2P -e "bash -c python\ DIndexServer.py\ -c\ config.json\ -s\ 3342;bash" &
python Peer.py -c config.json
wait

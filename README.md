# wifi-kali-usage
wifi kali usage (wifite + hashcat + drivers)

# hashcat resources:
- https://resources.infosecinstitute.com/topic/hashcat-tutorial-beginners/

# Archer T4U V3 drivers:
- https://www.tp-link.com/ar/support/download/archer-t4u/

# airmon-ng resources:
- https://www.youtube.com/watch?v=WfYxrLaqlN8

# wifite resources:
- https://www.youtube.com/watch?v=TDVM-BUChpY&t=4s

# cap2hccapx
- @TODO

# wlan troubleshooting
- Run kali linux in vmware vm

- Useful commands to locate wlan connection:
```
ifconfig
ip addr
iwconfig
```
- Troubleshooting airmon-ng and enabling monitor mode
```
sudo airmon-ng check kill
sudo airmon-ng start wlan0
```
- Check that Mode is set to Monitor
```
iwconfig
sudo airmon-ng
```

# Starting with wifite
- Run wifite
```
sudo wifite
```
- Save the hcap file.
```
sudo hcxpcapngtool -o hash.hc22000 -E wordlist hash.cap  
#https://s77rt.github.io/capJS/
```
- Convert cap file to hc22000 file

- hashcat cracking with dict
```
hashcat -m 22000 -a 0 -o cracked.txt hash.hc22000 dict.txt 
```

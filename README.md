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


# wifite usage
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
- Run wifite
```
sudo wifite
```

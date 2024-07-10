# rs5online

### Des
This is a little process for "when you use ResPi5 but forget the cable(micro-HDMI)"
You can get the Webhook to know the SSID and private ip for access it via ssh.

### How to?
- Put the main.py to a folder where you want.

- Create Service

```
sudo vim /etc/systemd/system/teams-webhook.service
```

- Put it in online service

```
sudo systemctl enable teams-webhook.service
```

- Test

```
sudo systemctl start teams-webhook.service
```


Create By KeepElapsedTime , Kevin
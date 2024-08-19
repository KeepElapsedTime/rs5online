# rs5online (Raspberry Pi5 Online Notify)

### Des
This is a little process for "when you use Raspberry Pi5 but forget the cable(micro-HDMI)"
You can get the Webhook to know the SSID and private ip for access it via ssh.

### How to?

#### Change the info you have
- In main.py , change webhook url
```
webhook_url = 'YOUR_WEBHOOK_URL'
```
- In discord/teams-webhook.service , change python path & user name in Pi5
```
ExecStart=python3 /TO/YOUR/PYTHON/FILE/PATH/main.py
User=YOUR_USER_NAME
```


- Put the main.py to a folder where you want.

- Create Service

```
sudo vim /etc/systemd/system/teams-webhook.service
sudo vim /etc/systemd/system/discord-webhook.service
```

- Put it in online service

```
sudo systemctl enable teams-webhook.service
sudo systemctl enable discord-webhook.service
```

- Test

```
sudo systemctl start teams-webhook.service
sudo systemctl start discord-webhook.service
```


Create By KeepElapsedTime , Kevin

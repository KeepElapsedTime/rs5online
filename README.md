# rs5online

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


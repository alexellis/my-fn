# my-fn

Functions with secrets.

Seal secrets:

```
$ faas-cli cloud seal --name=alexellis-fn-secrets --literal incoming-webhook-url=https://hooks.slack.com/services/etc/etc/etc --literal key=key --literal slack-token=slack-token
```


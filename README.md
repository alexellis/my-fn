# my-fn

Functions with secrets.

* join-welcome - welcomes new people to #OpenFaaS on Slack
* slack-me - example SlackBot demo that responds go messages in #test-channel
* hallo - simple function in Go to show reading a SealedSecret

To seal the secrets:

```
$ faas-cli cloud seal \
 --name=alexellis-fn-secrets \
 --literal incoming-webhook-url=https://hooks.slack.com/services/etc/etc/etc \
 --literal key=key \
 --literal slack-token=slack-token
```

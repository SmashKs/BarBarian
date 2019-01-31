from slackclient import SlackClient

# slack_token = os.environ["SLACK_API_TOKEN"]
slack_token = 'xoxp-58290430992-58295179509-390329096501-721745dc66076c84815eaf4a2ab2a89a'
sc = SlackClient(slack_token)
sc.api_call(
        "chat.postMessage",
        as_user="jieyi",
        text="Hello from Python! :tada:"
)

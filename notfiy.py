from flask import Flask, request
import requests

app = Flask(__name__)

SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/a6dd521e768857fcfc285b85bb045b6e4db6152b0f723ade'

@app.route('/notify', methods=['POST'])
def notify_slack():
    data = request.json
    message = {
        'text': f"Deployment Status: {data['status']}\nEnvironment: {data['environment']}\nVersion: {data['version']}"
    }
    response = requests.post(SLACK_WEBHOOK_URL, json=message)
    return "Notification sent", response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=5000)

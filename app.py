from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/tiktok-followers')
def get_followers():
    follower_count = 12345  # Replace with real logic later
    return jsonify({
        "frames": [
            {
                "text": f"Followers: {follower_count}",
                "icon": None
            }
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)

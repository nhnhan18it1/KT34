from flask import Flask
from redis import Redis

app = Flask(__name__)
re = Redis(host="192.168.233.128",port=6379,password=123)

@app.route("/",methods=['GET'])
def index():
    return re.get("hello").decode("utf-8")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
from flask import Flask
from requests.models import Response
import os

app = Flask(__name__)


@app.route('/api/<version>')
def home(version):
    return f"API version {version}"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.logger.info(f"Running on {port}")
    app.run(debug=True, host='0.0.0.0', port=port)

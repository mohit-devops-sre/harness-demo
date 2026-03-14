from flask import Flask
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    """Health check endpoint"""
    logger.info("Health check request received")
    return {'status': 'healthy', 'message': 'pong'}, 200


@app.route('/', methods=['GET'])
def index():
    """Root endpoint displaying HARNESS DEMO"""
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Harness Demo</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                font-family: Arial, sans-serif;
            }
            .container {
                text-align: center;
            }
            h1 {
                color: white;
                font-size: 72px;
                margin: 0;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                animation: pulse 2s infinite;
            }
            @keyframes pulse {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.05); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>HARNESS DEMO</h1>
        </div>
    </body>
    </html>
    '''
    return html, 200, {'Content-Type': 'text/html'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)

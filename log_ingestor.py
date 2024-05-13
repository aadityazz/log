import os
from datetime import datetime
from flask import Flask, jsonify
import logging

app = Flask(__name__)

if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging for INFO logs
info_logger = logging.getLogger('info')
info_logger.setLevel(logging.INFO)
info_handler = logging.FileHandler('logs/log1.log')
info_formatter = logging.Formatter('{"level": "%(levelname)s", "log_string": "%(message)s", "timestamp": "%(asctime)s", "metadata": {"source": "log1.log"}}')
info_handler.setFormatter(info_formatter)
info_logger.addHandler(info_handler)

# Configure logging for ERROR logs
error_logger = logging.getLogger('error')
error_logger.setLevel(logging.ERROR)
error_handler = logging.FileHandler('logs/log2.log')
error_formatter = logging.Formatter('{"level": "%(levelname)s", "log_string": "%(message)s", "timestamp": "%(asctime)s", "metadata": {"source": "log2.log"}}')
error_handler.setFormatter(error_formatter)
error_logger.addHandler(error_handler)

# Configure logging for SUCCESS logs
success_logger = logging.getLogger('success')
success_logger.setLevel(logging.INFO)
success_handler = logging.FileHandler('logs/log3.log')
success_formatter = logging.Formatter('{"level": "%(levelname)s", "log_string": "%(message)s", "timestamp": "%(asctime)s", "metadata": {"source": "log3.log"}}')
success_handler.setFormatter(success_formatter)
success_logger.addHandler(success_handler)

# Log ingestion function
def ingest_log(logger, log_string):
    logger.info(log_string)

# Home Page -- INFO GET
@app.route('/infoget', methods=['GET'])
def info_get():
    log_string = 'Access the Home Page - INFO GET'
    ingest_log(info_logger, log_string)
    return jsonify({'log_string': log_string,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}), 200

# Home Page -- INFO DELETE
@app.route('/infodel', methods=['DELETE'])
def info_delete():
    log_string = 'Item Deleted - INFO DELETE'
    ingest_log(info_logger, log_string)
    return jsonify({'log_string': log_string,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}), 200

# Home Page -- ERROR GET
@app.route('/errget', methods=['GET'])
def err_get():
    log_string = 'Unable to access the Home Page - ERROR GET'
    ingest_log(error_logger, log_string)
    return jsonify({'log_string': log_string,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}), 400

# Home Page -- ERROR POST
@app.route('/errpost', methods=['POST'])
def err_post():
    log_string = 'Unable to send page - ERROR POST'
    ingest_log(error_logger, log_string)
    return jsonify({'log_string': log_string,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}), 400

# Home Page -- ERROR PUT
@app.route('/errput', methods=['PUT'])
def err_put():
    log_string = 'Unable to update page - ERROR PUT'
    ingest_log(error_logger, log_string)
    return jsonify({'log_string': log_string,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}), 400

# Home Page -- ERROR DELETE
@app.route('/errdel', methods=['DELETE'])
def err_delete():
    log_string = 'Unable to delete page - ERROR DELETE'
    ingest_log(error_logger, log_string)
    return jsonify({'log_string': log_string,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}), 400

# Home Page -- SUCCESS POST
@app.route('/sucpost', methods=['POST'])
def suc_post():
    log_string = 'Posted page successfully - SUCCESS POST'
    ingest_log(error_logger, log_string)
    return jsonify({'log_string': log_string,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}), 200

# Home Page -- SUCCESS PUT
@app.route('/sucput', methods=['PUT'])
def suc_put():
    log_string = 'Updated page successfully - SUCCESS PUT'
    ingest_log(success_logger, log_string)
    return jsonify({'log_string': log_string,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}), 200

# Home Page -- SUCCESS DELETE
@app.route('/sucdel', methods=['DELETE'])
def suc_delete():
    log_string = 'Deleted page successfully - SUCCESS DELETE'
    ingest_log(success_logger, log_string)
    return jsonify({'log_string': log_string,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}), 200

if __name__ == '__main__':
    app.run(debug=True)


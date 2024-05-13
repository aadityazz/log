from flask import Flask, render_template, request, jsonify
import os
import glob
import json
import re

app = Flask(__name__)

# Define the folder containing log files
LOG_FOLDER = 'logs'

# Function to search logs based on filters
def search_logs(query, filters):
    result = []
    log_files = glob.glob(os.path.join(LOG_FOLDER, '*.log'))

    for log_file in log_files:
        with open(log_file, 'r') as f:
            for line in f:
                log_data = json.loads(line)
                log_string = log_data.get('log_string', '')
                level = log_data.get('level', '')

                # Compile regex pattern for the query
                query_pattern = re.compile(re.escape(query), re.IGNORECASE)

                # Check if log_string or level matches the query pattern
                if query_pattern.search(log_string) or query_pattern.search(level):
                    match_filters = all(
                        re.search(re.escape(value), log_data.get(key, ''), re.IGNORECASE) for key, value in filters.items()
                    )
                    if match_filters:
                        result.append(log_data)

    return result




# Home page with search form
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


# Search results page
@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    level = request.form.get('level')
    log_string = request.form['log_string']
    timestamp = request.form['timestamp']
    source = request.form['source']

    filters = {}
    if level:
        filters['level'] = level
    if log_string:
        filters['log_string'] = log_string
    if timestamp:
        filters['timestamp'] = timestamp
    if source:
        filters['metadata.source'] = source

    #print(filters)
    search_result = search_logs(query, filters)
    return jsonify(search_result)


if __name__ == '__main__':
    app.run(debug=True)

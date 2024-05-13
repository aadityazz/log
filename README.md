# Log Search System

## Description
This project is a log search system that allows users to search through log files based on various filters such as query, level, log string, timestamp, and source. It utilizes Flask for the backend API and provides a simple web interface for users to interact with.

## How to Run
1. Clone the repository to your local machine:
[git clone](https://github.com/yourusername/log-search-system.git)
2. Navigate to the project directory:
cd log-search-system
3. Install the required dependencies using pip:
pip install -r requirements.txt
4. Set up your log files in the designated folder (`log/`) with the appropriate format.
5. Start the Flask application:
python query_interface.py
6. Access the application in your browser at [http://localhost:5000](http://localhost:5000).

## System Design
The system consists of the following components:
- Flask Application: Provides the backend API for log search functionality.
- HTML/CSS/JavaScript: Implements the frontend interface for users to input search queries.
- Python Modules: Includes functions for searching logs, parsing log files, and handling user requests.

## Features Implemented
1. Full-text search across log files.
2. Filter logs by level, log string, timestamp, and source.
3. Search within specific date ranges.
4. Regex-based search for advanced filtering.
5. Simple and intuitive user interface for search queries.
6. Combining Multiple feature for search
7. Provided real-time log ingestion and searching capabilities.

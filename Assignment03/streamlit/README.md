# German Credit Streamlit Tutorial App (Containerized with Docker)

This is a Streamlit-based dashboard web application for exploring the German Credit Data.
It is containerized for reproducibility and cross-system compatibility purposes.

# Requirements

- Docker

# Instructions to Run the App

- Download the zip file and extract all files in one folder:

  - "Dockerfile"
  - "streamlit.py"
  - "german_credit_data_processed.csv"
  - "README.md"

- Open a terminal and navigate to the project folder.

- Build the Docker image:

  $ docker build -t german-credit-app .

- Run the Docker image:

  $ docker run -p 8501:8501 german_credit_app

- In you browser open the following URL/port

  http://localhost:8501

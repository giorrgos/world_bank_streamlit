# Set base image in Python 3.9
FROM python:3.9-slim

# Expose port 8501 for app to be run on
EXPOSE 8501

# Set working directory
WORKDIR /app

# Copy packages required from local requirements file   
# to Docker image requirements file
COPY requirements.txt ./requirements.txt

# Run specific command line instructions
RUN pip3 install -r requirements.txt

# Copy all files from local projects to Docker image
COPY . .

# Command to run Streamlit application
CMD streamlit run app.py

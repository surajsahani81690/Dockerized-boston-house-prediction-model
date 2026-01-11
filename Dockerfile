# Code for the Docker file
# for building the docker image in your docker run in terminal : docker build -t your_user_name/image_name .,eg:"suraj5178/api ."
# Then run docker login with username and pass
# Then run docker push suraj5178/api , it creates the image on your docker hub
# To run the iamge in your Docker container docker run -d -p 8000:8000 suraj5178/api



FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

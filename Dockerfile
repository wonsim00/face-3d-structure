FROM python:3

WORKDIR /usr/src/app
COPY ./requirements.txt ./requirements.txt

EXPOSE 5000

RUN pip install --no-cache-dir -r requirements.txt
RUN export FLASK_APP=face_3d_structure
RUN export FLASK_ENV=development
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# 435assignment

## RAD
We will create a Discussion forum application.

Endpoints:
1) /create will create posts which will be stored using block storage via S3. Posts will have a post ID and text. 
2) /delete will delete posts with the same post ID
3) /login will log in users based on username and password

We will use Tkinter to create the front end.

## Setup

1. Clone and open the repository
2. In the terminal, type and enter:

    docker run -p 9000:9000 -p 9001:9001 --name minio -d quay.io/minio/minio server /data --console-address ":9001"

   Which will start the minio server locally at http://localhost:9001/

3. In minio, create a bucket with the name "posts".
4. On the left sidebar, click on "Access Keys" and create an access key with the key "access_key" and secret "secret_key" (very secure)
5. Run the backend from the terminal using: python app.py
6. Run the frontend from the terminal using: python .\Frontend\MainApp.py
7. Login using username "username" and password "password" (very secure)
8. Create, delete, and refresh posts!

## Setup

1. Clone and open the repository
2. In the terminal, type and enter:

    docker run -p 9000:9000 -p 9001:9001 --name minio -d quay.io/minio/minio server /data --console-address ":9001"

   Which will start the minio server locally at http://localhost:9001/

3. In minio, create a bucket with the name "posts".
4. On the left sidebar, click on "Access Keys" and create an access key with the key "access_key" and secret "secret_key" (very secure)
5. Run the backend from the terminal using: python app.py
6. Run the frontend from the terminal using: python .\Frontend\MainApp.py
7. Login using username "username" and password "password" (very secure)
8. Create, delete, and refresh posts!

## Setup

1. Clone and open the repository
2. In the terminal, type and enter:

    docker run -p 9000:9000 -p 9001:9001 --name minio -d quay.io/minio/minio server /data --console-address ":9001"

   Which will start the minio server locally at http://localhost:9001/

3. In minio, create a bucket with the name "posts".
4. On the left sidebar, click on "Access Keys" and create an access key with the key "username" and secret "password" (very secure)
5. Run the backend from the terminal using: python app.py
6. Run the frontend from the terminal using: python .\Frontend\MainApp.py
7. Login using username "username" and password "password" (very secure)
8. Create, delete, and refresh posts!
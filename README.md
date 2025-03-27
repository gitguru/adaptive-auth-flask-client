# Flask-Demo

## Set up & Installation.

### 1 .Clone/Fork the git repo and create a virtual environment 
                    
**Windows**
          
```bash
git clone https://github.com/gitguru/adaptive-auth-flask-client.git
cd adaptive-auth-flask-client
py -3 -m venv venv

```
          
**macOS/Linux**
          
```bash
git clone https://github.com/gitguru/adaptive-auth-flask-client.git
cd adaptive-auth-flask-client
python3 -m venv venv

```
### 2 .Activate the environment
          
**Windows** 

```venv\Scripts\activate```
          
**macOS/Linux**

```. venv/bin/activate```
or
```source venv/bin/activate```


### 3 .Install the requirements

Applies for windows/macOS/Linux

```
pip install -r requirements.txt
```

### 5. Run the application
`python app.py`

# OR

## Create a new application from scratch

### 1. Create a directory with a name **"Adaptive-Auth-Flask-Client"**
`mkdir adaptive-auth-flask-client`

### 2. Navigate to the newly created directory

`cd adaptive-auth-flask-client`

### 3. Create a virtual environment

**Windows**

`py -3 -m venv venv`
<br>

**macOS/Linux**

`python3 -m venv venv`

### 4. Activate the environment
          
**Windows** 

```venv\Scripts\activate```
          
**macOS/Linux**

```. venv/bin/activate```
or
```source venv/bin/activate```

### 3 .Install Flask

`pip install Flask`

### 4. Create the required files
Create two files; **app.py** and **Dockerfile**

`touch app.py Dockerfile`

## Docker
### Creating the image
```
docker build -t flask-demo .
```

### Running the development container
```
docker run -it -p 5101:5000 --name flask-demo-dev --rm --volume $(pwd):/usr/src/app flask-demo:latest bash
```

## Running built app
```
flask --app flaskr init-db
flask --app flaskr run --host=0.0.0.0 --debug
```

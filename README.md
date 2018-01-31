# flask-react-template

Full stack website template with Python (Flask) and JavaScript (React)

## Setup

Clone this repo 
```commandline
git clone https://github.com/victor-iyiola/flask-react-template.git
```

Or download the project [here](https://github.com/victor-iyiola/flask-react-template/archive/master.zip)

Then change your working directory as show below
```commandline
cd flask-react-template
```

Install python dependencies
```commandline
pip install --upgrade pip
pip install --upgrade -r requirements.txt
```

Install npm dependencies
```commandline
cd flask_react_template/client/static
npm install
```

After installing the dependencies. You can now start webpack (to compile all client files into a single javascript file. `bundle.js`)

For development
```commandline
npm run watch
```

For Production
```commandline
npm run build
```

Excellent. Now it's time to start the Python (flask) web server.
```
cd <flask-react-template>
python run.py --debug=True
```

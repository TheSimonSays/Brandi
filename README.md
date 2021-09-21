# Brandi <img src="https://img.shields.io/badge/version-0.0.1--pre--beta-red" />

 <img src="docs/static/brandi.png" alt="brandi logo" width="150" align="right"/>

Brandi is a simple Python 3.8+ web wsgi framework inspired by Flask. It is designed as an academic project as well as for personal purposes. Brandi uses mako templates to simplify development and distinguish it from flask. It works on [Gunicorn](https://github.com/benoitc/gunicorn)
<br/>
<br/>
<br/>
> ⚠️ Brandi does not have an installation pypi package yet

## Installation
```bash
git clone git@github.com:TheSimonSays/Brandi.git
```
Install development requirements 
```bash
pip install -r requirements/requrements.dev.txt
```
## Usage
Simple app
```python
# app.py
from brandi import Brandi, json

app = Brandi(__name__)

@app.route('/', methods=['GET', 'POST'])
def index(request):
    return json({'message': 'Hello world'}, 200)
```
Using mako
```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
    % if title:
        <h1>${title}</h1>
    % else:
        <h1>default</h1>
    % endif
</body>
</html>
```
```python
# app.py
from brandi import Brandi, template

app = Brandi(__name__, templates_folder='templates/')

@app.route('/', methods=['GET'])
def index(request):
    return template('index.html', 200, title='Brandi')
```
Path parameters
```python
# app.py
from brandi import Brandi, text

app = Brandi(__name__)

@app.route('/user/<string:user_name>', methods=['GET', 'POST'])
def index(user_name, request):
    return text(f'Hello, {user_name}')
```

Run app
```bash
gunicorn app:app --reload
```

## Contributing
**Contributions Welcome!**

## Roadmap

- ~~variable rules to ULR (path parameters)~~
- group exceptions
- blueprints
- logging
- middlewares
- cookies
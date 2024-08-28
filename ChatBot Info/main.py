from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def fetch_response(prompt):
    api_key = '76dd42fee7ac4459062fcaa5850d2775'
    model = 'gpt-3.5-turbo'
    api_url = f'http://195.179.229.119/gpt/api.php?prompt={requests.utils.quote(prompt)}&api_key={requests.utils.quote(api_key)}&model={requests.utils.quote(model)}'

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        content = data.get('content', 'No content available')
        return content
    except requests.RequestException as e:
        return f'Request Error: {e}'

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = fetch_response(prompt)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)

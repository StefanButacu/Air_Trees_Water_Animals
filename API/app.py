import torch
from flask import Flask, request
from flask_cors import CORS

from models.ANN_v2 import TempChangeNN
from models.checkpoint import load_checkpoint

model = TempChangeNN()
FILENAME = '../notebooks/checkpoint.pth.tar'
load_checkpoint(torch.load(FILENAME), model)
model.eval()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/predict', methods=['GET'])
def predict():  # put application's code here
    month = float(request.args.get('month')) - 1
    year = float(request.args.get('year'))
    min_train_input = 1961.
    max_train_input = 2019.
    year = (year - min_train_input) / (max_train_input - min_train_input)
    x = torch.tensor([month, year ])
    with torch.no_grad():
        out = model(x)
    return str(out.numpy()[0])


if __name__ == '__main__':
    app.run()

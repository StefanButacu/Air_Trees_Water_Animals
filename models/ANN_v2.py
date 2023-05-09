import torch
from torch import nn


class TempChangeNN(nn.Module):
    def __init__(self):
        super(TempChangeNN, self).__init__()

        self.lrelu = nn.ELU()

        self.fc1 = nn.Linear(2, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 32)
        self.fc4 = nn.Linear(32, 16)
        self.fc5 = nn.Linear(16, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.lrelu(x)
        x = self.fc2(x)
        x = self.lrelu(x)
        x = self.fc3(x)
        x = self.lrelu(x)
        x = self.fc4(x)
        x = self.lrelu(x)
        x = self.fc5(x)

        return x

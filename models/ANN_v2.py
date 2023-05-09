import torch
from torch import nn


class TempChangeNN(nn.Module):
    def __init__(self):
        super(TempChangeNN, self).__init__()

        self.lrelu = nn.LeakyReLU(negative_slope=0.05)

        self.fc1 = nn.Linear(2, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 32)
        self.fc4 = nn.Linear(32, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.lrelu(x)
        x = self.fc2(x)
        x = self.lrelu(x)
        x = self.fc3(x)
        x = self.lrelu(x)
        x = self.fc4(x)

        return x


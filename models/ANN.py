import torch
from torch import nn


class TempChangeNN(nn.Module):
    def __init__(self):
        super(TempChangeNN, self).__init__()

        self.fc1 = nn.Linear(2, 64)
        self.lrelu1 = nn.LeakyReLU(negative_slope=0.01)
        self.fc2 = nn.Linear(64, 32)
        self.lrelu2 = nn.LeakyReLU(negative_slope=0.01)
        self.fc3 = nn.Linear(32, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.lrelu1(x)
        x = self.fc2(x)
        x = self.lrelu2(x)
        x = self.fc3(x)

        return x


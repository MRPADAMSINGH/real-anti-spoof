# real_anti_spoof/spoofmodels/FasNet.py

import torch
import torch.nn as nn
from .FasNetBackbone import Backbone

class FasNet(nn.Module):
    def __init__(self):
        super(FasNet, self).__init__()
        self.backbone = Backbone()
        self.fc = nn.Linear(512, 1)  # Example layer, adjust according to the actual architecture

    def forward(self, x):
        x = self.backbone(x)
        x = self.fc(x)
        return torch.sigmoid(x)

    def predict(self, x):
        self.eval()
        with torch.no_grad():
            output = self.forward(x)
        return output.item()

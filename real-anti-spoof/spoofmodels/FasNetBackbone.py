# real_anti_spoof/spoofmodels/FasNetBackbone.py

import torch.nn as nn
import torchvision.models as models

class Backbone(nn.Module):
    def __init__(self):
        super(Backbone, self).__init__()
        # Example using a pre-trained ResNet
        self.model = models.resnet18(pretrained=True)
        self.model = nn.Sequential(*list(self.model.children())[:-1])  # Remove the final classification layer

    def forward(self, x):
        x = self.model(x)
        x = x.view(x.size(0), -1)  # Flatten the output
        return x

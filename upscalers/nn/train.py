#!/bin/env python


from sys import argv

if len(argv) > 2:
    raise RuntimeError("invalid arguments given, only pass a checkpoint path if you want to continue training a model, nothing more")


import torch
import torch.nn as nn
import torch.optim as optim

from torchvision.datasets import ImageFolder
from torch.utils.data import random_split
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader

from pathlib import Path

from srcnn import SRCNN


print("welcome to this training helper script\n")


gpu = torch.device('cuda:0')
model = SRCNN(argv[1] if len(argv) == 2 else "")

full_dataset = ImageFolder("dataset", transform=ToTensor())

if Path("checkpoints/train_dataset.pkl").exists() and Path("checkpoints/test_dataset.pkl").exists():
    train_dataset, test_dataset = torch.load("checkpoints/train_dataset.pkl"), torch.load("checkpoints/test_dataset.pkl")
else:
    train_dataset, test_dataset = random_split(full_dataset, (0.9, 0.1))
    torch.save(train_dataset, "checkpoints/train_dataset.pkl")
    torch.save(test_dataset, "checkpoints/test_dataset.pkl")

train_loader = DataLoader(dataset=train_dataset, shuffle=False, batch_size=5)
test_loader = DataLoader(dataset=test_dataset, shuffle=False, batch_size=5)

print(f"dataset size : {len(full_dataset)}\ntrain dataset size : {len(train_dataset)}\ntest dataset size : {len(test_dataset)}\n")


model.train_model(optim.Adam(model.parameters(), lr=6942.0), nn.MSELoss(), train_loader, test_loader)

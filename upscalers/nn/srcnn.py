#!/bin/env python

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import torchvision as tv

from pathlib import Path
import sys


class SRCNN(nn.Module):

	# just initializes neural network's layers
	def __init__ (self, checkpoint_path:str=""):
		nn.Module.__init__(self)

		self.computing_device = torch.device('cuda:0')

		self.cl1 = nn.Conv2d(3, 8, 9, device=self.computing_device, padding=4, padding_mode='circular')
		self.cl2 = nn.Conv2d(8, 7, 1, device=self.computing_device)
		self.cl3 = nn.Conv2d(7, 3, 5, device=self.computing_device, padding=2, padding_mode='circular')


		if checkpoint_path != "" and Path(checkpoint_path).exists():
			self.load_state_dict(torch.load(checkpoint_path))

		self.checkpoint_path = checkpoint_path
		self.downscale_mode = 'bicubic'
		self.upscale_mode = 'bicubic'


	# magic formula here, do not touch
	def forward (self, input_matrices:torch.Tensor):

		input_matrices = self.cl1(input_matrices)
		input_matrices = torch.relu(input_matrices)

		input_matrices = self.cl2(input_matrices)
		input_matrices = torch.relu(input_matrices)

		input_matrices = self.cl3(input_matrices)

		return input_matrices

	def upscale_matrices (self, input_matrices:torch.Tensor, scale_factor:float = 2.0):
		return self(F.interpolate(input_matrices, scale_factor=scale_factor, mode=self.upscale_mode))


	# trains the model with a minimalistic helper
	def train_model (self, optimizer, loss_function, train_dataset, test_dataset):
		if self.checkpoint_path != "":
			if input("\ndo you want to test your model before beginning [y/N] ?  ") in ['y', 'Y']:
				self.test_model(loss_function, test_dataset)

		epoch = 0
		while not input("\ntrain once with the whole dataset [Y/n] ?  ") in ['N', 'n']:
			learning_rate = float(input("\nplease enter the learning rate for this epoch :  "))
			for g in optimizer.param_groups:
				g['lr'] = learning_rate


			self.train()
			runningLoss = 0
			for i, pictures in enumerate(train_dataset):
				pictures = pictures[0].to(self.computing_device)
				downscaled_pictures = F.interpolate(pictures, scale_factor=0.5, mode=self.downscale_mode).to(self.computing_device)

				optimizer.zero_grad(optimizer)

				outputs = self.upscale_matrices(downscaled_pictures, 2)
				lossValue = loss_function(outputs, pictures)
				lossValue.backward()

				optimizer.step()

				runningLoss += lossValue.item()
				if i % 100 == 99:
					print(f"[{epoch}, {i + 1}]: {runningLoss / 100}")
					runningLoss = 0
			

			self.test_model(loss_function, test_dataset)

			if self.checkpoint_path != "":
				if input("\noverwrite old checkpoint [y/N] ?  ") in ['Y', 'y']:
					torch.save(self.state_dict(), self.checkpoint_path)

			epoch += 1
		
		if self.checkpoint_path == "":
			self.save_model(input("please name your checkpoint file :  "))

	# computes and displays the current loss compared to the chosen basic upscale method
	def test_model(self, loss_function, test_dataset):
		self.eval()
		runningLoss = 0
		for i, pictures in enumerate(test_dataset):
			pictures = pictures[0].to(self.computing_device)
			downscaled_pictures = F.interpolate(pictures, scale_factor=0.5, mode=self.downscale_mode).to(self.computing_device)

			outputs = self.upscale_matrices(downscaled_pictures, 2)
			lossValue = loss_function(outputs, pictures)

			runningLoss += lossValue.item()


		print(f"test srcnn : {runningLoss / len(test_dataset)}\ntest {self.upscale_mode} : {loss_function(F.interpolate(downscaled_pictures, scale_factor=2.0, mode=self.upscale_mode), pictures)}")

	# just saves the model
	def save_model(self, checkpoint_path):
		if Path(checkpoint_path).exists():
			if input("Already existing checkpoint file, replace (y/N) ?  ") in ['y', 'Y']:
				torch.save(self.state_dict(), checkpoint_path)

		else:
			torch.save(self.state_dict(), checkpoint_path)

	
	# the only function that should be called by the user
	def upscale (self, input_picture_path:str, output_picture_path:str, scale_factor:float = 2.0):
		tv.utils.save_image(self.upscale_matrices(torch.stack([tv.io.read_image(input_picture_path).to(self.computing_device) / 255.0]), scale_factor=scale_factor), fp=output_picture_path)
	

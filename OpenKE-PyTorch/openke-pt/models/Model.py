import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

class Model(nn.Module):
	r"""The base model for knowledge embedding

    Args:
        config: the instance of class :class:`config.Config.Config`
    """

	def __init__(self,config):
		super(Model,self).__init__()
		self.config = config

	def get_postive_instance(self):
		r"""This method gets the positive samples from batch

		Returns:
			list: [self.postive_h, self.postive_t,self.positive_r], the shape is [batch_size]
		"""
		self.postive_h = Variable(torch.from_numpy(self.config.batch_h[0:self.config.batch_size])).cuda()
		self.postive_t = Variable(torch.from_numpy(self.config.batch_t[0:self.config.batch_size])).cuda()
		self.postive_r = Variable(torch.from_numpy(self.config.batch_r[0:self.config.batch_size])).cuda()
		return self.postive_h,self.postive_t,self.postive_r

	def get_negtive_instance(self):
		r"""This method gets the negative samples through negative sampling

		Returns:
			list: [self.negtive_h, self.negtive_t,self.negitive_r], the shape is [batch_size]
		"""
		self.negtive_h = Variable(torch.from_numpy(self.config.batch_h[self.config.batch_size:self.config.batch_seq_size])).cuda()
		self.negtive_t = Variable(torch.from_numpy(self.config.batch_t[self.config.batch_size:self.config.batch_seq_size])).cuda()
		self.negtive_r = Variable(torch.from_numpy(self.config.batch_r[self.config.batch_size:self.config.batch_seq_size])).cuda()
		return self.negtive_h,self.negtive_t,self.negtive_r

	def get_all_instance(self):
		r"""This method gets all samples from batch, including positive samples and negative samples

		Returns:
			list: [self.batch_h, self.batch_t, self.batch_y], the shape is [batch_size * (1 + negative_ent + negative_rel)]

		"""
		self.batch_h = Variable(torch.from_numpy(self.config.batch_h)).cuda()
		self.batch_t = Variable(torch.from_numpy(self.config.batch_t)).cuda()
		self.batch_r = Variable(torch.from_numpy(self.config.batch_r)).cuda()
		return self.batch_h, self.batch_t, self.batch_r

	def get_all_labels(self):
		r"""This method gets all labels for the samples, ``1`` for positive triples and ``-1`` for negative triples

		Returns:
			Variable: self.batch_y, the shape is [batch_size * (1 + negative_ent + negative_rel)]

		"""
		self.batch_y=Variable(torch.from_numpy(self.config.batch_y)).cuda()
		return self.batch_y

	def predict(self):
		pass

	def forward(self):
		pass

	def loss_func(self):
		pass


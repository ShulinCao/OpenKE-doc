import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from Model import *
class RESCAL(Model):
	r"""THis class implements RESCAL model based on :class:`models.Model`
	
	Args:
		config: configuration information
	Shape:
		- Output: loss value which is a scalar
	"""
	def __init__(self,config):
		super(RESCAL,self).__init__(config)
		self.ent_embeddings=nn.Embedding(self.config.entTotal,self.config.hidden_size)
		self.rel_matrices=nn.Embedding(self.config.relTotal,self.config.hidden_size*self.config.hidden_size)
		self.init_weights()
	def init_weights(self):
		r"""Init entity and relation embeddings. In this model, we use ``xaview_uniform``
		"""
		nn.init.xavier_uniform(self.ent_embeddings.weight.data)
		nn.init.xavier_uniform(self.rel_matrices.weight.data)
	def _calc(self,h,t,r):
		return h*torch.matmul(r,t)
	def loss_func(self,p_score,n_score):
		r"""This method calculatest the pairwise margin-based loss

		Args:
			p_score (float): the score for positive triple
			n_score (float): the score for negative triple

		Returns:
			float: the margin-based loss for this pair 

		"""
		criterion= nn.MarginRankingLoss(self.config.margin,False).cuda()
		y=Variable(torch.Tensor([1])).cuda()
		loss=criterion(p_score,n_score,y)
		return loss
	def forward(self):
		pos_h,pos_t,pos_r=self.get_postive_instance()
		neg_h,neg_t,neg_r=self.get_negtive_instance()
		p_h=self.ent_embeddings(pos_h).view(-1,self.config.hidden_size,1)
		p_t=self.ent_embeddings(pos_t).view(-1,self.config.hidden_size,1)
		p_r=self.rel_matrices(pos_r).view(-1,self.config.hidden_size,self.config.hidden_size)
		n_h=self.ent_embeddings(neg_h).view(-1,self.config.hidden_size,1)
		n_t=self.ent_embeddings(neg_t).view(-1,self.config.hidden_size,1)
		n_r=self.rel_matrices(neg_r).view(-1,self.config.hidden_size,self.config.hidden_size)
		_p_score = self._calc(p_h, p_t, p_r).view(-1, 1, self.config.hidden_size)
		_n_score = self._calc(n_h, n_t, n_r).view(-1, 1, self.config.hidden_size)
		p_score=torch.sum(torch.mean(_p_score,1,False),1)
		n_score=torch.sum(torch.mean(_n_score,1,False),1)
		loss=self.loss_func(p_score,n_score)
		return loss
	def predict(self, predict_h, predict_t, predict_r):
		r"""This method predictss the score for testting sample

		Args:
			predict_h: head entity of triple
			predict_t: tail entity of triple
			predict_r: relaiton of triple
			
		Returns:
			float: the score for testing triple
		"""
		p_h_e=self.ent_embeddings(Variable(torch.from_numpy(predict_h)).cuda()).view(-1,self.config.hidden_size,1)
		p_t_e=self.ent_embeddings(Variable(torch.from_numpy(predict_t)).cuda()).view(-1,self.config.hidden_size,1)
		p_r_e=self.rel_matrices(Variable(torch.from_numpy(predict_r)).cuda()).view(-1,self.config.hidden_size,self.config.hidden_size)
		p_score=-torch.sum(self._calc(p_h_e, p_t_e, p_r_e),1)
		return p_score.cpu()
		
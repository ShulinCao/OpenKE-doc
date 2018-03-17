import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from Model import *
class TransH(Model):
	r"""THis class implements TransH model based on :class:`models.Model`
	
	Args:
		config: configuration information
	Shape:
		- Output: loss value which is a scalar
	"""
	def __init__(self,config):
		super(TransH,self).__init__(config)
		self.ent_embeddings=nn.Embedding(config.entTotal,config.hidden_size)
		self.rel_embeddings=nn.Embedding(config.relTotal,config.hidden_size)
		self.norm_vector=nn.Embedding(config.relTotal,config.hidden_size)
		self.init_weights()
	def init_weights(self):
		r"""Init entity and relation embeddings. In this model, we use ``xaview_uniform``
		"""
		nn.init.xavier_uniform(self.ent_embeddings.weight.data)
		nn.init.xavier_uniform(self.rel_embeddings.weight.data)
		nn.init.xavier_uniform(self.norm_vector.weight.data)
	def _transfer(self,e,norm):
		return e - torch.sum(e * norm, 1, True) * norm
	def _calc(self,h,t,r):
		r"""The definition of loss function
		"""
		return torch.abs(h+r-t)
	def loss_func(self,p_score,n_score):
		r"""This method calculatest the pairwise margin-based loss

		Args:
			p_score (float): the score for positive triple
			n_score (float): the score for negative triple

		Returns:
			float: the margin-based loss for this pair 

		"""
		criterion= nn.MarginRankingLoss(self.config.margin,False).cuda()
		y=Variable(torch.Tensor([-1])).cuda()
		loss=criterion(p_score,n_score,y)
		return loss
	def forward(self):
		pos_h,pos_t,pos_r=self.get_postive_instance()
		neg_h,neg_t,neg_r=self.get_negtive_instance()
		p_h_e=self.ent_embeddings(pos_h)
		p_t_e=self.ent_embeddings(pos_t)
		p_r_e=self.rel_embeddings(pos_r)
		n_h_e=self.ent_embeddings(neg_h)
		n_t_e=self.ent_embeddings(neg_t)
		n_r_e=self.rel_embeddings(neg_r)
		p_norm=self.norm_vector(pos_r)
		n_norm=self.norm_vector(neg_r)

		p_h=self._transfer(p_h_e,p_norm)
		p_t=self._transfer(p_t_e,p_norm)
		p_r=p_r_e
		n_h=self._transfer(n_h_e,n_norm)
		n_t=self._transfer(n_t_e,n_norm)
		n_r=n_r_e

		_p_score = self._calc(p_h, p_t, p_r)
		_n_score = self._calc(n_h, n_t, n_r)
		p_score=torch.sum(_p_score,1)
		n_score=torch.sum(_n_score,1)
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
		p_h_e=self.ent_embeddings(Variable(torch.from_numpy(predict_h)).cuda())
		p_t_e=self.ent_embeddings(Variable(torch.from_numpy(predict_t)).cuda())
		p_r_e=self.rel_embeddings(Variable(torch.from_numpy(predict_r)).cuda())
		p_norm=self.norm_vector(Variable(torch.from_numpy(predict_r)).cuda())
		p_h=self._transfer(p_h_e,p_norm)
		p_t=self._transfer(p_t_e,p_norm)
		p_r=p_r_e
		_p_score=self._calc(p_h, p_t, p_r)
		p_score=torch.sum(_p_score,1)
		return p_score.cpu()

		

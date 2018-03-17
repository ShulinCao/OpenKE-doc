How to Train
============

To compute a knowledge graph embedding, first import datasets and set configure parameters for training, then train models and export results. For instance, we write an example_train_transe.py to train TransE::

	import config
	import numpy as np

	con = config.Config()
	#Input training files from benchmarks/FB15K/ folder.
	con.set_in_path("./benchmarks/FB15K/")

	con.set_work_threads(4)
	con.set_train_times(500)
	con.set_nbatches(100)
	con.set_alpha(0.001)
	con.set_margin(1.0)
	con.set_bern(0)
	con.set_dimension(50)
	con.set_ent_neg_rate(1)
	con.set_rel_neg_rate(0)
	con.set_opt_method("SGD")

	#Models will be exported via torch.save() automatically.
	con.set_export_files("./res/model.vec.pt")
	#Model parameters will be exported to json files automatically.
	con.set_out_files("./res/embedding.vec.json")
	#Initialize experimental settings.
	con.init()
	#Set the knowledge embedding model
	con.set_model(models.TransE)
	#Train the model.
	con.run()

Step 1: Import Datasets
-----------------------
We set the path of datasets::

	con.set_in_path("benchmarks/FB15K/")

We import knowledge graphs from benchmarks/FB15K/ folder. The data consists of three essential files mentioned before

	- ``train2id.txt``
	- ``entity2id.txt``
	- ``relation2id.txt``

Validation and test files are required and used to evaluate the training results, However, they are not indispensable for training::

	con.set_work_threads(8)

Step 2: Set Configure Parameters
--------------------------------

We set the parameters, including the data traversing rounds, learning rate, batch size, and dimensions of entity and relation embeddings::

	con.set_train_times(500)
	con.set_nbatches(100)
	con.set_alpha(0.5)
	con.set_dimension(200)
	con.set_margin(1)

For negative sampling, we can corrupt entities and relations to construct negative triples. ``set_bern(0)`` will use the traditional sampling method, and ``set_bern(1)`` will use the method in (Wang et al. 2014) denoted as "bern".

We can select a proper gradient descent optimization algorithm to train models::

	con.set_optimizer("SGD")

Step 3: Export Results
----------------------

Models will be exported via ``torch.save()`` automatically every few rounds. Also, model parameters will be exported to json files finally::

	con.set_export_files("./res/model.vec.pt")

	con.set_out_files("./res/embedding.vec.json")

Step 4: Train Models
--------------------

We set the knowledge graph embedding model and start the training process::

	con.init()
	con.set_model(models.TransE)
	con.run()



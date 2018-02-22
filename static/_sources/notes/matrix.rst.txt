How to Get Embedding Matrix
===========================

There are four approaches to get the embedding matrix.

Set Import Files
----------------

Set import files and OpenKE will automatically load models via torch.load()::

	import json
	import numpy as py
	
	import config
	import models
	con = config.Config()
	con.set_in_path("./benchmarks/FB15K/")
	con.set_test_flag(True)
	con.set_work_threads(4)
	con.set_dimension(100)
	con.set_import_files("./res/model.vec.pt")
	con.init()
	con.set_model(models.TransE)
	# Get the embeddings (numpy.array)
	embeddings = con.get_parameters("numpy")
	# Get the embeddings (python list)
	embeddings = con.get_parameters()

Read Parameters From Json Files
-------------------------------

Read model parameters from json files and manually load parameters::

	import json
	import numpy as py
	import config
	import models
	con = config.Config()
	con.set_in_path("./benchmarks/FB15K/")
	con.set_test_flag(True)
	con.set_work_threads(4)
	con.set_dimension(100)
	con.init()
	con.set_model(models.TransE)
	f = open("./res/embedding.vec.json", "r")
	embeddings = json.loads(f.read())
	f.close()

Manually Load Models Parameters
-------------------------------

Manually load models via ``torch.load()``::
	
	con = config.Config()
	con.set_in_path("./benchmarks/FB15K/")
	con.set_test_flag(True)
	con.set_work_threads(4)
	con.set_dimension(100)
	con.init()
	con.set_model(models.TransE)
	con.import_variables("./res/model.vec.pt")
	# Get the embeddings (numpy.array)
	embeddings = con.get_parameters("numpy")
	# Get the embeddings (python list)
	embeddings = con.get_parameters()

Get the Embeddings After Training
---------------------------------

Immediately get the embeddings after training the model::

	...
	...
	...
	#Models will be exported via tf.Saver() automatically.
	con.set_export_files("./res/model.vec.pt")
	#Model parameters will be exported to json files automatically.
	con.set_out_files("./res/embedding.vec.json")
	#Initialize experimental settings.
	con.init()
	#Set the knowledge embedding model
	con.set_model(models.TransE)
	#Train the model.
	con.run()
	#Get the embeddings (numpy.array)
	embeddings = con.get_parameters("numpy")
	#Get the embeddings (python list)
	embeddings = con.get_parameters()

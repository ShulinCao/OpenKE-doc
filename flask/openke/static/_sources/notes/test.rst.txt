How to Test
===========

To evaluate the model, first import datasets and set essential configure paramters, then set model parameters and test the model. For instance, we write an example_test_transe.py to test TransE.

There are three approaches to test models.

Load Models from Import Files
-----------------------------
Set import files and OpenKE-PyTorch will automatically load models via torch.load()::

	import config
	import models
	import numpy as np
	import json

	con = config.Config()
	con.set_in_path("./benchmarks/FB15K/")
	con.set_test_flag(True)
	con.set_work_threads(4)
	con.set_dimension(100)
	con.set_import_files("./res/model.vec.pt")
	con.init()
	con.set_model(models.TransE)
	icon.test()

Read Model Parameters from Json Files
-------------------------------------

Read model parameters from json files and manually load parameters::

	import config
	import models
	import numpy as np
	import json

	con = config.Config()
	con.set_in_path("./benchmarks/FB15K/")
	con.set_test_flag(True)
	con.set_work_threads(4)
	con.set_dimension(100)
	con.init()
	con.set_model(models.TransE)
	f = open("./res/embedding.vec.json", "r")
	content = json.loads(f.read())
	f.close()
	con.set_parameters(content)
	con.test()

Manually Load Models
--------------------

Manually load models via torch.load()::

	import config
	import models
	import numpy as np
	import json

	con = config.Config()
	con.set_in_path("./benchmarks/FB15K/")
	con.set_test_flag(True)
	con.set_work_threads(4)
	con.set_dimension(100)
	con.init()
	con.set_model(models.TransE)
	con.import_variables("./res/model.vec.pt")
	con.test()

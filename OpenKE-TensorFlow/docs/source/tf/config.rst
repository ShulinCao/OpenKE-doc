Config
===================================
.. automodule:: config
.. currentmodule:: config
.. autoclass:: Config

Getting Statistics of Dataset
--------------------------------

.. automethod:: config.Config.get_ent_total
.. automethod:: config.Config.get_rel_total


Setting Configuration Parameters
--------------------------------

.. automethod:: config.Config.set_alpha
.. automethod:: config.Config.set_margin
.. automethod:: config.Config.set_bern
.. automethod:: config.Config.set_dimension
.. automethod:: config.Config.set_ent_dimension
.. automethod:: config.Config.set_rel_dimension
.. automethod:: config.Config.set_train_times
.. automethod:: config.Config.set_nbatches
.. automethod:: config.Config.set_work_threads
.. automethod:: config.Config.set_ent_neg_rate
.. automethod:: config.Config.set_rel_neg_rate
.. automethod:: config.Config.set_lr_decay
.. automethod:: config.Config.set_weight_decay
.. automethod:: config.Config.set_opt_method
.. automethod:: config.Config.set_log_on


Setting Inpath and Outpath
---------------------------------
.. automethod:: config.Config.set_in_path
.. automethod:: config.Config.set_out_files
.. automethod:: config.Config.set_import_files
.. automethod:: config.Config.set_export_files
.. automethod:: config.Config.set_export_steps

Saving and Loading Models
---------------------------------
.. automethod:: config.Config.save_tensorflow
.. automethod:: config.Config.restore_tensorflow
.. automethod:: config.Config.export_variables
.. automethod:: config.Config.import_variables
.. automethod:: config.Config.get_parameters
.. automethod:: config.Config.save_parameters

Setting Models
---------------------------------
.. automethod:: config.Config.set_model
.. automethod:: config.Config.sampling

Training Models
----------------------------------
.. automethod:: config.Config.train_step
.. automethod:: config.Config.run


Testing Models
----------------------------------
.. automethod:: config.Config.set_test_flag
.. automethod:: config.Config.test_step
.. automethod:: config.Config.test

import config
import models
import json

con = config.Config()
con.set_test_flag(True)
con.set_in_path("./benchmarks/FB15K/")
con.set_out_path("./benchmarks/FB15K/a.vec")
# con.set_export_files("res.vec")
#con.set_import_files("res.vec")
# con.set_export_steps(10)
con.set_log_on(1)
con.set_work_threads(8)
con.set_train_times(1000)
con.set_nbatches(100)	
con.set_alpha(0.001)
con.set_bern(0)
con.set_dimension(100)
con.set_margin(1.0)
con.set_ent_neg_rate(1)
con.set_rel_neg_rate(0)
con.set_opt_method("SGD")
con.init()
con.set_model(models.TransH)
# f = open("a.vec", "r")
# content = json.loads(f.read())
# f.close()
# con.set_parameters(content)
con.run()
con.test()

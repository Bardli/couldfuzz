results = dict()
import tensorflow as tf
import time
try:
  try:
    condition_0 = True
    condition_1 = False
    condition_2 = False
    condition_3 = True
    condition = [condition_0,condition_1,condition_2,condition_3,]
    data_0 = 1
    data_1 = 2
    data_2 = 3
    data_3 = 4
    data = [data_0,data_1,data_2,data_3,]
    summarize_0 = 99
    summarize_1 = -1024
    summarize_2 = 298
    summarize_3 = 401
    summarize = [summarize_0,summarize_1,summarize_2,summarize_3,]
    name = None
    results["res_low"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
    t_start = time.time()
    results["res_low"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    condition = [condition_0,condition_1,condition_2,condition_3,]
    data = [data_0,data_1,data_2,data_3,]
    summarize = [summarize_0,summarize_1,summarize_2,summarize_3,]
    results["res_high"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
    t_start = time.time()
    results["res_high"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
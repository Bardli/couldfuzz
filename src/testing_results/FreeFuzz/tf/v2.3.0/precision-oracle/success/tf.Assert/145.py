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
    data_0 = 2
    data_1 = 3
    data_2 = 1024
    data_3 = 3
    data = [data_0,data_1,data_2,data_3,]
    summarize_0 = 100
    summarize_1 = 200
    summarize_2 = 300
    summarize_3 = 400
    summarize = [summarize_0,summarize_1,summarize_2,summarize_3,]
    name_tensor = tf.random.uniform([1, 2], dtype=tf.float16)
    name = tf.identity(name_tensor)
    name = tf.Variable(name)
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
    name = tf.identity(name_tensor)
    name = tf.cast(name, tf.float32)
    name = tf.Variable(name)
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
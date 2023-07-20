results = dict()
import tensorflow as tf
import time
try:
  try:
    tensor_0_0 = 16
    tensor_0_1 = 16
    tensor_0 = [tensor_0_0,tensor_0_1,]
    tensor_1_0 = -3
    tensor_1_1 = 1
    tensor_1 = [tensor_1_0,tensor_1_1,]
    tensor_2_0 = True
    tensor_2_1 = 1024
    tensor_2 = [tensor_2_0,tensor_2_1,]
    tensor = [tensor_0,tensor_1,tensor_2,]
    indices_0_0 = -1
    indices_0_1 = -2
    indices_0 = [indices_0_0,indices_0_1,]
    indices_1_0 = 2
    indices_1_1 = -1
    indices_1 = [indices_1_0,indices_1_1,]
    indices = [indices_0,indices_1,]
    updates_0 = 5
    updates_1 = 10
    updates = [updates_0,updates_1,]
    name = None
    results["res_low"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
    t_start = time.time()
    results["res_low"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    tensor_0 = [tensor_0_0,tensor_0_1,]
    tensor_1 = [tensor_1_0,tensor_1_1,]
    tensor_2 = [tensor_2_0,tensor_2_1,]
    tensor = [tensor_0,tensor_1,tensor_2,]
    indices_0 = [indices_0_0,indices_0_1,]
    indices_1 = [indices_1_0,indices_1_1,]
    indices = [indices_0,indices_1,]
    updates = [updates_0,updates_1,]
    results["res_high"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
    t_start = time.time()
    results["res_high"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

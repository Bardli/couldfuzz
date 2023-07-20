results = dict()
import tensorflow as tf
import time
try:
  try:
    tensor_tensor = tf.random.uniform([13, 11, 7, 5, 3], dtype=tf.float16)
    tensor = tf.identity(tensor_tensor)
    indices_0_0 = 0
    indices_0_1 = 1
    indices_0 = [indices_0_0,indices_0_1,]
    indices_1_0 = 1025
    indices_1_1 = -4
    indices_1 = [indices_1_0,indices_1_1,]
    indices_2_0 = 0
    indices_2_1 = -1
    indices_2 = [indices_2_0,indices_2_1,]
    indices = [indices_0,indices_1,indices_2,]
    updates_tensor = tf.random.uniform([3, 7, 5, 3], dtype=tf.float16)
    updates = tf.identity(updates_tensor)
    name = None
    results["res_low"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
    t_start = time.time()
    results["res_low"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    tensor = tf.identity(tensor_tensor)
    tensor = tf.cast(tensor, tf.float32)
    indices_0 = [indices_0_0,indices_0_1,]
    indices_1 = [indices_1_0,indices_1_1,]
    indices_2 = [indices_2_0,indices_2_1,]
    indices = [indices_0,indices_1,indices_2,]
    updates = tf.identity(updates_tensor)
    updates = tf.cast(updates, tf.float32)
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

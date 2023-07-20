results = dict()
import tensorflow as tf
import time
try:
  try:
    tensor_tensor = tf.random.uniform([5, 5], dtype=tf.float16)
    tensor = tf.identity(tensor_tensor)
    indices_tensor = tf.saturate_cast(tf.random.uniform([2, 5, 2], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int8)
    indices = tf.identity(indices_tensor)
    updates_0_0 = 1
    updates_0_1 = 1
    updates_0_2 = 1
    updates_0_3 = 1
    updates_0_4 = 1
    updates_0 = [updates_0_0,updates_0_1,updates_0_2,updates_0_3,updates_0_4,]
    updates_1_0 = 1
    updates_1_1 = 1
    updates_1_2 = 1
    updates_1_3 = 1
    updates_1_4 = 1
    updates_1 = [updates_1_0,updates_1_1,updates_1_2,updates_1_3,updates_1_4,]
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
    tensor = tf.identity(tensor_tensor)
    tensor = tf.cast(tensor, tf.float32)
    indices = tf.identity(indices_tensor)
    indices = tf.cast(indices, tf.int32)
    updates_0 = [updates_0_0,updates_0_1,updates_0_2,updates_0_3,updates_0_4,]
    updates_1 = [updates_1_0,updates_1_1,updates_1_2,updates_1_3,updates_1_4,]
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

results = dict()
import tensorflow as tf
import time
try:
  try:
    tensor_tensor = tf.random.uniform([3, 512, 768], dtype=tf.float16)
    tensor = tf.identity(tensor_tensor)
    indices_tensor = tf.saturate_cast(tf.random.uniform([3, 2], minval=0, maxval=256, dtype=tf.int64), dtype=tf.uint8)
    indices = tf.identity(indices_tensor)
    updates_tensor = tf.random.uniform([3, 768], dtype=tf.float16)
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
    indices = tf.identity(indices_tensor)
    indices = tf.cast(indices, tf.uint8)
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
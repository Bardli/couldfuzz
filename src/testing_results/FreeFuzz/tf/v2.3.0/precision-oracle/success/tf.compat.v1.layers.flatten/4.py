results = dict()
import tensorflow as tf
import time
try:
  try:
    inputs_tensor = tf.random.uniform([2, 2], dtype=tf.float16)
    inputs = tf.identity(inputs_tensor)
    name = True
    results["res_low"] = tf.compat.v1.layers.flatten(inputs=inputs,name=name,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.layers.flatten(inputs=inputs,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    inputs = tf.identity(inputs_tensor)
    inputs = tf.cast(inputs, tf.float32)
    results["res_high"] = tf.compat.v1.layers.flatten(inputs=inputs,name=name,)
    t_start = time.time()
    results["res_high"] = tf.compat.v1.layers.flatten(inputs=inputs,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

results = dict()
import tensorflow as tf
import time
try:
  try:
    arg_0_tensor = tf.random.uniform([1], dtype=tf.float16)
    arg_0 = tf.identity(arg_0_tensor)
    results["res_low"] = tf.reduce_min(arg_0,)
    t_start = time.time()
    results["res_low"] = tf.reduce_min(arg_0,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    arg_0 = tf.identity(arg_0_tensor)
    arg_0 = tf.cast(arg_0, tf.float64)
    results["res_high"] = tf.reduce_min(arg_0,)
    t_start = time.time()
    results["res_high"] = tf.reduce_min(arg_0,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

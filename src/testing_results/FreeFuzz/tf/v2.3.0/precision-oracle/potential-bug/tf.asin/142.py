results = dict()
import tensorflow as tf
import time
try:
  try:
    x_tensor = tf.random.uniform([410, 512], dtype=tf.float16)
    x = tf.identity(x_tensor)
    name_tensor = tf.random.uniform([2, 2], dtype=tf.float16)
    name = tf.identity(name_tensor)
    results["res_low"] = tf.asin(x=x,name=name,)
    t_start = time.time()
    results["res_low"] = tf.asin(x=x,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    x = tf.identity(x_tensor)
    x = tf.cast(x, tf.float32)
    name = tf.identity(name_tensor)
    name = tf.cast(name, tf.float64)
    results["res_high"] = tf.asin(x=x,name=name,)
    t_start = time.time()
    results["res_high"] = tf.asin(x=x,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

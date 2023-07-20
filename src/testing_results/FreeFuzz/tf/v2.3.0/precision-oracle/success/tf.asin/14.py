results = dict()
import tensorflow as tf
import time
try:
  try:
    x_tensor = tf.cast(tf.random.uniform([358, 384], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
    x = tf.identity(x_tensor)
    name = tf.uint8
    results["res_low"] = tf.asin(x=x,name=name,)
    t_start = time.time()
    results["res_low"] = tf.asin(x=x,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    x = tf.identity(x_tensor)
    x = tf.cast(x, tf.bool)
    name = tf.uint8
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
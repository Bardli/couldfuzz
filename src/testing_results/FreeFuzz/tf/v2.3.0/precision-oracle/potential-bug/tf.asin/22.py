results = dict()
import tensorflow as tf
import time
try:
  try:
    x_tensor = tf.random.uniform([372, 512], dtype=tf.float16)
    x = tf.identity(x_tensor)
    name_tensor = tf.saturate_cast(tf.random.uniform([1, 2], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int8)
    name = tf.identity(name_tensor)
    name = tf.Variable(name)
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
    name = tf.cast(name, tf.int32)
    name = tf.Variable(name)
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

results = dict()
import tensorflow as tf
import time
try:
  try:
    x_tensor = tf.random.uniform([1, 256], dtype=tf.float16)
    x = tf.identity(x_tensor)
    name_0 = -1
    name_1 = 0
    name = (name_0,name_1,)
    results["res_low"] = tf.compat.v1.tan(x=x,name=name,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.tan(x=x,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    x = tf.identity(x_tensor)
    x = tf.cast(x, tf.float32)
    name = (name_0,name_1,)
    results["res_high"] = tf.compat.v1.tan(x=x,name=name,)
    t_start = time.time()
    results["res_high"] = tf.compat.v1.tan(x=x,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

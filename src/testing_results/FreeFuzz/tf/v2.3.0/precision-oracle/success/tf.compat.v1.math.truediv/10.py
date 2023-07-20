results = dict()
import tensorflow as tf
import time
try:
  try:
    x_tensor = tf.random.uniform([3, 12, 5, 5], dtype=tf.float16)
    x = tf.identity(x_tensor)
    y_tensor = tf.random.uniform([], dtype=tf.float16)
    y = tf.identity(y_tensor)
    name = None
    results["res_low"] = tf.compat.v1.math.truediv(x=x,y=y,name=name,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.math.truediv(x=x,y=y,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    x = tf.identity(x_tensor)
    x = tf.cast(x, tf.float32)
    y = tf.identity(y_tensor)
    y = tf.cast(y, tf.float32)
    results["res_high"] = tf.compat.v1.math.truediv(x=x,y=y,name=name,)
    t_start = time.time()
    results["res_high"] = tf.compat.v1.math.truediv(x=x,y=y,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

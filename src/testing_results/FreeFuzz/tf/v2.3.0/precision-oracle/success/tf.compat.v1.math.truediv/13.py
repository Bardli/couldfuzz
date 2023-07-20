results = dict()
import tensorflow as tf
import time
try:
  try:
    x_tensor = tf.random.uniform([1, 1, 16, 16], dtype=tf.float16)
    x = tf.identity(x_tensor)
    y_tensor = tf.saturate_cast(tf.random.uniform([], minval=0, maxval=256, dtype=tf.int64), dtype=tf.uint8)
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
    y = tf.cast(y, tf.uint8)
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
results = dict()
import tensorflow as tf
import time
try:
  try:
    x_tensor = tf.saturate_cast(tf.random.uniform([394, 512], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint64)
    x = tf.identity(x_tensor)
    results["res_low"] = tf.compat.v1.tan(x=x,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.tan(x=x,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    x = tf.identity(x_tensor)
    x = tf.cast(x, tf.uint64)
    results["res_high"] = tf.compat.v1.tan(x=x,)
    t_start = time.time()
    results["res_high"] = tf.compat.v1.tan(x=x,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
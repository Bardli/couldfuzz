results = dict()
import tensorflow as tf
import time
try:
  try:
    x_tensor = tf.random.uniform([442, 384], dtype=tf.bfloat16)
    x = tf.identity(x_tensor)
    name = None
    results["res_low"] = tf.raw_ops.Asinh(x=x,name=name,)
    t_start = time.time()
    results["res_low"] = tf.raw_ops.Asinh(x=x,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    x = tf.identity(x_tensor)
    x = tf.cast(x, tf.bfloat16)
    results["res_high"] = tf.raw_ops.Asinh(x=x,name=name,)
    t_start = time.time()
    results["res_high"] = tf.raw_ops.Asinh(x=x,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

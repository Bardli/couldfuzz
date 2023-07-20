results = dict()
import tensorflow as tf
import time
try:
  try:
    trainable = True
    name = None
    dtype_tensor = tf.saturate_cast(tf.random.uniform([2, 1], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int8)
    dtype = tf.identity(dtype_tensor)
    results["res_low"] = tf.compat.v1.layers.Layer(trainable=trainable,name=name,dtype=dtype,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.layers.Layer(trainable=trainable,name=name,dtype=dtype,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    dtype = tf.identity(dtype_tensor)
    dtype = tf.cast(dtype, tf.int32)
    results["res_high"] = tf.compat.v1.layers.Layer(trainable=trainable,name=name,dtype=dtype,)
    t_start = time.time()
    results["res_high"] = tf.compat.v1.layers.Layer(trainable=trainable,name=name,dtype=dtype,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

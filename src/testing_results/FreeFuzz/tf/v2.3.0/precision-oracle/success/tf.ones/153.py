results = dict()
import tensorflow as tf
import time
try:
  try:
    shape_0_tensor = tf.saturate_cast(tf.random.uniform([], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int8)
    shape_0 = tf.identity(shape_0_tensor)
    shape_1 = -1
    shape = [shape_0,shape_1,]
    dtype = "int64"
    results["res_low"] = tf.ones(shape=shape,dtype=dtype,)
    t_start = time.time()
    results["res_low"] = tf.ones(shape=shape,dtype=dtype,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    shape_0 = tf.identity(shape_0_tensor)
    shape_0 = tf.cast(shape_0, tf.int64)
    shape = [shape_0,shape_1,]
    results["res_high"] = tf.ones(shape=shape,dtype=dtype,)
    t_start = time.time()
    results["res_high"] = tf.ones(shape=shape,dtype=dtype,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

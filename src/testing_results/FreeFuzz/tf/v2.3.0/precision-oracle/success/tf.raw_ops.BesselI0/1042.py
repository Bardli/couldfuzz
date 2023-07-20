results = dict()
import tensorflow as tf
import time
try:
  try:
    x_0 = -1.0
    x_1 = -0.1
    x_2 = 0.1
    x_3 = 1.0
    x = [x_0,x_1,x_2,x_3,]
    name_tensor = tf.saturate_cast(tf.random.uniform([2, 1], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int8)
    name = tf.identity(name_tensor)
    name = tf.Variable(name)
    results["res_low"] = tf.raw_ops.BesselI0(x=x,name=name,)
    t_start = time.time()
    results["res_low"] = tf.raw_ops.BesselI0(x=x,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    x = [x_0,x_1,x_2,x_3,]
    name = tf.identity(name_tensor)
    name = tf.cast(name, tf.int32)
    name = tf.Variable(name)
    results["res_high"] = tf.raw_ops.BesselI0(x=x,name=name,)
    t_start = time.time()
    results["res_high"] = tf.raw_ops.BesselI0(x=x,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

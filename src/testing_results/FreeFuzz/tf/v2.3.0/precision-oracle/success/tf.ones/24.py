results = dict()
import tensorflow as tf
import time
try:
  try:
    arg_0_0_tensor = tf.saturate_cast(tf.random.uniform([], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint64)
    arg_0_0 = tf.identity(arg_0_0_tensor)
    arg_0_1 = 3
    arg_0_2 = 1
    arg_0_3 = 510
    arg_0 = [arg_0_0,arg_0_1,arg_0_2,arg_0_3,]
    results["res_low"] = tf.ones(arg_0,)
    t_start = time.time()
    results["res_low"] = tf.ones(arg_0,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    arg_0_0 = tf.identity(arg_0_0_tensor)
    arg_0_0 = tf.cast(arg_0_0, tf.uint64)
    arg_0 = [arg_0_0,arg_0_1,arg_0_2,arg_0_3,]
    results["res_high"] = tf.ones(arg_0,)
    t_start = time.time()
    results["res_high"] = tf.ones(arg_0,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

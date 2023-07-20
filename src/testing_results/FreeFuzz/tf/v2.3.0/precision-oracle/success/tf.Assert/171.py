results = dict()
import tensorflow as tf
import time
try:
  try:
    condition_tensor = tf.cast(tf.random.uniform([], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
    condition = tf.identity(condition_tensor)
    data_tensor = tf.saturate_cast(tf.random.uniform([], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int8)
    data = tf.identity(data_tensor)
    summarize = 1
    name = None
    results["res_low"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
    t_start = time.time()
    results["res_low"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    condition = tf.identity(condition_tensor)
    condition = tf.cast(condition, tf.bool)
    data = tf.identity(data_tensor)
    data = tf.cast(data, tf.int32)
    results["res_high"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
    t_start = time.time()
    results["res_high"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

results = dict()
import tensorflow as tf
import time
try:
  try:
    condition_tensor = tf.complex(tf.random.uniform([1, 1], dtype=tf.float32),tf.random.uniform([1, 1], dtype=tf.float32))
    condition = tf.identity(condition_tensor)
    data_tensor = tf.saturate_cast(tf.random.uniform([1, 1], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int8)
    data = tf.identity(data_tensor)
    summarize_tensor = tf.saturate_cast(tf.random.uniform([1, 1], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int8)
    summarize = tf.identity(summarize_tensor)
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
    condition = tf.cast(condition, tf.complex128)
    data = tf.identity(data_tensor)
    data = tf.cast(data, tf.int32)
    summarize = tf.identity(summarize_tensor)
    summarize = tf.cast(summarize, tf.int32)
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

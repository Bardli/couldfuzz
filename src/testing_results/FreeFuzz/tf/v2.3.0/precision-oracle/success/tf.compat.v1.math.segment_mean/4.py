results = dict()
import tensorflow as tf
import time
try:
  try:
    data_tensor = tf.saturate_cast(tf.random.uniform([2, 3], minval=0, maxval=256, dtype=tf.int64), dtype=tf.uint8)
    data = tf.identity(data_tensor)
    segment_ids_0 = 0
    segment_ids_1 = 1
    segment_ids = [segment_ids_0,segment_ids_1,]
    name = None
    results["res_low"] = tf.compat.v1.math.segment_mean(data=data,segment_ids=segment_ids,name=name,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.math.segment_mean(data=data,segment_ids=segment_ids,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    data = tf.identity(data_tensor)
    data = tf.cast(data, tf.uint8)
    segment_ids = [segment_ids_0,segment_ids_1,]
    results["res_high"] = tf.compat.v1.math.segment_mean(data=data,segment_ids=segment_ids,name=name,)
    t_start = time.time()
    results["res_high"] = tf.compat.v1.math.segment_mean(data=data,segment_ids=segment_ids,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

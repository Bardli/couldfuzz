results = dict()
import tensorflow as tf
import time
try:
  try:
    data_tensor = tf.random.uniform([3, 1, 2, 3], dtype=tf.float16)
    data = tf.identity(data_tensor)
    segment_ids_0 = -1024
    segment_ids_1 = 3
    segment_ids_2 = 1
    segment_ids = [segment_ids_0,segment_ids_1,segment_ids_2,]
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
    data = tf.cast(data, tf.float32)
    segment_ids = [segment_ids_0,segment_ids_1,segment_ids_2,]
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

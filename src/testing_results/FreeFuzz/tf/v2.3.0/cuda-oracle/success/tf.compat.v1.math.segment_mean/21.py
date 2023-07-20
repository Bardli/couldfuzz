results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      data_tensor = tf.saturate_cast(tf.random.uniform([2, 3], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint16)
      data = tf.identity(data_tensor)
      segment_ids_0 = 0
      segment_ids_1 = 1
      segment_ids = [segment_ids_0,segment_ids_1,]
      name = None
      results["res_cpu"] = tf.compat.v1.math.segment_mean(data=data,segment_ids=segment_ids,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      data = tf.identity(data_tensor)
      data = tf.cast(data, tf.uint16)
      segment_ids = [segment_ids_0,segment_ids_1,]
      results["res_gpu"] = tf.compat.v1.math.segment_mean(data=data,segment_ids=segment_ids,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

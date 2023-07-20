results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      data_tensor = tf.random.uniform([3, 1, 0, 3], dtype=tf.float64)
      data = tf.identity(data_tensor)
      segment_ids_0 = 1024
      segment_ids_1 = 1
      segment_ids_2 = 0
      segment_ids = [segment_ids_0,segment_ids_1,segment_ids_2,]
      name = None
      results["res_cpu"] = tf.compat.v1.math.segment_mean(data=data,segment_ids=segment_ids,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      data = tf.identity(data_tensor)
      data = tf.cast(data, tf.float64)
      segment_ids = [segment_ids_0,segment_ids_1,segment_ids_2,]
      results["res_gpu"] = tf.compat.v1.math.segment_mean(data=data,segment_ids=segment_ids,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

import tensorflow as tf
try:
  data_tensor = tf.random.uniform([1, 3, 1], dtype=tf.float32)
  data = tf.identity(data_tensor)
  segment_ids_0 = 0
  segment_ids_1 = 1
  segment_ids = [segment_ids_0,segment_ids_1,]
  name = None
  results["res"] = tf.compat.v1.math.segment_mean(data=data,segment_ids=segment_ids,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

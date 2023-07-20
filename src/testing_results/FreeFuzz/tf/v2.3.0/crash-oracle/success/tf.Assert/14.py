import tensorflow as tf
try:
  condition_tensor = tf.complex(tf.random.uniform([1, 1], dtype=tf.float64),tf.random.uniform([1, 1], dtype=tf.float64))
  condition = tf.identity(condition_tensor)
  data_tensor = tf.random.uniform([1, 1], minval=-256, maxval=257, dtype=tf.int32)
  data = tf.identity(data_tensor)
  summarize_tensor = tf.random.uniform([1, 1], minval=-256, maxval=257, dtype=tf.int32)
  summarize = tf.identity(summarize_tensor)
  name = None
  results["res"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
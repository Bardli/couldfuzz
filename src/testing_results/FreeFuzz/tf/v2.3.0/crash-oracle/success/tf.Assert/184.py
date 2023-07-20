import tensorflow as tf
try:
  condition_tensor = tf.cast(tf.random.uniform([], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
  condition = tf.identity(condition_tensor)
  data_tensor = tf.random.uniform([], dtype=tf.float32)
  data = tf.identity(data_tensor)
  summarize_tensor = tf.random.uniform([], minval=-256, maxval=257, dtype=tf.int64)
  summarize = tf.identity(summarize_tensor)
  name = None
  results["res"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

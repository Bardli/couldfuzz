results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      condition_tensor = tf.cast(tf.random.uniform([], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
      condition = tf.identity(condition_tensor)
      data_tensor = tf.random.uniform([], dtype=tf.float32)
      data = tf.identity(data_tensor)
      summarize_tensor = tf.random.uniform([], dtype=tf.float32)
      summarize = tf.identity(summarize_tensor)
      name = None
      results["res_cpu"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      condition = tf.identity(condition_tensor)
      condition = tf.cast(condition, tf.bool)
      data = tf.identity(data_tensor)
      data = tf.cast(data, tf.float32)
      summarize = tf.identity(summarize_tensor)
      summarize = tf.cast(summarize, tf.float32)
      results["res_gpu"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

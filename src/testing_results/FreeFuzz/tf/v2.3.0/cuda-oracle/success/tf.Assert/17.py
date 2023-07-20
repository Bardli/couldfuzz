results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      condition_tensor = tf.complex(tf.random.uniform([1, 1], dtype=tf.float64),tf.random.uniform([1, 1], dtype=tf.float64))
      condition = tf.identity(condition_tensor)
      data_tensor = tf.random.uniform([1, 1], minval=-256, maxval=257, dtype=tf.int32)
      data = tf.identity(data_tensor)
      summarize_tensor = tf.random.uniform([1, 1], minval=-256, maxval=257, dtype=tf.int32)
      summarize = tf.identity(summarize_tensor)
      name = None
      results["res_cpu"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      condition = tf.identity(condition_tensor)
      condition = tf.cast(condition, tf.complex128)
      data = tf.identity(data_tensor)
      data = tf.cast(data, tf.int32)
      summarize = tf.identity(summarize_tensor)
      summarize = tf.cast(summarize, tf.int32)
      results["res_gpu"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x_tensor = tf.saturate_cast(tf.random.uniform([10000, 1], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int16)
      x = tf.identity(x_tensor)
      results["res_cpu"] = tf.compat.v1.tan(x=x,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      x = tf.identity(x_tensor)
      x = tf.cast(x, tf.int16)
      results["res_gpu"] = tf.compat.v1.tan(x=x,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

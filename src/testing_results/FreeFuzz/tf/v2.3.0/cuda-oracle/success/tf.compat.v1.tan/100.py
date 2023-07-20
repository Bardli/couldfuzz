results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x_tensor = tf.saturate_cast(tf.random.uniform([394, 512], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint32)
      x = tf.identity(x_tensor)
      results["res_cpu"] = tf.compat.v1.tan(x=x,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      x = tf.identity(x_tensor)
      x = tf.cast(x, tf.uint32)
      results["res_gpu"] = tf.compat.v1.tan(x=x,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

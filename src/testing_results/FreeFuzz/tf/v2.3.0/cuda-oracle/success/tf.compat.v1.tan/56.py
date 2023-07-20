results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x_tensor = tf.cast(tf.random.uniform([1, 256], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
      x = tf.identity(x_tensor)
      results["res_cpu"] = tf.compat.v1.tan(x=x,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      x = tf.identity(x_tensor)
      x = tf.cast(x, tf.bool)
      results["res_gpu"] = tf.compat.v1.tan(x=x,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

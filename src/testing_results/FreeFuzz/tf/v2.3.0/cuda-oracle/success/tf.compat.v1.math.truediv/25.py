results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x_tensor = tf.saturate_cast(tf.random.uniform([1, 16, 229, 229], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint64)
      x = tf.identity(x_tensor)
      y_tensor = tf.random.uniform([], dtype=tf.float32)
      y = tf.identity(y_tensor)
      name = None
      results["res_cpu"] = tf.compat.v1.math.truediv(x=x,y=y,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      x = tf.identity(x_tensor)
      x = tf.cast(x, tf.uint64)
      y = tf.identity(y_tensor)
      y = tf.cast(y, tf.float32)
      results["res_gpu"] = tf.compat.v1.math.truediv(x=x,y=y,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

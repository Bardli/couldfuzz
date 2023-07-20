results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x_tensor = tf.cast(tf.random.uniform([1], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
      x = tf.identity(x_tensor)
      y_tensor = tf.cast(tf.random.uniform([4], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
      y = tf.identity(y_tensor)
      name = None
      results["res_cpu"] = tf.logical_and(x=x,y=y,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      x = tf.identity(x_tensor)
      x = tf.cast(x, tf.bool)
      y = tf.identity(y_tensor)
      y = tf.cast(y, tf.bool)
      results["res_gpu"] = tf.logical_and(x=x,y=y,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

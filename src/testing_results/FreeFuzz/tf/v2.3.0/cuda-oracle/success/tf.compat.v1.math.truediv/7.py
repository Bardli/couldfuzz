results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x_tensor = tf.random.uniform([1, 12, 229, 229], dtype=tf.float16)
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
      x = tf.cast(x, tf.float16)
      y = tf.identity(y_tensor)
      y = tf.cast(y, tf.float32)
      results["res_gpu"] = tf.compat.v1.math.truediv(x=x,y=y,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x_tensor = tf.random.uniform([201, 81], dtype=tf.float32)
      x = tf.identity(x_tensor)
      name_tensor = tf.random.uniform([1, 2], dtype=tf.float64)
      name = tf.identity(name_tensor)
      name = tf.Variable(name)
      results["res_cpu"] = tf.compat.v1.tan(x=x,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      x = tf.identity(x_tensor)
      x = tf.cast(x, tf.float32)
      name = tf.identity(name_tensor)
      name = tf.cast(name, tf.float64)
      name = tf.Variable(name)
      results["res_gpu"] = tf.compat.v1.tan(x=x,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

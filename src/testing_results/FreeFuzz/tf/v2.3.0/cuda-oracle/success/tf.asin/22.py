results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x_tensor = tf.random.uniform([372, 512], dtype=tf.float32)
      x = tf.identity(x_tensor)
      name_tensor = tf.random.uniform([1, 2], minval=-256, maxval=257, dtype=tf.int32)
      name = tf.identity(name_tensor)
      name = tf.Variable(name)
      results["res_cpu"] = tf.asin(x=x,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      x = tf.identity(x_tensor)
      x = tf.cast(x, tf.float32)
      name = tf.identity(name_tensor)
      name = tf.cast(name, tf.int32)
      name = tf.Variable(name)
      results["res_gpu"] = tf.asin(x=x,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

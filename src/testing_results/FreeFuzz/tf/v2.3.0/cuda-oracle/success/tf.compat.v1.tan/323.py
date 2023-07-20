results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x_tensor = tf.random.uniform([1, 256], dtype=tf.float32)
      x = tf.identity(x_tensor)
      name_0 = -1
      name_1 = 0
      name = (name_0,name_1,)
      results["res_cpu"] = tf.compat.v1.tan(x=x,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      x = tf.identity(x_tensor)
      x = tf.cast(x, tf.float32)
      name = (name_0,name_1,)
      results["res_gpu"] = tf.compat.v1.tan(x=x,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

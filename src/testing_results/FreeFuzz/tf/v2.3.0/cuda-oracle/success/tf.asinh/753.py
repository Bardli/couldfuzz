results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x_tensor = tf.random.uniform([403, 384, 1], dtype=tf.bfloat16)
      x = tf.identity(x_tensor)
      name = None
      results["res_cpu"] = tf.asinh(x=x,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      x = tf.identity(x_tensor)
      x = tf.cast(x, tf.bfloat16)
      results["res_gpu"] = tf.asinh(x=x,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

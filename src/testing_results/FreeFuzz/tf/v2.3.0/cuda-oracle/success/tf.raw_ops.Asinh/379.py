results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x_tensor = tf.saturate_cast(tf.random.uniform([430, 384], minval=-128, maxval=128, dtype=tf.int64), dtype=tf.int8)
      x = tf.identity(x_tensor)
      name = None
      results["res_cpu"] = tf.raw_ops.Asinh(x=x,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      x = tf.identity(x_tensor)
      x = tf.cast(x, tf.int8)
      results["res_gpu"] = tf.raw_ops.Asinh(x=x,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

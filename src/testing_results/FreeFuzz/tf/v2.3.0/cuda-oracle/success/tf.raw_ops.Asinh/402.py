results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x_tensor = tf.saturate_cast(tf.random.uniform([10, 512], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint16)
      x = tf.identity(x_tensor)
      name_0 = 2
      name_1 = -1024
      name = [name_0,name_1,]
      results["res_cpu"] = tf.raw_ops.Asinh(x=x,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      x = tf.identity(x_tensor)
      x = tf.cast(x, tf.uint16)
      name = [name_0,name_1,]
      results["res_gpu"] = tf.raw_ops.Asinh(x=x,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x_tensor = tf.complex(tf.random.uniform([380, 384], dtype=tf.float32),tf.random.uniform([380, 384], dtype=tf.float32))
      x = tf.identity(x_tensor)
      name = None
      results["res_cpu"] = tf.raw_ops.Asinh(x=x,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      x = tf.identity(x_tensor)
      x = tf.cast(x, tf.complex64)
      results["res_gpu"] = tf.raw_ops.Asinh(x=x,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

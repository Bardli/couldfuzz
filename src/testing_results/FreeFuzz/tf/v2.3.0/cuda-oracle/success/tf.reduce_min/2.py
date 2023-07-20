results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      arg_0_tensor = tf.complex(tf.random.uniform([2, 2], dtype=tf.float64),tf.random.uniform([2, 2], dtype=tf.float64))
      arg_0 = tf.identity(arg_0_tensor)
      results["res_cpu"] = tf.reduce_min(arg_0,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      arg_0 = tf.identity(arg_0_tensor)
      arg_0 = tf.cast(arg_0, tf.complex128)
      results["res_gpu"] = tf.reduce_min(arg_0,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      tensor_tensor = tf.random.uniform([36, 2, 256, 513], dtype=tf.float32)
      tensor = tf.identity(tensor_tensor)
      paddings_tensor = tf.random.uniform([4, 2, 1], minval=-256, maxval=257, dtype=tf.int64)
      paddings = tf.identity(paddings_tensor)
      mode = "CONSTANT"
      name = None
      constant_values = 0
      results["res_cpu"] = tf.compat.v1.pad(tensor=tensor,paddings=paddings,mode=mode,name=name,constant_values=constant_values,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      tensor = tf.identity(tensor_tensor)
      tensor = tf.cast(tensor, tf.float32)
      paddings = tf.identity(paddings_tensor)
      paddings = tf.cast(paddings, tf.int64)
      results["res_gpu"] = tf.compat.v1.pad(tensor=tensor,paddings=paddings,mode=mode,name=name,constant_values=constant_values,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
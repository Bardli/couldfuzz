results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      tensor_tensor = tf.random.uniform([1, 8, 12, 512], dtype=tf.float32)
      tensor = tf.identity(tensor_tensor)
      indices_tensor = tf.random.uniform([0, 2], dtype=tf.float64)
      indices = tf.identity(indices_tensor)
      updates_tensor = tf.random.uniform([0, 12, 512], dtype=tf.float16)
      updates = tf.identity(updates_tensor)
      name = None
      results["res_cpu"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      tensor = tf.identity(tensor_tensor)
      tensor = tf.cast(tensor, tf.float32)
      indices = tf.identity(indices_tensor)
      indices = tf.cast(indices, tf.float64)
      updates = tf.identity(updates_tensor)
      updates = tf.cast(updates, tf.float16)
      results["res_gpu"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
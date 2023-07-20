results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      tensor_tensor = tf.random.uniform([3, 512, 768], dtype=tf.float32)
      tensor = tf.identity(tensor_tensor)
      indices_tensor = tf.saturate_cast(tf.random.uniform([3, 2], minval=0, maxval=256, dtype=tf.int64), dtype=tf.uint8)
      indices = tf.identity(indices_tensor)
      updates_tensor = tf.random.uniform([3, 768], dtype=tf.float32)
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
      indices = tf.cast(indices, tf.uint8)
      updates = tf.identity(updates_tensor)
      updates = tf.cast(updates, tf.float32)
      results["res_gpu"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

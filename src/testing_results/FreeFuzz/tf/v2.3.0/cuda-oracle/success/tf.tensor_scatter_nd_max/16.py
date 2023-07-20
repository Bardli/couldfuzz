results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      tensor_tensor = tf.saturate_cast(tf.random.uniform([1, 35, 12, 512], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint16)
      tensor = tf.identity(tensor_tensor)
      indices_tensor = tf.random.uniform([0, 2], minval=-256, maxval=257, dtype=tf.int64)
      indices = tf.identity(indices_tensor)
      updates_tensor = tf.random.uniform([0, 12, 512], dtype=tf.float32)
      updates = tf.identity(updates_tensor)
      name = None
      results["res_cpu"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      tensor = tf.identity(tensor_tensor)
      tensor = tf.cast(tensor, tf.uint16)
      indices = tf.identity(indices_tensor)
      indices = tf.cast(indices, tf.int64)
      updates = tf.identity(updates_tensor)
      updates = tf.cast(updates, tf.float32)
      results["res_gpu"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
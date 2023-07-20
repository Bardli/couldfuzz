results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      tensor_tensor = tf.random.uniform([6, 3], minval=-256, maxval=257, dtype=tf.int32)
      tensor = tf.identity(tensor_tensor)
      indices_tensor = tf.random.uniform([2, 1], minval=-256, maxval=257, dtype=tf.int32)
      indices = tf.identity(indices_tensor)
      updates_tensor = tf.cast(tf.random.uniform([2, 3], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
      updates = tf.identity(updates_tensor)
      name = None
      results["res_cpu"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      tensor = tf.identity(tensor_tensor)
      tensor = tf.cast(tensor, tf.int32)
      indices = tf.identity(indices_tensor)
      indices = tf.cast(indices, tf.int32)
      updates = tf.identity(updates_tensor)
      updates = tf.cast(updates, tf.bool)
      results["res_gpu"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

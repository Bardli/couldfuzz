import tensorflow as tf
try:
  tensor_tensor = tf.random.uniform([1, 35, 12, 512], dtype=tf.float32)
  tensor = tf.identity(tensor_tensor)
  indices_tensor = tf.random.uniform([0, 2], minval=-256, maxval=257, dtype=tf.int64)
  indices = tf.identity(indices_tensor)
  updates_tensor = tf.random.uniform([0, 12, 512], dtype=tf.float32)
  updates = tf.identity(updates_tensor)
  name = None
  results["res"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

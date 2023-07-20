import tensorflow as tf
try:
  tensor_tensor = tf.random.uniform([3, 512, 768], dtype=tf.float32)
  tensor = tf.identity(tensor_tensor)
  indices_tensor = tf.saturate_cast(tf.random.uniform([3, 2], minval=0, maxval=256, dtype=tf.int64), dtype=tf.uint8)
  indices = tf.identity(indices_tensor)
  updates_tensor = tf.random.uniform([3, 768], dtype=tf.float32)
  updates = tf.identity(updates_tensor)
  name = None
  results["res"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

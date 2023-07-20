import tensorflow as tf
try:
  tensor_tensor = tf.random.uniform([5, 5], dtype=tf.float32)
  tensor = tf.identity(tensor_tensor)
  indices_tensor = tf.random.uniform([2, 5, 2], minval=-256, maxval=257, dtype=tf.int32)
  indices = tf.identity(indices_tensor)
  updates_0_0 = 1
  updates_0_1 = 1
  updates_0_2 = 1
  updates_0_3 = 1
  updates_0_4 = 1
  updates_0 = [updates_0_0,updates_0_1,updates_0_2,updates_0_3,updates_0_4,]
  updates_1_0 = 1
  updates_1_1 = 1
  updates_1_2 = 1
  updates_1_3 = 1
  updates_1_4 = 1
  updates_1 = [updates_1_0,updates_1_1,updates_1_2,updates_1_3,updates_1_4,]
  updates = [updates_0,updates_1,]
  name = None
  results["res"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

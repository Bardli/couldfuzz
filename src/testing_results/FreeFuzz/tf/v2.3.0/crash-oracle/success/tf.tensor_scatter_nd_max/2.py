import tensorflow as tf
try:
  tensor_tensor = tf.random.uniform([13, 11, 7, 5, 3], dtype=tf.float32)
  tensor = tf.identity(tensor_tensor)
  indices_0_0 = 0
  indices_0_1 = 0
  indices_0 = [indices_0_0,indices_0_1,]
  indices_1_0 = 1
  indices_1_1 = 0
  indices_1 = [indices_1_0,indices_1_1,]
  indices_2_0 = 2
  indices_2_1 = 0
  indices_2 = [indices_2_0,indices_2_1,]
  indices = [indices_0,indices_1,indices_2,]
  updates_tensor = tf.random.uniform([3, 7, 5, 3], dtype=tf.float32)
  updates = tf.identity(updates_tensor)
  name = None
  results["res"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

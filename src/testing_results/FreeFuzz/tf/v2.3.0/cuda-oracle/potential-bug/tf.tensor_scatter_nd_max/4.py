results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      tensor_tensor = tf.random.uniform([13, 11, 7, 5, 3], dtype=tf.float32)
      tensor = tf.identity(tensor_tensor)
      indices_0_0 = 0
      indices_0_1 = 1
      indices_0 = [indices_0_0,indices_0_1,]
      indices_1_0 = 1025
      indices_1_1 = -4
      indices_1 = [indices_1_0,indices_1_1,]
      indices_2_0 = 0
      indices_2_1 = -1
      indices_2 = [indices_2_0,indices_2_1,]
      indices = [indices_0,indices_1,indices_2,]
      updates_tensor = tf.random.uniform([3, 7, 5, 3], dtype=tf.float32)
      updates = tf.identity(updates_tensor)
      name = None
      results["res_cpu"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      tensor = tf.identity(tensor_tensor)
      tensor = tf.cast(tensor, tf.float32)
      indices_0 = [indices_0_0,indices_0_1,]
      indices_1 = [indices_1_0,indices_1_1,]
      indices_2 = [indices_2_0,indices_2_1,]
      indices = [indices_0,indices_1,indices_2,]
      updates = tf.identity(updates_tensor)
      updates = tf.cast(updates, tf.float32)
      results["res_gpu"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

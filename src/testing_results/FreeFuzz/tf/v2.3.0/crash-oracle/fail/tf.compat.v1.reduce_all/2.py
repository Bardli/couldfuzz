import tensorflow as tf
try:
  input_tensor_tensor = tf.random.uniform([3, 512], minval=-256, maxval=257, dtype=tf.int64)
  input_tensor = tf.identity(input_tensor_tensor)
  axis = None
  keepdims = False
  name = None
  results["res"] = tf.compat.v1.reduce_all(input_tensor=input_tensor,axis=axis,keepdims=keepdims,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

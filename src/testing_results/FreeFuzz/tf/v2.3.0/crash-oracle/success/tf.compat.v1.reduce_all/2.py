import tensorflow as tf
try:
  input_tensor_tensor = tf.cast(tf.random.uniform([2, 1], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
  input_tensor = tf.identity(input_tensor_tensor)
  axis = None
  keepdims = False
  name = None
  results["res"] = tf.compat.v1.reduce_all(input_tensor=input_tensor,axis=axis,keepdims=keepdims,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

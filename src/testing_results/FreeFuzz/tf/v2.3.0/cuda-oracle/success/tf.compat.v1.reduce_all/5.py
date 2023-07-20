results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      input_tensor_tensor = tf.cast(tf.random.uniform([4, 1], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
      input_tensor = tf.identity(input_tensor_tensor)
      axis = None
      keepdims = True
      name = None
      results["res_cpu"] = tf.compat.v1.reduce_all(input_tensor=input_tensor,axis=axis,keepdims=keepdims,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      input_tensor = tf.identity(input_tensor_tensor)
      input_tensor = tf.cast(input_tensor, tf.bool)
      results["res_gpu"] = tf.compat.v1.reduce_all(input_tensor=input_tensor,axis=axis,keepdims=keepdims,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

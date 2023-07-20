results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      input_tensor_tensor = tf.random.uniform([3, 512], minval=-256, maxval=257, dtype=tf.int64)
      input_tensor = tf.identity(input_tensor_tensor)
      axis = None
      keepdims = False
      name = None
      results["res_cpu"] = tf.compat.v1.reduce_all(input_tensor=input_tensor,axis=axis,keepdims=keepdims,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      input_tensor = tf.identity(input_tensor_tensor)
      input_tensor = tf.cast(input_tensor, tf.int64)
      results["res_gpu"] = tf.compat.v1.reduce_all(input_tensor=input_tensor,axis=axis,keepdims=keepdims,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

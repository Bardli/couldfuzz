import tensorflow as tf
try:
  arg_0_tensor = tf.random.uniform([1], dtype=tf.float64)
  arg_0 = tf.identity(arg_0_tensor)
  results["res"] = tf.reduce_min(arg_0,)
except Exception as e:
  results["err"] = "Error:"+str(e)

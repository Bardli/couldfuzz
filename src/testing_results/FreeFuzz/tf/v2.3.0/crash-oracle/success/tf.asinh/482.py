import tensorflow as tf
try:
  x_tensor = tf.random.uniform([394, 384], dtype=tf.float32)
  x = tf.identity(x_tensor)
  name = tf.int64
  results["res"] = tf.asinh(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

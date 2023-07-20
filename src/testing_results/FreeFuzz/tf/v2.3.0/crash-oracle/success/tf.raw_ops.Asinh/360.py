import tensorflow as tf
try:
  x_tensor = tf.random.uniform([354, 384], dtype=tf.float32)
  x = tf.identity(x_tensor)
  name_tensor = tf.random.uniform([2, 2], dtype=tf.float32)
  name = tf.identity(name_tensor)
  results["res"] = tf.raw_ops.Asinh(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

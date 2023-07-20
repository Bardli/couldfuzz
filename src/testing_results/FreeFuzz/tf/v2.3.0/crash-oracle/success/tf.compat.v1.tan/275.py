import tensorflow as tf
try:
  x_tensor = tf.random.uniform([201, 81], dtype=tf.float32)
  x = tf.identity(x_tensor)
  name_tensor = tf.random.uniform([1, 2], dtype=tf.float64)
  name = tf.identity(name_tensor)
  name = tf.Variable(name)
  results["res"] = tf.compat.v1.tan(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

import tensorflow as tf
try:
  x_tensor = tf.random.uniform([1, 256], dtype=tf.float32)
  x = tf.identity(x_tensor)
  name_0 = -1
  name_1 = 0
  name = (name_0,name_1,)
  results["res"] = tf.compat.v1.tan(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

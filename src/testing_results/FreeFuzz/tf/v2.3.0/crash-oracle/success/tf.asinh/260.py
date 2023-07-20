import tensorflow as tf
try:
  x_tensor = tf.random.uniform([450, 384], dtype=tf.float32)
  x = tf.identity(x_tensor)
  name_0 = -1
  name_1 = 0
  name = (name_0,name_1,)
  results["res"] = tf.asinh(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

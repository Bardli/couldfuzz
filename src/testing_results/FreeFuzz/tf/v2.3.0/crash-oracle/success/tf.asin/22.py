import tensorflow as tf
try:
  x_tensor = tf.random.uniform([372, 512], dtype=tf.float32)
  x = tf.identity(x_tensor)
  name_tensor = tf.random.uniform([1, 2], minval=-256, maxval=257, dtype=tf.int32)
  name = tf.identity(name_tensor)
  name = tf.Variable(name)
  results["res"] = tf.asin(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

import tensorflow as tf
try:
  x_tensor = tf.complex(tf.random.uniform([408, 513], dtype=tf.float32),tf.random.uniform([408, 513], dtype=tf.float32))
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.asinh(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
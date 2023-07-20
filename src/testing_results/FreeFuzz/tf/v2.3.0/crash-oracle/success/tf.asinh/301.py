import tensorflow as tf
try:
  x_tensor = tf.complex(tf.random.uniform([392], dtype=tf.float64),tf.random.uniform([392], dtype=tf.float64))
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.asinh(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

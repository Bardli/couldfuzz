import tensorflow as tf
try:
  x_tensor = tf.complex(tf.random.uniform([380, 384], dtype=tf.float32),tf.random.uniform([380, 384], dtype=tf.float32))
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.raw_ops.Asinh(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

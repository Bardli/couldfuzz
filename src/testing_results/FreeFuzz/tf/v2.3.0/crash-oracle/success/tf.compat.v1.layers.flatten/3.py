import tensorflow as tf
try:
  inputs_tensor = tf.random.uniform([3, 3], dtype=tf.float32)
  inputs = tf.identity(inputs_tensor)
  name = False
  results["res"] = tf.compat.v1.layers.flatten(inputs=inputs,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
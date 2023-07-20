import tensorflow as tf
try:
  *size = 1233
  results["res"] = tf.experimental.numpy.random.rand(*size=*size,)
except Exception as e:
  results["err"] = "Error:"+str(e)

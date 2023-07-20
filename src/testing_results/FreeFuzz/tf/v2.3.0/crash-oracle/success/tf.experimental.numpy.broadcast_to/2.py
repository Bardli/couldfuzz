import tensorflow as tf
try:
  array_tensor = tf.random.uniform([4, 1], dtype=tf.float32)
  array = tf.identity(array_tensor)
  shape_0 = 4
  shape_1 = 32128
  shape = [shape_0,shape_1,]
  results["res"] = tf.experimental.numpy.broadcast_to(array=array,shape=shape,)
except Exception as e:
  results["err"] = "Error:"+str(e)

import tensorflow as tf
try:
  array_tensor = tf.random.uniform([1, 1, 20], minval=-256, maxval=257, dtype=tf.int32)
  array = tf.identity(array_tensor)
  shape_0 = -1024
  shape_1 = 4
  shape_2 = 20
  shape = [shape_0,shape_1,shape_2,]
  results["res"] = tf.experimental.numpy.broadcast_to(array=array,shape=shape,)
except Exception as e:
  results["err"] = "Error:"+str(e)
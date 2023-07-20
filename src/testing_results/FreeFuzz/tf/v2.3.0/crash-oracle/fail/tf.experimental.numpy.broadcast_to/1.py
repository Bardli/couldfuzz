import tensorflow as tf
try:
  array_0 = 1
  array_1 = 2
  array_2 = 3
  array = [array_0,array_1,array_2,]
  shape_0 = 1
  shape_1 = 1
  shape_2 = 2
  shape = [shape_0,shape_1,shape_2,]
  results["res"] = tf.experimental.numpy.broadcast_to(array=array,shape=shape,)
except Exception as e:
  results["err"] = "Error:"+str(e)

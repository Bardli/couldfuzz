import tensorflow as tf
try:
  shape_0 = 16
  shape_1 = 0
  shape = [shape_0,shape_1,]
  results["res"] = tf.ones(shape=shape,)
except Exception as e:
  results["err"] = "Error:"+str(e)

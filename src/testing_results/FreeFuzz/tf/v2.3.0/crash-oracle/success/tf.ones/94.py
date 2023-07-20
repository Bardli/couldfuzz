import tensorflow as tf
try:
  shape_0 = 1
  shape_1 = True
  shape = [shape_0,shape_1,]
  results["res"] = tf.ones(shape=shape,)
except Exception as e:
  results["err"] = "Error:"+str(e)

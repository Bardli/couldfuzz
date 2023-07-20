import tensorflow as tf
try:
  x = 1
  y_0 = 2
  y_1 = 1
  y_2 = 0
  y = [y_0,y_1,y_2,]
  name = None
  results["res"] = tf.compat.v1.math.pow(x=x,y=y,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

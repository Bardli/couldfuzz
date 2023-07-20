import tensorflow as tf
try:
  x = 0
  y_0 = 3
  y_1 = 2
  y_2 = 0
  y = [y_0,y_1,y_2,]
  name = None
  results["res"] = tf.compat.v1.math.pow(x=x,y=y,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

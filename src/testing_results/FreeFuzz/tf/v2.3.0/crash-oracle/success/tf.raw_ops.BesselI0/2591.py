import tensorflow as tf
try:
  x_0 = -14.0
  x_1 = -8.1
  x_2 = 7.1
  x_3 = -6.0
  x = [x_0,x_1,x_2,x_3,]
  name = None
  results["res"] = tf.raw_ops.BesselI0(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

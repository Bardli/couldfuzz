import tensorflow as tf
try:
  x_0 = 17.0
  x_1 = 14.5
  x_2 = 1.0
  x_3 = 2.0
  x = [x_0,x_1,x_2,x_3,]
  name = None
  results["res"] = tf.raw_ops.BesselI0(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
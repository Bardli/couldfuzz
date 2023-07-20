import tensorflow as tf
try:
  x_0 = -11.0
  x_1 = -50.5
  x_2 = 4.5
  x_3 = 33.0
  x = [x_0,x_1,x_2,x_3,]
  name = None
  results["res"] = tf.raw_ops.BesselI0(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

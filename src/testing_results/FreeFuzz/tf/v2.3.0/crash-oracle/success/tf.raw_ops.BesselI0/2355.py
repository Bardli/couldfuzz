import tensorflow as tf
try:
  x_0 = -101.0
  x_1 = -23.0
  x_2 = 1e+20
  x_3 = -1.0
  x = [x_0,x_1,x_2,x_3,]
  name = None
  results["res"] = tf.raw_ops.BesselI0(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
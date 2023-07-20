import tensorflow as tf
try:
  x_0 = 0.0
  x_1 = -9.5
  x_2 = 47.5
  x_3 = -1024.0
  x = [x_0,x_1,x_2,x_3,]
  name = None
  results["res"] = tf.raw_ops.BesselI0(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

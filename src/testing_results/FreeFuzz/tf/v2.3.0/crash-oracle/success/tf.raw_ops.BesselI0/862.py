import tensorflow as tf
try:
  x_0 = 38.5
  x_1 = -23.0
  x_2 = -13.0
  x_3 = -41.0
  x = [x_0,x_1,x_2,x_3,]
  name = None
  results["res"] = tf.raw_ops.BesselI0(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

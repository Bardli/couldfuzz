import tensorflow as tf
try:
  x_0 = -33.0
  x_1 = -52.9
  x_2 = -41.9
  x_3 = -54.9
  x = [x_0,x_1,x_2,x_3,]
  name = None
  results["res"] = tf.raw_ops.BesselI0(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

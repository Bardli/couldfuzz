import tensorflow as tf
try:
  arg_0_0 = 1
  arg_0_1 = -16
  arg_0 = [arg_0_0,arg_0_1,]
  arg_1 = None
  results["res"] = tf.ones(arg_0,arg_1,)
except Exception as e:
  results["err"] = "Error:"+str(e)

import tensorflow as tf
try:
  arg_0_0 = 1
  arg_0_1 = 236
  arg_0_2 = 235
  arg_0 = [arg_0_0,arg_0_1,arg_0_2,]
  results["res"] = tf.ones(arg_0,)
except Exception as e:
  results["err"] = "Error:"+str(e)

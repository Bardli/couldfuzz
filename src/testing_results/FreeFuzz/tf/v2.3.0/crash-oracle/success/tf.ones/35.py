import tensorflow as tf
try:
  arg_0_0 = 10
  arg_0_1 = 2
  arg_0_2 = 3
  arg_0 = [arg_0_0,arg_0_1,arg_0_2,]
  results["res"] = tf.ones(arg_0,)
except Exception as e:
  results["err"] = "Error:"+str(e)

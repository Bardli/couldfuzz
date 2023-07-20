import tensorflow as tf
try:
  tensor_0_0 = 1
  tensor_0_1 = 2
  tensor_0 = [tensor_0_0,tensor_0_1,]
  tensor_1_0 = -1
  tensor_1_1 = 1024
  tensor_1 = [tensor_1_0,tensor_1_1,]
  tensor_2_0 = 2
  tensor_2_1 = -1
  tensor_2 = [tensor_2_0,tensor_2_1,]
  tensor = [tensor_0,tensor_1,tensor_2,]
  indices_0_0 = 2
  indices_0_1 = 0
  indices_0 = [indices_0_0,indices_0_1,]
  indices_1_0 = -3
  indices_1_1 = -16
  indices_1 = [indices_1_0,indices_1_1,]
  indices = [indices_0,indices_1,]
  updates_0 = 5
  updates_1 = 10
  updates = [updates_0,updates_1,]
  name = None
  results["res"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)

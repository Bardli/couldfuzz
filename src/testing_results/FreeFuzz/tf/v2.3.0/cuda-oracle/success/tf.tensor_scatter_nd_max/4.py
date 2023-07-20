results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      tensor_0 = 0
      tensor_1 = 0
      tensor_2 = 0
      tensor_3 = 0
      tensor_4 = 0
      tensor_5 = 0
      tensor_6 = 0
      tensor_7 = 0
      tensor = [tensor_0,tensor_1,tensor_2,tensor_3,tensor_4,tensor_5,tensor_6,tensor_7,]
      indices_0_0 = 1
      indices_0 = [indices_0_0,]
      indices_1_0 = 3
      indices_1 = [indices_1_0,]
      indices_2_0 = 3
      indices_2 = [indices_2_0,]
      indices_3_0 = 8
      indices_3 = [indices_3_0,]
      indices = [indices_0,indices_1,indices_2,indices_3,]
      updates_0 = -16
      updates_1 = 10
      updates_2 = -16
      updates_3 = 11
      updates = [updates_0,updates_1,updates_2,updates_3,]
      name = None
      results["res_cpu"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      tensor = [tensor_0,tensor_1,tensor_2,tensor_3,tensor_4,tensor_5,tensor_6,tensor_7,]
      indices_0 = [indices_0_0,]
      indices_1 = [indices_1_0,]
      indices_2 = [indices_2_0,]
      indices_3 = [indices_3_0,]
      indices = [indices_0,indices_1,indices_2,indices_3,]
      updates = [updates_0,updates_1,updates_2,updates_3,]
      results["res_gpu"] = tf.tensor_scatter_nd_max(tensor=tensor,indices=indices,updates=updates,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

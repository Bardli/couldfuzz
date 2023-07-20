results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      array_0 = 1
      array_1 = 2
      array_2 = 3
      array = [array_0,array_1,array_2,]
      shape_0 = 1
      shape_1 = 1
      shape_2 = 2
      shape = [shape_0,shape_1,shape_2,]
      results["res_cpu"] = tf.experimental.numpy.broadcast_to(array=array,shape=shape,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      array = [array_0,array_1,array_2,]
      shape = [shape_0,shape_1,shape_2,]
      results["res_gpu"] = tf.experimental.numpy.broadcast_to(array=array,shape=shape,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)

results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      name = True
      trainable = True
      dtype = "float32"
      data_format = 0
      results["res_cpu"] = tf.keras.layers.GlobalAveragePooling2D(name=name,trainable=trainable,dtype=dtype,data_format=data_format,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      results["res_gpu"] = tf.keras.layers.GlobalAveragePooling2D(name=name,trainable=trainable,dtype=dtype,data_format=data_format,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      image_0_0_0 = -17.0
      image_0_0_1 = -1
      image_0_0_2 = -52.0
      image_0_0 = [image_0_0_0,image_0_0_1,image_0_0_2,]
      image_0_1_0 = 49.0
      image_0_1_1 = -42.0
      image_0_1_2 = 30.0
      image_0_1 = [image_0_1_0,image_0_1_1,image_0_1_2,]
      image_0 = [image_0_0,image_0_1,]
      image_1_0_0 = 50.0
      image_1_0_1 = -29.0
      image_1_0_2 = -42.0
      image_1_0 = [image_1_0_0,image_1_0_1,image_1_0_2,]
      image_1_1 = []
      image_1 = [image_1_0,image_1_1,]
      image = [image_0,image_1,]
      dtype = 5
      saturate = 10
      name = None
      results["res_cpu"] = tf.compat.v1.image.convert_image_dtype(image=image,dtype=dtype,saturate=saturate,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      image_0_0 = [image_0_0_0,image_0_0_1,image_0_0_2,]
      image_0_1 = [image_0_1_0,image_0_1_1,image_0_1_2,]
      image_0 = [image_0_0,image_0_1,]
      image_1_0 = [image_1_0_0,image_1_0_1,image_1_0_2,]
      image_1_1 = []
      image_1 = [image_1_0,image_1_1,]
      image = [image_0,image_1,]
      results["res_gpu"] = tf.compat.v1.image.convert_image_dtype(image=image,dtype=dtype,saturate=saturate,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
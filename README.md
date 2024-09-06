Create a dataset with a structure of 
![螢幕擷取畫面 2024-09-06 165950](https://github.com/user-attachments/assets/5c7effbf-c654-47ac-b6b1-e73a567a34ef)
with also a .yaml inside the dataset folder. The format of .yaml is
![螢幕擷取畫面 2024-09-06 170207](https://github.com/user-attachments/assets/8a589e25-6d22-4795-b6f0-b7e238ca730b)
the label of the dataset must be .txt if you use labelme to label the pictures  run txt.py to transform the files then run volov8.py to train your data.
Than a run folder will appear you can find all the results there . If you want to combine to curve in a picture you can run losscurve2.py to acheieve your goal.
You can also test your model after running the losscurve2.py if the train and validation curve decrease smothly and converges the result is acceptible, otherwise you have to do some adjustments.

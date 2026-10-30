from joblib import load

# Load the object or model from the file
loaded_object = joblib.load("./models/car_value_model.joblib")

# Now you can use it normally
print(type(loaded_object))



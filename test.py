from clarifai.rest import ClarifaiApp
app= ClarifaiApp(api_key='fb55a24f035040a3a86ed081b89bb64c')
model= app.models.get('food-items-v1.0')
response=model.predict_by_url(url='http://www.athenaspizzaamherst.com/wp-content/uploads/2013/05/front-1-1008x500.jpg')
print response
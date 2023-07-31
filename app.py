import pickle
from flask import Flask,render_template,request

#Create a flask object
app=Flask(__name__)
#Loading the pickle files(model)
regmodel=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')       

@app.route('/predict',methods=['POST'])
def predict():
    #print(request.form)
    gender = int(request.form['gender'])
    branch = int(request.form['branch'])
    ssc_cgpa = float(request.form['ssc_cgpa'])
    hsc_cgpa = float(request.form['hsc_cgpa'])
    ug_cgpa = float(request.form['ug_cgpa'])
    workexp = float(request.form['workexp'])
    num_of_projects = float(request.form['num_of_projects'])
    num_of_global_certifications = float(request.form['num_of_global_certifications'])
    github_acc= int(request.form['github_acc'])
    github_repo= float(request.form['github_repo'])
    input_values=[[gender,branch,ssc_cgpa,hsc_cgpa,ug_cgpa,workexp,num_of_projects,num_of_global_certifications ,github_acc,github_repo]]
    prediction = regmodel.predict(input_values)

    # Convert the prediction to a string and return it
    if prediction == 0:
        result = "Placed"
    else:
        result = "Not Placed"

    return render_template('index.html', prediction="{}".format(result))

if __name__ == '__main__':
    app.run(debug=True)

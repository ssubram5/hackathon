import subprocess
from flask.app import Flask
from flask.globals import request
from flask.templating import render_template
import requests
import json

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def home():
    result=[]
    if request.method == 'GET':
        return render_template('hack.html')
    elif request.method == 'POST':
        vnet_id = request.form['vnet_id']
        subnet_id = request.form['subnet_id']
        grafana = request.form['grafana']
        dynamic_vars = {
            "vnet_id": vnet_id,
            "subnet_id": subnet_id,
            "grafana": grafana,
        }

        # Define the path to the var.tf file
        var_tf_path = "var.tf"

        # Create and write the var.tf file
        with open(var_tf_path, "w") as var_tf_file:
            var_tf_file.write('variable "vnet_id" {\n')
            var_tf_file.write(f'  default = "{dynamic_vars["vnet_id"]}"\n')
            var_tf_file.write('}\n\n')

            var_tf_file.write('variable "subnet_id" {\n')
            var_tf_file.write(f'  default = "{dynamic_vars["subnet_id"]}"\n')
            var_tf_file.write('}\n\n')

            var_tf_file.write('variable "grafana" {\n')
            var_tf_file.write(f'  default = "{dynamic_vars["grafana"]}"\n')
            var_tf_file.write('}\n\n')

        print(f"Created {var_tf_path} with dynamic variables.")
    return "Form submitted successfully"

if __name__ == '__main__':
 app.run(debug=True)
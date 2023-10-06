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
        cluster_name = request.form['cluster_name']
        region = request.form['region']
        enable_karpenter = request.form['enable_karpenter']
        enable_external_dns = request.form['enable_external_dns']
        enable_argocd = request.form['enable_argocd']
        enable_ingress_nginx = request.form['enable_ingress_nginx']
        enable_velero = request.form['enable_velero']
        enable_cert_manager = request.form['enable_cert_manager']
        # Define the path to the var.tf file
        var_tf_path = "var.tf"

        # Create and write the var.tf file
        with open(var_tf_path, "w") as var_tf_file:
            var_tf_file.write('variable "cluster_name" {\n')
            var_tf_file.write(f'  default = "{cluster_name}"\n')
            var_tf_file.write('}\n\n')

            var_tf_file.write('variable "region" {\n')
            var_tf_file.write(f'  default = "{region}"\n')
            var_tf_file.write('}\n\n')

            var_tf_file.write('variable "enable_karpenter" {\n')
            var_tf_file.write(f'  default = "{enable_karpenter}"\n')
            var_tf_file.write('}\n\n')
            
            var_tf_file.write('variable "enable_external_dns" {\n')
            var_tf_file.write(f'  default = "{enable_external_dns}"\n')
            var_tf_file.write('}\n\n')
            
            var_tf_file.write('variable "enable_argocd" {\n')
            var_tf_file.write(f'  default = "{enable_argocd}"\n')
            var_tf_file.write('}\n\n')

            var_tf_file.write('variable "enable_ingress_nginx" {\n')
            var_tf_file.write(f'  default = "{enable_ingress_nginx}"\n')
            var_tf_file.write('}\n\n')
            
            var_tf_file.write('variable "enable_velero" {\n')
            var_tf_file.write(f'  default = "{enable_velero}"\n')
            var_tf_file.write('}\n\n')
            
            var_tf_file.write('variable "enable_cert_manager" {\n')
            var_tf_file.write(f'  default = "{enable_cert_manager}"\n')
            var_tf_file.write('}\n\n')
        print(f"Created {var_tf_path} with dynamic variables.")
    return "Form submitted successfully"

if __name__ == '__main__':
 app.run(debug=True)
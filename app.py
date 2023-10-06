import subprocess
import json

dynamic_vars = {
    "vnet_id": "value1",
    "subnet_id": "value2",
    "grafana": "value3",
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
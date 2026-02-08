from pathlib import Path
'''
# Déplacez le modèle ONNX vers le chemin du modèle Triton
#source_path = Path("/home/ec2-user/triton/yolo11l.onnx")
#destination_path = Path("/home/ec2-user/triton/trt-amani/yolo") / "1" / "model.onnx"

# Déplacer le fichier
#source_path.rename(destination_path)
Path("yolo11l.onnx").rename("/home/ec2-user/triton/trt_amani/yolo" / "1" / "model.onnx")

# Créez le fichier de configuration
config_path = Path("/home/ec2-user/triton/trt-amani/yolo") / "config.pbtxt"
'''
# Définir le chemin du modèle source
source_model = Path("model.plan")

# Définir le chemin de destination
destination_model = Path("/home/ec2-user/triton/trt_amani/yolo") / "1" / "model.plan"

# S'assurer que le dossier de destination existe
destination_model.parent.mkdir(parents=True, exist_ok=True)

# Renommer (déplacer) le fichier
source_model.rename(destination_model)

# Créez le fichier de configuration
config_path = Path("/home/ec2-user/triton/trt_amani/yolo") / "config.pbtxt"
# Données de configuration pour Triton
data = """
name: "yolo"
platform: "tensorrt_plan"
max_batch_size: 16

input [
  {
    name: "images"
    data_type: TYPE_FP16
    dims: [3, 640, 640]
  }
]

output [
  {
    name: "output0"
    data_type: TYPE_FP16
    dims: [84, -1]
  }
]

instance_group [
  {
    count: 1
    kind: KIND_GPU
  }
]
"""

# Écrire la configuration dans le fichier
with open(config_path, "w") as f:
    f.write(data)

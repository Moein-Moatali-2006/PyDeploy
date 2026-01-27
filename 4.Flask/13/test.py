from deepface import Deepface

objs = Deepface.analyze(
    img_path = "uploads/Linux_commands.png",
    actions = ["age"]
)

print(objs)
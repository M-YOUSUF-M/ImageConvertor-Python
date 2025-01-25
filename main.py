import subprocess
import sys
try:
  from PIL import Image
except Exception as e:
  subprocess.run([sys.executable,"-m","pip install","-r","requirment.txt"])


print("convert image [png <-> jpg <-> webp]")

while(True):

  print("enter 'exit' or 'Ctrl + C' to exit.")

  image_path:str = input('enter the image path[witout qoutes("")]: ')

  if(image_path.lower() == 'exit'):
    exit()

  print("1. image -> png")
  print("2. image -> jpg")
  print("3. image -> webp")

  try:
    options:int = int(input("Option: "))
  except Exception as e:
    print(e)

  try:
    new_path = f"{image_path.split('.')[0]}"
    im = Image.open(image_path).convert("RGB")
    match options:
      case 1:
        new_path +=".png"
        im.save(new_path,"png")
      case 2:
        new_path +=".jpg"
        im.save(new_path,"jpeg")
      case 3:
        new_path += ".webp"
        im.save(new_path,"webp")
    print(f"image converted. and saved as {new_path}")
  except Exception as e:
    print(e)
  print("\n")
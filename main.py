from rembg import remove
from PIL import Image

# Função para remover o fundo da imagem
def remove_background(image_path, output_path):
    image = Image.open(image_path)  # Carregar a imagem

    result = remove(image)  # Remover o fundo

    result.save(output_path, 'PNG')  # Salvar a imagem

# Executar a função
remove_background('imagem.jpg', 'imagem_sem_fundo.png')

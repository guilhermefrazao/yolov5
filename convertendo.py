import os

def convert_to_yolo_format(x_min, y_min, x_max, y_max, image_width, image_height):

    return 
    
def process_annotation_file(annotation_file, image_width, image_height, class_id):
    with open(annotation_file, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        # Supondo que os valores estão no formato: x_min y_min x_max y_max class_name class_id
        values = line.split()
        x_min = float(values[0])
        y_min = float(values[1])
        x_max = float(values[2])
        y_max = float(values[3])
        
        # Converte para o formato YOLO
        x_center, y_center, width, height = convert_to_yolo_format(x_min, y_min, x_max, y_max, image_width, image_height)
        
        # Escreve os novos valores no formato YOLOv5: <class_id> <x_center> <y_center> <width> <height>
        new_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

    # Salvar o arquivo modificado
    with open(annotation_file, 'w') as file:
        file.writelines(new_lines)


def process_all_annotations(directory, image_width, image_height, class_id=0):
    # Loop em todos os arquivos .txt no diretório
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            annotation_file = os.path.join(directory, filename)
            process_annotation_file(annotation_file, image_width, image_height, class_id)
            print(f"Processed {annotation_file}")


# Exemplo de uso
annotations_directory = 'dataset/train/labels'
image_width = 640  # Substitua pela largura das suas imagens
image_height = 480  # Substitua pela altura das suas imagens
class_id = 0 

process_all_annotations(annotations_directory, image_width, image_height, class_id)

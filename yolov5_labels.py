import os

def convert_to_yolo_format():
    return 

def process_annotation_file(annotation_file, image_width, image_height, class_id):
    with open(annotation_file, 'r') as file:
        lines = file.readlines()
    print(lines)
    new_lines = []
    for line in lines:
        values = line.split()
        x_min = float(values[0])
        y_min = float(values[1])
        x_max = float(values[2])
        y_max = float(values[3])

        x_center, y_center, width, height = convert_to_yolo_format(x_min, y_min, x_max, y_max, image_width, image_height)

        new_lines.append(f"{class_id}{x_center}{y_center}{width}{height}\n")

    return 

def process_labels(path, image_width, image_height, class_id):
    for filename in os.listdir(path):
        if filename.endswith("txt"):
            annotation_file = os.path.join(path, filename)
            process_annotation_file(annotation_file, image_width, image_height, class_id)
            print(f"Processed {annotation_file}")       


path = "dataset/train/labels"
image_height = 640
image_width = 480
class_id = 0

process_labels(path, image_width, image_height, class_id)
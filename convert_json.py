import json
import sys

def convert_json(input_file, output_file):
    # Load the original JSON data
    with open(input_file, "r") as file:
        original_data = json.load(file)

    # Initialize a list to store the converted data
    converted_data = []

    # Iterate through the original data and convert it
    for key, value in original_data.items():
        # Create a new data entry
        data_entry = {
            "id": 80571,
            "data": {
                "image": f"/data/local-files/?d=Hamza/datasets/hyper-kvasir/segmented-images/images/{key}.jpg"
            },
            "annotations": []
        }

        # Initialize an empty result list for the annotations
        result = []

        for idx, box in enumerate(value["bbox"]):
            # Create an annotation entry for each object
            annotation = {
                "id": f"object-{idx + 1}",
                "type": "rectanglelabels",
                "value": {
                    "x": (box['xmin'] / value['width']) * 100,
                    "y": (box['ymin'] / value['height']) * 100,
                    "width": ((box['xmax'] - box['xmin']) / value['width']) * 100,
                    "height": ((box['ymax'] - box['ymin']) / value['height']) * 100,
                    "rectanglelabels": ["polyp"]
                },
                "to_name": "image",
                "from_name": "label",
                "image_rotation": 0,
                "original_width": value["width"],
                "original_height": value["height"]
            }

            # Append the annotation to the result list
            result.append(annotation)

        # Add the result list to the data entry
        data_entry["annotations"] = [{"result": result}]

        # Append the converted data entry to the list
        converted_data.append(data_entry)

    # Save the converted data to a new JSON file
    with open(output_file, "w") as file:
        json.dump(converted_data, file, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_json(input_file, output_file)

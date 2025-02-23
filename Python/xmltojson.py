import xml.etree.ElementTree as ET
import json

def element_to_dict(element):
    """Recursively converts an XML ElementTree element to a Python dictionary,
    directly using text content as value when appropriate."""
    output_dict = {}
    if element.attrib:
        output_dict["attributes"] = element.attrib

    text = element.text
    if text and text.strip():
        clean_text = text.strip()
        if not element.attrib and not list(element): # Element has only text, no attributes and no children
            return clean_text # Return text directly as value
        else:
            output_dict["text"] = clean_text # Keep text under 'text' key if other attributes or children exist

    for child in element:
        child_dict = element_to_dict(child)
        if child.tag in output_dict:
            if type(output_dict[child.tag]) is list:
                output_dict[child.tag].append(child_dict)
            else:
                output_dict[child.tag] = [output_dict[child.tag], child_dict]
        else:
            output_dict[child.tag] = child_dict

    if not output_dict and not text: # Handle empty tags that have no attributes and no text explicitly as empty dict
        return {} # Return empty dictionary for empty tags

    return output_dict

def xml_to_json(xml_file_path, json_file_path=None):
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
    except FileNotFoundError:
        print(f"Error: XML file not found at {xml_file_path}")
        return None
    except ET.ParseError as e:
        print(f"Error: XML parsing failed for {xml_file_path}: {e}")
        return None

    root_dict_unwrapped = element_to_dict(root) # Get the dictionary from the root element
    root_dict = {root.tag: root_dict_unwrapped} # Now wrap it with the root tag

    json_output = json.dumps(root_dict, indent=4, ensure_ascii=False)

    if json_file_path:
        try:
            with open(json_file_path, 'w', encoding='utf-8') as f:
                json.dump(root_dict, f, indent=4, ensure_ascii=False)
            print(f"Successfully converted XML to JSON and saved to {json_file_path}")
        except Exception as e:
            print(f"Error writing JSON to file {json_file_path}: {e}")
    else:
        return json_output

    return json_output

# Example Usage:
xml_file = 'world_utf8.xml' # Replace with your XML file path
json_file = 'world.json'          # Replace with your desired JSON output file path (optional)

json_string = xml_to_json(xml_file, json_file)

if json_string:
    print("\nJSON Output (string):")
    # You can now work with the json_string variable
    # or if you saved to a file, check 'output.json'
    # print(json_string)
    pass
else:
    print("XML to JSON conversion failed.")

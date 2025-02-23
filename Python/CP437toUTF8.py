import xml.etree.ElementTree as ET
import re

def convert_cp437_to_utf8_xml(input_file, output_file):
    """
    Converts a CP437 XML file to UTF-8 XML, cleaning invalid characters.
    """
    try:
        with open(input_file, 'rb') as f:
            cp437_data = f.read()

        unicode_data = cp437_data.decode('cp437', errors='replace')
        unicode_data = unicode_data.replace('\ufffd', '') # Replace unicode replacement characters with spaces.

        # Remove or replace control characters (ASCII 0-31, 127)
        cleaned_unicode_data = re.sub(r'[\x00-\x1F\x7F]', ' ', unicode_data) # replace with space

        root = ET.fromstring(cleaned_unicode_data)

        tree = ET.ElementTree(root)
        tree.write(output_file, encoding='utf-8', xml_declaration=True)

        print(f"Successfully converted {input_file} to {output_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except ET.ParseError as e:
        print(f"Error: Failed to parse XML from '{input_file}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
input_filename = 'world.xml'
output_filename = 'world_utf8.xml'

convert_cp437_to_utf8_xml(input_filename, output_filename)

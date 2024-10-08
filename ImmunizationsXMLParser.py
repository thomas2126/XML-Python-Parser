import xml.etree.ElementTree as ET
import json

namespaces = {'hl7': 'urn:hl7-org:v3', 'sdtc': 'urn:hl7-org:sdtc'}

def xml_to_dict(element):
    if len(element) == 0:
        return element.text
    return {child.tag.split('}')[-1]: xml_to_dict(child) for child in element}

def parse_immunizations(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    try:
        immunizations_section = None
        for section in root.findall('.//hl7:section', namespaces):
            template_id = section.find('hl7:templateId', namespaces)
            #print(f"Checking section with templateId: {template_id.get('root') if template_id is not None else 'None'}")  # Log the templateId
            if template_id is not None and template_id.get('root') == '2.16.840.1.113883.10.20.22.2.2':
                immunizations_section = section
                break

        if immunizations_section is None:
            raise ValueError("Immunizations section not found in the XML file.")

        immunizations_dict = xml_to_dict(immunizations_section)
        return json.dumps(immunizations_dict)
    except Exception as e:
        print(f"Error parsing immunizations: {e}")
        return None

# Example usage
if __name__ == "__main__":
    xml_file = './CCD-Files/Ambulatory-Summary-CCD-Sample.xml'
    print(parse_immunizations(xml_file))
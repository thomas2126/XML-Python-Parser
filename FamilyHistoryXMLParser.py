import xml.etree.ElementTree as ET
import json

namespaces = {'hl7': 'urn:hl7-org:v3', 'sdtc': 'urn:hl7-org:sdtc'}

def xml_to_dict(element):
    if len(element) == 0:
        return element.text
    return {child.tag.split('}')[-1]: xml_to_dict(child) for child in element}

def parse_family_history(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    try:
        family_history_section = None
        for section in root.findall('.//hl7:section', namespaces):
            template_id = section.find('hl7:templateId', namespaces)
            #print(f"Checking section with templateId: {template_id.get('root') if template_id is not None else 'None'}")  # Log the templateId
            if template_id is not None and template_id.get('root') == '2.16.840.1.113883.10.20.22.2.15':
                family_history_section = section
                break

        if family_history_section is None:
            raise ValueError("Family History section not found in the XML file.")

        family_history_dict = xml_to_dict(family_history_section)
        return json.dumps(family_history_dict)
    except Exception as e:
        print(f"Error parsing family history: {e}")
        return None

# Example usage
if __name__ == "__main__":
    xml_file = './CCD-Files/Ambulatory-Summary-CCD-Sample.xml'
    print(parse_family_history(xml_file))

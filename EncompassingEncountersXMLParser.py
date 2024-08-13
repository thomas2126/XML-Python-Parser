import json
import xml.etree.ElementTree as ET

# Register the namespace to handle XML namespaces
namespaces = {'hl7': 'urn:hl7-org:v3', 'sdtc': 'urn:hl7-org:sdtc'}

def xml_to_dict(element):
    if len(element) == 0:
        return element.text
    return {child.tag.split('}')[-1]: xml_to_dict(child) for child in element}

def parse_encompassing_encounters(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    encompassing_encounters_dict = [xml_to_dict(encounter) for encounter in root.findall('hl7:component/hl7:structuredBody/hl7:component/hl7:section/hl7:entry/hl7:encounter', namespaces)]
    encompassing_encounters_json = json.dumps(encompassing_encounters_dict)
    return encompassing_encounters_json

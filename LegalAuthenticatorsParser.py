import json
import xml.etree.ElementTree as ET

# Register the namespace to handle XML namespaces
namespaces = {'hl7': 'urn:hl7-org:v3', 'sdtc': 'urn:hl7-org:sdtc'}

def xml_to_dict(element):
    if len(element) == 0:
        return element.text
    return {child.tag.split('}')[-1]: xml_to_dict(child) for child in element}

def parse_legal_authenticators(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    legal_authenticators_dict = [xml_to_dict(authenticator) for authenticator in root.findall('hl7:legalAuthenticator', namespaces)]
    legal_authenticators_json = json.dumps(legal_authenticators_dict)
    return legal_authenticators_json

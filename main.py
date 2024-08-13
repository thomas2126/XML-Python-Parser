import psycopg2
from ClinicalDocumentXMLParser import parse_clinical_document
from RecordTargetXMLParser import parse_record_target
from AuthorsXMLParser import parse_authors
from CustodiansXMLParser import parse_custodians
from InformationRecipientsXMLParser import parse_information_recipients
from LegalAuthenticatorsParser import parse_legal_authenticators
from ParticipantsXMLParser import parse_participants
from EncompassingEncountersXMLParser import parse_encompassing_encounters
from AllergiesXMLParser import parse_allergies
from EncountersXMLParser import parse_encounters
from FamilyHistoryXMLParser import parse_family_history
from ImmunizationsXMLParser import parse_immunizations
from MedicationsXMLParser import parse_medications

# Load the XML file
xml_file = './CCD-Files/Ambulatory-Summary-CCD-Sample.xml'

# Parse the sections
clinical_document_json = parse_clinical_document(xml_file)
record_target_json = parse_record_target(xml_file)
authors_json = parse_authors(xml_file)
custodians_json = parse_custodians(xml_file)
information_recipients_json = parse_information_recipients(xml_file)
legal_authenticators_json = parse_legal_authenticators(xml_file)
participants_json = parse_participants(xml_file)
encompassing_encounters_json = parse_encompassing_encounters(xml_file)
allergies_json = parse_allergies(xml_file)
encounters_json = parse_encounters(xml_file)
family_history_json = parse_family_history(xml_file)
immunizations_json = parse_immunizations(xml_file)
medications_json = parse_medications(xml_file)

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="",
    user="",
    password="",
    host="",
    port=""
)
cur = conn.cursor()

# Insert the JSON data into the Postgres table
cur.execute('''
    INSERT INTO public."table-name" (
        "DocumentType",
        "ClinicalDocument",
        "RecordTarget",
        "Authors",
        "Custodians",
        "InformationRecipients",
        "LegalAuthenticators",
        "Participants",
        "EncompassingEncounters",
        "Allergies",
        "Encounters",
        "FamilyHistory",
        "Immunizations",
        "Medications"
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
''', [
    'Ambulatory Summary',
    clinical_document_json,
    record_target_json,
    authors_json,
    custodians_json,
    information_recipients_json,
    legal_authenticators_json,
    participants_json,
    encompassing_encounters_json,
    allergies_json,
    encounters_json,
    family_history_json,
    immunizations_json,
    medications_json
])

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Data inserted successfully")

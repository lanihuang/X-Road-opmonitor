import logging
import os
from logging.handlers import RotatingFileHandler

# --------------------------------------------------------
# Configure General settings
# --------------------------------------------------------
APPDIR = "/srv/app"
# X-Road instances in Estonia: ee-dev, ee-test, EE
INSTANCE = "sample"

# --------------------------------------------------------
# Configure Mongo Database
# --------------------------------------------------------
MONGODB_USER = "reports_{0}".format(INSTANCE)
MONGODB_PWD = ""
MONGODB_SERVER = "opmon"
MONGODB_SUFFIX = "{0}".format(INSTANCE)
# For pointer
REPORT_USERNAME = "reports_{0}".format(INSTANCE)

# --------------------------------------------------------
# Configure general report settings
# --------------------------------------------------------
# Reports output directory
REPORTS_PATH = "{0}/{1}/reports/".format(APPDIR, INSTANCE)
REPORT_DATES_PATH = "reports_module/external_files/get_dates_reports.sh"
SUBSYSTEM_INFO_PATH = "reports_module/external_files/riha.json"

# --------------------------------------------------------
# Report constants
# --------------------------------------------------------
# The column order for produced services
PRODUCED_SERVICES_COLUMN_ORDER = ["SERVICE", "CLIENT", "SUCCEEDED_QUERIES", "FAILED_QUERIES",
                                  "DURATION_MIN_MEAN_MAX_MS", "REQUEST_SIZE_MIN_MEAN_MAX_B",
                                  "RESPONSE_SIZE_MIN_MEAN_MAX_B"]
# The column order for consumed services
CONSUMED_SERVICES_COLUMN_ORDER = ["PRODUCER", "SERVICE", "SUCCEEDED_QUERIES", "FAILED_QUERIES",
                                  "DURATION_MIN_MEAN_MAX_MS", "REQUEST_SIZE_MIN_MEAN_MAX_B",
                                  "RESPONSE_SIZE_MIN_MEAN_MAX_B"]
# Sort the report rows by the following columns
PRODUCED_SERVICES_SORTING_ORDER = ["SERVICE", "CLIENT"]
CONSUMED_SERVICES_SORTING_ORDER = ["PRODUCER", "SERVICE"]
# Group the report rows by the following columns
PRODUCED_SERVICES_GROUPING_ORDER = ["SERVICE", "CLIENT"]
CONSUMED_SERVICES_GROUPING_ORDER = ["PRODUCER", "SERVICE"]
# The list of services that are considered as meta services
META_SERVICE_LIST = ["getWsdl", "listMethods", "allowedMethods", "getSecurityServerMetrics",
                     "getSecurityServerOperationalData", "getSecurityServerHealthData"]
# The following producer fields are merged
PRODUCER_MERGED_FIELDS_1 = (["serviceCode", "serviceVersion"], ".", "service")
PRODUCER_MERGED_FIELDS_2 = (
    ["clientXRoadInstance", "clientMemberClass", "clientMemberCode", "clientSubsystemCode"], "/", "client")
# The following consumer fields are merged
CONSUMER_MERGED_FIELDS_1 = (["serviceCode", "serviceVersion"], ".", "service")
CONSUMER_MERGED_FIELDS_2 = (
    ["serviceXRoadInstance", "serviceMemberClass", "serviceMemberCode", "serviceSubsystemCode"], "/", "producer")
HTML_TEMPLATE_PATH = "/reports_module/pdf_files/pdf_report_template.html"
CSS_FILES = ["reports_module/pdf_files/pdf_report_style.css"]
# Load RIA images
RIA_IMAGE_1 = "reports_module/pdf_files/header_images/ria_75_{LANGUAGE}.png"
RIA_IMAGE_2 = "reports_module/pdf_files/header_images/eu_rdf_75_{LANGUAGE}.png"
RIA_IMAGE_3 = "reports_module/pdf_files/header_images/xroad_75_{LANGUAGE}.png"
# Translations
TRANSLATION_FILES = 'reports_module/lang/{LANGUAGE}_lang.json'

# --------------------------------------------------------
# Configure logger
# --------------------------------------------------------
LOGGER_NAME = 'reports_module'
LOGGER_PATH = '{0}/{1}/logs/'.format(APPDIR, INSTANCE)
logger = logging.getLogger(LOGGER_NAME)
LOGGER__MAX_SIZE = 2 * 1024 * 1024
LOGGER_BACKUP_COUNT = 10

# INFO - logs INFO & WARNING & ERROR
# WARNING - logs WARNING & ERROR
# ERROR - logs ERROR
logger.setLevel(logging.INFO)
log_file_name = '{0}_{1}.json'.format(LOGGER_NAME, INSTANCE)
formatter = logging.Formatter("%(message)s")

rotate_handler = RotatingFileHandler(os.path.join(LOGGER_PATH, log_file_name), maxBytes=LOGGER__MAX_SIZE,
                                     backupCount=LOGGER_BACKUP_COUNT)
rotate_handler.setFormatter(formatter)
logger.addHandler(rotate_handler)

# --------------------------------------------------------
# Configure heartbeats
# --------------------------------------------------------
HEARTBEAT_LOGGER_PATH = '{0}/{1}/heartbeat/'.format(APPDIR, INSTANCE)
REPORT_HEARTBEAT_NAME = 'heartbeat_report_{0}.json'.format(INSTANCE)
FACTSHEET_HEARTBEAT_NAME = 'heartbeat_factsheet_{0}.json'.format(INSTANCE)
INTERANNUAL_HEARTBEAT_NAME = 'heartbeat_interannual_factsheet_{0}.json'.format(INSTANCE)

# --------------------------------------------------------
# Configure FactSheet
# --------------------------------------------------------
factsheet_username = "factsheet_{0}".format(INSTANCE)
# The number of top producers to have in the output file.
number_of_top_producers = 5
# The number of top consumers to have in the output file.
number_of_top_consumers = 5
# These member_code's will be excluded from the top_producers and top_consumers.
excluded_client_member_code = ["code_1", "code_2"]
# The path where the FactSheets will be generated.
FACTSHEET_PATH = "{0}/{1}/factsheets/".format(APPDIR, INSTANCE)
# The path where the dates will be taken for the FactSheet.
FACTSHEET_DATES_PATH = "reports_module/external_files/get_dates_factsheet.sh"

# --------------------------------------------------------
# Configure notifications
# --------------------------------------------------------
SENDER_EMAIL = "yourname@yourdomain"
SMTP_HOST = 'smtp.yourdomain'
SMTP_PORT = 25
EMAIL_SUBJECT = '{X_ROAD_INSTANCE}/{MEMBER_CLASS}/{MEMBER_CODE}/{SUBSYSTEM_CODE} kasutusraport {START_DATE} - {END_DATE}'
EMAIL_BODY = """
Lugupeetud {EMAIL_NAME}

Saate selle kirja kuna olete RIHAs alamsüsteemi {MEMBER_CODE}/{SUBSYSTEM_CODE} kontaktisik.

Teile on koostatud selle alamsüsteemi X-tee keskkonna {X_ROAD_INSTANCE} kasutusraport perioodi {START_DATE} - {END_DATE} kohta.

Raporti võite leida aadressilt: https://www.ria.ee/x-tee/reports/{X_ROAD_INSTANCE}/{MEMBER_CLASS}/{MEMBER_CODE}/{REPORT_NAME}

Raport on koostatud RIA-le kättesaadavate X-tee v6 kasutusstatistika / monitooringu andmete põhjal.
Raportite abitekst - https://github.com/ria-ee/X-Road-opmonitor/blob/master/docs/user_guide/ug_reports_et.md

Lugupidamisega
Riigi Infosüsteemi Amet
"""

# --------------------------------------------------------
# Configure inter-annual statistics
# --------------------------------------------------------
# "last_incident"
# LAST_INCIDENT = "2001-12-17T18:25:43.511Z"
# LAST_INCIDENT = "2017-09-12T22:44:00.000Z"
LAST_INCIDENT = "2017-11-23T23:44:00.000Z"
# "affected_parties"
AFFECTED_PARTIES = 52000
# "effective_query_proportion"
EFFECTIVE_QUERY_PROPORTION = 0.05
# "effective_query_minutes"
EFFECTIVE_QUERY_MINUTES = 15
# "protocol_changes"
PROTOCOL_CHANGES = 4
# Base file location
BASE_FILE_LOCATION = "{0}/{1}/interannual_factsheet/".format(APPDIR, INSTANCE)
# Base file name
BASE_FILE_NAME = "data_v6.json"
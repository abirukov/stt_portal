HEADERS = [
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
]

TEXT_FORMAT = [
    "bold",
    "italic",
    "link",
]

ADDITIONAL_TEXT_FORMAT = [
    "code",
    "blockquote",
]

DOCUMENT_LINK = ["document-link"]
IMAGE = ["image"]
EMBED = ["embed"]

ALL_WITHOUT_FILES = HEADERS + TEXT_FORMAT + ADDITIONAL_TEXT_FORMAT + DOCUMENT_LINK
ALL = HEADERS + TEXT_FORMAT + ADDITIONAL_TEXT_FORMAT + DOCUMENT_LINK + IMAGE + EMBED

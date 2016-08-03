from distutils.core import setup
import py2exe

#setup(console=['Rtf2Txt.py'])
options = {'py2exe': {
    'includes': ['Rtf2Html.py','RtfParser.py']}}

setup(
    windows = [
        {
            "script": "Rtf2Txt.py",
            "icon_resources": [(1, "rtf2txt.ico")]
        }
    ],
)

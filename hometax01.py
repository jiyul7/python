import sys
import requests 
import xml.etree.ElementTree as ElementTree
import win32clipboard
# python .\CRN.py 3051577349 8995800075 8996300123 8997600079 8997700057 1010540144 1010863774 1011127195 1011230533 1011268892 1011275340 1011652137 1012151049 1020361041 1021551153
# pyinstaller .\CRN.py --onefile --nowindowed
PostUrl = "https://teht.hometax.go.kr/wqAction.do?actionId=ATTABZAA001R08&screenId=UTEABAAA13&popupYn=false&realScreenId="
XmlRaw = "<map id=\"ATTABZAA001R08\"><pubcUserNo/><mobYn>N</mobYn><inqrTrgtClCd>1</inqrTrgtClCd><txprDscmNo>\{CRN\}</txprDscmNo><dongCode>15</dongCode><psbSearch>Y</psbSearch><map id=\"userReqInfoVO\"/></map>"


def call(crn):
    res = requests.post(PostUrl, data=XmlRaw.replace("\{CRN\}", crn), headers={'Content-Type': 'text/xml'})
    xml = ElementTree.fromstring(res.text).findtext("trtCntn")
    result = crn + "\t" + xml.replace("\n","").replace("\t", " ") + "\n"
    return result
def setClip(text):    
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, result)
    win32clipboard.CloseClipboard()

if (len(sys.argv) < 2):
    print("매개변수에 사업자등록번호를 입력하십시오")
    exit()

result = ""
for idx, value in enumerate(sys.argv):
    if(idx == 0): continue
    result += call(value)

result = result.strip()
print(result)
setClip(result)
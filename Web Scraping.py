from bs4 import BeautifulSoup
import requests
import lxml
import json


url="https://elbadrgroupeg.store/laptop"
htmlFile=requests.get(url).content
soup=BeautifulSoup(htmlFile,"lxml")
def getProductInfo(index):
    productInfo={
        "img":soup.css.select("[class~=product-layout]")[index].findAll("img")[0]["data-src"],
        "name":soup.css.select("[class~=name]")[index].find("a").string,
        "price":soup.css.select("[class~=price-normal]")[index].string,
        "Brand":soup.css.select("[class~=stat-1]")[index].find("a").string
    }
    return productInfo

length=len(soup.css.select("[class~=stats]"))
def createListOfData():
    allData=[]
    for productIndex in range(len(soup.css.select("[class~=stats]"))) :
        productInfo=getProductInfo(productIndex)
        allData.append(productInfo)
    return json.dumps(allData,indent=2)
fileName="computer Fake data.json"
def createTheFile(string,fileName):
    f = open("computer Fake data.json", "w")
    f.write(string)
    f.close()
# createTheFile(createListOfData())

def readFileWithDicType(fileName):
    f = open(fileName, "r")
    whatIsType=json.load(f)
    return whatIsType
    f.close()
def editFile(fileName):
    f=open(fileName,"w")
    fileData=json.load(f)


# print(type(json.load(readFile())))


# print(getProductInfo(1))

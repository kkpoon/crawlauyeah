# -*- coding: utf-8 -*-
import scrapy

from datagovhk.items import FehdLicenseItem


def mapIdText(sel):
    KEY = sel.xpath("@ID").extract()[0]
    DESC = sel.xpath("text()").extract()[0]
    return (KEY, DESC)


def mapLicenseToItem(updatedAt, department, typeDict, distDict, infoDict):
    def f(sel):
        infoSel = sel.xpath("INFO/text()").extract()
        infoCode = infoSel[0] if 0 < len(infoSel) else None
        typeCode = sel.xpath("TYPE/text()").extract()[0]
        distCode = sel.xpath("DIST/text()").extract()[0]
        licno = sel.xpath("LICNO/text()").extract()[0]
        ss = sel.xpath("SS/text()").extract()[0]
        adr = sel.xpath("ADR/text()").extract()[0]
        expdate = sel.xpath("EXPDATE/text()").extract()[0]

        item = FehdLicenseItem()
        item["updatedAt"] = updatedAt
        item["department"] = department
        item["licenseType"] = typeDict.get(typeCode, None)
        item["district"] = distDict.get(distCode, None)
        item["licenseNo"] = licno
        item["owner"] = ss
        item["address"] = adr
        item["info"] = infoDict.get(infoCode, None)
        item["expireDate"] = expdate
        return item
    return f


class FehdLicensingSpider(scrapy.Spider):
    name = "fehd-licensing"
    allowed_domains = ["fehd.gov.hk"]
    def __init__(self, language="tc"):
        if language == "en":
            url = "http://www.fehd.gov.hk/english/licensing/license/text/LP_NonFood_EN.XML"
        else:
            url = "http://www.fehd.gov.hk/tc_chi/licensing/license/text/LP_NonFood_TC.XML"
        self.start_urls = (url,)

    def parse(self, response):
        typeDict = dict(map(mapIdText, response.xpath("//TYPE_CODE/CODE")))
        distDict = dict(map(mapIdText, response.xpath("//DIST_CODE/CODE")))
        infoDict = dict(map(mapIdText, response.xpath("//INFO_CODE/CODE")))

        updatedAt = response.xpath("//GENERATION_DATE/text()").extract()[0]
        department = response.xpath("//DEPARTMENT/text()").extract()[0]

        mapItem = mapLicenseToItem(
                updatedAt,
                department,
                typeDict,
                distDict,
                infoDict
                )

        for item in map(mapItem, response.xpath("//LPS/LP")):
            yield item

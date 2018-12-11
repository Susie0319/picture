# -*- coding: utf-8 -*-
import sys
import os
import re
import string
import xml.dom.minidom
import xlrd
import xlwt
from xlutils.copy import copy

xlrd.Book.encoding = "gbk"


def getfeatureOpeNameDict(operatorNameFilePath):
    operatorNameDict = {}
    dom = xml.dom.minidom.parse(operatorNameFilePath)
    root = dom.documentElement
    dict_list = dom.getElementsByTagName("dict")
    for node in dict_list:
        childNode_list = node.getElementsByTagName("string")
        mcc_mnc = ""
        operator_name = ""
        for childNode in childNode_list:
            if childNode.getAttribute("key") == "operator_key":
                mcc_mnc = str(childNode.firstChild.data)
            if childNode.getAttribute("key") == "operator_name":
                operator_name = str(childNode.firstChild.data)
        if mcc_mnc not in operatorNameDict:
            operatorNameDict[mcc_mnc]= operator_name
    return operatorNameDict

def getFeaturePlmnDict(featureOperatorName):
    plmnDict = {}
    for key in featureOperatorName:
        if featureOperatorName[key] != "":
            if featureOperatorName[key] not in plmnDict:
                plmnList = []
                plmnList.append(key)
                plmnDict[featureOperatorName[key]] = plmnList
            else:
                plmnDict[featureOperatorName[key]].append(key)
    # print plmnDict
    return plmnDict

def getIpTypeDict(ipTypeFilePath):
    ipTypeExcel = xlrd.open_workbook(ipTypeFilePath)
    ipTypeTable = ipTypeExcel.sheets()[0]
    ipTypeDict = {}
    for i in range(1, ipTypeTable.nrows):
        if(int(ipTypeTable.cell(i, 5).value) != 3):
            ipTypeDict[ipTypeTable.cell(i, 0).value] = int(ipTypeTable.cell(i, 5).value)
    # print ipTypeDict
    return ipTypeDict

def getProductOperatorNameList(productAreaCollectFilePath, featureOperatorName, versionsList):
    # print featureOperatorName
    productAreaCollectExcel = xlrd.open_workbook(productAreaCollectFilePath)
    opkeyTable = productAreaCollectExcel.sheets()[0]
    
    productOperatorNameList = []
    for i in range(1, opkeyTable.nrows):
        if opkeyTable.cell(i, 2).value == u'\u672a\u627e\u5230':
            print opkeyTable.cell(i, 0).value + "_" + opkeyTable.cell(i, 1).value + ":not found"
            continue
        opkeyList = opkeyTable.cell(i, 2).value.split(',')
        for e in opkeyList:
            # print e
            operatorName = featureOperatorName[e]
            # print operatorName
            if operatorName not in productOperatorNameList:
                productOperatorNameList.append(operatorName)
    # print productOperatorNameList
    return productOperatorNameList

def isIpTypeNeedChange(openkey, onlineTable):
    needChangeCell = []
    for row in range(1, onlineTable.nrows):
        if(str(onlineTable.cell(row, 0).value).split('.')[0] == openkey):
            # print openkey
            for col in range(1, 10):
                if(col == 8):
                    continue
                content = str(onlineTable.cell(row, col).value)
                # print content
                if "apn type:ims\nauthentication type:\nprotocol:IPV4/IPV6" in content:
                    # print row
                    needChangeCell.append(row)
                    needChangeCell.append(col)
                    break
            needChangeCell.append(-1)   
            break
    # print needChangeCell
    return needChangeCell


def writeInUpdateRecord(out_updateRecordFilePath, ipv4PlmnList, ipv6PlmnList, globalParameterFilePath):
    recordUpdateExcel = xlwt.Workbook(encoding = 'utf-8')
    recordUpdateSteet = recordUpdateExcel.add_sheet('record_update', cell_overwrite_ok=True)
    
    globalParametersExcel = xlrd.open_workbook(globalParameterFilePath)
    globalTable = globalParametersExcel.sheets()[1]
    onlineTable = globalParametersExcel.sheets()[2]

    # print ipv4PlmnList
    # print ipv6PlmnList

    write_raw = 1
    for k in range(1, globalTable.nrows):
        openkey = str(globalTable.cell(k, 10).value).split('.')[0]
        # 需要改成ipv4
        if openkey in ipv4PlmnList:
            # print k
            needChangeCell = isIpTypeNeedChange(openkey, onlineTable)   # 需要修改的列的编号，-1表示不需要修改
            # print needChangeCell
            if needChangeCell[0] == -1:
                continue
            recordUpdateSteet.write(write_raw, 0, label = '2018/12/7')
            recordUpdateSteet.write(write_raw, 1, label = '张兵兵')
            recordUpdateSteet.write(write_raw, 2, label = 'AR000B9TT5')
            for m in range(3, 14):
                recordUpdateSteet.write(write_raw, m, label = globalTable.cell(k, m-3).value)
            recordUpdateSteet.write(write_raw, 14, label = onlineTable.cell(0, needChangeCell[1]).value)
            oriContent = onlineTable.cell(needChangeCell[0], needChangeCell[1]).value
            newContent = oriContent.replace("apn type:ims\nauthentication type:\nprotocol:IPV4/IPV6\nroaming protocol:IPV4/IPV6", \
                                            "apn type:ims\nauthentication type:\nprotocol:IPV4\nroaming protocol:IPV4")
            recordUpdateSteet.write(write_raw, 15, label = oriContent)
            recordUpdateSteet.write(write_raw, 16, label = newContent)
            recordUpdateSteet.write(write_raw, 23, label = needChangeCell[1])
            write_raw = write_raw + 1
        # 需要改成ipv6
        elif openkey in ipv6PlmnList:
            needChangeCell = isIpTypeNeedChange(openkey, onlineTable)   # 需要修改的列的编号，-1表示不需要修改
            if needChangeCell[0] == -1:
                continue
            recordUpdateSteet.write(write_raw, 0, label = '2018/12/7')
            recordUpdateSteet.write(write_raw, 1, label = '张兵兵')
            recordUpdateSteet.write(write_raw, 2, label = 'AR000B9TT5')
            for m in range(3, 14):
                recordUpdateSteet.write(write_raw, m, label = globalTable.cell(k, m-3).value)
            recordUpdateSteet.write(write_raw, 14, label = onlineTable.cell(0, needChangeCell[1]).value)
            oriContent = onlineTable.cell(needChangeCell[0], needChangeCell[1]).value
            newContent = oriContent.replace("apn type:ims\nauthentication type:\nprotocol:IPV4/IPV6\nroaming protocol:IPV4/IPV6", \
                                            "apn type:ims\nauthentication type:\nprotocol:IPV6\nroaming protocol:IPV6")
            recordUpdateSteet.write(write_raw, 15, label = oriContent)
            recordUpdateSteet.write(write_raw, 16, label = newContent)
            recordUpdateSteet.write(write_raw, 23, label = needChangeCell[1])
            write_raw = write_raw + 1   
            
    recordUpdateExcel.save(out_updateRecordFilePath) 

def writeInOnlinePara(out_updateRecordFilePath, globalParameterFilePath, out_globalParameterFilePath):
    recordUpdateExcel = xlrd.open_workbook(out_updateRecordFilePath)
    recordUpdateTable = recordUpdateExcel.sheets()[0]
    globalParametersExcel = xlrd.open_workbook(globalParameterFilePath)
    onlineTable = globalParametersExcel.sheets()[2]
    onlineParaData = copy(globalParametersExcel)
    onlineParaSheet = onlineParaData.get_sheet(2)
    for i in range(1, recordUpdateTable.nrows):
        for n in range(1, onlineTable.nrows):
            if(str(onlineTable.cell(n, 0).value) == str(recordUpdateTable.cell(i, 13).value)):
                onlineParaSheet.write(n, int(recordUpdateTable.cell(i, 23).value), label = recordUpdateTable.cell(i, 16).value)

    onlineParaData.save(out_globalParameterFilePath)
    

if __name__ == "__main__":
    versionsList = ["开箱", "MR", "MR\'", "MR？"]
    # input file
    operatorNameFilePath = "input_file/simInfo_mapping.xml"
    productAreaCollectFilePath = "input_file/result.xls"
    globalParameterFilePath = "input_file/Global_parameters_EMUI9.xlsm"
    ipTypeFilePath = "input_file/ipType.xlsx"

    # output file
    out_updateRecordFilePath = "output_file/update_record.xls"
    out_globalParameterFilePath = "output_file/new_Global_parameters_EMUI9.xls"

    # 从simInfo_mapping中得到operatorname和plmn的对应
    featureOperatorName = getfeatureOpeNameDict(operatorNameFilePath)
    featurePlmnDict = getFeaturePlmnDict(featureOperatorName)

    # 从ip类型的表中得到需要修改为单v4或者单v6的operatorname
    ipTypeDict = getIpTypeDict(ipTypeFilePath)

    # 从产品范围收集表中得到需要修改ip类型的operatorname
    productOperatorNameList = getProductOperatorNameList(productAreaCollectFilePath, featureOperatorName, versionsList)

    ipv4PlmnList = []
    ipv6PlmnList = []
    for j in productOperatorNameList:
        if j in ipTypeDict:
            if ipTypeDict[j] == 1:
                ipv4PlmnList = ipv4PlmnList + featurePlmnDict[j]
            elif ipTypeDict[j] == 2:
                ipv6PlmnList = ipv6PlmnList + featurePlmnDict[j]

    writeInUpdateRecord(out_updateRecordFilePath, ipv4PlmnList, ipv6PlmnList, globalParameterFilePath)
    writeInOnlinePara(out_updateRecordFilePath, globalParameterFilePath, out_globalParameterFilePath)

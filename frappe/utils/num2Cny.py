from __future__ import unicode_literals

# IMPORTANT: only import safe functions as this module will be included in jinja environment
import frappe

import math

def num2Cny(num, lang):     
    capUnit = [frappe._("WAN"),frappe._("YI"),frappe._("WAN"),frappe._("YUAN"),'']     
    capDigit = { 2:[frappe._("JIAO"),frappe._("FEN"),''], 4:[frappe._("QIAN"),frappe._("BAI"),frappe._("SHI"),'']}     
    capNum=[frappe._("ling"),frappe._("yi"),frappe._("er"),frappe._("san"),frappe._("si"),frappe._("wu"),frappe._("liu"),frappe._("qi"),frappe._("ba"),frappe._("jiu")]     
    snum = str('%019.02f') % num     
    if snum.index('.')>16:     
        return ''    
    ret,nodeNum,subret,subChr='','','',''    
    CurChr=['','']     
    for i in range(5):     
        j=int(i*4+math.floor(i/4))     
        subret=''    
        nodeNum=snum[j:j+4]     
        lens=len(nodeNum)     
        for k in range(lens):     
            if int(nodeNum[k:])==0:     
                continue    
            CurChr[k%2] = capNum[int(nodeNum[k:k+1])]     
            if nodeNum[k:k+1] != '0':     
                CurChr[k%2] += capDigit[lens][k]     
            if  not ((CurChr[0]==CurChr[1]) and (CurChr[0]==capNum[0])):     
                if not((CurChr[k%2] == capNum[0]) and (subret=='') and (ret=='')):     
                    subret += CurChr[k%2]     
        subChr = [subret,subret+capUnit[i]][subret!='']     
        if not ((subChr == capNum[0]) and (ret=='')):     
            ret += subChr     
    return [ret,capNum[0]+capUnit[3]][ret=='']    
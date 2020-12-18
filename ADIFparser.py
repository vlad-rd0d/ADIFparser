#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        <ADIFparser>
# Purpose:     <>
#
# Author:      Vladimir Shchekunov RD0D
#
# Created:     08.12.2020
# Copyright:
# Licence:     GPL
#-------------------------------------------------------------------------------

adif = '<BAND:3>20M <CALL:6>DL1BCL <CONT:2>EU <CQZ:2>14 <DXCC:3>230 <FREQ:9>14.131000 <ITUZ:2>28 <MODE:3>SSB <OPERATOR:6>UR4LGA <PFX:3>DL1 <QSLMSG:19>TNX For QSO TU 73!. <QSO_DATE:8:D>20131011 <TIME_ON:6>184700 <RST_RCVD:2>57 <RST_SENT:2>57 <TIME_OFF:6>184700 <eQSL_QSL_RCVD:1>Y <APP_LOGGER32_QSO_NUMBER:1>1<EOR>'

def parseStringAdi(str_adif):
    tags = {}
    for word in str_adif.split('<'):
        if word == 'EOR>':
            break
        elif word != '':
            name = word.split(':')[0]
            tag = word.split('>')[1].strip()
            tags.update({name:tag})
    return tags


def main():
    tags = parseStringAdi(adif)
    print('Band: ' + tags.get('BAND') + '\nFreq: ' + tags.get('FREQ') + '\nCall: ' + tags.get('CALL') + '\nRS: ' + tags.get('RST_RCVD') + '\nMODE: ' + tags.get('MODE'))
    for key, val in tags.items():
        print("%s: %s" % (key, val))

if __name__ == '__main__':
    main()
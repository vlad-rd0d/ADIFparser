#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        <ADIFparser>
# Purpose:     <>
#
# Author:      Vladimir Shchekunov RD0D
#
# Created:     <>
# Copyright:
# Licence:     <>
#-------------------------------------------------------------------------------

adif = '<QSO_DATE:8>20171126<TIME_ON:4>0416<TIME_OFF:4>0416<CALL:6>JH1QDB<MODE:2>CW<FREQ:6>14.061<BAND:3>20M<RST_SENT:3>599<RST_RCVD:3>599<NAME:8>Kunihiko<QSL_SENT:1>N<QSL_RCVD:1>N<GRIDSQUARE:4>PM94<MY_GRIDSQUARE:6>PN68lt<TX_PWR:3>100<APP_CQRLOG_DXCC:2>JA<DXCC:3>339<ITUZ:2>45<CQZ:2>25<LOTW_QSL_SENT:1>Y<LOTW_QSLSDATE:8>20200702<LOTW_QSL_RCVD:1>Y<LOTW_QSLRDATE:8>20190116<EQS_QSL_SENT:1>Y<EQSL_QSLSDATE:8>20190116<EOR>'

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
    for key, value in tags.items():
        print("%s: %s" % (key, value))

if __name__ == '__main__':
    main()

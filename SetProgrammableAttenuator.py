#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 21:19:24 2020

@author: venkatesh
"""
import requests # to control the programmable attenuator

#def set_programamble_attenuator_function(atten_values, set_both_atten):
def set_programamble_attenuator_function(atten_R30_1, atten_R40_1):
#    if set_both_atten == 0:
#        atten_R30_1 = atten_values
#        # only R30 is to be set
#        string_setatten_R30_1 = 'http://192.168.30.1/setatt=' + str(atten_R30_1)
#        response_30_1 = requests.get(string_setatten_R30_1)
#        print("Status of atten setting for 192.168.30.1 programmable attenuator is: ", response_30_1.text)
#        string_getatten_R30_1 = 'http://192.168.30.1/att?'
#        response_30_1 = requests.get(string_getatten_R30_1, params={'':''})
#        print("Attenutation value read from 192.168.30.1 is: ",response_30_1.text)
#        
#    else:
#        # set both attenuators
#    atten_R30_1 = atten_values[0]
#    atten_R40_1 = atten_values[1]
    print("Attempting to set attenuations of ", atten_R30_1, ' and ', atten_R40_1, ' on 192.168.30.1 and 40.1 respectively.')
    string_setatten_R30_1 = 'http://192.168.30.1/setatt=' + str(atten_R30_1)
    string_setatten_R40_1 = 'http://192.168.40.1/setatt=' + str(atten_R40_1)
    response_30_1 = requests.get(string_setatten_R30_1)
    #print("Status of atten setting for 192.168.30.1 programmable attenuator is: ", response_30_1.text)
    response_40_1 = requests.get(string_setatten_R40_1)
    #print("Status of atten setting for 192.168.40.1 programmable attenuator is: ", response_40_1.text)
    string_getatten_R30_1 = 'http://192.168.30.1/att?'
    string_getatten_R40_1 = 'http://192.168.40.1/att?'
    response_30_1 = requests.get(string_getatten_R30_1, params={'':''})
    response_40_1 = requests.get(string_getatten_R40_1, params={'':''})
    print("Attenutation value read from 192.168.30.1 and 192.168.40.1 after setting is: ",response_30_1.text,response_40_1.text)
    
    #print("Attenutation value read from 192.168.40.1 after setting is: ",response_40_1.text)
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 18:47:46 2020

@author: camil
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class Mots :
    
    """Iterateur sur la liste de mot proposee par le site 10FastFinger"""
    
    def __init__(self, driver) :
        self.driver = driver
        self.num_span = 1
        
    def __iter__(self) :
        return self
    
    def __next__(self) :    
        try :
            element = self.driver.find_element_by_xpath( '//*[@id="row1"]/span[{}]'.format(self.num_span) )
            self.num_span += 1
            return element.text
        
        except NoSuchElementException :
            raise StopIteration
            


class TenFastFinger :
    
    """Bot jouant sur le site https://10fastfingers.com/typing-test/english#"""
    
    def __init__(self) :
        
        #Ouvre le site
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get('https://10fastfingers.com/typing-test/english#')
        
        #Champ ou l'on ecrit
        self.champ_ecriture = self.driver.find_element_by_xpath('//*[@id="inputfield"]')
                     
    def entrer_mot(self, mot) :
        """Entre le mot entre en parametre"""
        
        self.text = self.driver.find_element_by_xpath('//*[@id="inputfield"]') 
        self.text.send_keys( '{} '.format(mot) )
        
    def jouer(self) :
        """complete la liste de mots donnee par le site"""
        
        for mot in Mots(self.driver) :
            self.entrer_mot(mot)
        
        
if __name__ == '__main__' :
    script = TenFastFinger()
    time.sleep(3)
    script.jouer()
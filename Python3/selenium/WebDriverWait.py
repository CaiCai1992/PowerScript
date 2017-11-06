#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

base_url = "http://www.baidu.com"
driver = webdriver.Firefox()
driver.implicitly_wait(5)
'''��ʽ�ȴ�����ʾ�ȴ�������ʱ����ʱʱ��ȡ�����нϴ��'''
locator = (By.ID,'kw')
driver.get(base_url)

WebDriverWait(driver,10).until(EC.title_is(u"�ٶ�һ�£����֪��"))
'''�ж�title,���ز���ֵ'''

WebDriverWait(driver,10).until(EC.title_contains(u"�ٶ�һ��"))
'''�ж�title�����ز���ֵ'''

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'kw')))
'''�ж�ĳ��Ԫ���Ƿ񱻼ӵ���dom������������Ԫ��һ���ɼ��������λ���ͷ���WebElement'''

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'su')))
'''�ж�ĳ��Ԫ���Ƿ���ӵ���dom�ﲢ�ҿɼ����ɼ�����Ԫ�ؿ���ʾ�ҿ�͸߶�����0'''

WebDriverWait(driver,10).until(EC.visibility_of(driver.find_element(by=By.ID,value='kw')))
'''�ж�Ԫ���Ƿ�ɼ�������ɼ��ͷ������Ԫ��'''

WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.mnav')))
'''�ж��Ƿ�������1��Ԫ�ش�����dom���У������λ���ͷ����б�'''

WebDriverWait(driver,10).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR,'.mnav')))
'''�ж��Ƿ�������һ��Ԫ����ҳ���пɼ��������λ���ͷ����б�'''

WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@id='u1']/a[8]"),u'����'))
'''�ж�ָ����Ԫ�����Ƿ������Ԥ�ڵ��ַ��������ز���ֵ'''

WebDriverWait(driver,10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR,'#su'),u'�ٶ�һ��'))
'''�ж�ָ��Ԫ�ص�����ֵ���Ƿ������Ԥ�ڵ��ַ��������ز���ֵ'''

#WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it(locator))
'''�жϸ�frame�Ƿ����switch��ȥ��������ԵĻ�������True����switch��ȥ�����򷵻�False'''
#ע�����ﲢû��һ��frame�����л���ȥ

WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#swfEveryCookieWrap')))
'''�ж�ĳ��Ԫ�����Ƿ������dom�򲻿ɼ�,����ɼ�����False,���ɼ��������Ԫ��'''
#ע��#swfEveryCookieWrap�ڴ�ҳ������һ�����ص�Ԫ��

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='u1']/a[8]"))).click()
'''�ж�ĳ��Ԫ�����Ƿ�ɼ�������enable�ģ�����ɵ��'''
driver.find_element_by_xpath("//*[@id='wrapper']/div[6]/a[1]").click()
#WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='wrapper']/div[6]/a[1]"))).click()

#WebDriverWait(driver,10).until(EC.staleness_of(driver.find_element(By.ID,'su')))
'''�ȴ�ĳ��Ԫ�ش�dom�����Ƴ�'''
#����û���ҵ����ʵ�����

WebDriverWait(driver,10).until(EC.element_to_be_selected(driver.find_element(By.XPATH,"//*[@id='nr']/option[1]")))
'''�ж�ĳ��Ԫ���Ƿ�ѡ����,һ�����������б�'''

WebDriverWait(driver,10).until(EC.element_selection_state_to_be(driver.find_element(By.XPATH,"//*[@id='nr']/option[1]"),True))
'''�ж�ĳ��Ԫ�ص�ѡ��״̬�Ƿ����Ԥ��'''

WebDriverWait(driver,10).until(EC.element_located_selection_state_to_be((By.XPATH,"//*[@id='nr']/option[1]"),True))
'''�ж�ĳ��Ԫ�ص�ѡ��״̬�Ƿ����Ԥ��'''
driver.find_element_by_xpath(".//*[@id='gxszButton']/a[1]").click()

instance = WebDriverWait(driver,10).until(EC.alert_is_present())
'''�ж�ҳ�����Ƿ����alert,����о��л���alert������alert������'''
print instance.text
instance.accept()

driver.close()
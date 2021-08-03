#selenium library
import time
import re
import html
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
from selenium.common.exceptions import NoSuchElementException

from accounts.models import user_post
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os

onlineHate_model = 'accounts/model/onlineHate_model.sav'
racism_model = 'accounts/model/racism_model.sav'
sexism_model = 'accounts/model/sexism_model.sav'
insult_model = 'accounts/model/insult_model.sav'
obscene_model = 'accounts/model/obscene_model.sav'
toxic_model = 'accounts/model/toxic_model.sav'

onlineHate_data = 'accounts/model/onlineHate_corpus.csv'
racism_data = 'accounts/model/racism_corpus.csv'
sexism_data = 'accounts/model/sexism_corpus.csv'
toxic_data = 'accounts/model/train_corpus.csv'

onlineHate_corpus = pd.read_csv(onlineHate_data)
racism_corpus = pd.read_csv(racism_data)
sexism_corpus = pd.read_csv(sexism_data)
toxic_corpus = pd.read_csv(toxic_data)

origin_onlineHate_vect = TfidfVectorizer(max_features=5000)
origin_racism_vect = TfidfVectorizer(max_features=5000)
origin_sexism_vect = TfidfVectorizer(max_features=5000)
origin_toxic_vect = TfidfVectorizer(max_features=5000)

origin_onlineHate_vect.fit(onlineHate_corpus['text_final'])
origin_racism_vect.fit(racism_corpus['text_final'])
origin_sexism_vect.fit(sexism_corpus['text_final'])
origin_toxic_vect.fit(toxic_corpus['text_final'])
    
onlineHate_label = joblib.load(onlineHate_model)
racism_label = joblib.load(racism_model)
sexism_label = joblib.load(sexism_model)
insult_label = joblib.load(insult_model)
obscene_label = joblib.load(obscene_model)
toxic_label = joblib.load(toxic_model)

def extract_post_name(title,user_fb_name,driver):
    convert_list=[]
    post_list=[]
    final_stored_list = []
    search = ''
    data_1 =''
    data_2= ''
    new_data = True
    try:
        click_more_button = driver.find_elements_by_css_selector("div.j83agx80.buofh1pr.jklb3kyz.l9j0dhe7 > div.oajrlxb2.bp9cbjyn.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.pq6dq46d.mg4g778l.btwxx1t3.g5gj957u.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.p8fzw8mz.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.lzcic4wl.abiwlrkh.gpro0wi8.m9osqain.buofh1pr[role='button']")
        print("test_button",len(click_more_button))
        if click_more_button:
            for click_more in click_more_button:
                print("test_button",click_more.get_attribute("innerText"))
                driver.execute_script("arguments[0].click();", click_more)
    except NoSuchElementException:
        pass
    time.sleep(4)
    try:
        see_more_button = driver.find_elements_by_css_selector("div.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.oo9gr5id.gpro0wi8.lrazzd5p[role='button']")
        print("test_button",len(see_more_button))
        if see_more_button:
            for see_more in see_more_button:
                print("test_button",see_more.get_attribute("innerText"))
                driver.execute_script("arguments[0].click();", see_more)
    except NoSuchElementException:
        pass
    for i in range(len(title)):
        print("True or False",title[i].find_elements_by_css_selector("h2.gmql0nx0.l94mrbxd.p1ri9a11.lzcic4wl.aahdfvyu.hzawbc8m > div > div > span:nth-child(1) > div > a > span"))
        if not title[i].find_elements_by_css_selector("h2.gmql0nx0.l94mrbxd.p1ri9a11.lzcic4wl.aahdfvyu.hzawbc8m > div > div > span:nth-child(1) > span > a > span"):
            print("pass")
            name_2 = title[i].find_elements_by_css_selector("div.pybr56ya.dati1w0a.hv4rvrfc.n851cfcs.btwxx1t3.j83agx80.ll8tlv6m > div.buofh1pr > div > div > span > h2 > span > a > strong > span")
            print("True or False 4",name_2)
            if name_2:
                for name_2_1 in name_2:
                    print("pass_2")
                    print("name_2",name_2_1.text)
                    data_1=name_2_1.get_attribute("innerText")
                    print("name_2_name_2",data_1)
            #post = title[i].find_elements_by_css_selector("div.ecm0bbzt.hv4rvrfc.ihqw7lf3.dati1w0a > div > div > span > div")
            #convert_1 = title[i].find_elements_by_css_selector("div.ecm0bbzt.hv4rvrfc.ihqw7lf3.dati1w0a")
            convert_1 = title[i].find_elements_by_css_selector("div.qt6c0cv9.hv4rvrfc.dati1w0a.jb3vyjys")
            for convert_1_1 in convert_1:
                convert_list.append(convert_1_1.get_attribute('id'))
            for convert_word in convert_list:
                if convert_word:
                    search = re.findall('jsc_c_.*', convert_word)
                    print("test 2",search)
            final_search = ''.join(search)
            #print("test 3",final_search)
            post = title[i].find_elements_by_css_selector("div.qt6c0cv9.hv4rvrfc.dati1w0a.jb3vyjys[id='"+final_search+"'] > div")
            convert_list.clear()
            del final_search
            print("True or False 3",post)
            if not post: 
                post_3 = title[i].find_elements_by_css_selector("div.ecm0bbzt.hv4rvrfc.e5nlhep0.dati1w0a > div > div > span > div")
                if not post_3:
                    #scrape content with image and video
                    convert_2 = title[i].find_elements_by_css_selector("div.ecm0bbzt.hv4rvrfc.ihqw7lf3.dati1w0a > div > div > span")
                    for convert_2_1 in convert_2:
                        print("True or False 6",convert_2_1.get_attribute("innerText"))
                        post_list.append(convert_2_1.get_attribute("innerText"))
                    if len(post_list) > 0 :
                        print("testtest",post_list[0])
                        data_2 = post_list[0]
                    post_list.clear()
                else:
                    print("True or False 5",post_3)
                    for post_3_1 in post_3:
                        #print("content_3_content_3",post_3_1.get_attribute("innerHTML"))
                        print("content_3_content_3_content_3",post_3_1.get_attribute("innerText"))
                        print("content_3",post_3_1.text)
                        data_2 = post_3_1.get_attribute("innerText")
                        print("data_2 stored",data_2)
            else:  
                for post_1 in post:
                    #print(post_1.get_attribute("innerHTML"))
                    print("content",post_1.text) #the content still have mix other post content, should be fixed later # might use break instead of continue
                    #print("content_content",post_1.get_attribute("innerHTML"))
                    print("content_content_content",post_1.get_attribute("innerText"))
                    data_2 = post_1.get_attribute("innerText")
                    print("data_2 stored",data_2)
            onlineHate, racism, sexism, insult, obscene, toxic = aggression_label(data_2)
            for test_obj in final_stored_list:
                if test_obj["post_user"] == data_1 and test_obj["content"] == data_2:
                    print("exist data")
                    new_data = False
            if new_data:
                    final_stored_list.append({'post_user':data_1, 'content': data_2, 'onlineHate': onlineHate, 'racism': racism, 'sexism': sexism, 'insult': insult, 'obscene': obscene, 'toxic': toxic} )
            new_data = True            
            #if user_post.objects.filter(fb_username=user_fb_name).exists():
                #obj = user_post.objects.get(fb_username=user_fb_name)
                #onlineHate, racism, sexism, insult, obscene, toxic = aggression_label(data_2)
                #for obj_2 in obj.post:
                    #if obj_2["post_user"] == data_1 and obj_2["content"] == data_2:
                        #print("exist data")
                        #new_data = False
                        #break
                #if new_data:
                    #obj.post.insert(0, {'post_user':data_1, 'content': data_2, 'onlineHate': onlineHate, 'racism': racism, 'sexism': sexism, 'insult': insult, 'obscene': obscene, 'toxic': toxic} )
                    #obj.save()
                #new_data = True
                #jsc_c_qb > div > div > span:nth-child(1) > span > a > span
        else:
            name_1 = title[i].find_elements_by_css_selector("h2.gmql0nx0.l94mrbxd.p1ri9a11.lzcic4wl.aahdfvyu.hzawbc8m > div > div > span:nth-child(1) > span > a > span")
            for name_1_1 in name_1:
                print("name",name_1_1.text)
                data_1 = name_1_1.get_attribute("innerText")
                print("name_name",data_1)
            post_2 = title[i].find_elements_by_css_selector("div.ecm0bbzt.hv4rvrfc.e5nlhep0.dati1w0a > div > div > span > div.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.c1et5uql.ii04i59q")
            print("True or False 2",post_2)
            for post_2_1 in post_2:
                print("content_2",post_2_1.text)
                data_2 = post_2_1.get_attribute("innerText")
                print("content_2_content_2",data_2)
            onlineHate, racism, sexism, insult, obscene, toxic = aggression_label(data_2)
            for test_obj in final_stored_list:
                if test_obj["post_user"] == data_1 and test_obj["content"] == data_2:
                    print("exist data")
                    new_data = False
            if new_data:
                final_stored_list.append({'post_user':data_1, 'content': data_2, 'onlineHate': onlineHate, 'racism': racism, 'sexism': sexism, 'insult': insult, 'obscene': obscene, 'toxic': toxic} )
            new_data = True
            #if user_post.objects.filter(fb_username=user_fb_name).exists():
                #obj = user_post.objects.get(fb_username=user_fb_name)
                #onlineHate, racism, sexism, insult, obscene, toxic = aggression_label(data_2)
                #for obj_2 in obj.post:
                    #if obj_2["post_user"] == data_1 and obj_2["content"] == data_2:
                        #print("exist data")
                        #new_data = False
                #if new_data:
                    #obj.post.insert(0, {'post_user':data_1, 'content': data_2, 'onlineHate': onlineHate, 'racism': racism, 'sexism': sexism, 'insult': insult, 'obscene': obscene, 'toxic': toxic} )
                    #obj.save()
                #new_data = True
        print("count",i)
    if user_post.objects.filter(fb_username=user_fb_name).exists():
        obj = user_post.objects.get(fb_username=user_fb_name)
        obj.post = final_stored_list
        obj.save()


def extract_comment_name(title,user_fb_name):
    new_data = True
    final_comment_list = []
    data_1 = ''
    data_2 = ''
    for j in range(len(title)):
        comment_section = title[j].find_elements_by_css_selector("div._680y")
        if comment_section:
            for k in range(len(comment_section)): 
                comment_name = comment_section[k].find_elements_by_css_selector("span.nc684nl6 > a > span > span") #get comment person correctly
                if comment_name:
                    for comment_2 in comment_name:
                        print("Comment_Name:",comment_2.text)
                        data_1 = comment_2.get_attribute("innerText")
                        print("Comment_Name_Comment_Name",data_1)
                comment_body = comment_section[k].find_elements_by_css_selector("div.ecm0bbzt.e5nlhep0.a8c37x1j > span > div > div") #get comment correctly
                if comment_body:
                    for comment_1 in comment_body:
                        print("Comment_Body:",comment_1.text)
                        data_2 = comment_1.get_attribute("innerText")
                        print("Comment_Body_Comment_Body",data_2)
                onlineHate, racism, sexism, insult, obscene, toxic = aggression_label(data_2)
                for test_obj in final_comment_list:
                    if test_obj["comment_user"] == data_1 and test_obj["content"] == data_2:
                        print("exist data")
                        new_data = False
                if new_data:
                    final_comment_list.append( {'comment_user':data_1, 'content': data_2, 'onlineHate': onlineHate, 'racism': racism, 'sexism': sexism, 'insult': insult, 'obscene': obscene, 'toxic': toxic} )
                #if user_post.objects.filter(fb_username=user_fb_name).exists():
                    #obj = user_post.objects.get(fb_username=user_fb_name)
                    #onlineHate, racism, sexism, insult, obscene, toxic = aggression_label(data_2)
                    #for obj_2 in obj.comment:
                        #if obj_2["comment_user"] == data_1 and obj_2["content"] == data_2:
                            #print("exist data")
                            #new_data = False
                    #if new_data:
                        #obj.comment.insert(0, {'comment_user':data_1, 'content': data_2, 'onlineHate': onlineHate, 'racism': racism, 'sexism': sexism, 'insult': insult, 'obscene': obscene, 'toxic': toxic} )
                        #obj.save()
                    #new_data = True
            print("Comment_Count_1:",k)
        print("Comment_Count_2:",j)
    if user_post.objects.filter(fb_username=user_fb_name).exists():
        obj = user_post.objects.get(fb_username=user_fb_name)
        obj.comment = final_comment_list
        obj.save()

def aggression_label(content):
    onlineHate = "0"
    racism = "0"
    sexism = "0"
    insult = "0"
    obscene = "0"
    toxic = "0"
    
    review = content
    onlineHate_vector = origin_onlineHate_vect.transform([review]) # vectorizing
    racism_vector = origin_racism_vect.transform([review]) # vectorizing
    sexism_vector = origin_sexism_vect.transform([review]) # vectorizing
    toxic_vector = origin_toxic_vect.transform([review]) # vectorizing
    # labelling
    
    #print(onlineHate_label.predict(onlineHate_vector))
    #print(onlineHate_vector)
    if onlineHate_label.predict(onlineHate_vector) == 1:
        onlineHate = "1"
    
    #print(racism_vector)
    #print(racism_label.predict(racism_vector))
    if racism_label.predict(racism_vector) == 1:
        racism = "1"
    
    #print(sexism_vector)
    #print(sexism_label.predict(sexism_vector))
    if sexism_label.predict(sexism_vector) == 1:
        sexism = "1"

    #print(toxic_vector)
    #print(insult_label.predict(toxic_vector))
    if insult_label.predict(toxic_vector) == 1:
        insult = "1"
    
    #print(toxic_vector)
    #print(obscene_label.predict(toxic_vector))
    if obscene_label.predict(toxic_vector) == 1:
        obscene = "1"
    
    #print(toxic_vector)
    #print(toxic_label.predict(toxic_vector))
    if toxic_label.predict(toxic_vector) == 1:
        toxic = "1"

    return onlineHate, racism, sexism, insult, obscene, toxic


def scraper(user_fb_name, user_fb_email, user_fb_password, user_fb_link):
    usr = user_fb_email
    pwd = user_fb_password
    facebook_url = user_fb_link

    url = "https://facebook.com/" 
    chrome_options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_setting_values.notifications' : 2}
    chrome_options.add_experimental_option('prefs',prefs)
    #driver = webdriver.Chrome(executable_path='C:/User/user/Desktop/driver/chromedriver', chrome_options=chrome_options) 
    #chrome_options.add_argument("headless") #please do this only when ready
    driver = webdriver.Chrome(options=chrome_options) #need to put chromedriver in the user/AppData/Local/Program/Python/python39/scripts folder to make it work

    driver.get(url)

    time.sleep(3)
 
    elem = driver.find_element_by_id("email")
    elem.send_keys(usr)
 
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)
    #changing id , need to keep track of valid element
    elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
    elem.click()

    time.sleep(6)

    # To test if user insert email and password correctly
    try:
        elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/form/div[1]/a/div[1]/div/span/span")
        print("test_test_1",elem.get_attribute("innerText"))
        if elem.get_attribute("innerText") == "Log Masuk":
            driver.close()
            return False
    except:
        pass
    
    ori_name = user_fb_name
    split_name = ori_name.split()
    lower_name = [x.lower() for x in split_name]
    print("splited name",lower_name)

    # To test if link is directed correctly
    try:
        driver.get(facebook_url)
        print("current url",driver.current_url)
        for name_sub in lower_name:
            if 'facebook' not in driver.current_url or name_sub not in driver.current_url:
                driver.close()
                return False
    except:
        driver.close()
        return False

    time.sleep(6)

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
    # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(4)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    time.sleep(4)

    try:
        title = driver.find_elements_by_css_selector("div.du4w35lb.k4urcfbm.l9j0dhe7.sjgh65i0")
    except NoSuchElementException:
        driver.close()
        return False
    
    #extract_comment_name(title)
    extract_post_name(title,user_fb_name,driver)
    extract_comment_name(title,user_fb_name)

    print("sucess")

    driver.close()

    return True
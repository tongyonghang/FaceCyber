from django.shortcuts import render, redirect
from accounts.models import user_register , user_post
from django.contrib import messages
import json

def reverse_sort(e):
    return e['bully_score_count']

def score(login_username):
    onlineHate_score = 0
    racism_score = 0
    sexism_score = 0
    insult_score = 0
    obscene_score = 0
    toxic_score = 0
    normal_score = 0
    user_post_number = 0 #total post for user
    user_comment_number = 0 #total comment for user
    user_total_score = 0 #score for analyse user post and comment
    user_non_toxic_post = 0
    user_non_toxic_comment =0
    bully_score = 0
        # comment
    comment_onlineHate_score = 0
    comment_racism_score = 0
    comment_sexism_score = 0
    comment_insult_score = 0
    comment_obscene_score = 0
    comment_toxic_score = 0
    comment_normal_score = 0
    friend_total_score = 0 # score for analyse friend post and comment
    friend_non_toxic_post = 0
    friend_non_toxic_comment =0
        #ranking
    ranking = []
    ranking_score = 0
    friend_post_number = 0 #total post for friend
    friend_comment_number = 0 #total comment for friend
    friend_exist = False
    post_content = []
    comment_content=[]
    #
    user_post_onlineHate = 0
    user_post_racism = 0   
    user_post_sexism = 0
    user_post_insult = 0
    user_post_obscene = 0
    user_post_toxic = 0
    #normal post -> user_non_toxic_post
    user_comment_onlineHate = 0
    user_comment_racism = 0   
    user_comment_sexism = 0
    user_comment_insult = 0
    user_comment_obscene = 0
    user_comment_toxic = 0
    #normal comment -> user_non_toxic_comment
    #
    friend_post_onlineHate = 0
    friend_post_racism = 0   
    friend_post_sexism = 0
    friend_post_insult = 0
    friend_post_obscene = 0
    friend_post_toxic = 0
    #normal -> friend_non_toxic_post
    friend_comment_onlineHate = 0
    friend_comment_racism = 0   
    friend_comment_sexism = 0
    friend_comment_insult = 0
    friend_comment_obscene = 0
    friend_comment_toxic = 0
    each_friend_bully_score = 0
    each_friend_bully_score_count = 0
    friend_total_content = 1
    #normal -> friend_non_toxic_comment
    
    obj = user_register.objects.get(username=login_username)
    try:
        post_result = user_post.objects.get(fb_username=obj.facebook_name)
        #print("passing done")
        for label_score in post_result.post:
            #print(label_score["post_user"])
            if label_score["post_user"] == obj.facebook_name:
                if label_score["onlineHate"] == "1" :
                    onlineHate_score += 1
                    user_post_onlineHate +=1
                if label_score["racism"] == "1" :
                    racism_score += 1
                    user_post_racism +=1
                if label_score["sexism"] == "1" :
                    sexism_score += 1
                    user_post_sexism +=1
                if label_score["insult"] == "1" :
                    insult_score += 1
                    user_post_insult +=1
                if label_score["obscene"] == "1" :
                    obscene_score += 1
                    user_post_obscene +=1
                if label_score["toxic"] == "1" :
                    toxic_score += 1
                    user_post_toxic +=1
                if label_score["onlineHate"] == "0" and label_score["racism"] =="0" and label_score["sexism"] == "0" and label_score["insult"] == "0" and label_score["obscene"] =="0" and label_score["toxic"] == "0":
                    normal_score += 1
                    user_non_toxic_post += 1
                user_post_number += 1 
                #print(user_post_number)
            else:
                #print("no pass")
                if label_score["onlineHate"] == "1" :
                    comment_onlineHate_score += 1
                    friend_post_onlineHate +=1
                    ranking_score += 1
                if label_score["racism"] == "1" :
                    comment_racism_score += 1
                    friend_post_racism +=1
                    ranking_score += 1
                if label_score["sexism"] == "1" :
                    comment_sexism_score += 1
                    friend_post_sexism +=1
                    ranking_score += 1
                if label_score["insult"] == "1" :
                    comment_insult_score += 1
                    friend_post_insult +=1
                    ranking_score += 1
                if label_score["obscene"] == "1" :
                    comment_obscene_score += 1
                    friend_post_obscene += 1
                    ranking_score += 1
                if label_score["toxic"] == "1" :
                    comment_toxic_score += 1
                    friend_post_toxic += 1
                    ranking_score += 1
                if label_score["onlineHate"] == "0" and label_score["racism"] =="0" and label_score["sexism"] == "0" and label_score["insult"] == "0" and label_score["obscene"] =="0" and label_score["toxic"] == "0":
                    comment_normal_score += 1
                    friend_non_toxic_post += 1
                else:
                    each_friend_bully_score_count += 1
                friend_post_number += 1
                #print(friend_post_number)
                if len(ranking) == 0:
                    ranking.append({'friend':label_score["post_user"],'score':ranking_score,'bully_score_count':each_friend_bully_score_count,'bully_score':each_friend_bully_score,'total_content':friend_total_content})
                else:
                    for rank_user in ranking:
                        if rank_user["friend"] == label_score["post_user"]:
                            rank_user["score"] += ranking_score
                            rank_user["bully_score_count"] += each_friend_bully_score_count
                            rank_user["total_content"] += 1
                            friend_exist = True
                    if friend_exist == False:
                        # else new friend added
                        ranking.append({'friend':label_score["post_user"],'score':ranking_score,'bully_score_count':each_friend_bully_score_count,'bully_score':each_friend_bully_score,'total_content':friend_total_content})
                ranking_score = 0
                each_friend_bully_score_count = 0
                friend_exist= False
                #end loop

        for label_score in post_result.comment:
            if label_score["comment_user"] == obj.facebook_name:
                if label_score["onlineHate"] == "1" :
                    onlineHate_score += 1
                    user_comment_onlineHate +=1
                if label_score["racism"] == "1" :
                    racism_score += 1
                    user_comment_racism += 1
                if label_score["sexism"] == "1" :
                    sexism_score += 1
                    user_comment_sexism += 1
                if label_score["insult"] == "1" :
                    insult_score += 1
                    user_comment_insult +=1
                if label_score["obscene"] == "1" :
                    obscene_score += 1
                    user_comment_obscene +=1
                if label_score["toxic"] == "1" :
                    toxic_score += 1
                    user_comment_toxic +=1
                if label_score["onlineHate"] == "0" and label_score["racism"] =="0" and label_score["sexism"] == "0" and label_score["insult"] == "0" and label_score["obscene"] =="0" and label_score["toxic"] == "0":
                    normal_score += 1
                    user_non_toxic_comment += 1
                user_comment_number += 1 
            else:
                if label_score["onlineHate"] == "1" :
                    comment_onlineHate_score += 1
                    friend_comment_onlineHate +=1
                    ranking_score += 1
                if label_score["racism"] == "1" :
                    comment_racism_score += 1
                    friend_comment_racism +=1
                    ranking_score += 1
                if label_score["sexism"] == "1" :
                    comment_sexism_score += 1
                    friend_comment_sexism +=1
                    ranking_score += 1
                if label_score["insult"] == "1" :
                    comment_insult_score += 1
                    friend_comment_insult +=1
                    ranking_score += 1
                if label_score["obscene"] == "1" :
                    comment_obscene_score += 1
                    friend_comment_obscene +=1
                    ranking_score += 1
                if label_score["toxic"] == "1" :
                    comment_toxic_score += 1
                    friend_comment_toxic +=1
                    ranking_score += 1
                if label_score["onlineHate"] == "0" and label_score["racism"] =="0" and label_score["sexism"] == "0" and label_score["insult"] == "0" and label_score["obscene"] =="0" and label_score["toxic"] == "0":
                    comment_normal_score += 1
                    friend_non_toxic_comment +=1
                else:
                    each_friend_bully_score_count += 1
                friend_comment_number += 1
                if len(ranking) == 0:
                    ranking.append({'friend':label_score["comment_user"],'score':ranking_score,'bully_score_count':each_friend_bully_score_count,'bully_score':each_friend_bully_score,'total_content':friend_total_content})
                else:
                    for rank_user in ranking:
                        if rank_user["friend"] == label_score["comment_user"]:
                            rank_user["score"] += ranking_score
                            rank_user["bully_score_count"] += each_friend_bully_score_count
                            rank_user["total_content"] += 1
                            friend_exist = True
                    if friend_exist == False:
                        # else new friend added
                        ranking.append({'friend':label_score["comment_user"],'score':ranking_score,'bully_score_count':each_friend_bully_score_count,'bully_score':each_friend_bully_score,'total_content':friend_total_content})
                ranking_score = 0
                each_friend_bully_score_count = 0
                friend_exist= False
                #end loop
        
        ranking.sort(reverse=True,key=reverse_sort)
        # user percentage
        user_total_score = onlineHate_score + racism_score + sexism_score + insult_score + obscene_score + toxic_score + normal_score 
        onlineHate_percen = str(round(onlineHate_score/user_total_score*100,2))+"%"
        racism_percen = str(round(racism_score/user_total_score*100,2))+"%"
        sexism_percen = str(round(sexism_score/user_total_score*100,2))+"%"
        insult_percen = str(round(insult_score/user_total_score*100,2))+"%"
        obscene_percen = str(round(obscene_score/user_total_score*100,2))+"%"
        toxic_percen = str(round(toxic_score/user_total_score*100,2))+"%"
        normal_percen = str(round(normal_score/user_total_score*100,2))+"%"
        #post bar high
        onlineHate_score_percen = str(onlineHate_score)+"%"
        racism_score_percen = str(racism_score)+"%"
        sexism_score_percen = str(sexism_score)+"%"
        insult_score_percen = str(insult_score)+"%"
        obscene_score_percen = str(obscene_score)+"%"
        toxic_score_percen = str(toxic_score)+"%"
        normal_score_percen = str(normal_score)+"%"
        #friend percentage
        friend_total_score = comment_onlineHate_score + comment_racism_score + comment_sexism_score + comment_insult_score + comment_obscene_score + comment_toxic_score + comment_normal_score
        comment_onlineHate_percen = str(round(comment_onlineHate_score/friend_total_score*100,2))+"%"
        comment_racism_percen = str(round(comment_racism_score/friend_total_score*100,2))+"%"
        comment_sexism_percen = str(round(comment_sexism_score/friend_total_score*100,2))+"%"
        comment_insult_percen = str(round(comment_insult_score/friend_total_score*100,2))+"%"
        comment_obscene_percen = str(round(comment_obscene_score/friend_total_score*100,2))+"%"
        comment_toxic_percen = str(round(comment_toxic_score/friend_total_score*100,2))+"%"
        comment_normal_percen = str(round(comment_normal_score/friend_total_score*100,2))+"%"
        #friend bar high
        comment_onlineHate_score_percen = str(comment_onlineHate_score)+"%"
        comment_racism_score_percen = str(comment_racism_score)+"%"
        comment_sexism_score_percen = str(comment_sexism_score)+"%"
        comment_insult_score_percen = str(comment_insult_score)+"%"
        comment_obscene_score_percen = str(comment_obscene_score)+"%"
        comment_toxic_score_percen = str(comment_toxic_score)+"%"
        comment_normal_score_percen = str(comment_normal_score)+"%"
        #user
        bully_score = user_total_score - normal_score #bully score with post with comment
        total_user_toxic = user_comment_number + user_post_number - normal_score
        total_user_post_comment = user_comment_number + user_post_number
        total_user_toxic_post = user_post_number - user_non_toxic_post
        total_user_toxic_comment = user_comment_number - user_non_toxic_comment
        real_bully_score = round(total_user_toxic/total_user_post_comment*100,1)
        real_bully_score_percen = str(real_bully_score)+"%"
        #friend
        friend_bully_score = friend_total_score - comment_normal_score
        friend_bully_score_1 = int(friend_bully_score*0.8)
        friend_bully_score_2 = int(friend_bully_score*0.6)
        friend_bully_score_3 = int(friend_bully_score*0.4)
        friend_bully_score_4 = int(friend_bully_score*0.2)
        total_friend_toxic = friend_comment_number + friend_post_number - comment_normal_score
        total_friend_post_comment = friend_comment_number + friend_post_number
        total_friend_toxic_post = friend_post_number - friend_non_toxic_post
        total_friend_toxic_comment = friend_comment_number - friend_non_toxic_comment
        #
        scale_range = int(bully_score/user_total_score*100)
        scale_range_percen = str(scale_range)+"%"
        post_result.user_score = bully_score
        post_bar_score = user_total_score/5
        friend_bar_score = friend_total_score/5
        for rank_user in ranking:
            rank_user["bully_score"] = round(rank_user["bully_score_count"]/rank_user["total_content"]*100,1)
        print("ranking",ranking)
        post_content = post_result.post
        comment_content = post_result.comment
        user_fb_name = post_result.fb_username
        post_result.friend_score = ranking
        post_result.save()
        context = {
            'username': obj.username,
            'password': obj.password,
            'facebook_name': obj.facebook_name,
            'facebook_email': obj.facebook_email,
            'facebook_password': obj.facebook_password,
            'facebook_link': obj.facebook_link,
            #post score
            'onlineHate_score': onlineHate_score,
            'racism_score': racism_score,
            'sexism_score': sexism_score,
            'insult_score': insult_score,
            'obscene_score': obscene_score,
            'toxic_score': toxic_score,
            'normal_score': normal_score,
            'onlineHate_percen': onlineHate_percen,
            'racism_percen': racism_percen,
            'sexism_percen': sexism_percen,
            'insult_percen': insult_percen,
            'obscene_percen': obscene_percen,
            'toxic_percen': toxic_percen,
            'normal_percen': normal_percen,
            #comment score
            'comment_onlineHate_score': comment_onlineHate_score,
            'comment_racism_score': comment_racism_score,
            'comment_sexism_score': comment_sexism_score,
            'comment_insult_score': comment_insult_score,
            'comment_obscene_score': comment_obscene_score,
            'comment_toxic_score': comment_toxic_score,
            'comment_normal_score': comment_normal_score,
            'comment_onlineHate_percen': comment_onlineHate_percen,
            'comment_racism_percen': comment_racism_percen,
            'comment_sexism_percen': comment_sexism_percen,
            'comment_insult_percen': comment_insult_percen,
            'comment_obscene_percen': comment_obscene_percen,
            'comment_toxic_percen': comment_toxic_percen,
            'comment_normal_percen': comment_normal_percen,
            #post and comment number
            'user_post_number': user_post_number,
            'user_comment_number': user_comment_number,
            'friend_post_number': friend_post_number,
            'friend_comment_number': friend_comment_number,
            'total_user_toxic':total_user_toxic,
            'total_user_toxic_post':total_user_toxic_post,
            'total_user_toxic_comment':total_user_toxic_comment,
            'total_user_post_comment':total_user_post_comment,
            'total_friend_toxic':total_friend_toxic,
            'total_friend_post_comment':total_friend_post_comment,
            'total_friend_toxic_post':total_friend_toxic_post,
            'total_friend_toxic_comment':total_friend_toxic_comment,
            'friend_bully_score':friend_bully_score,
            'friend_bully_score_1':friend_bully_score_1,
            'friend_bully_score_2':friend_bully_score_2,
            'friend_bully_score_3':friend_bully_score_3,
            'friend_bully_score_4':friend_bully_score_4,
            #bar data
            'user_post_onlineHate':user_post_onlineHate,
            'user_post_racism':user_post_racism,
            'user_post_sexism':user_post_sexism,
            'user_post_insult':user_post_insult,
            'user_post_obscene':user_post_obscene,
            'user_post_toxic':user_post_toxic,
            'user_non_toxic_post':user_non_toxic_post,
            'user_comment_onlineHate':user_comment_onlineHate,
            'user_comment_racism':user_comment_racism,
            'user_comment_sexism':user_comment_sexism,
            'user_comment_insult':user_comment_insult,
            'user_comment_obscene':user_comment_obscene,
            'user_comment_toxic':user_comment_toxic,
            'user_non_toxic_comment':user_non_toxic_comment,
            'friend_post_onlineHate':friend_post_onlineHate,
            'friend_post_racism':friend_post_racism,
            'friend_post_sexism':friend_post_sexism,
            'friend_post_insult':friend_post_insult,
            'friend_post_obscene':friend_post_obscene,
            'friend_post_toxic':friend_post_toxic,
            'friend_non_toxic_post':friend_non_toxic_post,
            'friend_comment_onlineHate':friend_comment_onlineHate,
            'friend_comment_racism':friend_comment_racism,
            'friend_comment_sexism':friend_comment_sexism,
            'friend_comment_insult':friend_comment_insult,
            'friend_comment_obscene':friend_comment_obscene,
            'friend_comment_toxic':friend_comment_toxic,
            'friend_non_toxic_comment':friend_non_toxic_comment,
            #score
            'bully_score':bully_score,
            'ranking':ranking,
            'post_content':post_content,
            'comment_content':comment_content,
            'user_fb_name':user_fb_name,
            'post_bar_score':post_bar_score,
            'friend_bar_score':friend_bar_score,
            'scale_range':scale_range,
            'scale_range_percen':scale_range_percen,
            'user_total_score':user_total_score,
            'real_bully_score':real_bully_score,
            'real_bully_score_percen':real_bully_score_percen,
            #bar high
            'onlineHate_score_percen':onlineHate_score_percen,
            'racism_score_percen':racism_score_percen,
            'sexism_score_percen':sexism_score_percen,
            'insult_score_percen':insult_score_percen,
            'obscene_score_percen':obscene_score_percen,
            'toxic_score_percen':toxic_score_percen,
            'normal_score_percen':normal_score_percen,
            'comment_onlineHate_score_percen':comment_onlineHate_score_percen,
            'comment_racism_score_percen':comment_racism_score_percen,
            'comment_sexism_score_percen':comment_sexism_score_percen,
            'comment_insult_score_percen':comment_insult_score_percen,
            'comment_obscene_score_percen':comment_obscene_score_percen,
            'comment_toxic_score_percen':comment_toxic_score_percen,
            'comment_normal_score_percen':comment_normal_score_percen
        }

        return context
    except Exception as e:
        print(e)
        fail_fb = obj.facebook_name
        fail_email = obj.facebook_email
        fail_password = obj.facebook_password
        fail_link = obj.facebook_link
        user_total_score = onlineHate_score + racism_score + sexism_score + insult_score + obscene_score + toxic_score + normal_score 
        onlineHate_percen = str(0.00)+"%"
        racism_percen = str(0.00)+"%"
        sexism_percen = str(0.00)+"%"
        insult_percen = str(0.00)+"%"
        obscene_percen = str(0.00)+"%"
        toxic_percen = str(0.00)+"%"
        normal_percen = str(0.00)+"%"
        #friend percentage
        friend_total_score = comment_onlineHate_score + comment_racism_score + comment_sexism_score + comment_insult_score + comment_obscene_score + comment_toxic_score + comment_normal_score
        comment_onlineHate_percen = str(0.00)+"%"
        comment_racism_percen = str(0.00)+"%"
        comment_sexism_percen = str(0.00)+"%"
        comment_insult_percen = str(0.00)+"%"
        comment_obscene_percen = str(0.00)+"%"
        comment_toxic_percen = str(0.00)+"%"
        comment_normal_percen = str(0.00)+"%"
        post_bar_score = 0
        friend_bar_score = 0
        real_bully_score = 0
        real_bully_score_percen = str(0)+"%"
        context = {
            'username': obj.username,
            'password': obj.password,
            'facebook_name': fail_fb,
            'facebook_email': fail_email,
            'facebook_password': fail_password,
            'facebook_link': fail_link,
            #post score
            'onlineHate_score': onlineHate_score,
            'racism_score': racism_score,
            'sexism_score': sexism_score,
            'insult_score': insult_score,
            'obscene_score': obscene_score,
            'toxic_score': toxic_score,
            'normal_score': normal_score,
            'onlineHate_percen': onlineHate_percen,
            'racism_percen': racism_percen,
            'sexism_percen': sexism_percen,
            'insult_percen': insult_percen,
            'obscene_percen': obscene_percen,
            'toxic_percen': toxic_percen,
            'normal_percen': normal_percen,
            #comment score
            'comment_onlineHate_score': comment_onlineHate_score,
            'comment_racism_score': comment_racism_score,
            'comment_sexism_score': comment_sexism_score,
            'comment_insult_score': comment_insult_score,
            'comment_obscene_score': comment_obscene_score,
            'comment_toxic_score': comment_toxic_score,
            'comment_normal_score': comment_normal_score,
            'comment_onlineHate_percen': comment_onlineHate_percen,
            'comment_racism_percen': comment_racism_percen,
            'comment_sexism_percen': comment_sexism_percen,
            'comment_insult_percen': comment_insult_percen,
            'comment_obscene_percen': comment_obscene_percen,
            'comment_toxic_percen': comment_toxic_percen,
            'comment_normal_percen': comment_normal_percen,
            #post and comment number
            'user_post_number': user_post_number,
            'user_comment_number': user_comment_number,
            'friend_post_number': friend_post_number,
            'friend_comment_number': friend_comment_number,
            #score
            'bully_score':bully_score,
            'ranking':ranking,
            'post_content':post_content,
            'comment_content':comment_content,
            'user_fb_name':fail_fb,
            'post_bar_score':post_bar_score,
            'friend_bar_score':friend_bar_score,
            'real_bully_score':real_bully_score,
            'real_bully_score_percen':real_bully_score_percen
        }

        return context

from django.shortcuts import render, redirect
from mysqlconnection import connectToMySQL
from django.contrib import messages
from datetime import datetime

def postnewjob(request):
    if 'user_id' not in request.session:
        return redirect("/")
    else:
        return render(request, "postjob/addjobform.html")

def BTaddjob(request):
    mysql = connectToMySQL('bid_dash')
    query = 'INSERT INTO `bid_dash`.`jobs` (`users_id`,`category_id`,`title`,`description`,`max_price`,`start_datetime`,`end_datetime`,`addresses_id`) VALUES (%(iduser)s,%(idcate)s,%(title)s,%(description)s,%(max_price)s,%(start_datetime)s,%(end_datetime)s,%(addresses_id)s);'
    data = {
        'iduser': request.session['user_id'],
        'idcate' : request.POST['category'],
        'title' : request.POST['jobtitle'],
        'description' : request.POST['jobdescription'],
        'max_price' : request.POST['maxprice'],
        'start_datetime' : datetime.now(),
        'end_datetime' : request.POST['endtime'],
        'addresses_id': request.POST['location']
    }
    new_job_id = mysql.query_db(query, data)
    return redirect("/dashboard")

def addcategory(request):
    if 'user_id' not in request.session:
        return redirect("/")
    else:
        return render(request, "postjob/addcategoryform.html")

def BTaddcategory(request):
    mysql = connectToMySQL('bid_dash')
    query = 'INSERT INTO `bid_dash`.`categories` (`name`) VALUES (%(catename)s);'
    data = {
        'catename' : request.POST['categoryname']
    }
    new_category_id = mysql.query_db(query, data)
    return redirect("/dashboard")

def addlocation(request):
    if 'user_id' not in request.session:
        return redirect("/")
    else:
        return render(request, "postjob/addlocation.html")

def BTaddlocation(request):
    mysql = connectToMySQL('bid_dash')
    query = 'INSERT INTO `bid_dash`.`addresses` (`street_address`,`city`,`state`,`zip`) VALUES (%(street_address)s,%(city)s,%(state)s,%(zip)s);'
    data = {
        'street_address' : '123 abc st',
        'city' : request.POST['location'],
        'state' : 'IL',
        'zip' : '60630'
    }
    new_city_id = mysql.query_db(query, data)
    return redirect("/dashboard")
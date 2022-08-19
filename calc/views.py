from pickle import GET
from platform import node
from .models import data
from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import data
from django.contrib.auth.forms import UserCreationForm
import csv,io
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
"""
@Author= Karthik Aviansh
21BCS052
"""
#_______________________________________________________INITIALIZATIONS___________________________
#ELECTIVES ARE NOT HAVING LABS?
cse,dsai,ece,cse_th,dsai_th,ece_th,cse_tut,dsai_tut,ece_tut,cse_lab,dsai_lab,ece_lab=0,0,0,0,0,0,0,0,0,0,0,0
#________________________________INITIAL PLACE WHERE ALL NODES ARE SENT___________________________
class node_for_courses:
    def __init__(self,code,type,name,branch1,semester1,branch2,semester2,branch3,semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,tutorial,lab,lab_name=None):
            obj_for_class_rooms.insert(branch1+'_'+semester1,classroom_code1,semester1)
            if branch2!="NA":
                obj_for_class_rooms.insert(branch2+"_"+semester2,classroom_code2,semester2)
            if branch3!="NA":
                obj_for_class_rooms.insert(branch3+"_"+semester3,classroom_code3,semester3)
            if branch1[0]=='C' or branch1[0]=='c':
                global cse
                cse=1
                global cse_th
                global cse_tut
                global cse_lab
                if theory:cse_th=1
                if tutorial:cse_tut=1
                if lab:cse_lab=1
            if branch1[0]=='D' or branch1[0]=='d':
                global dsai
                dsai=1
                global dsai_th
                global dsai_tut
                global dsai_lab
                if theory:dsai_th=1
                if tutorial:dsai_tut=1
                if lab:dsai_lab=1
            if branch1[0]=='E' or branch1[0]=='e':
                global ece
                ece=1
                global ece_th
                global ece_tut
                global ece_lab
                if theory:ece_th=1
                if tutorial:ece_tut=1
                if lab:ece_lab=1
            global elective_courses
            if (type=='e' or type=='E' or type=="Elective" or type=="elective" or type=="ele" or type=="ELE"):obj_for_linked_list_for_electives.insert(code,type,name,branch1,semester1,branch2,semester2,branch3,semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,tutorial,lab,lab_name,30)
            else:
                if theory:obj_for_linked_list_for_traversing_theory.insert(code,type,name,branch1,semester1,branch2,semester2,branch3,semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,tutorial,lab,lab_name,30)
                if tutorial:obj_for_linked_list_for_traversing_tutorials.insert(code,type,name,branch1,semester1,branch2,semester2,branch3,semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,tutorial,lab,lab_name,30)
                if lab:obj_for_linked_list_for_traversing_labs.insert(code,type,name,branch1,semester1,branch2,semester2,branch3,semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,tutorial,lab,lab_name,30)
#_________________________________________NODES FOR LABS__________________________________________________
class node_for_labs:
    def __init__(self,code,type,name,branch1,sem_org1,semester1,branch2,sem_org2,semester2,branch3,sem_org3,semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,tutorial,lab,lab_name,capacity):
        self.code=code
        self.name=name
        self.type=type
        self.semester1=semester1
        self.semester2=semester2
        self.semester3=semester3
        obj_for_sem.insert(semester1,branch1,sem_org1,classroom_code1)
        if branch2!="NA":obj_for_sem.insert(semester2,branch2,sem_org2,classroom_code2)
        if branch3!="NA":obj_for_sem.insert(semester3,branch3,sem_org3,classroom_code3)
        self.faculty1=faculty1
        self.faculty2=faculty2
        self.faculty3=faculty3
        self.faculty1_id=1
        obj_for_facultys.insert(faculty1,self.faculty1_id)
        if faculty2!="NA":obj_for_facultys.insert(faculty2,self.faculty1_id)
        if faculty3!="NA":obj_for_facultys.insert(faculty3,self.faculty1_id)
        self.branch1=branch1
        self.branch2=branch2
        self.branch3=branch3
        self.lab_name=lab_name
        self.id=theory
        self.lab_code=None
        self.check=theory
        self.theory=0
        self.tutorial=0
        self.lab=lab*60
        self.next=None
#____________________________________________LINKED LIST FOR LABS______________________________________________
class linked_list_for_traversing_labs:
    def __init__(self):
        global i
        self.head_for_CSE=None
        self.head_for_ECE=None
        self.head_for_DSAI=None
    def insert(self,code,type,name,branch1,semester1,branch2,semester2,branch3,semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,tutorial,lab,lab_name=None,capacity=30):
                new_node_to_insert_lab1=node_for_labs(code+"_LAB_(B1) ",type,name,branch1,semester1,branch1+"_"+semester1,branch2,semester2,branch2+"_"+semester2,branch3,semester3,branch3+"_"+semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,1,0,lab,lab_name,capacity)
                new_node_to_insert_lab2=node_for_labs(code+"_LAB_(B2) ",type,name,branch1,semester1,branch1+"_"+semester1,branch2,semester2,branch2+"_"+semester2,branch3,semester3,branch3+"_"+semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,2,0,lab,lab_name,capacity)
                if branch1=='CSE':
                    if self.head_for_CSE==None :
                        if lab:
                            self.head_for_CSE=new_node_to_insert_lab1
                            self.head_for_CSE.next=new_node_to_insert_lab2
                        return
                    temp=self.head_for_CSE
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_lab1
                    temp.next.next=new_node_to_insert_lab2
                    return
                if branch1=='DSAI':
                    if self.head_for_DSAI==None :
                        if lab:
                            self.head_for_DSAI=new_node_to_insert_lab1
                            self.head_for_DSAI.next=new_node_to_insert_lab2
                        return
                    temp=self.head_for_DSAI
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_lab1
                    temp.next.next=new_node_to_insert_lab2
                    return
                if branch1=='ECE':
                    if self.head_for_ECE==None :
                        if lab:
                            self.head_for_ECE=new_node_to_insert_lab1
                            self.head_for_ECE.next=new_node_to_insert_lab2
                        return
                    temp=self.head_for_ECE
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_lab1
                    temp.next.next=new_node_to_insert_lab2
                    return
#_________________________________________________NODE FOR TUTORIAL_________________________________________________
class node_for_tutorial:
    def __init__(self,code,type,name,branch1,sem_org1,semester1,branch2,sem_org2,semester2,branch3,sem_org3,semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,tutorial,lab,lab_name,capacity):
        self.code=code
        self.name=name
        self.semester1=semester1
        self.semester2=semester2
        self.semester3=semester3
        self.type=type
        obj_for_sem.insert(semester1,branch1,sem_org1,classroom_code1)
        if branch2!="NA":obj_for_sem.insert(semester2,branch2,sem_org2,classroom_code2)
        if branch3!="NA":obj_for_sem.insert(semester3,branch3,sem_org3,classroom_code3)
        self.faculty1=faculty1
        self.faculty2=faculty2
        self.faculty3=faculty3
        self.faculty1_id=1
        obj_for_facultys.insert(faculty1,self.faculty1_id)
        if faculty2!="NA":obj_for_facultys.insert(faculty2,self.faculty1_id)
        if faculty3!="NA":obj_for_facultys.insert(faculty3,self.faculty1_id)
        self.branch1=branch1
        self.branch2=branch2
        self.branch3=branch3
        self.lab_name=lab_name
        self.theory=0
        self.tutorial=tutorial*60
        self.lab=0
        self.next=None
#______________________________________________LINKED LIST FOR TUTORIALS__________________________________________
class linked_list_for_traversing_tutorial:
    def __init__(self):
        self.head_for_CSE=None
        self.head_for_ECE=None
        self.head_for_DSAI=None
    def insert(self,code,type,name,branch1,semester1,branch2,semester2,branch3,semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,tutorial,lab,lab_name=None,capacity=30):
                new_node_to_insert_tutorial=node_for_tutorial(code+"_TUT",type,name,branch1,semester1,branch1+"_"+semester1,branch2,semester2,branch2+"_"+semester2,branch3,semester3,branch3+"_"+semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,tutorial,lab,lab_name,capacity)
                if branch1=='CSE':
                    if self.head_for_CSE==None :
                        self.head_for_CSE=new_node_to_insert_tutorial
                        return
                    temp=self.head_for_CSE
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_tutorial
                    return
                if branch1=='DSAI':
                    if self.head_for_DSAI==None :
                        if tutorial:
                            self.head_for_DSAI=new_node_to_insert_tutorial
                        return
                    temp=self.head_for_DSAI
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_tutorial
                    return
                if branch1=='ECE':
                    if self.head_for_ECE==None :
                        if tutorial:
                            self.head_for_ECE=new_node_to_insert_tutorial
                        return
                    temp=self.head_for_ECE
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_tutorial
                    return
#_______________________________________________NODE FOR THEORY AND ELECTIVES_____________________________________________
class node_for_courses_for_all:
    def __init__(self,code,type,name,branch1,sem_org1,semester1,branch2,sem_org2,semester2,branch3,sem_org3,semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,tutorial,lab,lab_name,capacity):
        self.code=code
        self.name=name
        self.type=type
        self.semester1=semester1
        self.semester2=semester2
        self.semester3=semester3
        if semester1!="NA":obj_for_sem.insert(semester1,branch1,sem_org1,classroom_code1)
        if semester2!="NA":obj_for_sem.insert(semester2,branch2,sem_org2,classroom_code2)
        if semester3!="NA":obj_for_sem.insert(semester3,branch3,sem_org3,classroom_code3)
        self.faculty1=faculty1
        self.faculty2=faculty2
        self.faculty3=faculty3
        self.lab_name=lab_name
        obj_for_facultys.insert(faculty1,1)
        if faculty2!="NA":obj_for_facultys.insert(faculty2,1)
        if faculty3!="NA":obj_for_facultys.insert(faculty3,1)
        self.branch1=branch1
        self.branch2=branch2
        self.branch3=branch3
        self.lab_name=lab_name
    #Number of minutes
        self.theory=theory*60
        self.tutorial=tutorial*60
        self.lab=lab*60
        self.next=None
        if type=="e":
            self.time1=theory
            self.time2=theory
            self.time3=theory
#_______________________________________________LINKED LIST FOR THEORY_______________________________________________
class linked_list_for_traversing_theory:
    def __init__(self):
        self.head_for_CSE=None
        self.head_for_ECE=None
        self.head_for_DSAI=None
    def insert(self,code,type,name,branch1,semester1,branch2,semester2,branch3,semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,tutorial,lab,lab_name=None,capacity=30):
                new_node_to_insert_theory=None
                if branch1=='CSE':
                    if theory:
                        new_node_to_insert_theory=node_for_courses_for_all(code+"_TH",type,name,branch1,semester1,branch1+"_"+semester1,branch2,semester2,branch2+"_"+semester2,branch3,semester3,branch3+"_"+semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,0,0,lab_name,capacity)
                    if self.head_for_CSE==None:
                        self.head_for_CSE=new_node_to_insert_theory
                        return
                    temp=self.head_for_CSE
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_theory
                if branch1=='DSAI':
                    if theory:
                        new_node_to_insert_theory=node_for_courses_for_all(code+"_TH",type,name,branch1,semester1,branch1+"_"+semester1,branch2,semester2,branch2+"_"+semester2,branch3,semester3,branch3+"_"+semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,0,0,lab_name,capacity)
                    if self.head_for_DSAI==None:
                        self.head_for_DSAI=new_node_to_insert_theory
                        return
                    temp=self.head_for_DSAI
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_theory
                if branch1=='ECE':
                    if theory:
                        new_node_to_insert_theory=node_for_courses_for_all(code+"_TH",type,name,branch1,semester1,branch1+"_"+semester1,branch2,semester2,branch2+"_"+semester2,branch3,semester3,branch3+"_"+semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,0,0,lab_name,capacity)
                    if self.head_for_ECE==None:
                        self.head_for_ECE=new_node_to_insert_theory
                        return
                    temp=self.head_for_ECE
                    while(temp.next):
                        temp=temp.next
                    temp.next=new_node_to_insert_theory
#____________________________________________LINKED LIST FOR ELECTIVES_______________________________________________
class linked_list_for_electives:
    def __init__(self):
        self.head_for_theory=None
        self.head_for_tutorial=None
        self.head_for_lab=None
    def insert(self,code,type,name,branch1,semester1,branch2,semester2,branch3,semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,tutorial,lab,lab_name,capacity):
        new_node_to_insert_theory=None
        new_node_to_insert_tutorial=None
        new_node_to_insert_lab=None
        if theory:
            new_node_to_insert_theory=node_for_courses_for_all(code+"_TH",type,name,branch1,semester1,branch1+"_"+semester1,branch2,semester2,branch2+"_"+semester2,branch3,semester3,branch3+"_"+semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,theory,0,0,lab_name,30)
            if self.head_for_theory==None:
                self.head_for_theory=new_node_to_insert_theory
            else:
                temp=self.head_for_theory
                while(temp.next):
                    temp=temp.next
                temp.next=new_node_to_insert_theory
        if tutorial:
            new_node_to_insert_tutorial=node_for_courses_for_all(code+"_TUT",type,name,branch1,semester1,branch1+"_"+semester1,branch2,semester2,branch2+"_"+semester2,branch3,semester3,branch3+"_"+semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,0,tutorial,0,lab_name,capacity)
            if self.head_for_tutorial==None:
                self.head_for_tutorial=new_node_to_insert_tutorial
            else:
                temp=self.head_for_tutorial
                while(temp.next):
                    temp=temp.next
                temp.next=new_node_to_insert_tutorial
        if lab:
            new_node_to_insert_lab=node_for_labs(code+"Lab",type,name,branch1,semester1,branch1+"_"+semester1,branch2,semester2,branch2+"_"+semester2,branch3,semester3,branch3+"_"+semester3,classroom_code1,classroom_code2,classroom_code3,faculty1,faculty2,faculty3,0,0,lab,lab_name,capacity)
            if self.head_for_lab==None:
                self.head_for_lab=new_node_to_insert_lab
            else:
                temp=self.head_for_lab
                while(temp.next):
                    temp=temp.next
                temp.next=new_node_to_insert_lab
#________________________________________________NODE FOR faculty_______________________________________________
class node_for_faculty:
    def __init__(self,f_name,id):
        self.faculty_name=f_name
        self.faculty_id=id
        self.next=None
        self.workload=1
        self.faculty_tt=[   ['Day/Time'     ,'8:30-9:30' ,'9:30-10:30' ,'10:30-11:30' ,'11:30-12:30' ,'12:30-1:30' ,"1:30-2:30" ,"2:30-3:30" ,"3:30-4:30" ,"4:30-5:30" ,"5:30-6:30" ,"6:30-7:30"],
                            ['Monday   '    ,'*'         ,'*'          ,'*'           ,'*'           ,'*'          ,"*"         ,"*"         ,"*"         ,"*"         ,"*"         ,"*"        ],
                            ['Tuesday  '    ,'*'         ,'*'          ,'*'           ,'*'           ,'*'          ,"*"         ,"*"         ,"*"         ,"*"         ,"*"         ,"*"        ],
                            ['Wednesday'    ,'*'         ,'*'          ,'*'           ,'*'           ,'*'          ,"*"         ,"*"         ,"*"         ,"*"         ,"*"         ,"*"        ],
                            ['Thursday'     ,'*'         ,'*'          ,'*'           ,'*'           ,'*'          ,"*"         ,"*"         ,"*"         ,"*"         ,"*"         ,"*"        ],
                            ['Friday'       ,'*'         ,'*'          ,'*'           ,'*'           ,'*'          ,"*"         ,"*"         ,"*"         ,"*"         ,"*"         ,"*"        ]]
        self.test_tt=   [   ['Day/Time'     ,'8:30-9:30' ,'9:30-10:30' ,'10:30-11:30' ,'11:30-12:30' ,'12:30-1:30' ,"1:30-2:30" ,"2:30-3:30" ,"3:30-4:30" ,"4:30-5:30" ,"5:30-6:30" ,"6:30-7:30"],
                            ['Monday   '    ,'*'         ,'*'          ,'*'           ,'*'           ,'*'          ,"*"         ,"*"         ,"*"         ,"*"         ,"*"         ,"*"        ],
                            ['Tuesday  '    ,'*'         ,'*'          ,'*'           ,'*'           ,'*'          ,"*"         ,"*"         ,"*"         ,"*"         ,"*"         ,"*"        ],
                            ['Wednesday'    ,'*'         ,'*'          ,'*'           ,'*'           ,'*'          ,"*"         ,"*"         ,"*"         ,"*"         ,"*"         ,"*"        ],
                            ['Thursday'     ,'*'         ,'*'          ,'*'           ,'*'           ,'*'          ,"*"         ,"*"         ,"*"         ,"*"         ,"*"         ,"*"        ],
                            ['Friday'       ,'*'         ,'*'          ,'*'           ,'*'           ,'*'          ,"*"         ,"*"         ,"*"         ,"*"         ,"*"         ,"*"        ]]

#_______________________________________________LINKED LIST FOR faculty1 NAME_______________________________________
class linked_list_for_faculty:
    def __init__(self):
        self.head_for_faculty_names=None
    def insert(self,f_name,id):
        new_node=node_for_faculty(f_name,id)
        if self.head_for_faculty_names==None:
            self.head_for_faculty_names=new_node
            return
        count=0
        temp=self.head_for_faculty_names
        while(temp):
            if temp.faculty_name==f_name:
                count+=1
                break
            temp=temp.next
        if count==0:
            temp=self.head_for_faculty_names
            while temp.next:
                temp=temp.next
            temp.next=new_node
#________________________________________________NODE FOR SEMESTER________________________________________________
class node_for_semesters:
    def __init__(self,sem,branch,sem_org,classroom_code):
        self.sem=sem
        self.sem_org=sem_org
        self.sem_without_branch=sem[4:]
        self.branch1=branch
        self.classroom_code=classroom_code
        if sem=="CSE_Sem_1_A" or sem=="CSE_Sem_1_B" or sem=="CSE_Sem_2_A" or sem=="CSE_Sem_2_B" or sem=="ECE_Sem_1" or sem=="ECE_Sem_2":
            self.sem_tt=[   ['Day/Time'     ,'9:00-10:30'             ,'10:45-11:45'          ,'11:45-12:45'                      ,'1:45-3:15'                         ,'3:15-4:15'              ,""  ,"."],
                            ['Monday   '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                            ['Tuesday  '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                            ['Wednesday'    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                            ['Thursday'     ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                            ['Friday'       ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."]]
        if sem=="CSE_Sem_3_A" or sem=="CSE_Sem_3_B" or sem=="CSE_Sem_4_A" or sem=="CSE_Sem_4_B"  or sem=="DSAI_Sem_3" or sem=="DSAI_Sem_4":
            self.sem_tt=[   ['Day/Time'     ,'9:00-10:30'             ,'11:00-12:00'          ,'12:00-1:00'                       ,'2:00-3:30'                         ,'3:30-5:00'              ,""  ,"."],
                            ['Monday   '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                            ['Tuesday  '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                            ['Wednesday'    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                            ['Thursday'     ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                            ['Friday'       ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."]]
        if sem=="CSE_Sem_5_A" or sem=="CSE_Sem_5_B" or sem=="CSE_Sem_6_A" or sem=="CSE_Sem_6_B" or sem=="DSAI_Sem_5" or sem=="DSAI_Sem_6" or sem=="ECE_Sem_5" or sem=="ECE_Sem_6":
            self.sem_tt=[   ['Day/Time'     ,'8:30-10:00'             ,'10:30-12:00'          ,'12:00-1:30'                       ,'2:30-3:30'                         ,'3:30-4:30'              ,""  ,"."],
                            ['Monday   '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                            ['Tuesday  '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                            ['Wednesday'    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                            ['Thursday'     ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                            ['Friday'       ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."]]
        if sem_org=="Sem_7_A" or sem_org=="Sem_7_B" or sem_org=="Sem_8_A" or sem_org=="Sem_8_B" or sem_org=="Sem_7" or sem_org=="Sem_8":
            self.sem_tt=[   ['Day/Time'     ,'8:30-10:00'             ,'10:00-11:30'          ,'11:30-1:00'                       ,'1:30-2:30'                         ,'2:30-3:30'              ,"3:30-5:00"            ,"5:00-6:00" ],
                            ['Monday   '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,'*'                    ,'*'         ],
                            ['Tuesday  '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,'*'                    ,'*'         ],
                            ['Wednesday'    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,'*'                    ,'*'         ],
                            ['Thursday'     ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,'*'                    ,'*'         ],
                            ['Friday'       ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,'*'                    ,'*'         ]]
        if sem=="DSAI_Sem_1" or sem=="DSAI_Sem_2" or sem=="DSAI_Sem_3" or sem=="ECE_Sem_3" or sem=="ECE_Sem_4":
            self.sem_tt=[   ['Day/Time'     ,'8:30-10:30'             ,'10:45-12:15'          ,'12:15-1:15'                       ,'2:15-3:45'                         ,'3:45-5:15'              ,""  ,"."],
                            ['Monday   '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                            ['Tuesday  '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                            ['Wednesday'    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                            ['Thursday'     ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                            ['Friday'       ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."]]
        if sem=="CSE_Sem_1_A" or sem=="CSE_Sem_1_B" or sem=="CSE_Sem_2_A" or sem=="CSE_Sem_2_B" or sem=="ECE_Sem_1" or sem=="ECE_Sem_2":
            self.sem_tt_new=[   ['Day/Time'     ,'9:00-10:30'             ,'10:45-11:45'          ,'11:45-12:45'                      ,'1:45-3:15'                         ,'3:15-4:15'              ,""  ,"."],
                                ['Monday   '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                ['Tuesday  '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                ['Wednesday'    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                ['Thursday'     ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                ['Friday'       ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."]]
        if sem=="CSE_Sem_3_A" or sem=="CSE_Sem_3_B" or sem=="CSE_Sem_4_A" or sem=="CSE_Sem_4_B"  or sem=="DSAI_Sem_4":
            self.sem_tt_new=[   ['Day/Time'     ,'9:00-10:30'             ,'11:00-12:00'          ,'12:00-1:00'                       ,'2:00-3:30'                         ,'3:30-5:00'              ,""  ,"."],
                                ['Monday   '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                ['Tuesday  '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                ['Wednesday'    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                ['Thursday'     ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                ['Friday'       ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."]]
        if sem=="CSE_Sem_5_A" or sem=="CSE_Sem_5_B" or sem=="CSE_Sem_6_A" or sem=="CSE_Sem_6_B" or sem=="DSAI_Sem_5" or sem=="DSAI_Sem_6" or sem=="ECE_Sem_5" or sem=="ECE_Sem_6":
            self.sem_tt_new=[   ['Day/Time'     ,'8:30-10:00'             ,'10:30-12:00'          ,'12:00-1:30'                       ,'2:30-3:30'                         ,'3:30-4:30'              ,""  ,"."],
                                ['Monday   '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                ['Tuesday  '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                ['Wednesday'    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                ['Thursday'     ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                ['Friday'       ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."]]
        if sem_org=="Sem_7_A" or sem_org=="Sem_7_B" or sem_org=="Sem_8_A" or sem_org=="Sem_8_B" or sem_org=="Sem_7" or sem_org=="Sem_8":
            self.sem_tt_new=[   ['Day/Time'     ,'8:30-10:00'             ,'10:00-11:30'          ,'11:30-1:00'                       ,'1:30-2:30'                         ,'2:30-3:30'              ,"3:30-5:00"            ,"5:00-6:00" ],
                                ['Monday   '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,'*'                    ,'*'         ],
                                ['Tuesday  '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,'*'                    ,'*'         ],
                                ['Wednesday'    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,'*'                    ,'*'         ],
                                ['Thursday'     ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,'*'                    ,'*'         ],
                                ['Friday'       ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,'*'                    ,'*'         ]]
        if sem=="DSAI_Sem_1" or sem=="DSAI_Sem_2" or sem=="DSAI_Sem_3" or sem=="ECE_Sem_3" or sem=="ECE_Sem_4":
            self.sem_tt_new=[   ['Day/Time'     ,'8:30-10:30'             ,'10:45-12:15'          ,'12:15-1:15'                       ,'2:15-3:45'                         ,'3:45-5:15'              ,""  ,"."],
                                ['Monday   '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                ['Tuesday  '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                ['Wednesday'    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                ['Thursday'     ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                ['Friday'       ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."]]
        self.next=None
#____________________________________________LINKED LIST TO TRAVERSE SEMESTERS______________________________________
class linked_list_to_travese_semester():
    def __init__(self):
        self.head_for_semesters=None
    def insert(self,sem,branch,sem_org,classroom_code):
        new_node=None
        if branch!="NA":
            new_node=node_for_semesters(sem,branch,sem_org,classroom_code)
        if self.head_for_semesters==None:
            self.head_for_semesters=new_node
            return
        count=0
        temp=self.head_for_semesters
        while(temp):
            if temp.sem==sem:
                count+=1
                break
            temp=temp.next
        if count==0:
            temp=self.head_for_semesters
            while(temp.next):
                temp=temp.next
            temp.next=new_node
#____________________________________________NODE FOR LAB ROOMS________________________________________
class node_for_linked_list_for_lab_rooms:
    def __init__(self,name,capacity,branch):
        self.name=name
        self.capacity=capacity
        self.branch1=branch
        self.tt=[   ['Day/Time'     ,'8:30-9:30' ,'9:30-10:30' ,'10:30-11:30' ,'11:30-12:30' ,'12:30-1:30' ,"1:30-2:30" ,"2:30-3:30" ,"3:30-4:30" ,"4:30-5:30" ,"5:30-6:30" ,"6:30-7:30"],
                    ['Monday   '    ,'*'         ,'*'          ,'*'           ,'*'           ,'*'          ,"*"         ,"*"         ,"*"         ,"*"         ,"*"         ,"*"        ],
                    ['Tuesday  '    ,'*'         ,'*'          ,'*'           ,'*'           ,'*'          ,"*"         ,"*"         ,"*"         ,"*"         ,"*"         ,"*"        ],
                    ['Wednesday'    ,'*'         ,'*'          ,'*'           ,'*'           ,'*'          ,"*"         ,"*"         ,"*"         ,"*"         ,"*"         ,"*"        ],
                    ['Thursday'     ,'*'         ,'*'          ,'*'           ,'*'           ,'*'          ,"*"         ,"*"         ,"*"         ,"*"         ,"*"         ,"*"        ],
                    ['Friday'       ,'*'         ,'*'          ,'*'           ,'*'           ,'*'          ,"*"         ,"*"         ,"*"         ,"*"         ,"*"         ,"*"        ]]
        self.next=None
#_____________________________________________LINKED LIST FOR TRAVERSING LAB ROOMS___________________________
class linked_list_for_traversing_lab_rooms:
    def __init__(self):
        self.head_for_CSE_rooms=None
        self.head_for_ECE_rooms=None
    def insert(self,name,capacity,branch):
        new_lab=node_for_linked_list_for_lab_rooms(name,capacity,branch)
        if branch=='CSE':
            if self.head_for_CSE_rooms==None:
                self.head_for_CSE_rooms=new_lab
                return
            count=0
            temp=self.head_for_CSE_rooms
            while(temp):
                if temp.name==name:
                    count+=1
                    break
                temp=temp.next
            if count==0:
                temp=self.head_for_CSE_rooms
                while(temp.next):
                    temp=temp.next
                temp.next=new_lab
        if branch=='ECE':
            if self.head_for_ECE_rooms==None:
                self.head_for_ECE_rooms=new_lab
                return
            count=0
            temp=self.head_for_ECE_rooms
            while(temp):
                if temp.name==name:
                    count+=1
                    break
                temp=temp.next
            if count==0:
                temp=self.head_for_ECE_rooms
                while(temp.next):
                    temp=temp.next
                temp.next=new_lab
#____________________________________________NODE FOR CLASS ROOMS________________________________________
class node_for_linked_list_for_class_rooms:
    def __init__(self,name,classroom_code,semester=None):
        self.name=name
        self.sem=semester
        self.classroom_tt=None
        self.classroom_code=classroom_code
        if name=="CSE_Sem_1_A" or name=="CSE_Sem_1_B" or name=="CSE_Sem_2_A" or name=="CSE_Sem_2_B" or name=="ECE_Sem_1" or name=="ECE_Sem_2":
            self.classroom_tt=[     ['Day/Time'     ,'9:00-10:30'             ,'10:45-11:45'          ,'11:45-12:45'                      ,'1:45-3:15'                         ,'3:15-4:15'              ,""  ,"."],
                                    ['Monday   '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                    ['Tuesday  '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                    ['Wednesday'    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                    ['Thursday'     ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                    ['Friday'       ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."]]
        if name=="CSE_Sem_3_A" or name=="CSE_Sem_3_B" or name=="CSE_Sem_4_A" or name=="CSE_Sem_4_B"  or name=="DSAI_Sem_4":
            self.classroom_tt=[     ['Day/Time'     ,'9:00-10:30'             ,'11:00-12:00'          ,'12:00-1:00'                       ,'2:00-3:30'                         ,'3:30-5:00'              ,""  ,"."],
                                    ['Monday   '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                    ['Tuesday  '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                    ['Wednesday'    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                    ['Thursday'     ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                    ['Friday'       ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."]]
        if name=="CSE_Sem_5_A" or name=="CSE_Sem_5_B" or name=="CSE_Sem_6_A" or name=="CSE_Sem_6_B" or name=="DSAI_Sem_5" or name=="DSAI_Sem_6" or name=="ECE_Sem_5" or name=="ECE_Sem_6":
            self.classroom_tt=[     ['Day/Time'     ,'8:30-10:00'             ,'10:30-12:00'          ,'12:00-1:30'                       ,'2:30-3:30'                         ,'3:30-4:30'              ,""  ,"."],
                                    ['Monday   '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                    ['Tuesday  '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                    ['Wednesday'    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                    ['Thursday'     ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                    ['Friday'       ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."]]
        if name=="CSE_Sem_7" or name=="CSE_Sem_8" or name=="DSAI_Sem_7" or name=="ECE_Sem_7" or name=="DSAI_Sem_8" or name=="ECE_Sem_8":
            self.classroom_tt=[     ['Day/Time'     ,'8:30-10:00'             ,'10:00-11:30'          ,'11:30-1:00'                       ,'1:30-2:30'                         ,'2:30-3:30'              ,"3:30-5:00"            ,"5:00-6:00" ],
                                    ['Monday   '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,'*'                    ,'*'         ],
                                    ['Tuesday  '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,'*'                    ,'*'         ],
                                    ['Wednesday'    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,'*'                    ,'*'         ],
                                    ['Thursday'     ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,'*'                    ,'*'         ],
                                    ['Friday'       ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,'*'                    ,'*'         ]]
        if name=="DSAI_Sem_1" or name=="DSAI_Sem_2" or name=="DSAI_Sem_3"  or name=="ECE_Sem_3" or name=="ECE_Sem_4":
            self.classroom_tt=[     ['Day/Time'     ,'8:30-10:30'             ,'10:45-12:15'          ,'12:15-1:15'                       ,'2:15-3:45'                         ,'3:45-5:15'              ,""  ,"."],
                                    ['Monday   '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                    ['Tuesday  '    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                    ['Wednesday'    ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                    ['Thursday'     ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."],
                                    ['Friday'       ,'*'                      ,'*'                    ,'*'                                ,'*'                                 ,'*'                      ,"." ,"."]]
        if self.classroom_tt==None:print(name)
        self.next=None
#_____________________________________________LINKED LIST FOR TRAVERSING CLASS ROOMS___________________________
class linked_list_for_traversing_class_rooms:
    def __init__(self):
        self.head_for_class_rooms=None
    def insert(self,name,classroom_code,semester=None):
        new_lab=node_for_linked_list_for_class_rooms(name,classroom_code,semester)
        if self.head_for_class_rooms==None:
            self.head_for_class_rooms=new_lab
            return
        count=0
        temp=self.head_for_class_rooms
        while(temp):
            if temp.name==name:
                count+=1
                break
            temp=temp.next
        if count==0:
            temp=self.head_for_class_rooms
            while(temp.next):
                temp=temp.next
            temp.next=new_lab
pty=0
#_______________________________________________________PLOTTING FUNCTION DECISION MAKING________________________________________
def plotting():
    global pty
    point=0
    pointer=0
    for i in range(9):
        variable_for_sem_generalized_head=None
        variable_for_classroom_generalized_head=None
        if i==0:
            if cse==0:continue
            temp1=obj_for_linked_list_for_traversing_labs.head_for_CSE
            variable_for_sem_generalized_head=obj_for_sem.head_for_semesters
            variable_for_classroom_generalized_head=obj_for_class_rooms.head_for_class_rooms
        if i==1:
            if cse==0:continue
            temp1=obj_for_linked_list_for_traversing_theory.head_for_CSE
            variable_for_sem_generalized_head=obj_for_sem.head_for_semesters
            variable_for_classroom_generalized_head=obj_for_class_rooms.head_for_class_rooms
        if i==2:
            if cse==0:continue
            temp1=obj_for_linked_list_for_traversing_tutorials.head_for_CSE
            variable_for_sem_generalized_head=obj_for_sem.head_for_semesters
            variable_for_classroom_generalized_head=obj_for_class_rooms.head_for_class_rooms
        if i==3:
            if dsai==0:continue
            temp1=obj_for_linked_list_for_traversing_labs.head_for_DSAI
            variable_for_sem_generalized_head=obj_for_sem.head_for_semesters
            variable_for_classroom_generalized_head=obj_for_class_rooms.head_for_class_rooms
        if i==5:
            if dsai==0:continue
            temp1=obj_for_linked_list_for_traversing_theory.head_for_DSAI
            variable_for_sem_generalized_head=obj_for_sem.head_for_semesters
            variable_for_classroom_generalized_head=obj_for_class_rooms.head_for_class_rooms
        if i==4:
            if dsai==0:continue
            temp1=obj_for_linked_list_for_traversing_tutorials.head_for_DSAI
            variable_for_sem_generalized_head=obj_for_sem.head_for_semesters
            variable_for_classroom_generalized_head=obj_for_class_rooms.head_for_class_rooms
        if i==6:
            if ece==0:continue
            temp1=obj_for_linked_list_for_traversing_labs.head_for_ECE
            variable_for_sem_generalized_head=obj_for_sem.head_for_semesters
            variable_for_classroom_generalized_head=obj_for_class_rooms.head_for_class_rooms
        if i==7:
            if ece==0:continue
            temp1=obj_for_linked_list_for_traversing_theory.head_for_ECE
            variable_for_sem_generalized_head=obj_for_sem.head_for_semesters
            variable_for_classroom_generalized_head=obj_for_class_rooms.head_for_class_rooms
        if i==8:
            if ece==0:continue
            temp1=obj_for_linked_list_for_traversing_tutorials.head_for_ECE
            variable_for_sem_generalized_head=obj_for_sem.head_for_semesters
            variable_for_classroom_generalized_head=obj_for_class_rooms.head_for_class_rooms
        #Holding node.
        temp_for_faculty=obj_for_facultys.head_for_faculty_names
        while(temp_for_faculty):
            while(temp1):
                if temp1.semester1=="CSE_Sem_2_A":
                    if i==1:
                        point+=1
                if point>0 :
                    if pty==0:
                        pty=1
                if temp1.faculty1==temp_for_faculty.faculty_name:
                    time=0

                temp2=obj_for_facultys.head_for_faculty_names
                while temp2:
                    if temp1.faculty1==temp2.faculty_name:
                        break
                    temp2=temp2.next
                #Fetching faculty2 if exists or else None
                temp22=obj_for_facultys.head_for_faculty_names
                while(temp22):
                    if temp1.faculty2==temp22.faculty_name:
                        break
                    temp22=temp22.next
                if temp1.faculty2=='NA':temp22=None
                #Fetching faculty3 if exists or else None
                temp222=obj_for_facultys.head_for_faculty_names
                while(temp222):
                    if temp1.faculty3==temp222.faculty_name:
                        break
                    temp222=temp222.next
                if temp1.faculty3=='NA':temp222=None
                #Fetching semester.
                temp3=variable_for_sem_generalized_head
                while temp3:
                    if temp1.semester1==temp3.sem:
                        break
                    temp3=temp3.next
                #Fetching classroom.
                temp4=variable_for_classroom_generalized_head
                while(temp4):
                    if (temp1.semester1)==temp4.name:
                        break
                    temp4=temp4.next
                #Fetching lab every time.
                temp5=None
                if temp1.lab_name=='CSE_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                if temp1.lab_name=='ECE_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                #Changing timetable.
                if "CSE_Sem_1_A"==temp1.semester1 or "CSE_Sem_1_B"==temp1.semester1 or "CSE_Sem_2_A"==temp1.semester1 or "CSE_Sem_2_B"==temp1.semester1 or "ECE_Sem_1"==temp1.semester1 or "ECE_Sem_2"==temp1.semester1 :
                    if temp1.theory:
                        time=0
                        for _ in range(4):
                            for i in range(6):
                                for j in range(8):
                                    if _<=2:
                                        shift=0
                                        for l in range(8):
                                            if temp2.test_tt[i][l]==temp1.semester1:
                                                shift=1
                                                break
                                        if shift==1:break
                                    if _<2:
                                        if i==1 and j==1 and (temp3.sem_tt[2][1]==temp1.code or temp3.sem_tt[1][2]==temp1.code ): break
                                        if i==2 and j==1 and (temp3.sem_tt[1][1]==temp1.code or temp3.sem_tt[2][2]==temp1.code or temp3.sem_tt[3][1]==temp1.code): break
                                        if i==3 and j==1 and (temp3.sem_tt[2][1]==temp1.code or temp3.sem_tt[3][2]==temp1.code or temp3.sem_tt[4][1]==temp1.code): break
                                        if i==4 and j==1 and (temp3.sem_tt[3][1]==temp1.code or temp3.sem_tt[4][2]==temp1.code or temp3.sem_tt[5][1]==temp1.code): break
                                        if i==5 and j==1 and (temp3.sem_tt[4][1]==temp1.code or temp3.sem_tt[5][2]==temp1.code ): break
                                        if i==1 and j==4 and (temp3.sem_tt[1][1]==temp1.code or temp3.sem_tt[2][4]==temp1.code ): break
                                        if i==2 and j==4 and (temp3.sem_tt[1][4]==temp1.code or temp3.sem_tt[2][4]==temp1.code or temp3.sem_tt[3][4]==temp1.code): break
                                        if i==3 and j==4 and (temp3.sem_tt[2][4]==temp1.code or temp3.sem_tt[3][4]==temp1.code or temp3.sem_tt[4][4]==temp1.code): break
                                        if i==4 and j==4 and (temp3.sem_tt[3][4]==temp1.code or temp3.sem_tt[4][4]==temp1.code or temp3.sem_tt[5][4]==temp1.code): break
                                        if i==5 and j==4 and (temp3.sem_tt[4][4]==temp1.code or temp3.sem_tt[5][1]==temp1.code ): break
                                    if j==1:
                                        if temp2:
                                            if temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][1]==temp22.faculty_tt[i][2]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][1]==temp222.faculty_tt[i][2]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][1]=temp1.semester1+" (9:00-10:30)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][2]="."
                                                                temp2.test_tt[i][1]=temp1.semester1
                                                                temp22.faculty_tt[i][1]=temp1.semester1+" (9:00-10:30)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][2]="."
                                                                temp222.faculty_tt[i][1]=temp1.semester1+" (9:00-10:30)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][2]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                            else:continue
                                                        else:
                                                            temp2.faculty_tt[i][1]=temp1.semester1+" (9:00-10:30)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][2]="."
                                                            temp2.test_tt[i][1]=temp1.semester1
                                                            temp22.faculty_tt[i][1]=temp1.semester1+" (9:00-10:30)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][2]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][1]=temp1.semester1+" (9:00-10:30)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][2]="."
                                                    temp2.test_tt[i][1]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                                    if j==4:
                                        if temp2:
                                            if temp2.faculty_tt[i][6]==temp2.faculty_tt[i][7]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][6]==temp22.faculty_tt[i][7]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][6]==temp222.faculty_tt[i][7]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][6]=temp1.semester1+" (1:45-3:15)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][7]="."
                                                                temp2.test_tt[i][6]=temp1.semester1
                                                                temp22.faculty_tt[i][6]=temp1.semester1+" (1:45-3:15)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][7]="."
                                                                temp222.faculty_tt[i][6]=temp1.semester1+" (1:45-3:15)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][7]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][6]=temp1.semester1+" (1:45-3:15)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][7]="."
                                                            temp2.test_tt[i][6]=temp1.semester1
                                                            temp22.faculty_tt[i][6]=temp1.semester1+" (1:45-3:15)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][7]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][6]=temp1.semester1+" (1:45-3:15)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][7]="."
                                                    temp2.test_tt[i][6]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                                    if j==5:
                                        if temp2:
                                            if temp2.faculty_tt[i][7]==temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][7]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][7]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][7]=temp1.semester1+" (3:15-4:45)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][8]=temp2.faculty_tt[i][9]="."
                                                                temp2.test_tt[i][7]=temp1.semester1
                                                                temp22.faculty_tt[i][7]=temp1.semester1+" (3:15-4:45)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][8]=temp22.faculty_tt[i][9]="."
                                                                temp222.faculty_tt[i][7]=temp1.semester1+" (3:15-4:45)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][8]=temp222.faculty_tt[i][9]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][7]=temp1.semester1+" (3:15-4:45)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][8]=temp2.faculty_tt[i][9]="."
                                                            temp2.test_tt[i][7]=temp1.semester1
                                                            temp22.faculty_tt[i][7]=temp1.semester1+" (3:15-4:45)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][8]=temp22.faculty_tt[i][9]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][7]=temp1.semester1+" (3:15-4:45)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp2.faculty_tt[i][9]="."
                                                    temp2.test_tt[i][7]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                                    # if j==2:
                                    #     if temp2:
                                    #         if temp2.faculty_tt[i][3]==temp2.faculty_tt[i][4]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                    #             if temp22:
                                    #                 if temp22.faculty_tt[i][3]==temp22.faculty_tt[i][4]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                    #                     if temp222:
                                    #                         if temp222.faculty_tt[i][3]==temp222.faculty_tt[i][4]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                    #                             temp2.faculty_tt[i][3]=temp1.semester1+" (1:45-3:15)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                    #                             temp2.faculty_tt[i][4]="."
                                    #                             temp2.test_tt[i][3]=temp1.semester1
                                    #                             temp22.faculty_tt[i][3]=temp1.semester1+" (1:45-3:15)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                    #                             temp22.faculty_tt[i][4]="."
                                    #                             temp222.faculty_tt[i][3]=temp1.semester1+" (1:45-3:15)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                    #                             temp222.faculty_tt[i][4]="."
                                    #                             temp3.sem_tt[i][j]=temp1.code
                                    #                             temp3.sem_tt_new[i][j]=temp1.code
                                    #                             temp4.classroom_tt[i][j]=temp1.name
                                    #                             time+=90
                                    #                             break
                                    #                     else:
                                    #                         temp2.faculty_tt[i][3]=temp1.semester1+" (1:45-3:15)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                    #                         temp2.faculty_tt[i][4]="."
                                    #                         temp2.test_tt[i][3]=temp1.semester1
                                    #                         temp22.faculty_tt[i][3]=temp1.semester1+" (1:45-3:15)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                    #                         temp22.faculty_tt[i][4]="."
                                    #                         temp3.sem_tt[i][j]=temp1.code
                                    #                         temp3.sem_tt_new[i][j]=temp1.code
                                    #                         temp4.classroom_tt[i][j]=temp1.name
                                    #                         time+=90
                                    #                         break
                                    #             else:
                                    #                 temp2.faculty_tt[i][3]=temp1.semester1+" (1:45-3:15)"+"_"+temp1.code+"_ ("+temp4.classroom_code+")"
                                    #                 temp2.faculty_tt[i][4]="."
                                    #                 temp2.test_tt[i][6]=temp1.semester1
                                    #                 temp3.sem_tt[i][j]=temp1.code
                                    #                 temp3.sem_tt_new[i][j]=temp1.code
                                    #                 temp4.classroom_tt[i][j]=temp1.name
                                    #                 time+=90
                                    #                 break
                    elif temp1.tutorial:
                        time=0
                        for _ in range(5):
                            for i in range(6):
                                for j in range(8):
                                    if _<=2:
                                        shift=0
                                        for l in range(8):
                                            if temp2.test_tt[i][l]==temp1.semester1:
                                                shift=1
                                                break
                                        if shift==1:break
                                    if j==5 and time<temp1.tutorial:
                                        if temp2.faculty_tt[i][7]==temp2.faculty_tt[i][8]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*':
                                            if j-1!=0 and temp2.faculty_tt[i][j-1]==temp1.semester1:break
                                            temp2.faculty_tt[i][7]=temp1.semester1+" (3:15-4:15)"+"_"+temp1.code+"_TUT ("+temp4.classroom_code+")"
                                            temp2.faculty_tt[i][8]="."
                                            temp2.test_tt[i][7]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if j==2:
                                        if temp2.faculty_tt[i][3]==temp2.faculty_tt[i][4]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][3]=temp1.semester1+" (10:45-11:45)"+"_"+temp1.code+"_TUT ("+temp4.classroom_code+")"
                                            temp2.faculty_tt[i][4]="."
                                            temp2.test_tt[i][3]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if j==3:
                                        if temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][4]=temp1.semester1+" (11:45-12:45)"+"_"+temp1.code+"_TUT ("+temp4.classroom_code+")"
                                            temp2.faculty_tt[i][5]="."
                                            temp2.test_tt[i][4]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if j==1:
                                        if temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][1]=temp1.semester1+" (9:00-10:00)"+"_"+temp1.code+"_TUT ("+temp4.classroom_code+")"
                                            temp2.faculty_tt[i][2]="."
                                            temp2.test_tt[i][1]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if j==4:
                                        if temp2.faculty_tt[i][6]==temp2.faculty_tt[i][7]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][6]=temp1.semester1+" (1:45-2:45)"+"_"+temp1.code+"_TUT ("+temp4.classroom_code+")"
                                            temp2.faculty_tt[i][7]="."
                                            temp2.test_tt[i][6]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                    elif temp1.lab:
                        time=0
                        for _ in range(4):
                            for i in range(6):
                                for j in range(8):

                                    if time>=temp1.lab:
                                        break
                                    elif j==2:
                                        if temp2.faculty_tt[i][3]==temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]=='*' and time<temp1.lab:
                                            #If there is no activity at that time...
                                            if temp3.sem_tt[i][j]==temp3.sem_tt[i][j+1]=='*' and (time+120)<=temp1.lab:
                                                if temp2.faculty_tt[i][1]==temp1.semester1:break
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp6):
                                                    if temp6.tt[i][3]==temp6.tt[i][4]==temp6.tt[i][5]=='*' and temp6.tt[i][j]=='*':
                                                        temp2.faculty_tt[i][3]=temp1.semester1+" (10:45-12:45)"+"_"+temp1.code+"_LAB ("+temp6.name+")"
                                                        temp2.faculty_tt[i][4]=temp2.faculty_tt[i][5]="."
                                                        temp2.test_tt[i][3]=temp1.semester1
                                                        temp3.sem_tt[i][j]=temp1.code
                                                        temp3.sem_tt[i][j+1]=temp1.code
                                                        temp3.sem_tt_new[i][j]=temp1.code+temp6.name
                                                        temp3.sem_tt_new[i][j+1]=temp1.code+temp6.name
                                                        temp6.tt[i][3]=temp1.semester1+"_"+temp1.code
                                                        temp6.tt[i][4]=temp1.semester1+"_"+temp1.code
                                                        temp6.tt[i][5]=temp1.semester1+"_"+temp1.code
                                                        time+=120
                                                        break
                                                    temp6=temp6.next
                                            elif temp3.sem_tt[i][j]==temp3.sem_tt[i][j+1] and time+120<=temp1.lab:
                                                if time>=temp1.lab:break
                                                temp5=None
                                                tip=0
                                                if temp1.branch1=="CSE":temp5=obj_for_linked_list_for_traversing_labs.head_for_CSE
                                                if temp1.branch1=="DSAI":temp5=obj_for_linked_list_for_traversing_labs.head_for_DSAI
                                                if temp1.branch1=="ECE":temp5=obj_for_linked_list_for_traversing_labs.head_for_ECE
                                                temp6=None
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp5):
                                                    if temp3.sem_tt[i][j]==temp5.code:
                                                        tip=1
                                                        break
                                                    temp5=temp5.next
                                                while(temp6):
                                                    if temp6.tt[i][3]==temp6.tt[i][4]==temp6.tt[i][5]=='*':
                                                        break
                                                    temp6=temp6.next
                                                if tip==1 and temp5.id!=temp1.id and temp6:
                                                    temp2.faculty_tt[i][3]=temp1.semester1+" (10:45-12:45)"+"_"+temp1.code+"_LAB ("+temp6.name+")"
                                                    temp2.faculty_tt[i][4]="."
                                                    temp2.test_tt[i][3]=temp1.semester1
                                                    temp2.faculty_tt[i][5]="."
                                                    temp3.sem_tt[i][j]+=" /" +temp1.code
                                                    temp3.sem_tt[i][j+1]+=" / "+temp1.code
                                                    temp3.sem_tt_new[i][j]+=" / "+temp1.code+temp6.name
                                                    temp3.sem_tt_new[i][j+1]+=" / "+temp1.code+temp6.name
                                                    temp6.tt[i][3]=temp1.semester1+"_"+temp1.code
                                                    temp6.tt[i][4]=temp1.semester1+"_"+temp1.code
                                                    temp6.tt[i][5]=temp1.semester1+"_"+temp1.code
                                                    time+=120
                                                    break
                                    if _<4 and j==5:
                                        if temp2.faculty_tt[i][7]==temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.lab:
                                            if temp1.lab_name=='CS_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                            if temp1.lab_name=='EC_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                            while(temp5):
                                                if temp5.tt[i][7]==temp5.tt[i][8]==temp5.tt[i][9]=='*' and time<temp1.lab:
                                                    temp5.tt[i][7]=temp5.tt[i][8]=temp5.tt[i][9]=temp1.semester1+"_"+temp1.code
                                                    temp2.faculty_tt[i][7]=temp1.semester1+" (3:15-5:15)"+"_"+temp1.code+"_LAB ("+temp5.name+")"
                                                    temp2.faculty_tt[i][8]=temp2.faculty_tt[i][9]="."
                                                    temp2.test_tt[i][7]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code+temp5.name
                                                    time+=120
                                                    break
                                                temp5=temp5.next
                if "DSAI_Sem_1"==temp1.semester1 or "DSAI_Sem_2"==temp1.semester1 or "ECE_Sem_3"==temp1.semester1 or "ECE_Sem_4"==temp1.semester1 or "DSAI_Sem_3"==temp1.semester1 :
                    if temp1.theory:
                        time=0
                        for _ in range(4):
                            for i in range(6):
                                for j in range(8):
                                    if _<2:
                                        if i==1 and j==2 and (temp3.sem_tt[1][4]==temp1.code or temp3.sem_tt[1][5]==temp1.code or temp3.sem_tt[3][2]==temp1.code ): break
                                        if i==2 and j==2 and (temp3.sem_tt[2][4]==temp1.code or temp3.sem_tt[2][5]==temp1.code or temp3.sem_tt[1][2]==temp1.code or temp3.sem_tt[3][2]==temp1.code): break
                                        if i==3 and j==2 and (temp3.sem_tt[3][4]==temp1.code or temp3.sem_tt[3][5]==temp1.code or temp3.sem_tt[2][2]==temp1.code or temp3.sem_tt[4][2]==temp1.code): break
                                        if i==4 and j==2 and (temp3.sem_tt[4][4]==temp1.code or temp3.sem_tt[4][5]==temp1.code or temp3.sem_tt[3][2]==temp1.code or temp3.sem_tt[5][2]==temp1.code): break
                                        if i==5 and j==2 and (temp3.sem_tt[5][4]==temp1.code or temp3.sem_tt[5][5]==temp1.code or temp3.sem_tt[4][2]==temp1.code ): break
                                        if i==1 and j==2 and (temp3.sem_tt[1][2]==temp1.code or temp3.sem_tt[1][5]==temp1.code or temp3.sem_tt[3][4]==temp1.code ): break
                                        if i==2 and j==2 and (temp3.sem_tt[2][2]==temp1.code or temp3.sem_tt[2][5]==temp1.code or temp3.sem_tt[1][4]==temp1.code or temp3.sem_tt[3][4]==temp1.code): break
                                        if i==3 and j==2 and (temp3.sem_tt[3][2]==temp1.code or temp3.sem_tt[3][5]==temp1.code or temp3.sem_tt[2][4]==temp1.code or temp3.sem_tt[4][4]==temp1.code): break
                                        if i==4 and j==2 and (temp3.sem_tt[4][2]==temp1.code or temp3.sem_tt[4][5]==temp1.code or temp3.sem_tt[3][4]==temp1.code or temp3.sem_tt[5][4]==temp1.code): break
                                        if i==5 and j==2 and (temp3.sem_tt[5][2]==temp1.code or temp3.sem_tt[5][5]==temp1.code or temp3.sem_tt[4][4]==temp1.code ): break
                                        if i==1 and j==2 and (temp3.sem_tt[1][2]==temp1.code or temp3.sem_tt[1][4]==temp1.code or temp3.sem_tt[1][5]==temp1.code ): break
                                        if i==2 and j==2 and (temp3.sem_tt[2][2]==temp1.code or temp3.sem_tt[2][4]==temp1.code or temp3.sem_tt[1][5]==temp1.code or temp3.sem_tt[3][5]==temp1.code): break
                                        if i==3 and j==2 and (temp3.sem_tt[3][2]==temp1.code or temp3.sem_tt[3][4]==temp1.code or temp3.sem_tt[2][5]==temp1.code or temp3.sem_tt[4][5]==temp1.code): break
                                        if i==4 and j==2 and (temp3.sem_tt[4][2]==temp1.code or temp3.sem_tt[4][4]==temp1.code or temp3.sem_tt[3][5]==temp1.code or temp3.sem_tt[5][5]==temp1.code): break
                                        if i==5 and j==2 and (temp3.sem_tt[5][2]==temp1.code or temp3.sem_tt[5][4]==temp1.code or temp3.sem_tt[4][5]==temp1.code ): break
                                    if _<=2:
                                        shift=0
                                        for l in range(8):
                                            if temp2.test_tt[i][l]==temp1.semester1:
                                                shift=1
                                                break
                                        if shift==1:break
                                    if _<4 and j==2:
                                        if temp2:
                                            if temp2.faculty_tt[i][3]==temp2.faculty_tt[i][4]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][3]==temp22.faculty_tt[i][4]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][3]==temp222.faculty_tt[i][4]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][3]=temp1.semester1+" (10:45-12:15)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][4]="."
                                                                temp2.test_tt[i][3]=temp1.semester1
                                                                temp22.faculty_tt[i][3]=temp1.semester1+" (10:45-12:15)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][4]="."
                                                                temp222.faculty_tt[i][3]=temp1.semester1+" (10:45-12:15)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][4]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][3]=temp1.semester1+" (10:45-12:15)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][4]="."
                                                            temp2.test_tt[i][3]=temp1.semester1
                                                            temp22.faculty_tt[i][3]=temp1.semester1+" (10:45-12:15)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][4]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][3]=temp1.semester1+" (10:45-12:15)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][4]="."
                                                    temp2.test_tt[i][3]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                                    if _<4 and j==4:
                                        if temp2:
                                            if temp2.faculty_tt[i][6]==temp2.faculty_tt[i][7]==temp2.faculty_tt[i][8]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][6]==temp22.faculty_tt[i][7]==temp22.faculty_tt[i][8]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][7]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][6]=temp1.semester1+" (2:15-3:45)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][7]=temp2.faculty_tt[i][8]="."
                                                                temp2.test_tt[i][6]=temp1.semester1
                                                                temp22.faculty_tt[i][6]=temp1.semester1+" (2:15-3:45)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][7]=temp22.faculty_tt[i][8]="."
                                                                temp222.faculty_tt[i][6]=temp1.semester1+" (2:15-3:45)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][7]=temp222.faculty_tt[i][8]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][6]=temp1.semester1+" (2:15-3:45)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][7]=temp2.faculty_tt[i][8]="."
                                                            temp2.test_tt[i][6]=temp1.semester1
                                                            temp22.faculty_tt[i][6]=temp1.semester1+" (2:15-3:45)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][7]=temp22.faculty_tt[i][8]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][6]=temp1.semester1+" (2:15-3:45)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][7]=temp2.faculty_tt[i][8]="."
                                                    temp2.test_tt[i][6]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                                    if _>1 and j==5:
                                        if temp2:
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][8]=temp1.semester1+" (3:45-5:15)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][9]="."
                                                                temp2.test_tt[i][8]=temp1.semester1
                                                                temp22.faculty_tt[i][8]=temp1.semester1+" (3:45-5:15)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][9]="."
                                                                temp222.faculty_tt[i][8]=temp1.semester1+" (3:45-5:15)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][9]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][8]=temp1.semester1+" (3:45-5:15)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][9]="."
                                                            temp2.test_tt[i][8]=temp1.semester1
                                                            temp22.faculty_tt[i][8]=temp1.semester1+" (3:45-5:15)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][9]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][8]=temp1.semester1+" (3:45-5:15)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][9]="."
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                    elif temp1.tutorial:
                        time=0
                        for _ in range(4):
                            for i in range(6):
                                for j in range(8):
                                    if _<=2:
                                        shift=0
                                        for l in range(8):
                                            if temp2.test_tt[i][l]==temp1.semester1:
                                                shift=1
                                                break
                                        if shift==1:break
                                    if j==1 and time<temp1.tutorial:
                                        if temp2.faculty_tt[i][2]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*':
                                            temp2.test_tt[i][2]=temp1.semester1
                                            temp2.faculty_tt[i][2]=temp1.semester1+" (9:00-10:00)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if _<4 and j==3:
                                        if temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][4]=temp1.semester1+" (12:15-1:15)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp2.faculty_tt[i][5]="."
                                            temp2.test_tt[i][4]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if _>=2 and j==4:
                                        if temp2.faculty_tt[i][6]==temp2.faculty_tt[i][7]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][6]=temp1.semester1+" (2:15-3:15)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp2.faculty_tt[i][7]="."
                                            temp2.test_tt[i][6]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if _>=2 and j==5:
                                        if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][8]=temp1.semester1+" (3:45-4:45)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp2.faculty_tt[i][9]="."
                                            temp2.test_tt[i][8]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if _>=2 and j==5:
                                        if temp2.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][9]=temp1.semester1+" (4:30-5:30)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp2.test_tt[i][9]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                    elif temp1.lab:
                        time=0
                        for _ in range(4):
                            for i in range(6):
                                for j in range(8):
                                    if time>=temp1.lab:
                                        break

                                    elif j==1:
                                        if temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]=='*' and time<temp1.lab:
                                            #If there is no activity at that time...
                                            if temp3.sem_tt[i][j]==temp3.sem_tt[i][j+1]==temp4.classroom_tt[i][j]==temp4.classroom_tt[i][j+1]=='*' and (time+120)<=temp1.lab:
                                                if temp2.faculty_tt[i][1]==temp1.semester1:
                                                    break
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp6):
                                                    if temp6.tt[i][1]==temp6.tt[i][2]=='*':
                                                        temp2.faculty_tt[i][1]=temp1.semester1+" (8:30-10:30)"+"_"+temp1.code+"_LAB ("+temp6.name+")"
                                                        temp2.faculty_tt[i][2]=temp2.faculty_tt[i][5]="."
                                                        temp2.test_tt[i][1]=temp1.semester1
                                                        temp3.sem_tt[i][j]=temp1.code
                                                        temp3.sem_tt_new[i][j]=temp1.code+temp6.name
                                                        temp6.tt[i][1]=temp1.semester1+"_"+temp1.code
                                                        temp6.tt[i][2]=temp1.semester1+"_"+temp1.code
                                                        time+=120
                                                        break
                                                    temp6=temp6.next
                                            elif temp3.sem_tt[i][j]!="*" and time+120<=temp1.lab:
                                                if time>=temp1.lab:break
                                                temp5=None
                                                tip=0
                                                if temp1.branch1=="CSE":temp5=obj_for_linked_list_for_traversing_labs.head_for_CSE
                                                if temp1.branch1=="DSAI":temp5=obj_for_linked_list_for_traversing_labs.head_for_DSAI
                                                if temp1.branch1=="ECE":temp5=obj_for_linked_list_for_traversing_labs.head_for_ECE
                                                temp6=None
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp5):
                                                    if temp3.sem_tt[i][j]==temp5.code:
                                                        tip=1
                                                        break
                                                    temp5=temp5.next
                                                while(temp6):
                                                    if temp6.tt[i][1]==temp6.tt[i][2]=='*':
                                                        break
                                                    temp6=temp6.next
                                                if tip==1 and temp5.id!=temp1.id and temp6:
                                                    temp2.faculty_tt[i][1]=temp1.semester1+" (8:30-10:30)"+"_"+temp1.code+"_LAB ("+temp6.name+")"
                                                    temp2.faculty_tt[i][2]="."
                                                    temp2.test_tt[i][1]=temp1.semester1
                                                    temp3.sem_tt[i][j]+=" /" +temp1.code
                                                    temp3.sem_tt_new[i][j]+=" / "+temp1.code+temp6.name
                                                    temp6.tt[i][1]=temp1.semester1+"_"+temp1.code
                                                    temp6.tt[i][2]=temp1.semester1+"_"+temp1.code
                                                    time+=120
                                                    break
                if "CSE_Sem_3_A"==temp1.semester1 or "CSE_Sem_3_B"==temp1.semester1 or "CSE_Sem_4_A"==temp1.semester1 or "CSE_Sem_4_B"==temp1.semester1 or "DSAI_Sem_4"==temp1.semester1:
                    if temp1.theory:
                        time=0
                        for _ in range(5):
                            for i in range(6):
                                for j in range(6):
                                    if _<2:
                                        if i==1 and j==1 and (temp3.sem_tt[1][4]==temp1.code or temp3.sem_tt[1][5]==temp1.code or temp3.sem_tt[2][1]==temp1.code): break
                                        if i==2 and j==1 and (temp3.sem_tt[2][4]==temp1.code or temp3.sem_tt[2][5]==temp1.code or temp3.sem_tt[1][1]==temp1.code or temp3.sem_tt[3][1]==temp1.code): break
                                        if i==3 and j==1 and (temp3.sem_tt[3][4]==temp1.code or temp3.sem_tt[3][5]==temp1.code or temp3.sem_tt[2][1]==temp1.code or temp3.sem_tt[4][1]==temp1.code): break
                                        if i==4 and j==1 and (temp3.sem_tt[4][4]==temp1.code or temp3.sem_tt[4][5]==temp1.code or temp3.sem_tt[3][1]==temp1.code or temp3.sem_tt[5][1]==temp1.code): break
                                        if i==5 and j==1 and (temp3.sem_tt[5][4]==temp1.code or temp3.sem_tt[5][5]==temp1.code or temp3.sem_tt[4][1]==temp1.code ): break
                                        if i==1 and j==4 and (temp3.sem_tt[1][1]==temp1.code or temp3.sem_tt[1][5]==temp1.code or temp3.sem_tt[2][4]==temp1.code): break
                                        if i==2 and j==4 and (temp3.sem_tt[2][1]==temp1.code or temp3.sem_tt[2][5]==temp1.code or temp3.sem_tt[1][4]==temp1.code or temp3.sem_tt[3][4]==temp1.code): break
                                        if i==3 and j==4 and (temp3.sem_tt[3][1]==temp1.code or temp3.sem_tt[3][5]==temp1.code or temp3.sem_tt[2][4]==temp1.code or temp3.sem_tt[4][4]==temp1.code): break
                                        if i==4 and j==4 and (temp3.sem_tt[4][1]==temp1.code or temp3.sem_tt[4][5]==temp1.code or temp3.sem_tt[3][4]==temp1.code or temp3.sem_tt[5][4]==temp1.code): break
                                        if i==5 and j==4 and (temp3.sem_tt[5][1]==temp1.code or temp3.sem_tt[5][5]==temp1.code or temp3.sem_tt[4][4]==temp1.code ): break
                                        if i==1 and j==5 and (temp3.sem_tt[1][1]==temp1.code or temp3.sem_tt[1][4]==temp1.code or temp3.sem_tt[2][5]==temp1.code): break
                                        if i==2 and j==5 and (temp3.sem_tt[2][1]==temp1.code or temp3.sem_tt[2][4]==temp1.code or temp3.sem_tt[1][5]==temp1.code or temp3.sem_tt[3][5]==temp1.code): break
                                        if i==3 and j==5 and (temp3.sem_tt[3][1]==temp1.code or temp3.sem_tt[3][4]==temp1.code or temp3.sem_tt[2][5]==temp1.code or temp3.sem_tt[4][5]==temp1.code): break
                                        if i==4 and j==5 and (temp3.sem_tt[4][1]==temp1.code or temp3.sem_tt[4][4]==temp1.code or temp3.sem_tt[3][5]==temp1.code or temp3.sem_tt[5][5]==temp1.code): break
                                        if i==5 and j==5 and (temp3.sem_tt[5][1]==temp1.code or temp3.sem_tt[5][4]==temp1.code or temp3.sem_tt[4][5]==temp1.code ): break
                                    if _<2:
                                        shift=0
                                        for l in range(8):
                                            if temp2.test_tt[i][l]==temp1.semester1:
                                                shift=1
                                                break
                                        if shift==1:break
                                    if _<5 and j==1 and time<temp1.theory:
                                        if temp2:
                                            if temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][1]==temp22.faculty_tt[i][2]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][1]==temp222.faculty_tt[i][2]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][1]=temp1.semester1+" (9:00-10:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][2]="."
                                                                temp2.test_tt[i][1]=temp1.semester1
                                                                temp22.faculty_tt[i][1]=temp1.semester1+" (9:00-10:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][2]="."
                                                                temp222.faculty_tt[i][1]=temp1.semester1+" (9:00-10:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][2]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code
                                                                temp4.classroom_tt[i][j]=temp1.nam
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][1]=temp1.semester1+" (9:00-10:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][2]="."
                                                            temp2.test_tt[i][1]=temp1.semester1
                                                            temp22.faculty_tt[i][1]=temp1.semester1+" (9:00-10:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][2]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][1]=temp1.semester1+" (9:00-10:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][2]="."
                                                    temp2.test_tt[i][1]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                                    if _<5 and j==4:
                                        if temp2:
                                            if temp2.faculty_tt[i][6]==temp2.faculty_tt[i][7]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][6]==temp22.faculty_tt[i][7]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][6]==temp222.faculty_tt[i][7]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][6]=temp1.semester1+" (2:00-3:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][7]="."
                                                                temp2.test_tt[i][6]=temp1.semester1
                                                                temp22.faculty_tt[i][6]=temp1.semester1+" (2:00-3:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][7]="."
                                                                temp222.faculty_tt[i][6]=temp1.semester1+" (2:00-3:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][7]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][6]=temp1.semester1+" (2:00-3:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][7]="."
                                                            temp2.test_tt[i][6]=temp1.semester1
                                                            temp22.faculty_tt[i][6]=temp1.semester1+" (2:00-3:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][7]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][6]=temp1.semester1+" (2:00-3:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][7]="."
                                                    temp2.test_tt[i][6]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                                    if _<5 and j==5:
                                        if temp2:
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][8]=temp1.semester1+" (3:30-5:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][9]="."
                                                                temp2.test_tt[i][8]=temp1.semester1
                                                                temp22.faculty_tt[i][8]=temp1.semester1+" (3:30-5:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][9]="."
                                                                temp222.faculty_tt[i][8]=temp1.semester1+" (3:30-5:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][9]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][8]=temp1.semester1+" (3:30-5:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][9]="."
                                                            temp2.test_tt[i][8]=temp1.semester1
                                                            temp22.faculty_tt[i][8]=temp1.semester1+" (3:30-5:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][9]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][8]=temp1.semester1+" (3:30-5:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][9]="."
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                    elif temp1.tutorial:
                        time=0
                        for _ in range(4):
                            for i in range(6):
                                for j in range(6):
                                    if _<=2:
                                        shift=0
                                        for l in range(8):
                                            if temp2.test_tt[i][l]==temp1.semester1:
                                                shift=1
                                                break
                                        if shift==1:break
                                    if j==2 and time<temp1.tutorial:
                                        if temp2.faculty_tt[i][3]==temp2.faculty_tt[i][4]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*':
                                            if j-1!=0 and temp2.faculty_tt[i][2]==temp1.semester1:
                                                break
                                            temp2.faculty_tt[i][3]=temp1.semester1+" (11:00-12:00)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp2.faculty_tt[i][4]="."
                                            temp2.test_tt[i][3]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if _<4 and j==3:
                                        if temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][4]=temp1.semester1+" (12:00-1:00)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp2.faculty_tt[i][5]="."
                                            temp2.test_tt[i][4]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if _>=2 and j==5:
                                        if temp2.faculty_tt[i][8]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][8]=temp1.semester1+" (3:30-4:30)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp2.test_tt[i][8]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if _>=3 and j==1:
                                        if temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][1]=temp1.semester1+" (9:00-10:00)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp2.faculty_tt[i][2]="."
                                            temp2.test_tt[i][1]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if _>=3 and j==4:
                                        if temp2.faculty_tt[i][6]==temp2.faculty_tt[i][7]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][6]=temp1.semester1+" (2:00-3:00)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp2.faculty_tt[i][7]="."
                                            temp2.test_tt[i][6]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                    elif temp1.lab:
                        time=0
                        for _ in range(5):
                            for i in range(6):
                                for j in range(8):

                                    if time>=temp1.lab:
                                        break
                                    elif j==2:
                                        if temp2.faculty_tt[i][3]==temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]=='*' and time<temp1.lab:
                                            #If there is no activity at that time...
                                            if temp3.sem_tt[i][j]==temp3.sem_tt[i][j+1]==temp4.classroom_tt[i][j]==temp4.classroom_tt[i][j+1]=='*' and (time+120)<=temp1.lab:
                                                if temp2.faculty_tt[i][1]==temp1.semester1:
                                                    break
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp6):
                                                    if temp6.tt[i][3]==temp6.tt[i][4]==temp6.tt[i][5]=='*':
                                                        temp2.faculty_tt[i][3]=temp1.semester1+" (11:00-1:00)"+"_"+temp1.code+"_LAB ("+temp6.name+")"
                                                        temp2.faculty_tt[i][4]=temp2.faculty_tt[i][5]="."
                                                        temp2.test_tt[i][3]=temp1.semester1
                                                        temp3.sem_tt[i][j]=temp1.code
                                                        temp3.sem_tt[i][j+1]=temp1.code
                                                        temp3.sem_tt_new[i][j]=temp1.code+temp6.name
                                                        temp3.sem_tt_new[i][j+1]=temp1.code+temp6.name

                                                        temp6.tt[i][3]=temp1.semester1+"_"+temp1.code
                                                        temp6.tt[i][4]=temp1.semester1+"_"+temp1.code
                                                        temp6.tt[i][5]=temp1.semester1+"_"+temp1.code
                                                        time+=120
                                                        break
                                                    temp6=temp6.next
                                            elif temp3.sem_tt[i][j]==temp3.sem_tt[i][j+1] and time+120<=temp1.lab:
                                                if time>=temp1.lab:break
                                                temp5=None
                                                tip=0
                                                if temp1.branch1=="CSE":temp5=obj_for_linked_list_for_traversing_labs.head_for_CSE
                                                if temp1.branch1=="DSAI":temp5=obj_for_linked_list_for_traversing_labs.head_for_DSAI
                                                if temp1.branch1=="ECE":temp5=obj_for_linked_list_for_traversing_labs.head_for_ECE
                                                temp6=None
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp5):
                                                    if temp3.sem_tt[i][j]==temp5.code:
                                                        tip=1
                                                        break
                                                    temp5=temp5.next
                                                while(temp6):
                                                    if temp6.tt[i][3]==temp6.tt[i][4]==temp6.tt[i][5]=='*':
                                                        break
                                                    temp6=temp6.next
                                                if tip==1 and temp5.id!=temp1.id and temp6:
                                                    temp2.faculty_tt[i][3]=temp1.semester1+" (11:00-1:00)"+"_"+temp1.code+"_LAB ("+temp6.name+")"
                                                    temp2.faculty_tt[i][4]="."
                                                    temp2.faculty_tt[i][5]="."
                                                    temp2.test_tt[i][3]=temp1.semester1
                                                    temp3.sem_tt[i][j]+=" /" +temp1.code
                                                    temp3.sem_tt[i][j+1]+=" / "+temp1.code
                                                    temp3.sem_tt_new[i][j]+=" / "+temp1.code+temp6.name
                                                    temp3.sem_tt_new[i][j+1]+=" / "+temp1.code+temp6.name

                                                    temp6.tt[i][3]=temp1.semester1+"_"+temp1.code
                                                    temp6.tt[i][4]=temp1.semester1+"_"+temp1.code
                                                    temp6.tt[i][5]=temp1.semester1+"_"+temp1.code
                                                    time+=120
                                                    break
                                    if _>3 and j==5:
                                        if temp2.faculty_tt[i][7]==temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.lab:
                                            if temp1.lab_name=='CS_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                            if temp1.lab_name=='EC_LAB':temp5=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                            while(temp5):
                                                if temp5.tt[i][7]==temp5.tt[i][8]==temp5.tt[i][9]=='*' and time<temp1.lab:
                                                    temp5.tt[i][7]=temp5.tt[i][8]=temp5.tt[i][9]=temp1.semester1+"_"+temp1.code
                                                    temp2.faculty_tt[i][7]=temp1.semester1+" (3:15-5:15)"+"_"+temp1.code+"_LAB ("+temp5.name+")"
                                                    temp2.faculty_tt[i][8]=temp2.faculty_tt[i][9]="."
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code+temp5.name

                                                    time+=120
                                                    break
                                                temp5=temp5.next
                if "CSE_Sem_5_A"==temp1.semester1 or "CSE_Sem_5_B"==temp1.semester1 or "CSE_Sem_6_A"==temp1.semester1 or "CSE_Sem_6_B"==temp1.semester1 or "DSAI_Sem_5"==temp1.semester1 or "DSAI_Sem_6"==temp1.semester1 or "ECE_Sem_5"==temp1.semester1 or "ECE_Sem_6"==temp1.semester1 :
                    if temp1.theory:
                        time=0
                        for _ in range(5):
                            for i in range(6):
                                for j in range(8):
                                    if _<3:
                                        if i==1 and j==1 and (temp3.sem_tt[1][2]==temp1.code or temp3.sem_tt[1][3]==temp1.code or temp3.sem_tt[2][1]==temp1.code): break
                                        if i==2 and j==1 and (temp3.sem_tt[2][2]==temp1.code or temp3.sem_tt[2][3]==temp1.code or temp3.sem_tt[1][1]==temp1.code or temp3.sem_tt[3][1]==temp1.code): break
                                        if i==3 and j==1 and (temp3.sem_tt[3][2]==temp1.code or temp3.sem_tt[3][3]==temp1.code or temp3.sem_tt[2][1]==temp1.code or temp3.sem_tt[4][1]==temp1.code): break
                                        if i==4 and j==1 and (temp3.sem_tt[4][2]==temp1.code or temp3.sem_tt[4][3]==temp1.code or temp3.sem_tt[3][1]==temp1.code or temp3.sem_tt[5][1]==temp1.code): break
                                        if i==5 and j==1 and (temp3.sem_tt[5][2]==temp1.code or temp3.sem_tt[5][3]==temp1.code or temp3.sem_tt[4][1]==temp1.code ): break
                                        if i==1 and j==2 and (temp3.sem_tt[1][1]==temp1.code or temp3.sem_tt[1][3]==temp1.code or temp3.sem_tt[2][2]==temp1.code): break
                                        if i==2 and j==2 and (temp3.sem_tt[2][1]==temp1.code or temp3.sem_tt[2][3]==temp1.code or temp3.sem_tt[1][2]==temp1.code or temp3.sem_tt[3][2]==temp1.code): break
                                        if i==3 and j==2 and (temp3.sem_tt[3][1]==temp1.code or temp3.sem_tt[3][3]==temp1.code or temp3.sem_tt[2][2]==temp1.code or temp3.sem_tt[4][2]==temp1.code): break
                                        if i==4 and j==2 and (temp3.sem_tt[4][1]==temp1.code or temp3.sem_tt[4][3]==temp1.code or temp3.sem_tt[3][2]==temp1.code or temp3.sem_tt[5][2]==temp1.code): break
                                        if i==5 and j==2 and (temp3.sem_tt[5][1]==temp1.code or temp3.sem_tt[5][3]==temp1.code or temp3.sem_tt[4][2]==temp1.code ): break
                                        if i==1 and j==3 and (temp3.sem_tt[1][1]==temp1.code or temp3.sem_tt[1][2]==temp1.code or temp3.sem_tt[2][3]==temp1.code): break
                                        if i==2 and j==3 and (temp3.sem_tt[2][1]==temp1.code or temp3.sem_tt[2][2]==temp1.code or temp3.sem_tt[1][3]==temp1.code or temp3.sem_tt[3][3]==temp1.code): break
                                        if i==3 and j==3 and (temp3.sem_tt[3][1]==temp1.code or temp3.sem_tt[3][2]==temp1.code or temp3.sem_tt[2][3]==temp1.code or temp3.sem_tt[4][3]==temp1.code): break
                                        if i==4 and j==3 and (temp3.sem_tt[4][1]==temp1.code or temp3.sem_tt[4][2]==temp1.code or temp3.sem_tt[3][3]==temp1.code or temp3.sem_tt[5][3]==temp1.code): break
                                        if i==5 and j==3 and (temp3.sem_tt[5][1]==temp1.code or temp3.sem_tt[5][2]==temp1.code or temp3.sem_tt[4][3]==temp1.code ): break
                                    if _<=2:
                                        shift=0
                                        for l in range(8):
                                            if temp2.test_tt[i][l]==temp1.semester1:
                                                shift=1
                                                break
                                        if shift==1:break
                                    if _<4 and j==1 and time<temp1.theory:
                                        if temp2:
                                            if temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][1]==temp22.faculty_tt[i][2]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][1]==temp222.faculty_tt[i][2]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][1]=temp1.semester1+" (8:30-10:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][2]="."
                                                                temp2.test_tt[i][1]=temp1.semester1
                                                                temp22.faculty_tt[i][1]=temp1.semester1+" (8:30-10:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][2]="."
                                                                temp222.faculty_tt[i][1]=temp1.semester1+" (8:30-10:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][2]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][1]=temp1.semester1+" (8:30-10:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][2]="."
                                                            temp2.test_tt[i][1]=temp1.semester1
                                                            temp22.faculty_tt[i][1]=temp1.semester1+" (8:30-10:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][2]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][1]=temp1.semester1+" (8:30-10:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][2]="."
                                                    temp2.test_tt[i][1]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                                    if _<4 and j==2:
                                        if temp2:
                                            if temp2.faculty_tt[i][3]==temp2.faculty_tt[i][4]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][3]==temp22.faculty_tt[i][4]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][3]==temp222.faculty_tt[i][4]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][3]=temp1.semester1+" (10:30-12:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][4]="."
                                                                temp2.test_tt[i][3]=temp1.semester1
                                                                temp22.faculty_tt[i][3]=temp1.semester1+" (10:30-12:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][4]="."
                                                                temp222.faculty_tt[i][3]=temp1.semester1+" (10:30-12:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][4]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][3]=temp1.semester1+" (10:30-12:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][4]="."
                                                            temp2.test_tt[i][3]=temp1.semester1
                                                            temp22.faculty_tt[i][3]=temp1.semester1+" (10:30-12:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][4]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][3]=temp1.semester1+" (10:30-12:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][4]="."
                                                    temp2.test_tt[i][3]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                                    if _<4 and j==3:
                                        if temp2:
                                            if temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][4]==temp22.faculty_tt[i][5]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][4]==temp222.faculty_tt[i][5]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][4]=temp1.semester1+" (12:00-1:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][5]="."
                                                                temp2.test_tt[i][4]=temp1.semester1
                                                                temp22.faculty_tt[i][4]=temp1.semester1+" (12:00-1:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][5]="."
                                                                temp222.faculty_tt[i][4]=temp1.semester1+" (12:00-1:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][5]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][4]=temp1.semester1+" (12:00-1:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][5]="."
                                                            temp2.test_tt[i][4]=temp1.semester1
                                                            temp22.faculty_tt[i][4]=temp1.semester1+" (12:00-1:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][5]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][4]=temp1.semester1+" (12:00-1:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][5]="."
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                                    if _<4 and j==4:
                                        if temp2:
                                            if temp2.faculty_tt[i][7]==temp2.faculty_tt[i][8]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][7]==temp22.faculty_tt[i][8]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][7]==temp222.faculty_tt[i][8]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][7]=temp1.semester1+" (2:30-4:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][8]="."
                                                                temp2.test_tt[i][7]=temp1.semester1
                                                                temp22.faculty_tt[i][7]=temp1.semester1+" (2:30-4:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][8]="."
                                                                temp222.faculty_tt[i][7]=temp1.semester1+" (2:30-4:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][8]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code+" (2:30-4:00)"
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][7]=temp1.semester1+" (2:30-4:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][8]="."
                                                            temp2.test_tt[i][7]=temp1.semester1
                                                            temp22.faculty_tt[i][7]=temp1.semester1+" (2:30-4:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][8]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code+" (2:30-4:00)"
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][7]=temp1.semester1+" (2:30-4:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][8]="."
                                                    temp2.test_tt[i][7]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code+" (2:30-4:00)"
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                                    if _<4 and j==5:
                                        if temp2:
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][8]=temp1.semester1+" (4:00-5:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][9]="."
                                                                temp2.test_tt[i][8]=temp1.semester1
                                                                temp22.faculty_tt[i][8]=temp1.semester1+" (4:00-5:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][9]="."
                                                                temp222.faculty_tt[i][8]=temp1.semester1+" (4:00-5:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][9]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code+" (4:00-5:30)"
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][8]=temp1.semester1+" (4:00-5:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][9]="."
                                                            temp2.test_tt[i][8]=temp1.semester1
                                                            temp22.faculty_tt[i][8]=temp1.semester1+" (4:00-5:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][9]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code+" (4:00-5:30)"
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][8]=temp1.semester1+" (4:00-5:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][9]="."
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code+" (4:00-5:30)"
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                    elif temp1.tutorial:
                        time=0
                        for _ in range(4):
                            for i in range(6):
                                for j in range(8):
                                    if _<=2:
                                        shift=0
                                        for l in range(8):
                                            if temp2.test_tt[i][l]==temp1.semester1:
                                                shift=1
                                                break
                                        if shift==1:break
                                    if j==3 and time<temp1.tutorial:
                                        if temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*':
                                            if j-1!=0 and temp2.faculty_tt[i][2]==temp1.semester1:
                                                break
                                            temp2.faculty_tt[i][4]=temp1.semester1+" (12:00-1:00)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp2.faculty_tt[i][5]="."
                                            temp2.test_tt[i][4]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code+" (12:00-1:00)"
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if j==3 and time<temp1.tutorial:
                                        if temp2.faculty_tt[i][5]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*':
                                            if j-1!=0 and temp2.faculty_tt[i][2]==temp1.semester1:break
                                            temp2.faculty_tt[i][5]=temp1.semester1+" (12:30-1:30)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp2.test_tt[i][5]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code+" (12:30-1:30)"
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if _<4 and j==4:
                                        if temp2.faculty_tt[i][7]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][7]=temp1.semester1+" (2:30-3:30)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp2.test_tt[i][7]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if _>=2 and j==5:
                                        if temp2.faculty_tt[i][8]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][8]=temp1.semester1+" (3:30-4:30)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp2.test_tt[i][8]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                    elif temp1.lab:
                        time=0
                        for _ in range(4):
                            for i in range(6):
                                for j in range(8):

                                    if time>=temp1.lab:break
                                    elif j==4:
                                        if temp2.faculty_tt[i][7]==temp2.faculty_tt[i][8]=='*' and time<temp1.lab:
                                            #If there is no activity at that time...
                                            if temp3.sem_tt[i][j]==temp3.sem_tt[i][j+1]==temp4.classroom_tt[i][j]==temp4.classroom_tt[i][j+1]=='*' and (time+120)<=temp1.lab:
                                                if temp2.faculty_tt[i][1]==temp1.semester1:break
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp6):
                                                    if temp6.tt[i][7]==temp6.tt[i][8]=='*':
                                                        temp2.faculty_tt[i][7]=temp1.semester1+" (2:30-4:30)"+"_"+temp1.code+"_LAB ("+temp6.name+")"
                                                        temp2.faculty_tt[i][8]="."
                                                        temp2.test_tt[i][7]=temp1.semester1
                                                        temp3.sem_tt[i][j]=temp1.code
                                                        temp3.sem_tt[i][j+1]=temp1.code
                                                        temp3.sem_tt_new[i][j]=temp1.code+temp6.name
                                                        temp3.sem_tt_new[i][j+1]=temp1.code+temp6.name

                                                        temp6.tt[i][7]=temp1.semester1+"_"+temp1.code
                                                        temp6.tt[i][8]=temp1.semester1+"_"+temp1.code
                                                        time+=120
                                                        break
                                                    temp6=temp6.next
                                            elif temp3.sem_tt[i][j]==temp3.sem_tt[i][j+1] and time+120<=temp1.lab:
                                                if time>=temp1.lab:break
                                                temp5=None
                                                tip=0
                                                if temp1.branch1=="CSE":temp5=obj_for_linked_list_for_traversing_labs.head_for_CSE
                                                if temp1.branch1=="DSAI":temp5=obj_for_linked_list_for_traversing_labs.head_for_DSAI
                                                if temp1.branch1=="ECE":temp5=obj_for_linked_list_for_traversing_labs.head_for_ECE
                                                temp6=None
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp5):
                                                    if temp3.sem_tt[i][j]==temp5.code:
                                                        tip=1
                                                        break
                                                    temp5=temp5.next
                                                while(temp6):
                                                    if temp6.tt[i][7]==temp6.tt[i][8]=='*':break
                                                    temp6=temp6.next
                                                if tip==1 and temp5.id!=temp1.id and temp6:
                                                    temp2.faculty_tt[i][7]=temp1.semester1+" (2:30-4:30)"+"_"+temp1.code+"_LAB ("+temp6.name+")"
                                                    temp2.faculty_tt[i][8]="."
                                                    temp2.test_tt[i][7]=temp1.semester1
                                                    temp3.sem_tt[i][j]+=" /" +temp1.code
                                                    temp3.sem_tt[i][j+1]+=" / "+temp1.code
                                                    temp3.sem_tt_new[i][j]+=" / "+temp1.code+temp6.name
                                                    temp3.sem_tt_new[i][j+1]+=" / "+temp1.code+temp6.name

                                                    temp6.tt[i][7]=temp1.semester1+"_"+temp1.code
                                                    temp6.tt[i][8]=temp1.semester1+"_"+temp1.code
                                                    time+=120
                                                    break
                if "CSE_Sem_7"==temp1.semester1 or "ECE_Sem_7"==temp1.semester1 or "DSAI_Sem_7"==temp1.semester1 :
                    if temp1.theory:
                        time=0
                        for _ in range(4):
                            for i in range(6):
                                for j in range(8):
                                    if _<2:
                                        if i==1 and j==1 and (temp3.sem_tt[1][2]==temp1.code or temp3.sem_tt[1][3]==temp1.code or temp3.sem_tt[1][6]==temp1.code or temp3.sem_tt[2][1]==temp1.code): break
                                        if i==2 and j==1 and (temp3.sem_tt[2][2]==temp1.code or temp3.sem_tt[2][3]==temp1.code or temp3.sem_tt[2][6]==temp1.code or temp3.sem_tt[1][1]==temp1.code or temp3.sem_tt[3][1]==temp1.code): break
                                        if i==3 and j==1 and (temp3.sem_tt[3][2]==temp1.code or temp3.sem_tt[3][3]==temp1.code or temp3.sem_tt[3][6]==temp1.code or temp3.sem_tt[2][1]==temp1.code or temp3.sem_tt[4][1]==temp1.code): break
                                        if i==4 and j==1 and (temp3.sem_tt[4][2]==temp1.code or temp3.sem_tt[4][3]==temp1.code or temp3.sem_tt[4][6]==temp1.code or temp3.sem_tt[3][1]==temp1.code or temp3.sem_tt[5][1]==temp1.code): break
                                        if i==5 and j==1 and (temp3.sem_tt[5][2]==temp1.code or temp3.sem_tt[5][3]==temp1.code or temp3.sem_tt[5][6]==temp1.code or temp3.sem_tt[4][1]==temp1.code ): break
                                        if i==1 and j==2 and (temp3.sem_tt[1][1]==temp1.code or temp3.sem_tt[1][3]==temp1.code or temp3.sem_tt[1][6]==temp1.code or temp3.sem_tt[2][2]==temp1.code ): break
                                        if i==2 and j==2 and (temp3.sem_tt[2][1]==temp1.code or temp3.sem_tt[2][3]==temp1.code or temp3.sem_tt[2][6]==temp1.code or temp3.sem_tt[1][2]==temp1.code or temp3.sem_tt[3][2]==temp1.code ): break
                                        if i==3 and j==2 and (temp3.sem_tt[3][1]==temp1.code or temp3.sem_tt[3][3]==temp1.code or temp3.sem_tt[3][6]==temp1.code or temp3.sem_tt[2][2]==temp1.code or temp3.sem_tt[4][2]==temp1.code ): break
                                        if i==4 and j==2 and (temp3.sem_tt[4][1]==temp1.code or temp3.sem_tt[4][3]==temp1.code or temp3.sem_tt[4][6]==temp1.code or temp3.sem_tt[3][2]==temp1.code or temp3.sem_tt[5][2]==temp1.code ): break
                                        if i==5 and j==2 and (temp3.sem_tt[5][1]==temp1.code or temp3.sem_tt[5][3]==temp1.code or temp3.sem_tt[5][6]==temp1.code or temp3.sem_tt[4][2]==temp1.code ): break
                                        if i==1 and j==3 and (temp3.sem_tt[1][1]==temp1.code or temp3.sem_tt[1][2]==temp1.code or temp3.sem_tt[1][6]==temp1.code or temp3.sem_tt[2][3]==temp1.code ): break
                                        if i==2 and j==3 and (temp3.sem_tt[2][1]==temp1.code or temp3.sem_tt[2][2]==temp1.code or temp3.sem_tt[2][6]==temp1.code or temp3.sem_tt[1][3]==temp1.code or temp3.sem_tt[3][3]==temp1.code ): break
                                        if i==3 and j==3 and (temp3.sem_tt[3][1]==temp1.code or temp3.sem_tt[3][2]==temp1.code or temp3.sem_tt[3][6]==temp1.code or temp3.sem_tt[2][3]==temp1.code or temp3.sem_tt[4][3]==temp1.code ): break
                                        if i==4 and j==3 and (temp3.sem_tt[4][1]==temp1.code or temp3.sem_tt[4][2]==temp1.code or temp3.sem_tt[4][6]==temp1.code or temp3.sem_tt[3][3]==temp1.code or temp3.sem_tt[5][3]==temp1.code ): break
                                        if i==5 and j==3 and (temp3.sem_tt[5][1]==temp1.code or temp3.sem_tt[5][2]==temp1.code or temp3.sem_tt[5][6]==temp1.code or temp3.sem_tt[4][3]==temp1.code ): break
                                        if i==1 and j==6 and (temp3.sem_tt[1][1]==temp1.code or temp3.sem_tt[1][2]==temp1.code or temp3.sem_tt[1][3]==temp1.code or temp3.sem_tt[2][6]==temp1.code ): break
                                        if i==2 and j==6 and (temp3.sem_tt[2][1]==temp1.code or temp3.sem_tt[2][2]==temp1.code or temp3.sem_tt[2][3]==temp1.code or temp3.sem_tt[1][6]==temp1.code or temp3.sem_tt[3][6]==temp1.code ): break
                                        if i==3 and j==6 and (temp3.sem_tt[3][1]==temp1.code or temp3.sem_tt[3][2]==temp1.code or temp3.sem_tt[3][3]==temp1.code or temp3.sem_tt[2][6]==temp1.code or temp3.sem_tt[4][6]==temp1.code ): break
                                        if i==4 and j==6 and (temp3.sem_tt[4][1]==temp1.code or temp3.sem_tt[4][2]==temp1.code or temp3.sem_tt[4][3]==temp1.code or temp3.sem_tt[3][6]==temp1.code or temp3.sem_tt[5][6]==temp1.code ): break
                                        if i==5 and j==6 and (temp3.sem_tt[5][1]==temp1.code or temp3.sem_tt[5][2]==temp1.code or temp3.sem_tt[5][3]==temp1.code or temp3.sem_tt[4][6]==temp1.code ): break
                                    if _<=2:
                                        shift=0
                                        for l in range(8):
                                            if temp2.test_tt[i][l]==temp1.semester1:
                                                shift=1
                                                break
                                        if shift==1:break
                                    if _<4 and j==1 and time<temp1.theory:
                                        if temp2:
                                            if temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][1]==temp22.faculty_tt[i][2]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][1]==temp222.faculty_tt[i][2]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][1]=temp1.semester1+" (8:30-10:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][2]="."
                                                                temp2.test_tt[i][1]=temp1.semester1
                                                                temp22.faculty_tt[i][1]=temp1.semester1+" (8:30-10:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][2]="."
                                                                temp222.faculty_tt[i][1]=temp1.semester1+" (8:30-10:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][2]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][1]=temp1.semester1+" (8:30-10:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][2]="."
                                                            temp2.test_tt[i][1]=temp1.semester1
                                                            temp22.faculty_tt[i][1]=temp1.semester1+" (8:30-10:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][2]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][1]=temp1.semester1+" (8:30-10:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][2]="."
                                                    temp2.test_tt[i][1]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                                    if _<4 and j==2:
                                        if temp2:
                                            if temp2.faculty_tt[i][2]==temp2.faculty_tt[i][3]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][2]==temp22.faculty_tt[i][3]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][2]==temp222.faculty_tt[i][3]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][2]=temp1.semester1+" (10:00-11:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][3]="."
                                                                temp2.test_tt[i][2]=temp1.semester1
                                                                temp22.faculty_tt[i][2]=temp1.semester1+" (10:00-11:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][3]="."
                                                                temp222.faculty_tt[i][2]=temp1.semester1+" (10:00-11:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][3]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][2]=temp1.semester1+" (10:00-11:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][3]="."
                                                            temp2.test_tt[i][2]=temp1.semester1
                                                            temp22.faculty_tt[i][2]=temp1.semester1+" (10:00-11:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][3]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][2]=temp1.semester1+" (10:00-11:30)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][3]="."
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                                    if _<4 and j==3:
                                        if temp2:
                                            if temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][4]==temp22.faculty_tt[i][5]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][4]==temp222.faculty_tt[i][5]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][4]=temp1.semester1+" (11:30-1:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][5]="."
                                                                temp2.test_tt[i][4]=temp1.semester1
                                                                temp22.faculty_tt[i][4]=temp1.semester1+" (11:30-1:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][5]="."
                                                                temp222.faculty_tt[i][4]=temp1.semester1+" (11:30-1:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][5]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][4]=temp1.semester1+" (11:30-1:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][5]="."
                                                            temp2.test_tt[i][4]=temp1.semester1
                                                            temp22.faculty_tt[i][4]=temp1.semester1+" (11:30-1:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][5]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][4]=temp1.semester1+" (11:30-1:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][5]="."
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                                    if _<4 and j==6:
                                        if temp2:
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                if temp22:
                                                    if temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                        if temp222:
                                                            if temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.theory:
                                                                temp2.faculty_tt[i][8]=temp1.semester1+" (3:30-5:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp2.faculty_tt[i][9]="."
                                                                temp2.test_tt[i][8]=temp1.semester1
                                                                temp22.faculty_tt[i][8]=temp1.semester1+" (3:30-5:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp22.faculty_tt[i][9]="."
                                                                temp222.faculty_tt[i][8]=temp1.semester1+" (3:30-5:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                                temp222.faculty_tt[i][9]="."
                                                                temp3.sem_tt[i][j]=temp1.code
                                                                temp3.sem_tt_new[i][j]=temp1.code
                                                                temp4.classroom_tt[i][j]=temp1.name
                                                                time+=90
                                                                break
                                                        else:
                                                            temp2.faculty_tt[i][8]=temp1.semester1+" (3:30-5:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp2.faculty_tt[i][9]="."
                                                            temp2.test_tt[i][8]=temp1.semester1
                                                            temp22.faculty_tt[i][8]=temp1.semester1+" (3:30-5:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                            temp22.faculty_tt[i][9]="."
                                                            temp3.sem_tt[i][j]=temp1.code
                                                            temp3.sem_tt_new[i][j]=temp1.code
                                                            temp4.classroom_tt[i][j]=temp1.name
                                                            time+=90
                                                            break
                                                else:
                                                    temp2.faculty_tt[i][8]=temp1.semester1+" (3:30-5:00)"+"_"+temp1.code+" ("+temp4.classroom_code+")"
                                                    temp2.faculty_tt[i][9]="."
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    temp3.sem_tt[i][j]=temp1.code
                                                    temp3.sem_tt_new[i][j]=temp1.code
                                                    temp4.classroom_tt[i][j]=temp1.name
                                                    time+=90
                                                    break
                    elif temp1.tutorial:
                        time=0
                        for _ in range(4):
                            for i in range(6):
                                for j in range(8):
                                    if _<=2:
                                        shift=0
                                        for l in range(8):
                                            if temp2.test_tt[i][l]==temp1.semester1:
                                                shift=1
                                                break
                                        if shift==1:break
                                    if j==4 and time<temp1.tutorial:
                                        if temp2.faculty_tt[i][6]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*':
                                            if j-1!=0 and temp2.faculty_tt[i][2]==temp1.semester1: break
                                            temp2.faculty_tt[i][6]=temp1.semester1+" (1:30-2:30)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp2.test_tt[i][6]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if _<4 and j==5:
                                        if temp2.faculty_tt[i][7]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][7]=temp1.semester1+" (2:30-3:30)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp2.test_tt[i][7]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if _<4 and j==6:
                                        if temp2.faculty_tt[i][8]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][8]=temp1.semester1+" (3:30-4:30)"+"_TUT "+temp1.code+" ("+temp4.classroom_code+")"
                                            temp2.test_tt[i][8]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code+" (3:30-4:30)"
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                                    if _<4 and j==6:
                                        if temp2.faculty_tt[i][9]==temp3.sem_tt[i][j]==temp4.classroom_tt[i][j]=='*' and time<temp1.tutorial:
                                            temp2.faculty_tt[i][9]=temp1.semester1+"_TUT (4:30-5:30)"
                                            temp2.test_tt[i][9]=temp1.semester1
                                            temp3.sem_tt[i][j]=temp1.code
                                            temp3.sem_tt_new[i][j]=temp1.code+" (4:30-5:30)"
                                            temp4.classroom_tt[i][j]=temp1.name
                                            time+=60
                                            break
                    elif temp1.lab:
                        time=0
                        for _ in range(4):
                            for i in range(6):
                                for j in range(8):
                                    if time>=temp1.lab:
                                        break

                                    elif j==4:
                                        if temp2.faculty_tt[i][6]==temp2.faculty_tt[i][7]=='*' and time<temp1.lab:
                                            #If there is no activity at that time...
                                            if temp3.sem_tt[i][j]==temp3.sem_tt[i][j+1]==temp4.classroom_tt[i][j]==temp4.classroom_tt[i][j+1]=='*' and (time+120)<=temp1.lab:
                                                if temp2.faculty_tt[i][1]==temp1.semester1:break
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp6):
                                                    if temp6.tt[i][6]==temp6.tt[i][7]=='*':
                                                        temp2.faculty_tt[i][6]=temp1.semester1+" (1:30-3:30)"+"_"+temp1.code+"_LAB ("+temp6.name+")"
                                                        temp2.faculty_tt[i][7]="."
                                                        temp2.test_tt[i][6]=temp1.semester1
                                                        temp3.sem_tt[i][j]=temp1.code
                                                        temp3.sem_tt[i][j+1]=temp1.code
                                                        temp3.sem_tt_new[i][j]=temp1.code+temp6.name
                                                        temp3.sem_tt_new[i][j+1]=temp1.code+temp6.name

                                                        temp6.tt[i][6]=temp1.semester1+"_"+temp1.code
                                                        temp6.tt[i][7]=temp1.semester1+"_"+temp1.code
                                                        time+=120
                                                        break
                                                    temp6=temp6.next
                                            elif temp3.sem_tt[i][j]==temp3.sem_tt[i][j+1] and time+120<=temp1.lab:
                                                if time>=temp1.lab:break
                                                temp5=None
                                                tip=0
                                                if temp1.branch1=="CSE":temp5=obj_for_linked_list_for_traversing_labs.head_for_CSE
                                                if temp1.branch1=="DSAI":temp5=obj_for_linked_list_for_traversing_labs.head_for_DSAI
                                                if temp1.branch1=="ECE":temp5=obj_for_linked_list_for_traversing_labs.head_for_ECE
                                                temp6=None
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp5):
                                                    if temp3.sem_tt[i][j]==temp5.code:
                                                        tip=1
                                                        break
                                                    temp5=temp5.next
                                                while(temp6):
                                                    if temp6.tt[i][6]==temp6.tt[i][7]=='*':
                                                        break
                                                    temp6=temp6.next
                                                if tip==1 and temp5.id!=temp1.id and temp6:
                                                    temp2.faculty_tt[i][6]=temp1.semester1+" (1:30-3:30)"+"_"+temp1.code+"_LAB ("+temp6.name+")"
                                                    temp2.faculty_tt[i][7]="."
                                                    temp2.test_tt[i][6]=temp1.semester1
                                                    temp3.sem_tt[i][j]+=" /" +temp1.code
                                                    temp3.sem_tt[i][j+1]+=" / "+temp1.code
                                                    temp3.sem_tt_new[i][j]+=" / "+temp1.code+temp6.name
                                                    temp3.sem_tt_new[i][j+1]+=" / "+temp1.code+temp6.name

                                                    temp6.tt[i][6]=temp1.semester1+"_"+temp1.code
                                                    temp6.tt[i][7]=temp1.semester1+"_"+temp1.code
                                                    time+=120
                                                    break
                if temp1.theory:
                    if time<temp1.theory:
                        print("theory not satisfied for ",temp1.name,"Semester: ",temp1.semester1,"time=",time)
                if temp1.tutorial:
                    if time<temp1.tutorial:
                        print("tutorial not satisfied for ",temp1.name,"Semester: ",temp1.semester1)
                if temp1.lab:
                    if time<temp1.lab:
                        print("lab not satisfied for ",temp1.name,"Semester: ",temp1.semester1)
                temp1=temp1.next
            temp_for_faculty=temp_for_faculty.next
def plotting_for_electives(openion=0):
    for k in range(6):
        if k==0:temp1=obj_for_linked_list_for_electives.head_for_lab
        if k==1:temp1=obj_for_linked_list_for_electives.head_for_theory
        if k==2:temp1=obj_for_linked_list_for_electives.head_for_tutorial
        if k==3:temp1=obj_for_linked_list_for_electives.head_for_lab
        if k==4:temp1=obj_for_linked_list_for_electives.head_for_theory
        if k==5:temp1=obj_for_linked_list_for_electives.head_for_tutorial
        while(temp1):
            if openion==1:
                if not(temp1.semester1=="CSE_Sem_3_A"):
                    temp1=temp1.next
                    continue
                print(temp1.semester1)
            if openion==0:
                if k==0 or k==1 or k==2:
                    if temp1.semester1=="CSE_Sem_5_A" or temp1.semester1=="ECE_Sem_5":
                        temp1=temp1.next
                        continue
                    print("openion : ",temp1.semester1)
                if k==3 or k==4 or k==5:
                    if temp1.semester1=="CSE_Sem_7" or temp1.semester1=="DSAI_Sem_7" or temp1.semester1=="ECE_Sem_7" or temp1.semester1=="CSE_Sem_3_A" :
                        temp1=temp1.next
                        continue
                    print("openion ",temp1.semester1)
            temp2=obj_for_facultys.head_for_faculty_names
            while temp2:
                if temp1.faculty1==temp2.faculty_name:
                    break
                temp2=temp2.next
            if temp1.faculty1=="NA":temp2=None
            temp22=obj_for_facultys.head_for_faculty_names
            while(temp22):
                if temp1.faculty2==temp22.faculty_name:
                    break
                temp22=temp22.next
            if temp1.faculty2=="NA":temp22=None
            temp222=obj_for_facultys.head_for_faculty_names
            while(temp222):
                if temp1.faculty3==temp222.faculty_name:
                    break
                temp222=temp222.next
            if temp1.faculty3=="NA":temp222=None
            temp4=obj_for_sem.head_for_semesters
            while(temp4):
                if temp4.sem==temp1.semester1:
                    break
                temp4=temp4.next
            if temp1.semester1=="NA":temp4=None
            temp44=obj_for_sem.head_for_semesters
            while(temp44):
                if temp44.sem==temp1.semester2:
                    break
                temp44=temp44.next
            if temp1.semester2=="NA":temp44=None
            temp444=obj_for_sem.head_for_semesters
            while(temp444):
                if temp444.sem==temp1.semester3:
                    break
                temp444=temp444.next
            if temp1.semester3=="NA":temp444=None
            temp5=obj_for_class_rooms.head_for_class_rooms
            while(temp5):
                if temp1.semester1==temp5.name:
                    break
                temp5=temp5.next
            temp55=obj_for_class_rooms.head_for_class_rooms
            while(temp55):
                if temp1.semester1==temp55.name:
                    break
                temp55=temp55.next
            temp555=obj_for_class_rooms.head_for_class_rooms
            while(temp555):
                if temp1.semester1==temp555.name:
                    break
                temp555=temp555.next
            if temp1.semester1=="CSE_Sem_7" or temp1.semester1=="DSAI_Sem_7" or temp1.semester1=="ECE_Sem_7":
                if temp1.theory:
                    time1,time2,time3=0,0,0
                    for _ in range(6):
                        for i in range(6):
                            for j in range(8):
                                if _<=2:
                                        shift=0
                                        for l in range(8):
                                            if temp2.test_tt[i][l]==temp1.semester1:
                                                shift=1
                                                break
                                        if shift==1:break
                                if _<4:
                                    if i==1 and j==1 and (temp4.sem_tt[1][2]==temp1.code or temp4.sem_tt[1][3]==temp1.code or temp4.sem_tt[1][6]==temp1.code or temp4.sem_tt[2][1]==temp1.code): break
                                    if i==2 and j==1 and (temp4.sem_tt[2][2]==temp1.code or temp4.sem_tt[2][3]==temp1.code or temp4.sem_tt[2][6]==temp1.code or temp4.sem_tt[1][1]==temp1.code or temp4.sem_tt[3][1]==temp1.code): break
                                    if i==3 and j==1 and (temp4.sem_tt[3][2]==temp1.code or temp4.sem_tt[3][3]==temp1.code or temp4.sem_tt[3][6]==temp1.code or temp4.sem_tt[2][1]==temp1.code or temp4.sem_tt[4][1]==temp1.code): break
                                    if i==4 and j==1 and (temp4.sem_tt[4][2]==temp1.code or temp4.sem_tt[4][3]==temp1.code or temp4.sem_tt[4][6]==temp1.code or temp4.sem_tt[3][1]==temp1.code or temp4.sem_tt[5][1]==temp1.code): break
                                    if i==5 and j==1 and (temp4.sem_tt[5][2]==temp1.code or temp4.sem_tt[5][3]==temp1.code or temp4.sem_tt[5][6]==temp1.code or temp4.sem_tt[4][1]==temp1.code ): break
                                    if i==1 and j==2 and (temp4.sem_tt[1][1]==temp1.code or temp4.sem_tt[1][3]==temp1.code or temp4.sem_tt[1][6]==temp1.code or temp4.sem_tt[2][2]==temp1.code ): break
                                    if i==2 and j==2 and (temp4.sem_tt[2][1]==temp1.code or temp4.sem_tt[2][3]==temp1.code or temp4.sem_tt[2][6]==temp1.code or temp4.sem_tt[1][2]==temp1.code or temp4.sem_tt[3][2]==temp1.code ): break
                                    if i==3 and j==2 and (temp4.sem_tt[3][1]==temp1.code or temp4.sem_tt[3][3]==temp1.code or temp4.sem_tt[3][6]==temp1.code or temp4.sem_tt[2][2]==temp1.code or temp4.sem_tt[4][2]==temp1.code ): break
                                    if i==4 and j==2 and (temp4.sem_tt[4][1]==temp1.code or temp4.sem_tt[4][3]==temp1.code or temp4.sem_tt[4][6]==temp1.code or temp4.sem_tt[3][2]==temp1.code or temp4.sem_tt[5][2]==temp1.code ): break
                                    if i==5 and j==2 and (temp4.sem_tt[5][1]==temp1.code or temp4.sem_tt[5][3]==temp1.code or temp4.sem_tt[5][6]==temp1.code or temp4.sem_tt[4][2]==temp1.code ): break
                                    if i==1 and j==3 and (temp4.sem_tt[1][1]==temp1.code or temp4.sem_tt[1][2]==temp1.code or temp4.sem_tt[1][6]==temp1.code or temp4.sem_tt[2][3]==temp1.code ): break
                                    if i==2 and j==3 and (temp4.sem_tt[2][1]==temp1.code or temp4.sem_tt[2][2]==temp1.code or temp4.sem_tt[2][6]==temp1.code or temp4.sem_tt[1][3]==temp1.code or temp4.sem_tt[3][3]==temp1.code ): break
                                    if i==3 and j==3 and (temp4.sem_tt[3][1]==temp1.code or temp4.sem_tt[3][2]==temp1.code or temp4.sem_tt[3][6]==temp1.code or temp4.sem_tt[2][3]==temp1.code or temp4.sem_tt[4][3]==temp1.code ): break
                                    if i==4 and j==3 and (temp4.sem_tt[4][1]==temp1.code or temp4.sem_tt[4][2]==temp1.code or temp4.sem_tt[4][6]==temp1.code or temp4.sem_tt[3][3]==temp1.code or temp4.sem_tt[5][3]==temp1.code ): break
                                    if i==5 and j==3 and (temp4.sem_tt[5][1]==temp1.code or temp4.sem_tt[5][2]==temp1.code or temp4.sem_tt[5][6]==temp1.code or temp4.sem_tt[4][3]==temp1.code ): break
                                    if i==1 and j==6 and (temp4.sem_tt[1][1]==temp1.code or temp4.sem_tt[1][2]==temp1.code or temp4.sem_tt[1][3]==temp1.code or temp4.sem_tt[2][6]==temp1.code ): break
                                    if i==2 and j==6 and (temp4.sem_tt[2][1]==temp1.code or temp4.sem_tt[2][2]==temp1.code or temp4.sem_tt[2][3]==temp1.code or temp4.sem_tt[1][6]==temp1.code or temp4.sem_tt[3][6]==temp1.code ): break
                                    if i==3 and j==6 and (temp4.sem_tt[3][1]==temp1.code or temp4.sem_tt[3][2]==temp1.code or temp4.sem_tt[3][3]==temp1.code or temp4.sem_tt[2][6]==temp1.code or temp4.sem_tt[4][6]==temp1.code ): break
                                    if i==4 and j==6 and (temp4.sem_tt[4][1]==temp1.code or temp4.sem_tt[4][2]==temp1.code or temp4.sem_tt[4][3]==temp1.code or temp4.sem_tt[3][6]==temp1.code or temp4.sem_tt[5][6]==temp1.code ): break
                                    if i==5 and j==6 and (temp4.sem_tt[5][1]==temp1.code or temp4.sem_tt[5][2]==temp1.code or temp4.sem_tt[5][3]==temp1.code or temp4.sem_tt[4][6]==temp1.code ): break
                                if j==1:
                                    if temp2:
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][1]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][2]="."
                                                    temp2.test_tt[i][1]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][1]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][2]="."
                                                    temp2.test_tt[i][1]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][1]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][2]="."
                                                    temp2.test_tt[i][1]=temp1.semester1
                                                    break
                                        elif temp4!=None and temp44!=None :
                                            if temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][1]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][2]="."
                                                    temp2.test_tt[i][1]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][1]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][2]="."
                                                    temp2.test_tt[i][1]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][1]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][2]="."
                                                    temp2.test_tt[i][1]=temp1.semester1
                                                    break
                                        elif temp4!=None:
                                            if temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][1]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][2]="."
                                                    temp2.test_tt[i][1]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][1]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][2]="."
                                                    temp2.test_tt[i][1]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][1]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][2]="."
                                                    temp2.test_tt[i][1]=temp1.semester1
                                                    break
                                if j==2:
                                    if temp2 :
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][2]==temp2.faculty_tt[i][3]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][3]="."
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][2]==temp2.faculty_tt[i][3]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][3]="."
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][2]==temp2.faculty_tt[i][3]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][3]="."
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                        elif temp4!=None and temp44!=None :
                                            if temp2.faculty_tt[i][2]==temp2.faculty_tt[i][3]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][3]="."
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][2]==temp2.faculty_tt[i][3]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][3]="."
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][2]==temp2.faculty_tt[i][3]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][3]="."
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                        elif temp4!=None:
                                            if temp2.faculty_tt[i][2]==temp2.faculty_tt[i][3]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][3]="."
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][2]==temp2.faculty_tt[i][3]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][3]="."
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][2]==temp2.faculty_tt[i][3]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][3]="."
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                if j==3:
                                    if temp2 :
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][5]="."
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][5]="."
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][5]="."
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                        elif temp4!=None and temp44!=None :
                                            if temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][5]="."
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][5]="."
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][5]="."
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                        elif temp4!=None:
                                            if temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][5]="."
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][5]="."
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][4]==temp2.faculty_tt[i][5]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][5]="."
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                if j==6:
                                    if temp2:
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][9]="."
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][9]="."
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][9]="."
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                        elif temp4!=None and temp44!=None :
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][9]="."
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][9]="."
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][9]="."
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                        elif temp4!=None:
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][9]="."
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][9]="."
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.theory:
                                                    time1+=90
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][9]="."
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                if temp1.tutorial:
                    time1,time2,time3=0,0,0
                    for _ in range(5):
                        for i in range(6):
                            for j in range(8):
                                if _<=2:
                                        shift=0
                                        for l in range(8):
                                            if temp2.test_tt[i][l]==temp1.semester1:
                                                shift=1
                                                break
                                        if shift==1:break
                                if j==5:
                                    if temp2:
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][7]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][7]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][7]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][7]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][7]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][7]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][7]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][7]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][7]=temp1.semester1
                                                    break
                                        elif temp4!=None and temp44!=None :
                                            if temp2.faculty_tt[i][7]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][7]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][7]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][7]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][7]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][7]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][7]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][7]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][7]=temp1.semester1
                                                    break
                                        elif temp4!=None:
                                            if temp2.faculty_tt[i][7]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][7]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][7]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][7]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][7]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][7]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][7]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][7]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][7]=temp1.semester1
                                                    break
                                if j==6:
                                    if temp2 :
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][8]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code+"(3:30-4:30)"
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][8]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][8]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                        elif temp4!=None and temp44!=None :
                                            if temp2.faculty_tt[i][8]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][8]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][8]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                        elif temp4!=None:
                                            if temp2.faculty_tt[i][8]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][8]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][8]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][8]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][8]=temp1.semester1
                                                    break
                                if j==6:
                                    if temp2 :
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][9]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][9]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][9]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][9]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][9]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][9]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][9]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][9]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][9]=temp1.semester1
                                                    break
                                        elif temp4!=None and temp44!=None :
                                            if temp2.faculty_tt[i][9]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][9]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][9]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][9]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][9]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][9]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][9]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][9]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][9]=temp1.semester1
                                                    break
                                        elif temp4!=None:
                                            if temp2.faculty_tt[i][9]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][9]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][9]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][9]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][9]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][9]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][9]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][9]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][9]=temp1.semester1
                                                    break
                                if j==1:
                                    if temp2 :
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][2]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][2]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][2]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                        elif temp4!=None and temp44!=None :
                                            if temp2.faculty_tt[i][2]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][2]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][2]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                        elif temp4!=None:
                                            if temp2.faculty_tt[i][2]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][2]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][2]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][2]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][2]=temp1.semester1
                                                    break
                                if j==2:
                                    if temp2 :
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][3]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][3]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][3]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][3]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][3]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][3]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][3]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][3]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][3]=temp1.semester1
                                                    break
                                        elif temp4!=None and temp44!=None :
                                            if temp2.faculty_tt[i][3]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][3]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][3]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][3]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][3]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][3]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][3]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][3]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][3]=temp1.semester1
                                                    break
                                        elif temp4!=None:
                                            if temp2.faculty_tt[i][3]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][3]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][3]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][3]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][3]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][3]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][3]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][3]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][3]=temp1.semester1
                                                    break
                                if j==3:
                                    if temp2 :
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][4]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][4]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][4]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp444.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp444.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                        elif temp4!=None and temp44!=None :
                                            if temp2.faculty_tt[i][4]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][4]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][4]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp44.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp44.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                        elif temp4!=None:
                                            if temp2.faculty_tt[i][4]==temp5.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp5.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp5.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp5.classroom_code+")"
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][4]==temp55.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp55.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp55.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp55.classroom_code+")"
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                                            elif temp2.faculty_tt[i][4]==temp555.classroom_tt[i][j]==temp4.sem_tt[i][j]=="*":
                                                if time1<temp1.tutorial:
                                                    time1+=60
                                                    temp555.classroom_tt[i][j]=temp1.code
                                                    temp4.sem_tt[i][j]=temp1.code
                                                    temp4.sem_tt_new[i][j]=temp1.code+"("+temp555.classroom_code+")"
                                                    temp2.faculty_tt[i][4]=temp1.code+"_ELE ("+temp555.classroom_code+")"
                                                    temp2.test_tt[i][4]=temp1.semester1
                                                    break
                if temp1.lab:
                    time1,time2,time3=0,0,0
                    for _ in range(5):
                        for i in range(6):
                            for j in range(8):
                                if _<=2:
                                        shift=0
                                        for l in range(8):
                                            if temp2.test_tt[i][l]==temp1.semester1:
                                                shift=1
                                                break
                                        if shift==1:break
                                if temp4!=None and temp44!=None and temp444!=None:
                                    if j==4 and temp2:
                                        if temp2.faculty_tt[i][6]==temp2.faculty_tt[i][7]=='*' and time1<temp1.lab:
                                            #If there is no activity at that time1...
                                            if temp4.sem_tt[i][j]==temp4.sem_tt[i][j+1]==temp44.sem_tt[i][j]==temp44.sem_tt[i][j+1]==temp444.sem_tt[i][j]==temp444.sem_tt[i][j+1]=='*' and (time1+120)<=temp1.lab:
                                                if temp2.faculty_tt[i][1]==temp1.semester1:
                                                    break
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp6):
                                                    if temp6.tt[i][6]==temp6.tt[i][7]==temp6.tt[i][7]=='*':
                                                        temp2.faculty_tt[i][6]=temp1.code+"_LAB (10:45-12:45)"
                                                        temp2.faculty_tt[i][7]="."
                                                        temp2.test_tt[i][6]=temp1.semester1
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j+1]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j+1]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j+1]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"LAB ("+temp6.name+")"
                                                        temp4.sem_tt_new[i][j+1]=temp1.code+"LAB ("+temp6.name+")"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"LAB ("+temp6.name+")"
                                                        temp44.sem_tt_new[i][j+1]=temp1.code+"LAB ("+temp6.name+")"
                                                        temp444.sem_tt_new[i][j]=temp1.code+"LAB ("+temp6.name+")"
                                                        temp444.sem_tt_new[i][j+1]=temp1.code+"LAB ("+temp6.name+")"
                                                        temp6.tt[i][6]=temp1.code
                                                        temp6.tt[i][7]=temp1.code
                                                        time1+=120
                                                        break
                                                    temp6=temp6.next
                                            elif temp4.sem_tt[i][j]==temp4.sem_tt[i][j+1]==temp44.sem_tt[i][j]==temp44.sem_tt[i][j+1]==temp444.sem_tt[i][j]==temp444.sem_tt[i][j+1] and time1+120<=temp1.lab:
                                                if time1>=temp1.lab:break
                                                temp9=None
                                                tip=0
                                                temp9=obj_for_linked_list_for_electives.head_for_lab
                                                temp6=None
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp9):
                                                    if temp4.sem_tt[i][j]==temp9.code:
                                                        tip=1
                                                        break
                                                    temp9=temp9.next
                                                while(temp6):
                                                    if temp6.tt[i][6]==temp6.tt[i][7]=='*':
                                                        break
                                                    temp6=temp6.next
                                                if tip==1 and temp9.id!=temp1.id and temp6:
                                                    temp2.faculty_tt[i][6]=temp1.code+"_LAB (10:45-12:45)"
                                                    temp2.faculty_tt[i][7]="."
                                                    temp2.test_tt[i][6]=temp1.semester1
                                                    temp4.sem_tt[i][j]+=" /" +temp1.code
                                                    temp4.sem_tt[i][j+1]+=" /" +temp1.code
                                                    temp44.sem_tt[i][j]+=" /" +temp1.code
                                                    temp44.sem_tt[i][j+1]+=" /" +temp1.code
                                                    temp444.sem_tt[i][j]+=" /" +temp1.code
                                                    temp444.sem_tt[i][j+1]+=" /" +temp1.code
                                                    temp4.sem_tt_new[i][j]+=" /" +temp1.code+"LAB ("+temp6.name+")"
                                                    temp4.sem_tt_new[i][j+1]+=" /" +temp1.code+"LAB ("+temp6.name+")"
                                                    temp44.sem_tt_new[i][j]+=" /" +temp1.code+"LAB ("+temp6.name+")"
                                                    temp44.sem_tt_new[i][j+1]+=" /" +temp1.code+"LAB ("+temp6.name+")"
                                                    temp444.sem_tt_new[i][j]+=" /" +temp1.code+"("+temp6.name+")"
                                                    temp444.sem_tt_new[i][j+1]+=" /" +temp1.code
                                                    temp6.tt[i][6]=temp1.code
                                                    temp6.tt[i][7]=temp1.code
                                                    time1+=120
                                                    break
                                elif temp4!=None and temp44!=None :
                                    if j==4 and temp2:
                                        if temp2.faculty_tt[i][6]==temp2.faculty_tt[i][7]=='*' and time1<temp1.lab:
                                            #If there is no activity at that time1...
                                            if temp4.sem_tt[i][j]==temp4.sem_tt[i][j+1]==temp44.sem_tt[i][j]==temp44.sem_tt[i][j+1]=='*' and (time1+120)<=temp1.lab:
                                                if temp2.faculty_tt[i][1]==temp1.semester1:
                                                    break
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp6):
                                                    if temp6.tt[i][6]==temp6.tt[i][7]==temp6.tt[i][7]=='*':
                                                        temp2.faculty_tt[i][6]=temp1.code+"_LAB (10:45-12:45)"
                                                        temp2.faculty_tt[i][7]="."
                                                        temp2.test_tt[i][6]=temp1.semester1
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j+1]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j+1]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp6.name+")"
                                                        temp4.sem_tt_new[i][j+1]=temp1.code+"("+temp6.name+")"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"("+temp6.name+")"
                                                        temp44.sem_tt_new[i][j+1]=temp1.code+"("+temp6.name+")"
                                                        temp6.tt[i][6]=temp1.code
                                                        temp6.tt[i][7]=temp1.code
                                                        time1+=120
                                                        break
                                                    temp6=temp6.next
                                            elif temp4.sem_tt[i][j]==temp4.sem_tt[i][j+1]==temp44.sem_tt[i][j]==temp44.sem_tt[i][j+1] and time1+120<=temp1.lab:
                                                if time1>=temp1.lab:break
                                                temp9=None
                                                tip=0
                                                temp9=obj_for_linked_list_for_electives.head_for_lab
                                                temp6=None
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp9):
                                                    if temp4.sem_tt[i][j]==temp9.code:
                                                        tip=1
                                                        break
                                                    temp9=temp9.next
                                                while(temp6):
                                                    if temp6.tt[i][6]==temp6.tt[i][7]=='*':break
                                                    temp6=temp6.next
                                                if tip==1 and temp9.id!=temp1.id and temp6:
                                                    temp2.faculty_tt[i][6]=temp1.code+"_LAB (10:45-12:45)"
                                                    temp2.faculty_tt[i][7]="."
                                                    temp2.test_tt[i][6]=temp1.semester1
                                                    temp4.sem_tt[i][j]+=" /" +temp1.code
                                                    temp4.sem_tt[i][j+1]+=" /" +temp1.code
                                                    temp44.sem_tt[i][j]+=" /" +temp1.code
                                                    temp44.sem_tt[i][j+1]+=" /" +temp1.code
                                                    temp4.sem_tt_new[i][j]+=" /" +temp1.code+"("+temp6.name+")"
                                                    temp4.sem_tt_new[i][j+1]+=" /" +temp1.code+"("+temp6.name+")"
                                                    temp44.sem_tt_new[i][j]+=" /" +temp1.code+"("+temp6.name+")"
                                                    temp44.sem_tt_new[i][j+1]+=" /" +temp1.code+"("+temp6.name+")"
                                                    temp6.tt[i][6]=temp1.code
                                                    temp6.tt[i][7]=temp1.code
                                                    time1+=120
                                                    break
                                                #Lab
                                elif temp4!=None :
                                    if j==4 and temp2:
                                        if temp2.faculty_tt[i][6]==temp2.faculty_tt[i][7]=='*' and time1<temp1.lab:
                                            #If there is no activity at that time1...
                                            if temp4.sem_tt[i][j]==temp4.sem_tt[i][j+1]=='*' and (time1+120)<=temp1.lab:
                                                if temp2.faculty_tt[i][1]==temp1.semester1:break
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp6):
                                                    if temp6.tt[i][6]==temp6.tt[i][7]==temp6.tt[i][7]=='*':
                                                        temp2.faculty_tt[i][6]=temp1.code+"_LAB (10:45-12:45)"
                                                        temp2.faculty_tt[i][7]="."
                                                        temp2.test_tt[i][6]=temp1.semester1
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j+1]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp6.name+")"
                                                        temp4.sem_tt_new[i][j+1]=temp1.code+"("+temp6.name+")"
                                                        temp6.tt[i][6]=temp1.code
                                                        temp6.tt[i][7]=temp1.code
                                                        time1+=120
                                                        break
                                                    temp6=temp6.next
                                            elif temp4.sem_tt[i][j]==temp4.sem_tt[i][j+1] and time1+120<=temp1.lab:
                                                if time1>=temp1.lab:break
                                                temp9=None
                                                tip=0
                                                temp9=obj_for_linked_list_for_electives.head_for_lab
                                                temp6=None
                                                if temp1.lab_name=='CS_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
                                                if temp1.lab_name=='EC_LAB':temp6=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
                                                while(temp9):
                                                    if temp4.sem_tt[i][j]==temp9.code:
                                                        tip=1
                                                        break
                                                    temp9=temp9.next
                                                while(temp6):
                                                    if temp6.tt[i][6]==temp6.tt[i][7]=='*':
                                                        break
                                                    temp6=temp6.next
                                                if tip==1 and temp9.id!=temp1.id and temp6:
                                                    temp2.faculty_tt[i][6]=temp1.code+"_LAB (10:45-12:45)"
                                                    temp2.faculty_tt[i][7]="."
                                                    temp2.test_tt[i][6]=temp1.semester1
                                                    temp4.sem_tt[i][j]+=" /" +temp1.code
                                                    temp4.sem_tt[i][j+1]+=" /" +temp1.code
                                                    temp4.sem_tt_new[i][j]+=" /" +temp1.code+"("+temp6.name+")"
                                                    temp4.sem_tt_new[i][j+1]+=" /" +temp1.code+"("+temp6.name+")"
                                                    temp6.tt[i][6]=temp1.code
                                                    temp6.tt[i][7]=temp1.code
                                                    time1+=120
                                                    break
                if temp1.theory:
                    if time1<temp1.theory:print("theory not satisfied for ",temp1.name,"Semester: ",temp1.semester1)
                if temp1.tutorial:
                    if time1<temp1.tutorial:print("tutorial not satisfied for ",temp1.name,"Semester: ",temp1.semester1)
                if temp1.lab:
                    if time1<temp1.lab:print("Lab not satisfied for ",temp1.name,"Semester: ",temp1.semester1)
                temp1=temp1.next
            else:
                if temp1.theory:
                    time1=0
                    time2=0
                    time3=0
                    for _ in range(5):
                        for i in range(6):
                            for j in range(8):
                                if _<=2:
                                        shift=0
                                        for l in range(8):
                                            if temp2.test_tt[i][l]==temp1.semester1:
                                                shift=1
                                                break
                                        if shift==1:break
                                if j==5:
                                    if temp2 and temp22 and temp222:
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.theory):
                                                    if temp3.classroom_tt [i][6]==temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]=='*':
                                                        qwerty=0
                                                        if temp3.name=="DSAI_Sem_8" or temp3.sem=="Sem_7" or temp3.sem=="Sem_8" or temp3.name=="DSAI_Sem_7":
                                                            if temp1.semester1=="CSE_Sem_3_A" or temp1.semester1=="CSE_Sem_3_B" or temp1.semester1=="ECE_Sem_3" or temp1.semester1=="DSAI_Sem_3" or temp1.semester1=="CSE_Sem_4_A" or temp1.semester1=="CSE_Sem_4_B" or temp1.semester1=="ECE_Sem_4" or temp1.semester1=="DSAI_Sem_4":
                                                                time1+=90
                                                                temp3.classroom_tt[i][6]=temp1.code
                                                                temp4.sem_tt[i][j]=temp1.code
                                                                temp44.sem_tt[i][j]=temp1.code
                                                                temp444.sem_tt[i][j]=temp1.code
                                                                temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                                temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                                temp444.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                                temp2.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                                temp2.faculty_tt[i][9]="."
                                                                qwerty=1
                                                                break
                                                        elif qwerty==0:
                                                            time1+=90
                                                            temp3.classroom_tt[i][j]=temp1.code
                                                            temp4.sem_tt[i][j]=temp1.code
                                                            temp44.sem_tt[i][j]=temp1.code
                                                            temp444.sem_tt[i][j]=temp1.code
                                                            temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                            temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                            temp444.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                            temp2.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                            temp2.faculty_tt[i][9]="."
                                                            break
                                                    #temp1.code+"("+temp3.classroom_code+") /"
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.theory):
                                                    qwerty=0
                                                    if temp3.classroom_tt [i][6]==temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]=='*':
                                                        if temp3.name=="DSAI_Sem_8" or temp3.sem=="Sem_7" or temp3.sem=="Sem_8" or temp3.name=="DSAI_Sem_7":
                                                            if temp1.semester1=="CSE_Sem_3_A" or temp1.semester1=="CSE_Sem_3_B" or temp1.semester1=="ECE_Sem_3" or temp1.semester1=="DSAI_Sem_3" or temp1.semester1=="CSE_Sem_4_A" or temp1.semester1=="CSE_Sem_4_B" or temp1.semester1=="ECE_Sem_4" or temp1.semester1=="DSAI_Sem_4":
                                                                time2+=90
                                                                temp3.classroom_tt[i][j]=temp1.code
                                                                temp4.sem_tt[i][j]=temp1.code
                                                                temp44.sem_tt[i][j]=temp1.code
                                                                temp444.sem_tt[i][j]=temp1.code
                                                                temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                                temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                                temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                                temp22.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                                temp22.faculty_tt[i][9]="."
                                                                qwerty=1
                                                                break
                                                        elif qwerty==1:
                                                            time2+=90
                                                            temp3.classroom_tt[i][j]=temp1.code
                                                            temp4.sem_tt[i][j]=temp1.code
                                                            temp44.sem_tt[i][j]=temp1.code
                                                            temp444.sem_tt[i][j]=temp1.code
                                                            temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                            temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                            temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                            temp22.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                            temp22.faculty_tt[i][9]="."
                                                            break

                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]=='*':
                                                        qwerty=0
                                                        if temp3.name=="DSAI_Sem_8" or temp3.sem=="Sem_7" or temp3.sem=="Sem_8" or temp3.name=="DSAI_Sem_7":
                                                            if temp1.semester1=="CSE_Sem_3_A" or temp1.semester1=="CSE_Sem_3_B" or temp1.semester1=="ECE_Sem_3" or temp1.semester1=="DSAI_Sem_3" or temp1.semester1=="CSE_Sem_4_A" or temp1.semester1=="CSE_Sem_4_B" or temp1.semester1=="ECE_Sem_4" or temp1.semester1=="DSAI_Sem_4":
                                                                time3+=90
                                                                temp3.classroom_tt[i][j]=temp1.code
                                                                temp4.sem_tt[i][j]=temp1.code
                                                                temp44.sem_tt[i][j]=temp1.code
                                                                temp444.sem_tt[i][j]=temp1.code
                                                                temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                                temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                                temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                                temp222.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                                temp222.faculty_tt[i][9]="."
                                                                qwerty=1
                                                                break
                                                        elif qwerty==0:
                                                            time3+=90
                                                            temp3.classroom_tt[i][j]=temp1.code
                                                            temp4.sem_tt[i][j]=temp1.code
                                                            temp44.sem_tt[i][j]=temp1.code
                                                            temp444.sem_tt[i][j]=temp1.code
                                                            temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                            temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                            temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                            temp222.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                            temp222.faculty_tt[i][9]="."
                                                            break

                                                    temp3=temp3.next
                                        elif temp4!=None and temp44!=None :
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]=='*' and time1<temp1.theory:
                                                        time1+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]=='*' :
                                                        time2+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]=='*':
                                                        time3+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                        elif temp4!=None:
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp4.sem_tt[i][j]=="*":
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]=='*' and time1<temp1.theory:
                                                        time1+=90
                                                        temp3.classroom_tt[i]
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]=='*' :
                                                        time2+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]=='*':
                                                        time3+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                if _>2 and j==5:
                                    if temp2 and temp22 and temp222:
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.theory):
                                                    if temp3.classroom_tt[i][6]==temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]=='*' and time1<temp1.theory:
                                                        time1+=90
                                                        temp3.classroom_tt[i][6]=temp1.cod
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.cod
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.theory):
                                                    if temp3.classroom_tt[i][6]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]=='*' :
                                                        time2+=90
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.theory):
                                                    if temp3.classroom_tt[i][6]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]=='*':
                                                        time3+=90
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                        elif temp4!=None and temp44!=None :
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.theory):
                                                    if temp3.classroom_tt[i][6]==temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]=='*' and time1<temp1.theory:
                                                        time1+=90
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.theory):
                                                    if temp3.classroom_tt[i][6]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]=='*' :
                                                        time2+=90
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.theory):
                                                    if temp3.classroom_tt[i][6]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]=='*':
                                                        time3+=90
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                        elif temp4!=None:
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp4.sem_tt[i][j]=="*":
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.theory):
                                                    if temp3.classroom_tt[i][6]==temp4.sem_tt[i][j]==temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]=='*' and time1<temp1.theory:
                                                        time1+=90
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.theory):
                                                    if temp3.classroom_tt[i][6]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]=='*' :
                                                        time2+=90
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.theory):
                                                    if temp3.classroom_tt[i][6]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]=='*':
                                                        time3+=90
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                if _>3 and j==2:
                                    if temp2 and temp22 and temp222:
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][3]==temp2.faculty_tt[i][4]==temp22.faculty_tt[i][3]==temp22.faculty_tt[i][4]==temp222.faculty_tt[i][3]==temp222.faculty_tt[i][4]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp2.faculty_tt[i][3]==temp2.faculty_tt[i][4]=='*' and time1<temp1.theory:
                                                        time1+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][3]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][4]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][3]==temp22.faculty_tt[i][4]=='*' :
                                                        time2+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][3]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][4]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][3]==temp222.faculty_tt[i][4]=='*':
                                                        time3+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][3]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][4]="."
                                                        break
                                                    temp3=temp3.next
                                        elif temp4!=None and temp44!=None:
                                            if temp2.faculty_tt[i][3]==temp2.faculty_tt[i][4]==temp22.faculty_tt[i][3]==temp22.faculty_tt[i][4]==temp222.faculty_tt[i][3]==temp222.faculty_tt[i][4]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp2.faculty_tt[i][3]==temp2.faculty_tt[i][4]=='*' and time1<temp1.theory:
                                                        time1+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][3]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][4]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][3]==temp22.faculty_tt[i][4]=='*' :
                                                        time2+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][3]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][4]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][3]==temp222.faculty_tt[i][4]=='*':
                                                        time3+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][3]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][4]="."
                                                        break
                                                    temp3=temp3.next
                                        if temp4!=None :
                                            if temp2.faculty_tt[i][3]==temp2.faculty_tt[i][4]==temp22.faculty_tt[i][3]==temp22.faculty_tt[i][4]==temp222.faculty_tt[i][3]==temp222.faculty_tt[i][4]==temp4.sem_tt[i][j]=='*':
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp2.faculty_tt[i][3]==temp2.faculty_tt[i][4]=='*' and time1<temp1.theory:
                                                        time1+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][3]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][4]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][3]==temp22.faculty_tt[i][4]=='*' :
                                                        time2+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][3]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][4]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][3]==temp222.faculty_tt[i][4]=='*':
                                                        time3+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][3]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][4]="."
                                                        break
                                                    temp3=temp3.next
                                if _>3 and j==1:
                                    if temp2 and temp22 and temp222:
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp22.faculty_tt[i][1]==temp22.faculty_tt[i][2]==temp222.faculty_tt[i][1]==temp222.faculty_tt[i][2]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=='*':
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]=='*' and time1<temp1.theory:
                                                        time1+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][1]==temp22.faculty_tt[i][2]=='*' :
                                                        time2+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][1]==temp222.faculty_tt[i][2]=='*':
                                                        time3+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                                        elif temp4!=None and temp44!=None:
                                            if temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp22.faculty_tt[i][1]==temp22.faculty_tt[i][2]==temp222.faculty_tt[i][1]==temp222.faculty_tt[i][2]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=='*':
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]=='*' and time1<temp1.theory:
                                                        time1+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][1]==temp22.faculty_tt[i][2]=='*' :
                                                        time2+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][1]==temp222.faculty_tt[i][2]=='*':
                                                        time3+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                                        elif temp4!=None :
                                            if temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp22.faculty_tt[i][1]==temp22.faculty_tt[i][2]==temp222.faculty_tt[i][1]==temp222.faculty_tt[i][2]==temp4.sem_tt[i][j]=='*':
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]=='*' and time1<temp1.theory:
                                                        time1+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][1]==temp22.faculty_tt[i][2]=='*' :
                                                        time2+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.theory):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][1]==temp222.faculty_tt[i][2]=='*':
                                                        time3+=90
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                if temp1.tutorial:
                    time1=0
                    time2=0
                    time3=0
                    for _ in range(5):
                        for i in range(6):
                            for j in range(8):
                                if _<=2:
                                        shift=0
                                        for l in range(8):
                                            if temp2.test_tt[i][l]==temp1.semester1:
                                                shift=1
                                                break
                                        if shift==1:break
                                if _==4 and j==5:
                                    if temp2 and temp22 and temp222:
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]=='*' and time1<temp1.tutorial:
                                                        time1+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]=='*' :
                                                        time2+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]=='*':
                                                        time3+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                        elif temp4!=None and temp44!=None :
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]=='*' and time1<temp1.tutorial:
                                                        time1+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]=='*' :
                                                        time2+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]=='*':
                                                        time3+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                        elif temp4!=None:
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp4.sem_tt[i][j]=="*":
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]=='*' and time1<temp1.tutorial:
                                                        time1+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]=='*' :
                                                        time2+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]=='*':
                                                        time3+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                if _<4 and j==5:
                                    if temp2 and temp22 and temp222:
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.tutorial):
                                                    if temp3.classroom_tt[i][6]==temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]=='*' and time1<temp1.tutorial:
                                                        time1+=60
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.tutorial):
                                                    if temp3.classroom_tt[i][6]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]=='*' :
                                                        time2+=60
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.tutorial):
                                                    if temp3.classroom_tt[i][6]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]=='*':
                                                        time3+=60
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                        elif temp4!=None and temp44!=None :
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.tutorial):
                                                    if temp3.classroom_tt[i][6]==temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]=='*' and time1<temp1.tutorial:
                                                        time1+=60
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.tutorial):
                                                    if temp3.classroom_tt[i][6]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]=='*' :
                                                        time2+=60
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.tutorial):
                                                    if temp3.classroom_tt[i][6]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]=='*':
                                                        time3+=60
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                        elif temp4!=None:
                                            if temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]==temp4.sem_tt[i][j]=="*":
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.tutorial):
                                                    if temp3.classroom_tt[i][6]==temp4.sem_tt[i][j]==temp2.faculty_tt[i][8]==temp2.faculty_tt[i][9]=='*' and time1<temp1.tutorial:
                                                        time1+=60
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.tutorial):
                                                    if temp3.classroom_tt[i][6]==temp22.faculty_tt[i][8]==temp22.faculty_tt[i][9]=='*' :
                                                        time2+=60
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.tutorial):
                                                    if temp3.classroom_tt[i][6]==temp222.faculty_tt[i][8]==temp222.faculty_tt[i][9]=='*':
                                                        time3+=60
                                                        temp3.classroom_tt[i][6]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][8]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][9]="."
                                                        break
                                                    temp3=temp3.next
                                if _<4 and j==4:
                                    if temp2 and temp22 and temp222:
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][7]==temp22.faculty_tt[i][7]==temp222.faculty_tt[i][7]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=="*":
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp2.faculty_tt[i][7]=='*' and time1<temp1.tutorial:
                                                        time1+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][7]=temp1.code+temp3.classroom_code
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][7]=='*' :
                                                        time2+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][7]=temp1.code+temp3.classroom_code
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][7]=='*':
                                                        time3+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][7]=temp1.code+temp3.classroom_code
                                                        break
                                                    temp3=temp3.next
                                        elif temp4!=None and temp44!=None:
                                            if temp2.faculty_tt[i][7]==temp22.faculty_tt[i][7]==temp222.faculty_tt[i][7]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=="*":
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp2.faculty_tt[i][7]=='*' and time1<temp1.tutorial:
                                                        time1+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][7]=temp1.code+temp3.classroom_code
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][7]=='*' :
                                                        time2+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][7]=temp1.code+temp3.classroom_code
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][7]=='*':
                                                        time3+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][7]=temp1.code+temp3.classroom_code
                                                        break
                                                    temp3=temp3.next
                                        if temp4!=None :
                                            if temp2.faculty_tt[i][7]==temp22.faculty_tt[i][7]==temp222.faculty_tt[i][7]==temp4.sem_tt[i][j]=='*':
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp2.faculty_tt[i][7]=='*' and time1<temp1.tutorial:
                                                        time1+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][7]=temp1.code+temp3.classroom_code
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][7]=='*' :
                                                        time2+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][7]=temp1.code+temp3.classroom_code
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][7]=='*':
                                                        time3+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][7]=temp1.code+temp3.classroom_code
                                                        break
                                                    temp3=temp3.next
                                if _<4 and j==3:
                                    if temp2 and temp22 and temp222:
                                        if temp4!=None and temp44!=None and temp444!=None:
                                            if temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp22.faculty_tt[i][1]==temp22.faculty_tt[i][2]==temp222.faculty_tt[i][1]==temp222.faculty_tt[i][2]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]==temp444.sem_tt[i][j]=='*':
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]=='*' and time1<temp1.tutorial:
                                                        time1+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][1]==temp22.faculty_tt[i][2]=='*' :
                                                        time2+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][1]==temp222.faculty_tt[i][2]=='*':
                                                        time3+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp444.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp444.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                                        elif temp4!=None and temp44!=None:
                                            if temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp22.faculty_tt[i][1]==temp22.faculty_tt[i][2]==temp222.faculty_tt[i][1]==temp222.faculty_tt[i][2]==temp4.sem_tt[i][j]==temp44.sem_tt[i][j]=='*':
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]=='*' and time1<temp1.tutorial:
                                                        time1+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][1]==temp22.faculty_tt[i][2]=='*' :
                                                        time2+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][1]==temp222.faculty_tt[i][2]=='*':
                                                        time3+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp44.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp44.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                                        elif temp4!=None :
                                            if temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]==temp22.faculty_tt[i][1]==temp22.faculty_tt[i][2]==temp222.faculty_tt[i][1]==temp222.faculty_tt[i][2]==temp4.sem_tt[i][j]=='*':
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time1<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp4.sem_tt[i][j]==temp2.faculty_tt[i][1]==temp2.faculty_tt[i][2]=='*' and time1<temp1.tutorial:
                                                        time1+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp2.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp2.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time2<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp22.faculty_tt[i][1]==temp22.faculty_tt[i][2]=='*' :
                                                        time2+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp22.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp22.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                                                temp3=obj_for_class_rooms.head_for_class_rooms
                                                while(temp3 and time3<temp1.tutorial):
                                                    if temp3.classroom_tt[i][j]==temp222.faculty_tt[i][1]==temp222.faculty_tt[i][2]=='*':
                                                        time3+=60
                                                        temp3.classroom_tt[i][j]=temp1.code
                                                        temp4.sem_tt[i][j]=temp1.code
                                                        temp4.sem_tt_new[i][j]+=temp1.code+"("+temp3.classroom_code+") /"
                                                        temp222.faculty_tt[i][1]=temp1.code+temp3.classroom_code
                                                        temp222.faculty_tt[i][2]="."
                                                        break
                                                    temp3=temp3.next
                if temp1.theory:
                    if time1<temp1.theory:print("theory not satisfied for ",temp1.name,"Semester: ",temp1.semester1,"time1:",time1)
                    if temp44:
                        if time2<temp1.theory:print("Theory not satisfied for ",temp1.name,"Semester: ",temp1.semester2,"time2", time2)
                    if temp444:
                        if time3<temp1.theory:print("Theory not satisfied for ",temp1.name,"Semester: ",temp1.semester3,"time3",time3)
                if temp1.tutorial:
                    if time1<temp1.tutorial:print("tutorial not satisfied for ",temp1.name,"Semester: ",temp1.semester1,"time1",time1)
                    if temp44:
                        if time2<temp1.tutorial:print("tutorial not satisfied for ",temp1.name,"Semester: ",temp1.semester2,"time2",time2)
                    if temp444:
                        if time3<temp1.tutorial:print("tutorial not satisfied for ",temp1.name,"Semester: ",temp1.semester3,"time3",time3)
                temp1=temp1.next
    return

def clear1():
    temp=obj_for_facultys.head_for_faculty_names
    while(temp):
            for i in range(6):
                for j in range(11):
                    if j!=0 and i!=0:temp.faculty_tt[i][j]='*'
                    if j!=0 and i!=0:temp.test_tt[i][j]='*'
            temp=temp.next
def clear2():
    temp=obj_for_sem.head_for_semesters
    while(temp):
        if temp.sem_org=="Sem_7_A" or temp.sem_org=="Sem_7_B" or temp.sem_org=="Sem_8_A" or temp.sem_org=="Sem_8_B" or temp.sem_org=="Sem_7" or temp.sem_org=="Sem_8":
            for i in range(6):
                for j in range(8):
                    if j!=0 and i!=0:
                        temp.sem_tt[i][j]='*'
                        temp.sem_tt_new[i][j]='*'
        else:
            for i in range(6):
                for j in range(6):
                    if j!=0 and i!=0:
                        temp.sem_tt[i][j]='*'
                        temp.sem_tt_new[i][j]='*'
        temp=temp.next

def clear3():
    temp=obj_for_class_rooms.head_for_class_rooms
    while(temp):
        if temp.name=="CSE_Sem_7" or temp.name=="CSE_Sem_8" or temp.name=="DSAI_Sem_7" or temp.name=="ECE_Sem_7" or temp.name=="DSAI_Sem_8" or temp.name=="ECE_Sem_8":
            for i in range(6):
                for j in range(8):
                    if j!=0 and i!=0:
                        temp.classroom_tt[i][j]='*'

        else:
            for i in range(6):
                for j in range(6):
                    if j!=0 and i!=0:
                        temp.classroom_tt[i][j]='*'
        temp=temp.next
def clear4():
    temp=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
    while(temp):
            for i in range(6):
                for j in range(11):
                    if j!=0 and i!=0:temp.tt[i][j]='*'
            temp=temp.next
    temp=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
    while(temp):
            for i in range(6):
                for j in range(11):
                    if j!=0 and i!=0:temp.tt[i][j]='*'
            temp=temp.next
#___________________________________________________________OBJECT CREATION____________________________________________
obj_for_linked_list_for_traversing_theory=None
obj_for_linked_list_for_traversing_labs=None
obj_for_linked_list_for_traversing_tutorials=None
obj_for_linked_list_for_merged_codes=None
obj_for_linked_list_for_electives=None
obj_for_facultys=None
obj_for_sem=None
obj_for_linked_list_for_traversing_lab_rooms=None
obj_for_class_rooms=None
obj_for_linked_list_for_traversing_theory=linked_list_for_traversing_theory()
obj_for_linked_list_for_traversing_labs=linked_list_for_traversing_labs()
obj_for_linked_list_for_traversing_tutorials=linked_list_for_traversing_tutorial()
obj_for_linked_list_for_electives=linked_list_for_electives()
obj_for_facultys=linked_list_for_faculty()
obj_for_sem=linked_list_to_travese_semester()
obj_for_linked_list_for_traversing_lab_rooms=linked_list_for_traversing_lab_rooms()
obj_for_class_rooms=linked_list_for_traversing_class_rooms()

obj_for_linked_list_for_traversing_lab_rooms.insert('L106',50,'CSE')
obj_for_linked_list_for_traversing_lab_rooms.insert('L107',50,'CSE')
obj_for_linked_list_for_traversing_lab_rooms.insert('L206',50,'CSE')
obj_for_linked_list_for_traversing_lab_rooms.insert('L207',50,'CSE')
obj_for_linked_list_for_traversing_lab_rooms.insert('L306',50,'CSE')
obj_for_linked_list_for_traversing_lab_rooms.insert('L307',50,'CSE')
obj_for_linked_list_for_traversing_lab_rooms.insert('L406',50,'ECE')
obj_for_linked_list_for_traversing_lab_rooms.insert('L407',50,'ECE')
obj_for_class_rooms.insert('DSAI_Sem_7',"C209","Sem_7")# Extra classroom to be used..
obj_for_class_rooms.insert("DSAI_Sem_8","C210","Sem_8")

#            self,code          ,type   ,name                                                  ,branch1  ,semester1       ,branch2   ,semester2  ,branch3,semester3  ,classroom_code1,code2,code3  ,faculty1                   ,faculty2        ,faculty3    ,theory   ,tutorial  ,lab   ,lab_name=None
# node_for_courses("MA103"        ,"c"    ,"Math for CS"                                         ,"CSE"    ,"Sem_2_A"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C101"  ,"NA"  ,"NA"        ,"Dr. Tanay Saha"          ,"NA"             ,"NA"        ,3      ,1       ,0)
# node_for_courses("CS102"        ,"c"    ,"Data Structures"                                     ,"CSE"    ,"Sem_2_A"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C101"  ,"NA"  ,"NA"        ,"Dr. Avantika Singh"      ,"NA"             ,"NA"        ,3      ,1       ,2   ,"CS_LAB")
# node_for_courses("CS106"        ,"c"    ,"MPMC"                                                ,"CSE"    ,"Sem_2_A"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C101"  ,"NA"  ,"NA"        ,"Dr. Kishore V"           ,"NA"             ,"NA"        ,3      ,0       ,2   ,"CS_LAB")
# node_for_courses("PH105"        ,"c"    ,"Physics for IT"                                      ,"CSE"    ,"Sem_2_A"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C101"  ,"NA"  ,"NA"        ,"Dr. Aswath Babu"         ,"NA"             ,"NA"        ,3      ,1       ,0)
# node_for_courses("HS102"        ,"c"    ,"Professional Communication"                          ,"CSE"    ,"Sem_2_A"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C101"  ,"NA"  ,"NA"        ,"Dr. Rajesh N S"          ,"NA"             ,"NA"        ,2      ,0       ,2   ,"CS_LAB")

# node_for_courses("MA103"        ,"c"    ,"Math for CS"                                         ,"CSE"    ,"Sem_2_B"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C102"  ,"NA"  ,"NA"        ,"Dr. Gokul Raj"           ,"NA"             ,"NA"        ,3      ,1       ,0)
# node_for_courses("CS102"        ,"c"    ,"Data Structures"                                     ,"CSE"    ,"Sem_2_B"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C102"  ,"NA"  ,"NA"        ,"Dr. Radhika"             ,"NA"             ,"NA"        ,3      ,1       ,2   ,"CS_LAB")
# node_for_courses("CS106"        ,"c"    ,"MPMC"                                                ,"CSE"    ,"Sem_2_B"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C102"  ,"NA"  ,"NA"        ,"Dr. Kishore V"           ,"NA"             ,"NA"        ,3      ,0       ,2   ,"CS_LAB")
# node_for_courses("PH105"        ,"c"    ,"Physics for IT"                                      ,"CSE"    ,"Sem_2_B"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C102"  ,"NA"  ,"NA"        ,"Dr. Aswath Babu"         ,"NA"             ,"NA"        ,3      ,1       ,0)
# node_for_courses("HS102"        ,"c"    ,"Professional Communication"                          ,"CSE"    ,"Sem_2_B"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C102"  ,"NA"  ,"NA"        ,"Dr. Rajesh N S"          ,"NA"             ,"NA"        ,2      ,0       ,2   ,"CS_LAB")


node_for_courses("MA201"        ,"c"    ,"Probability"                                         ,"CSE"    ,"Sem_3_A"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C201"  ,"NA"  ,"NA"        ,"Dr. Lakshman"            ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("CS201"        ,"c"    ,"Discrete mathematics"                                ,"CSE"    ,"Sem_3_A"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C201"  ,"NA"  ,"NA"        ,"Dr. Prabhu Prasad"       ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("CS207"        ,"c"    ,"object oriented prog"                                ,"CSE"    ,"Sem_3_A"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C201"  ,"NA"  ,"NA"        ,"Dr. Vivekraj"            ,"NA"             ,"NA"        ,3      ,0       ,2   ,'CS_LAB')
node_for_courses("EC105"        ,"c"    ,"Computer_Archit"                                     ,"CSE"    ,"Sem_3_A"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C201"  ,"NA"  ,"NA"        ,"Dr. Pramod Yelmewad"     ,"NA"             ,"NA"        ,3      ,0       ,2   ,'CS_LAB')
node_for_courses("CS202"        ,"c"    ,"Design and analysis of algorithms"                   ,"CSE"    ,"Sem_3_A"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C201"  ,"NA"  ,"NA"        ,"Dr. Malay Kumar"         ,"NA"             ,"NA"        ,3      ,1       ,2   ,'CS_LAB')

node_for_courses("MA201"        ,"c"    ,"Probability"                                         ,"CSE"    ,"Sem_3_B"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C202"  ,"NA"  ,"NA"        ,"Dr. Lakshman"            ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("CS201"        ,"c"    ,"Discrete mathematics"                                ,"CSE"    ,"Sem_3_B"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C202"  ,"NA"  ,"NA"        ,"Dr. Pawan Kumar"         ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("CS207"        ,"c"    ,"object oriented prog"                                ,"CSE"    ,"Sem_3_B"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C202"  ,"NA"  ,"NA"        ,"CSNF1"                   ,"NA"             ,"NA"        ,3      ,0       ,2   ,'CS_LAB')
node_for_courses("EC105"        ,"c"    ,"Computer_Archit"                                     ,"CSE"    ,"Sem_3_B"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C202"  ,"NA"  ,"NA"        ,"Dr. Prabhu Prasad"       ,"NA"             ,"NA"        ,3      ,0       ,2   ,'CS_LAB')
node_for_courses("CS202"        ,"c"    ,"Design and analysis of algorithms"                   ,"CSE"    ,"Sem_3_B"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C202"  ,"NA"  ,"NA"        ,"CSNF2"                   ,"NA"             ,"NA"        ,3      ,1       ,2   ,'CS_LAB')
node_for_courses("HS206"        ,"e"    ,"Psychology/lifeskill/soc"                            ,"CSE"    ,"Sem_3_A"       ,"CSE"     ,"Sem_3_B"  ,"NA"   ,"NA"        ,"C201"  ,"C202"  ,"NA"        ,"ODNF1"                   ,"ODNF2"          ,"ODNF3"     ,3      ,1       ,0  )

node_for_courses("CS309"        ,"c"    ,"Statistics of CS"                                    ,"CSE"    ,"Sem_5_A"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C203"  ,"NA"  ,"NA"        ,"Dr. Ramesh Athe"         ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("CS303"        ,"c"    ,"Computer Networks"                                   ,"CSE"    ,"Sem_5_A"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C203"  ,"NA"  ,"NA"        ,"Dr. Radhika B.S"         ,"NA"             ,"NA"        ,3      ,1       ,2   ,'CS_LAB')
node_for_courses("CS304"        ,"c"    ,"AI"                                                  ,"CSE"    ,"Sem_5_A"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C203"  ,"NA"  ,"NA"        ,"Dr. Jaylakshmi"          ,"NA"             ,"NA"        ,3      ,1       ,0   ,'CS_LAB')

node_for_courses("5TB1"         ,"e"    ,"ele1_sem5"                                           ,"CSE"    ,"Sem_5_A"       ,"CSE"     ,"Sem_5_B"  ,"NA"   ,"NA"        ,"C203"  ,"C204","NA"        ,"Dr. Sadhvi"              ,"Dr. Pawan Kumar"       ,"Dr. Radhika B.S"  ,3      ,1       ,0  )#tut
node_for_courses("5ELE1"        ,"e"    ,"ele2_sem5"                                           ,"CSE"    ,"Sem_5_A"       ,"CSE"     ,"Sem_5_B"  ,"NA"   ,"NA"        ,"C203"  ,"C204","NA"        ,"Dr. Rajendra"            ,"Dr. Jagadeesha R Bhat" ,"Dr. Aswath Babu"  ,3      ,1       ,0  )#tut

node_for_courses("CS309"        ,"c"    ,"Statistics of CS"                                    ,"CSE"    ,"Sem_5_B"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C204"  ,"NA"  ,"NA"        ,"Dr.Ramesh Athe"         ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("CS303"        ,"c"    ,"Computer Networks"                                   ,"CSE"    ,"Sem_5_B"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C204"  ,"NA"  ,"NA"        ,"Dr. Sadhvi"              ,"NA"             ,"NA"        ,3      ,1       ,2   ,'CS_LAB')
node_for_courses("CS304"        ,"c"    ,"AI"                                                  ,"CSE"    ,"Sem_5_B"       ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C204"  ,"NA"  ,"NA"        ,"CSNF3"                   ,"NA"             ,"NA"        ,3      ,1       ,0   ,'CS_LAB')

node_for_courses("CS461"        ,"e"    ,"Cloud Security"                                      ,"CSE"    ,"Sem_7"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C205"  ,"NA"  ,"NA"        ,"Dr. Malay Kumar"         ,"NA"             ,"NA"        ,3      ,0       ,0  )
node_for_courses("CS462"        ,"e"    ,"Computer Graphics"                                   ,"CSE"    ,"Sem_7"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C205"  ,"NA"  ,"NA"        ,"Dr. Vivekraj"            ,"NA"             ,"NA"        ,3      ,0       ,2     , "CS_LAB")
node_for_courses("DS451"        ,"e"    ,"Systems and Big Data analytics"                      ,"CSE"    ,"Sem_7"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C205"  ,"NA"  ,"NA"        ,"Dr. Animesh"             ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("CS463"        ,"e"    ,"Parallel Computing"                                  ,"CSE"    ,"Sem_7"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C205"  ,"NA"  ,"NA"        ,"Dr. Pramod Yelmewad"     ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("MA452"        ,"e"    ,"Operational Research"                                ,"CSE"    ,"Sem_7"         ,"ECE"     ,"Sem_7"    ,"NA"   ,"NA"        ,"C205"  ,"C801","NA"        ,"Dr. Gokulraj"            ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("MA453"        ,"e"    ,"Computational Linear Algebra with Applications"      ,"CSE"    ,"Sem_7"         ,"ECE"     ,"Sem_7"    ,"NA"   ,"NA"        ,"C205"  ,"C801","NA"        ,"Dr. Tanay Saha"               ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("CS451"        ,"e"    ,"Deep Learning"                                       ,"CSE"    ,"Sem_7"         ,"ECE"     ,"Sem_7"    ,"NA"   ,"NA"        ,"C205"  ,"C801","NA"        ,"Dr. Deepak K T"          ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("CS460"        ,"e"    ,"Game Theory in Computer Science"                     ,"CSE"    ,"Sem_7"         ,"ECE"     ,"Sem_7"    ,"NA"   ,"NA"        ,"C205"  ,"C801","NA"        ,"Dr. Gokulraj"            ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("CS498"        ,"e"    ,"Mini-Project-2"                                      ,"CSE"    ,"Sem_7"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C205"  ,"NA"  ,"NA"        ,"None"                    ,"NA"             ,"NA"        ,0      ,0       ,0  )

node_for_courses("EC459"        ,"e"    ,"Machine Learning for Biomedical Signal Analysis"     ,"ECE"    ,"Sem_7"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C801"  ,"NA"  ,"NA"        ,"Dr. Sibasankar"          ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("EC458"        ,"e"    ,"Statistical Signal Processing"                       ,"ECE"    ,"Sem_7"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C801"  ,"NA"  ,"NA"        ,"Dr. Chinmayananda"       ,"NA"             ,"NA"        ,3      ,1       ,0  )

# node_for_courses("DS105"        ,"c"    ,"Probability and statistics"                          ,"DSAI"   ,"Sem_2"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C401"  ,"NA"  ,"NA"        ,"Dr. Ramesh Athe"         ,"NA"             ,"NA"        ,3      ,1       ,0  )
# node_for_courses("CS102"        ,"c"    ,"Data Structures"                                     ,"DSAI"   ,"Sem_2"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C401"  ,"NA"  ,"NA"        ,"Dr. Sunil Saumya"        ,"NA"             ,"NA"        ,3      ,1       ,2   ,'CS_LAB')
# node_for_courses("EG101"        ,"c"    ,"Engineering101"                                      ,"DSAI"   ,"Sem_2"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C401"  ,"NA"  ,"NA"        ,"Dr. Rajib Sharma"        ,"NA"             ,"NA"        ,2      ,1       ,2   ,'CS_LAB')
# node_for_courses("HS107"        ,"c"    ,"Economics"                                           ,"DSAI"   ,"Sem_2"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C401"  ,"NA"  ,"NA"        ,"Ms. Anushree K"          ,"NA"             ,"NA"        ,3      ,1       ,0   )
# node_for_courses("HS102"        ,"c"    ,"Professional Communication"                          ,"DSAI"   ,"Sem_2"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C401"  ,"NA"  ,"NA"        ,"Dr. Manjusha C B"        ,"NA"             ,"NA"        ,2      ,0       ,2   ,'CS_LAB')

node_for_courses("DS201"        ,"c"    ,"Data and Business Analytics"                         ,"DSAI"   ,"Sem_3"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C501"  ,"NA"  ,"NA"        ,"Dr. Rajib Sharma"        ,"NA"             ,"NA"        ,3      ,0       ,0  )
node_for_courses("CS201"        ,"c"    ,"Discrete Mathematics"                                ,"DSAI"   ,"Sem_3"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C501"  ,"NA"  ,"NA"        ,"Dr. Hariprasad HS"       ,"NA"             ,"NA"        ,3      ,1       ,0   ,'CS_LAB')
node_for_courses("CS207"        ,"c"    ,"Object Oriented Programming"                         ,"DSAI"   ,"Sem_3"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C501"  ,"NA"  ,"NA"        ,"Dr. Manjunath V"         ,"NA"             ,"NA"        ,3      ,0       ,2   ,'CS_LAB')
node_for_courses("HS201"        ,"c"    ,"Industrial Psychology"                               ,"DSAI"   ,"Sem_3"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C501"  ,"NA"  ,"NA"        ,"Ms. Anushree K"          ,"NA"             ,"NA"        ,3      ,0       ,0   )
node_for_courses("CS202"        ,"c"    ,"Design and Analysis of Algorithms"                   ,"DSAI"   ,"Sem_3"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C501"  ,"NA"  ,"NA"        ,"Dr. Sunil Saumya"        ,"NA"             ,"NA"        ,3      ,1       ,2   ,'CS_LAB')
node_for_courses("HS202"        ,"c"    ,"Ethics"                                              ,"DSAI"   ,"Sem_3"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C501"  ,"NA"  ,"NA"        ,"Dr. Rajesh N S"          ,"NA"             ,"NA"        ,3      ,0       ,0  )

node_for_courses("DS204"        ,"c"    ,"Graphs and Social Networks"                          ,"DSAI"   ,"Sem_5"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C601"  ,"NA"  ,"NA"        ,"Dr. Utkarsh"             ,"NA"             ,"NA"        ,3      ,1       ,0   ,'CS_LAB')
node_for_courses("DS205"        ,"c"    ,"Computer Communication Networks"                     ,"DSAI"   ,"Sem_5"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C601"  ,"NA"  ,"NA"        ,"Dr. Rajib Sharma"        ,"NA"             ,"NA"        ,3      ,1       ,2   ,'CS_LAB')
node_for_courses("DS206"        ,"c"    ,"Algorithms and Artificial Intelligence"              ,"DSAI"   ,"Sem_5"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C601"  ,"NA"  ,"NA"        ,"Ms. Animesh"             ,"NA"             ,"NA"        ,3      ,1       ,0   )
node_for_courses("DS207"        ,"c"    ,"Machine Learning"                                    ,"DSAI"   ,"Sem_5"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C601"  ,"NA"  ,"NA"        ,"Dr. Sunil Saumya"        ,"NA"             ,"NA"        ,3      ,1       ,0   ,'CS_LAB')
node_for_courses("DS208"        ,"c"    ,"Visualization and App Development"                   ,"DSAI"   ,"Sem_5"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C601"  ,"NA"  ,"NA"        ,"Dr. Manjunath"           ,"NA"             ,"NA"        ,2      ,1       ,2   ,'CS_LAB')

node_for_courses("HS102"        ,"c"    ,"Professional Communication"                          ,"ECE"    ,"Sem_3"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C701"  ,"NA"  ,"NA"        ,"Dr. Rajesh N S"          ,"NA"             ,"NA"        ,2      ,1       ,0  )
node_for_courses("MA202"        ,"c"    ,"Linear Algebra"                                      ,"ECE"    ,"Sem_3"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C701"  ,"NA"  ,"NA"        ,"Dr. Anand"               ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("EC207"        ,"c"    ,"Electromagnetic theory"                              ,"ECE"    ,"Sem_3"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C701"  ,"NA"  ,"NA"        ,"Dr. Samen B"             ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("EC206"        ,"c"    ,"Linear integrated circuits"                          ,"ECE"    ,"Sem_3"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C701"  ,"NA"  ,"NA"        ,"Dr. Prakash Pawar"       ,"NA"             ,"NA"        ,3      ,0       ,2   ,'EC_LAB')
node_for_courses("EC201"        ,"c"    ,"Signals and Systems"                                 ,"ECE"    ,"Sem_3"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C701"  ,"NA"  ,"NA"        ,"Dr. Mukesh Kunar Mishra" ,"NA"             ,"NA"        ,3      ,1       ,0   )
node_for_courses("EC202"        ,"c"    ,"MPMC"                                                ,"ECE"    ,"Sem_3"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C701"  ,"NA"  ,"NA"        ,"Dr. Nataraj"             ,"NA"             ,"NA"        ,3      ,0       ,2   ,'CS_LAB')

node_for_courses("EC306"        ,"c"    ,"Professional Communication"                          ,"ECE"    ,"Sem_5"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C701"  ,"NA"  ,"NA"        ,"Dr. Chinmayananda"       ,"NA"             ,"NA"        ,2      ,1       ,0  )
node_for_courses("EC301"        ,"c"    ,"Linear Algebra"                                      ,"ECE"    ,"Sem_5"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C701"  ,"NA"  ,"NA"        ,"Dr. Jagadish D N"        ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("HS351"        ,"c"    ,"Electromagnetic theory"                              ,"ECE"    ,"Sem_5"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C701"  ,"NA"  ,"NA"        ,"Dr. Anand Barangi"       ,"NA"             ,"NA"        ,3      ,1       ,0  )
node_for_courses("EC351"        ,"c"    ,"Linear integrated circuits"                          ,"ECE"    ,"Sem_5"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C701"  ,"NA"  ,"NA"        ,"Dr. Utkarsh"             ,"NA"             ,"NA"        ,3      ,1       ,0   ,'EC_LAB')
node_for_courses("EC357"        ,"c"    ,"Signals and Systems"                                 ,"ECE"    ,"Sem_5"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C701"  ,"NA"  ,"NA"        ,"Dr. Mukesh Kunar Mishra" ,"NA"             ,"NA"        ,3      ,1       ,0   )
node_for_courses("CS352/EC359/PH351","e","ece7_ele"                                            ,"ECE"    ,"Sem_5"         ,"NA"      ,"NA"       ,"NA"   ,"NA"        ,"C701"  ,"NA"  ,"NA"        ,"Dr. Rajemdra Hegadi"     ,"Dr. Jagadeesha R Bhat" ,"Dr. Aswath"        ,3      ,1       ,0   ,'CS_LAB')

def workload_calculate():
    for i in range(15):
        if i==0:temp=obj_for_linked_list_for_traversing_labs.head_for_CSE
        if i==1:temp=obj_for_linked_list_for_traversing_theory.head_for_CSE
        if i==2:temp=obj_for_linked_list_for_traversing_tutorials.head_for_CSE
        if i==3:temp=obj_for_linked_list_for_traversing_labs.head_for_DSAI
        if i==4:temp=obj_for_linked_list_for_traversing_theory.head_for_DSAI
        if i==5:temp=obj_for_linked_list_for_traversing_tutorials.head_for_DSAI
        if i==6:temp=obj_for_linked_list_for_traversing_labs.head_for_ECE
        if i==7:temp=obj_for_linked_list_for_traversing_theory.head_for_ECE
        if i==8:temp=obj_for_linked_list_for_traversing_tutorials.head_for_ECE
        if i==9:temp=obj_for_linked_list_for_electives.head_for_lab
        if i==10:temp=obj_for_linked_list_for_electives.head_for_theory
        if i==11:temp=obj_for_linked_list_for_electives.head_for_tutorial
        while(temp):
            temp1=obj_for_facultys.head_for_faculty_names
            while(temp1):
                if temp1.faculty_name==temp.faculty1:break
                temp1=temp1.next
            if temp1!=None:
                if temp.lab:temp1.workload+=(temp.lab*2)
                if temp.theory:temp1.workload+=(temp.theory)
                if temp.tutorial:temp1.workload+=(temp.tutorial)
            temp=temp.next
def sort_faculty_list():
        current = obj_for_facultys.head_for_faculty_names;
        index = None
        if(current == None):return
        else:
            while(current != None):
                index = current.next;
                while(index != None):
                    if(current.workload < index.workload):
                        tp = current.workload;
                        current.workload = index.workload;
                        index.workload = tp;
                        tp = current.faculty_id;
                        current.faculty_id = index.faculty_id;
                        index.faculty_id = tp;
                        tp = current.faculty_name;
                        current.faculty_name = index.faculty_name;
                        index.faculty_name = tp;
                        tp = current.faculty_tt;
                        current.faculty_tt = index.faculty_tt;
                        index.faculty_tt = tp;
                    index = index.next;
                current = current.next;















































def registerPage(request):
    form=UserCreationForm()
    context={'form':form}
    return render(request,'register.html',context)

def loginPage(request):
    context={}
    return render(request,'login.html',context)

def login1(request):
    return render(request,'login1.html')

def add(request):
        code=request.POST['code']
        name=request.POST['name']
        branch=request.POST['branch']
        semester=request.POST['semester']
        credit=(request.POST['credit'])
        faculty=request.POST['faculty']
        theory=int(request.POST['theory'])
        tutorial=int(request.POST['tutorial'])
        lab=int(request.POST['lab'])
        lab_name=(request.POST['lab_name'])
        node_for_courses(code,name,branch,semester,credit,faculty,theory,tutorial,lab,lab_name)
        return render(request,'getstarted.html')

num=0

def ind(request):
    global num
    if num==0:
        datas=data.objects.all()
        for i in datas:
            node_for_courses(remove_spaces(i.code),remove_spaces(i.type),remove_spaces(i.name),remove_spaces(i.branch1),remove_spaces(i.semester1),remove_spaces(i.branch2),remove_spaces(i.semester2),remove_spaces(i.branch3),remove_spaces(i.semester3),remove_spaces(i.classroom_code1),remove_spaces(i.classroom_code2),remove_spaces(i.classroom_code3),remove_spaces(i.faculty1),remove_spaces(i.faculty2),remove_spaces(i.faculty3),(i.theory),(i.tutorial),(i.lab),remove_spaces(i.lab_name))
        num=1
    return render(request,'index.html')

def about(request):
    return render(request,'About.html')

def get(request):
    return render(request,'getstarted.html')

def stu(request):
    return render(request,'Student-Time-Table.html')

def fac(request):
    return render(request,'Faculty-time-table.html')

def contact(request):
    return render(request,'Contact.html')

def faculty(request):
    lists=[]
    names=[]
    clear1()
    clear2()
    clear3()
    clear4()
    obj_for_linked_list_for_traversing_theory.head_for_CSE=None
    obj_for_linked_list_for_traversing_theory.head_for_DSAI=None
    obj_for_linked_list_for_traversing_theory.head_for_ECE=None

    obj_for_linked_list_for_traversing_labs.head_for_CSE=None
    obj_for_linked_list_for_traversing_labs.head_for_DSAI=None
    obj_for_linked_list_for_traversing_labs.head_for_ECE=None

    obj_for_linked_list_for_traversing_tutorials.head_for_CSE=None
    obj_for_linked_list_for_traversing_tutorials.head_for_DSAI=None
    obj_for_linked_list_for_traversing_tutorials.head_for_ECE=None

    obj_for_linked_list_for_electives.head_for_theory=None
    obj_for_linked_list_for_electives.head_for_tutorial=None
    obj_for_linked_list_for_electives.head_for_lab=None
    obj_for_facultys.head_for_faculty_names=None
    obj_for_sem.head_for_semesters=None
    obj_for_class_rooms.head_for_class_rooms=None
    datas=data.objects.all()
    for i in datas:
            node_for_courses(remove_spaces(i.code),remove_spaces(i.type),remove_spaces(i.name),remove_spaces(i.branch1),remove_spaces(i.semester1),remove_spaces(i.branch2),remove_spaces(i.semester2),remove_spaces(i.branch3),remove_spaces(i.semester3),remove_spaces(i.classroom_code1),remove_spaces(i.classroom_code2),remove_spaces(i.classroom_code3),remove_spaces(i.faculty1),remove_spaces(i.faculty2),remove_spaces(i.faculty3),(i.theory),(i.tutorial),(i.lab),remove_spaces(i.lab_name))
    workload_calculate()
    sort_faculty_list()
    plotting()
    plotting_for_electives()
    zipped_variable=zip(lists,names)
    temp1=obj_for_facultys.head_for_faculty_names
    while(temp1):
        names.append(temp1.faculty_name)
        lists.append(temp1.faculty_tt)
        temp1=temp1.next
    zipped_variable=zip(lists,names)
    return render(request,'Faculty-time-table.html',{'zipped':zipped_variable})

def remove_spaces(str):
    str1=str.replace(' ','')
    return str1

def student(request):
    #CSE_______________________________________
    #                         (self        ,code         ,name    ,branch ,semester   ,credit ,faculty       ,faculty_id,theory,tutorial,lab)
    #SEM_1
    lists=[]
    sem=[]
    clear1()
    clear2()
    clear3()
    clear4()
    obj_for_linked_list_for_traversing_theory.head_for_CSE=None
    obj_for_linked_list_for_traversing_theory.head_for_DSAI=None
    obj_for_linked_list_for_traversing_theory.head_for_ECE=None

    obj_for_linked_list_for_traversing_labs.head_for_CSE=None
    obj_for_linked_list_for_traversing_labs.head_for_DSAI=None
    obj_for_linked_list_for_traversing_labs.head_for_ECE=None

    obj_for_linked_list_for_traversing_tutorials.head_for_CSE=None
    obj_for_linked_list_for_traversing_tutorials.head_for_DSAI=None
    obj_for_linked_list_for_traversing_tutorials.head_for_ECE=None

    obj_for_linked_list_for_electives.head_for_theory=None
    obj_for_linked_list_for_electives.head_for_tutorial=None
    obj_for_linked_list_for_electives.head_for_lab=None
    obj_for_facultys.head_for_faculty_names=None
    obj_for_sem.head_for_semesters=None
    obj_for_class_rooms.head_for_class_rooms=None
    datas=data.objects.all()
    for i in datas:
            # print(remove_spaces(i.code),remove_spaces(i.type),remove_spaces(i.name),remove_spaces(i.branch1),remove_spaces(i.semester1),remove_spaces(i.branch2),remove_spaces(i.semester2),remove_spaces(i.branch3),remove_spaces(i.semester3),remove_spaces(i.classroom_code1),remove_spaces(i.classroom_code2),remove_spaces(i.classroom_code3),remove_spaces(i.faculty1),remove_spaces(i.faculty2),remove_spaces(i.faculty3),(i.theory),(i.tutorial),(i.lab),remove_spaces(i.lab_name))
            node_for_courses(remove_spaces(i.code),remove_spaces(i.type),remove_spaces(i.name),remove_spaces(i.branch1),remove_spaces(i.semester1),remove_spaces(i.branch2),remove_spaces(i.semester2),remove_spaces(i.branch3),remove_spaces(i.semester3),remove_spaces(i.classroom_code1),remove_spaces(i.classroom_code2),remove_spaces(i.classroom_code3),remove_spaces(i.faculty1),remove_spaces(i.faculty2),remove_spaces(i.faculty3),(i.theory),(i.tutorial),(i.lab),remove_spaces(i.lab_name))

    workload_calculate()
    sort_faculty_list()
    plotting()
    plotting_for_electives()
    temp1=obj_for_sem.head_for_semesters
    zipped_variable=zip(lists,sem)
    while(temp1):
        sem.append(temp1.sem)
        if temp1:
            lists.append(temp1.sem_tt_new)
        zipped_variable=zip(lists,sem)
        temp1=temp1.next
    return render(request,'Student-Time-Table.html',{'zipped':zipped_variable})

def classroom(request):
    lists=[]
    sem=[]
    clear1()
    clear2()
    clear3()
    clear4()
    obj_for_linked_list_for_traversing_theory.head_for_CSE=None
    obj_for_linked_list_for_traversing_theory.head_for_DSAI=None
    obj_for_linked_list_for_traversing_theory.head_for_ECE=None

    obj_for_linked_list_for_traversing_labs.head_for_CSE=None
    obj_for_linked_list_for_traversing_labs.head_for_DSAI=None
    obj_for_linked_list_for_traversing_labs.head_for_ECE=None

    obj_for_linked_list_for_traversing_tutorials.head_for_CSE=None
    obj_for_linked_list_for_traversing_tutorials.head_for_DSAI=None
    obj_for_linked_list_for_traversing_tutorials.head_for_ECE=None

    obj_for_linked_list_for_electives.head_for_theory=None
    obj_for_linked_list_for_electives.head_for_tutorial=None
    obj_for_linked_list_for_electives.head_for_lab=None
    obj_for_facultys.head_for_faculty_names=None
    obj_for_sem.head_for_semesters=None
    obj_for_class_rooms.head_for_class_rooms=None
    datas=data.objects.all()
    for i in datas:
            node_for_courses(remove_spaces(i.code),remove_spaces(i.type),remove_spaces(i.name),remove_spaces(i.branch1),remove_spaces(i.semester1),remove_spaces(i.branch2),remove_spaces(i.semester2),remove_spaces(i.branch3),remove_spaces(i.semester3),remove_spaces(i.classroom_code1),remove_spaces(i.classroom_code2),remove_spaces(i.classroom_code3),remove_spaces(i.faculty1),remove_spaces(i.faculty2),remove_spaces(i.faculty3),(i.theory),(i.tutorial),(i.lab),remove_spaces(i.lab_name))
    workload_calculate()
    sort_faculty_list()
    plotting()
    plotting_for_electives()
    temp1=obj_for_class_rooms.head_for_class_rooms
    zipped_variable=zip(lists,sem)
    while(temp1):
        sem.append(temp1.name)
        lists.append(temp1.classroom_tt)
        zipped_variable=zip(lists,sem)
        temp1=temp1.next
    return render(request,'classroom.html',{'zipped':zipped_variable})

def faculty(request):
    lists=[]
    sem=[]
    clear1()
    clear2()
    clear3()
    clear4()
    obj_for_linked_list_for_traversing_theory.head_for_CSE=None
    obj_for_linked_list_for_traversing_theory.head_for_DSAI=None
    obj_for_linked_list_for_traversing_theory.head_for_ECE=None

    obj_for_linked_list_for_traversing_labs.head_for_CSE=None
    obj_for_linked_list_for_traversing_labs.head_for_DSAI=None
    obj_for_linked_list_for_traversing_labs.head_for_ECE=None

    obj_for_linked_list_for_traversing_tutorials.head_for_CSE=None
    obj_for_linked_list_for_traversing_tutorials.head_for_DSAI=None
    obj_for_linked_list_for_traversing_tutorials.head_for_ECE=None

    obj_for_linked_list_for_electives.head_for_theory=None
    obj_for_linked_list_for_electives.head_for_tutorial=None
    obj_for_linked_list_for_electives.head_for_lab=None
    obj_for_facultys.head_for_faculty_names=None
    obj_for_sem.head_for_semesters=None
    obj_for_class_rooms.head_for_class_rooms=None
    datas=data.objects.all()
    for i in datas:
            node_for_courses(remove_spaces(i.code),remove_spaces(i.type),remove_spaces(i.name),remove_spaces(i.branch1),remove_spaces(i.semester1),remove_spaces(i.branch2),remove_spaces(i.semester2),remove_spaces(i.branch3),remove_spaces(i.semester3),remove_spaces(i.classroom_code1),remove_spaces(i.classroom_code2),remove_spaces(i.classroom_code3),remove_spaces(i.faculty1),remove_spaces(i.faculty2),remove_spaces(i.faculty3),(i.theory),(i.tutorial),(i.lab),remove_spaces(i.lab_name))
    workload_calculate()
    sort_faculty_list()
    plotting()
    plotting_for_electives()
    temp1=obj_for_facultys.head_for_faculty_names
    zipped_variable=zip(lists,sem)
    while(temp1):
        sem.append(temp1.faculty_name)
        lists.append(temp1.faculty_tt)
        zipped_variable=zip(lists,sem)
        temp1=temp1.next
    return render(request,'faculty.html',{'zipped':zipped_variable})

def lab(request):
    lists=[]
    sem=[]
    clear1()
    clear2()
    clear3()
    clear4()
    obj_for_linked_list_for_traversing_theory.head_for_CSE=None
    obj_for_linked_list_for_traversing_theory.head_for_DSAI=None
    obj_for_linked_list_for_traversing_theory.head_for_ECE=None

    obj_for_linked_list_for_traversing_labs.head_for_CSE=None
    obj_for_linked_list_for_traversing_labs.head_for_DSAI=None
    obj_for_linked_list_for_traversing_labs.head_for_ECE=None

    obj_for_linked_list_for_traversing_tutorials.head_for_CSE=None
    obj_for_linked_list_for_traversing_tutorials.head_for_DSAI=None
    obj_for_linked_list_for_traversing_tutorials.head_for_ECE=None

    obj_for_linked_list_for_electives.head_for_theory=None
    obj_for_linked_list_for_electives.head_for_tutorial=None
    obj_for_linked_list_for_electives.head_for_lab=None
    obj_for_facultys.head_for_faculty_names=None
    obj_for_sem.head_for_semesters=None
    obj_for_class_rooms.head_for_class_rooms=None
    datas=data.objects.all()
    for i in datas:
        node_for_courses(remove_spaces(i.code),remove_spaces(i.type),remove_spaces(i.name),remove_spaces(i.branch1),remove_spaces(i.semester1),remove_spaces(i.branch2),remove_spaces(i.semester2),remove_spaces(i.branch3),remove_spaces(i.semester3),remove_spaces(i.classroom_code1),remove_spaces(i.classroom_code2),remove_spaces(i.classroom_code3),remove_spaces(i.faculty1),remove_spaces(i.faculty2),remove_spaces(i.faculty3),(i.theory),(i.tutorial),(i.lab),remove_spaces(i.lab_name))
    workload_calculate()
    sort_faculty_list()
    plotting()
    plotting_for_electives()
    zipped_variable=zip(lists,sem)
    temp1=obj_for_linked_list_for_traversing_lab_rooms.head_for_CSE_rooms
    temp2=obj_for_linked_list_for_traversing_lab_rooms.head_for_ECE_rooms
    while(temp1):
        sem.append(temp1.name)
        lists.append(temp1.tt)
        zipped_variable=zip(lists,sem)
        temp1=temp1.next
    while(temp2):
        sem.append(temp2.name)
        lists.append(temp2.tt)
        zipped_variable=zip(lists,sem)
        temp2=temp2.next
    return render(request,'lab.html',{'zipped':zipped_variable})

def refresh_page(request):
    return render(request,'Contact.html')

def ref(request):
    clear1()
    clear2()
    clear3()
    clear4()
    obj_for_linked_list_for_traversing_theory.head_for_CSE=None
    obj_for_linked_list_for_traversing_theory.head_for_DSAI=None
    obj_for_linked_list_for_traversing_theory.head_for_ECE=None

    obj_for_linked_list_for_traversing_labs.head_for_CSE=None
    obj_for_linked_list_for_traversing_labs.head_for_DSAI=None
    obj_for_linked_list_for_traversing_labs.head_for_ECE=None

    obj_for_linked_list_for_traversing_tutorials.head_for_CSE=None
    obj_for_linked_list_for_traversing_tutorials.head_for_DSAI=None
    obj_for_linked_list_for_traversing_tutorials.head_for_ECE=None

    obj_for_linked_list_for_electives.head_for_theory=None
    obj_for_linked_list_for_electives.head_for_tutorial=None
    obj_for_linked_list_for_electives.head_for_lab=None
    obj_for_facultys.head_for_faculty_names=None
    obj_for_sem.head_for_semesters=None
    obj_for_class_rooms.head_for_class_rooms=None
    datas=data.objects.all()
    for i in datas:
        node_for_courses(remove_spaces(i.code),remove_spaces(i.type),remove_spaces(i.name),remove_spaces(i.branch1),remove_spaces(i.semester1),remove_spaces(i.branch2),remove_spaces(i.semester2),remove_spaces(i.branch3),remove_spaces(i.semester3),remove_spaces(i.classroom_code1),remove_spaces(i.classroom_code2),remove_spaces(i.classroom_code3),remove_spaces(i.faculty1),remove_spaces(i.faculty2),remove_spaces(i.faculty3),(i.theory),(i.tutorial),(i.lab),remove_spaces(i.lab_name))

    return render(request,'Contact.html')

@permission_required('admin.can_add_log_enter')
def contact_upload(request):
    template="contact_upload.html"
    prompt=None
    if request.method=="GET":
        return render(request,template,prompt)
    if len(request.FILES['file'])==0:
        return redirect('/')
    csv_file=request.FILES['file']
    # if not csv_file.name.endswith('.csv'):
    #     messages.error(request,'This is not a CSV file!')
    # if len(request.FILES)==0:
    #     return redirect('/')

    data_set=csv_file.read().decode('UTF-8')
    io_string=io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string,delimiter=',',quotechar="|"):
        _, created=data.objects.update_or_create(
            code = column[0],
            type=column[1],      
            name = column[2],             
            branch1 = column[3], 
            semester1 = column[4], 
            branch2 = column[5], 
            semester2 = column[6], 
            branch3 = column[7], 
            semester3 = column[8], 
            classroom_code1 = column[9],
            classroom_code2 = column[10], 
            classroom_code3 = column[11],
            faculty1 = column[12],
            faculty2 = column[13],
            faculty3 = column[14],           
            theory = (column[15]),
            tutorial = (column[16]),
            lab = (column[17]),
            lab_name = column[18]
              )
       
        context={}
        return render(request,template,context)

def dele(request):
    datas=data.objects.all()
    lt=[]
    for i in datas:
        lt=(int(i.id))
        instance = data.objects.get(id=lt)
        instance.delete()   
    return redirect('/') 

def dele2(request):
    return redirect('/home')
from django.shortcuts import redirect  
  
def redirect_view(request):  
    response = redirect('')  
    return response  


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
                user.save()
                
                return redirect('login')


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
    if request.method=="GET":
        return redirect('home')     
#login_user
    else:
        return render(request, 'registeration.html')
from django.contrib.auth.models import User, auth
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')



    else:
        return render(request, 'login.html')

def logout_user(request):
    auth.logout(request)
    return redirect('home')
    
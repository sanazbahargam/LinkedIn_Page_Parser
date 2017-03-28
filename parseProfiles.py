import os


data=''
if os.path.exists('parsed/profiles.txt'):
    os.remove('parsed/profiles.txt')
 
counter = 0 
for profile in os.listdir('./profiles'):
    counter +=1
    if counter%100==0:
        print('Working at ' +str(counter))
    path = './profiles/'+profile
    with open (path, mode='r', encoding='utf-8') as f:
        #print(profile)
        prof = f.read()
        
        #name----------------------------------------------
        start = prof.find('domain=linkedin.com')+57
        end = start + prof[start:].find('| LinkedIn</title>')-1
        name = prof[start:end]
        if len(name)<=4:
            continue
        if '&#40;' in name:
            name = name.replace('&#40;', '')
        if '&#41;' in name:
            name = name.replace('&#41;', '')
        
        name = name.replace('\t','').replace('\n','')
        if name=='':
            name='0'
        
        
        #miniJob-------------------------------------------
        start = prof.find('<p class="title"')+16
        mid = prof[start:].find('>')+1
        end = prof[start:].find('</p>')
        if start!=15 and end!=-1 and mid!=-1:
            miniJob = prof[start+mid:start+end]
        else:
            miniJob = '0'
            continue
        
        miniJob = miniJob.replace('\t','').replace('\n','')
        if miniJob=='':
            miniJob='0'
        
        #miniArea-------------------------------------------
        start = prof.find('name=\'location\'')
        end = prof[start:].find('</a>')
        mid = prof[start:start+end].find('>')+1
        if start!=-1 and mid!=-1 and end!=-1:
            miniArea = prof[start+mid:start+end]
        else:
            miniArea = '0'
        
        miniArea = miniArea.replace('\t','').replace('\n','')
        if miniArea=='':
            miniArea='0'
            
        
        #miniIndustry---------------------------------------
        start = prof.find('name="industry"')
        end = prof[start:].find('</a>')
        mid = prof[start:start+end].find('>')+1
        if start!=-1 and mid!=-1 and end!=-1:
            miniIndustry = prof[start+mid:start+end]
        else:
            miniIndustry = '0'
        
        miniIndustry = miniIndustry.replace('\t','').replace('\n','')
        if miniIndustry=='':
            miniIndustry='0'
        
        #miniCurrent---------------------------------------
        miniCurrent = ''
        start=0
        for i in range(1,20):
            if prof[start:].find('prof-0-ovw-curr_pos" dir')==-1:
               if i==1:
                    miniCurrent = '0||||'
               break 
            start = start + prof[start:].find('prof-0-ovw-curr_pos" dir')
            mid = prof[start:].find('>')+1
            end = prof[start:].find('</a>')
            miniCurrent = miniCurrent + prof[start+mid:start+end] +'||||'
            start = start+end
        miniCurrent = miniCurrent[:len(miniCurrent)-4]
        
        miniCurrent = miniCurrent.replace('\t','').replace('\n','')
        if miniCurrent=='':
            miniCUrrent='0'

        #miniPrevious--------------------------------------
        miniPrevious = ''
        start=0
        for i in range(1,20):
            if prof[start:].find('prof-0-ovw-prev_pos"')==-1:
               if i==1:
                    miniPrevious = '0||||'
               break 
            start = start + prof[start:].find('prof-0-ovw-prev_pos"')
            mid = prof[start:].find('>')+1
            end = prof[start:].find('</a>')
            miniPrevious = miniPrevious + prof[start+mid:start+end] +'||||'
            start = start+end
        miniPrevious = miniPrevious[:len(miniPrevious)-4]
        
        miniPrevious = miniPrevious.replace('\t','').replace('\n','')
        if miniPrevious=='':
            miniPrevious='0'

        #miniEducation--------------------------------------
        start = prof.find('prof-0-ovw-edu"')
        if start==-1:
            start = prof.find('trk=prof-edu-school-name')
            if start==-1:
                miniEducation = '0'
            else:
                mid = prof[start:].find('>')+1
                end = prof[start:].find('</a>')
                miniEducation = prof[start+mid:start+end]    
        else:
            mid = prof[start:].find('>')+1
            end = prof[start:].find('</a>')
            miniEducation = prof[start+mid:start+end] 
        
        miniEducation = miniEducation.replace('\t','').replace('\n','')
        if miniEducation=='':
            miniEducation='0'        
        
        
        #miniConnections------------------------------------
        start = prof.find('<div class="member-connections"><strong>')+40
        end = prof[start:].find('</strong>')
        miniConnections = prof[start:start+end]
        if miniConnections.isdigit()==False and prof.find('connections-link')!=-1 :
            start = prof.find('connections-link')+18
            end = prof[start:].find('<')
            miniConnections = prof[start:start+end]
        if miniConnections.isdigit()==False and miniConnections!='500+':      
            continue
        
        miniConnections = miniConnections.replace('\t','').replace('\n','')
        if miniConnections=='':
            miniConnections='0'
        
        #--------------------------------------------------       
        #summary-------------------------------------------
        #--------------------------------------------------
        start = prof.find('<div class="summary"><p class="description" dir="ltr">')+54
        end = start + prof[start:].find('</p>')
        if start!=53:        
            summary = prof[start:end].replace('&#x2022;','-').replace('\n','').replace('\t','')
        else:
            summary = '0'
        
        summary = summary.replace('\t','').replace('\n','')
        if summary=='':
            summary='0'
           
        #-------------------------------------------------       
        #experience----------------------------------------
        #--------------------------------------------------
        experience = ''
        start=0
        anchor = 'name=\'title\'' 
        for i in range(1,60):
            if prof[start:].find(anchor)==-1:
               if i==1:
                  anchor='title="Learn more about this title"'
                  if prof[start:].find(anchor)==-1:
                      experience = '0||||'                 
               if prof[start:].find(anchor)==-1:
                  break
            #title
            start = start + prof[start:].find(anchor)
            if prof[start+3:].find(anchor) ==-1:
                nextUp = start + 1000
            else:
                nextUp = start+prof[start+5:].find(anchor)
            mid = prof[start:].find('>')+1
            end = prof[start:].find('</a>')
            experience = experience + prof[start+mid:start+end] +'||'
            start = start+end
            #company
            start = start + prof[start:].find('dir="auto">')
            mid = prof[start:].find('>')+1
            end = prof[start:].find('</a>')
            experience = experience + prof[start+mid:start+end] +'||'
            start = start+end            
            #start
            start = start + prof[start:].find('<time>')
            mid = prof[start:].find('>')+1
            end = prof[start+mid:].find('<')
            experience = experience + prof[start+mid:start+mid+end] +'--'
            start = start+end
            #end
            start = start + prof[start:].find('&#8211;')+8
            end = prof[start:].find('(')-1
            experience = experience + prof[start:start+end].replace('<time>','').replace('</time>','')+'||'
            start = start+end
            #summary
            temp = prof[start:].find('dir="ltr">')
            if start+temp<nextUp:
                start = start+prof[start:].find('dir="ltr">')
                mid = prof[start:].find('>')+1
                end = prof[start+mid:].find('</p>')
                if '</a>' in prof[start+mid:start+mid+end]:
                    experience=experience+'nosummary||||'
                else:
                    experience = experience+ prof[start+mid:start+mid+end].replace('&#x2022;','-').replace('\n','').replace('\t','')+'||||'
            else:
                experience=experience+'nosummary||||'
        experience = experience[:len(experience)-4]
        
        experience = experience.replace('\t','').replace('\n','')
        if experience=='':
            experience='0'         
        
        #------------------------------------------------
        #Skills------------------------------------------
        #------------------------------------------------
        skills = ''
        start=0
        for i in range(1,80):
            if prof[start:].find('data-endorsed-item-name="')==-1:
               if i==1:
                    skills = '0||||'
               break 
            #skill
            start = start + prof[start:].find('data-endorsed-item-name="')
            mid = prof[start:].find('"')+1
            end = prof[start+mid:].find('"')
            skills = skills + prof[start+mid:start+mid+end]
            start = start+mid+end
            #endorsements
            start = start + prof[start:].find('class="endorse-item')
            mid = prof[start:].find('"')+1
            end = prof[start+mid:].find('"')
            if 'has-endorsements' in prof[start+mid:start+mid+end]:
                start = start + prof[start:].find('data-count="')
                mid = prof[start:].find('"')+1
                end = prof[start+mid:].find('"')
                skills = skills + '||'+prof[start+mid:start+mid+end] +'||||'
            else:
                skills = skills + '||0' +'||||'
            start = start+end            
        if skills=='0||||':
            skills=''
            start=0
            for i in range(1,80):
                if prof[start:].find('endorse-item-name-text')==-1:
                   if i==1:
                        skills = '0||||'
                   break 
                #skill
                start = start + prof[start:].find('endorse-item-name-text')
                mid = prof[start:].find('>')+1
                end = prof[start+mid:].find('<')
                skills = skills + prof[start+mid:start+mid+end] +'||0||||'
                start = start+mid+end

        skills = skills[:len(skills)-4]
        
        skills = skills.replace('\t','').replace('\n','')
        if skills=='':
            skills='0'
        
        #--------------------------------------------------        
        #education-----------------------------------------
        #--------------------------------------------------
        education = ''
        start=prof.find('<h3>Education</h3>')
        for i in range(1,10):
            if start==-1:
                education = '0||||'
                break
            if prof[start:].find('trk=prof-edu-school-name')==-1:
               if i==1:
                    education = '0||||'
               break
            #school
            start = start + prof[start:].find('trk=prof-edu-school-name')
            mid = prof[start:].find('>')+1
            end = prof[start+mid:].find('<')
            education = education + prof[start+mid:start+mid+end]
            start = start+mid+end
            if prof[start:].find('trk=prof-edu-school-name') ==-1:
                nextUp = start+10000
            else:
                nextUp = start+prof[start:].find('trk=prof-edu-school-name')
            #degree,majors,time  
            degree = 'nodegree'
            time = 'notime'
            major  = 'nomajor'
            for i in range(1,5):           
                start = start + prof[start:].find('<span class=')
                if start > nextUp:
                    break
                mid = prof[start:].find('"')+1
                end = prof[start+mid:].find('"')
                temp = prof[start+mid:start+mid+end]               
                if temp =='degree':
                    mid = prof[start:].find('>')+1
                    end = prof[start+mid:].find('<')
                    degree = prof[start+mid:start+mid+end-2]
                    start = start+mid+end
                elif temp =='major':
                    a = prof[start:].find('Find users with this keyword')
                    b = prof[start:].find('Explore this field of study')
                    if a==-1:
                        a = 100000
                    if b==-1:
                        b = 100000
                    if a<b:
                        anchor = 'Find users with this keyword'
                    else:
                        anchor = 'Explore this field of study'
                    start = start + prof[start:].find(anchor)
                    mid = prof[start:].find('>')+1
                    end = prof[start+mid:].find('<')
                    major = prof[start+mid:start+mid+end]
                    start = start+mid+end
                elif temp =='education-date':
                    mid = prof[start:].find('>')+1
                    end = prof[start+mid:].find('</span>')
                    time = prof[start+mid:start+mid+end].replace('<time>','').replace('</time>','').replace('&#8211;','-').replace(' ','')
                    if time =='':
                        time='notime'
                else:                   
                    break
                
            education = education +'||'+ degree +'||'+ major +'||'+ time+'||||'
        education = education[:len(education)-4]
        
        education = education.replace('\t','').replace('\n','')
        if education=='':
            education='0'
        
        #--------------------------------------------------        
        #recommendations-----------------------------------------
        #--------------------------------------------------
        recommendations = ''
        start=prof.find('recommendations-container')
        for i in range(1,50):
            if start==-1:
                recommendations = '0||||'
                break
            if prof[start:].find('="referrer"')==-1:
               if i==1:
                   recommendations = '0||||'
               break
            rec = '0'
            recCompany = '0'
            recQuote = '0' 
            recDate = '0'
            #rec
            start = start + prof[start:].find('="referrer"')+1
            start = start + prof[start:].find('="referrer"')+1
            start = start + prof[start:].find('authToken')
            start = start + prof[start:].find('>')+1
            end = prof[start:].find('<')
            rec = prof[start:start+end]
            #recCompany
            start = start + prof[start:].find('h6')
            start = start + prof[start:].find('>')+1
            end = prof[start:].find('</h6>')           
            recCompany = prof[start:start+end]
            if recCompany=='':
                recCompany='0'
            #quote      
            start = start + prof[start:].find('dir="ltr">')+10
            end = prof[start:].find('</p>')
            recQuote = prof[start:start+end].replace('\n','')
            start = start+end
            #date
            start = start + prof[start:].find('endorsement-date')
            mid = prof[start:].find('>')+1
            end = prof[start+mid:].find('<')
            recDate = prof[start+mid:start+mid+end]
            
            recommendations = recommendations+ 'R||'+ rec +'||'+ recCompany +'||'+ recQuote +'||'+ recDate+'||||'
        for i in range(1,50):
            if prof[start:].find('"recommendee"')==-1:
               break
            else:
               if recommendations=='0||||':
                   recommendations=''
            rec = '0'
            recCompany = '0'
            recQuote = '0' 
            recDate = '0'
            #rec
            start = start + prof[start:].find('="recommendee"')+1
            start = start + prof[start:].find('="recommendee"')+1
            start = start + prof[start:].find('authToken')
            start = start + prof[start:].find('>')+1
            end = prof[start:].find('<')
            rec = prof[start:start+end]
            #recCompany
            start = start + prof[start:].find('h6')
            start = start + prof[start:].find('>')+1
            end = prof[start:].find('</h6>')           
            recCompany = prof[start:start+end]
            if recCompany=='':
                recCompany='0'
            #quote      
            start = start + prof[start:].find('dir="ltr">')+10
            end = prof[start:].find('</p>')
            recQuote = prof[start:start++end].replace('\n','')
            start = start+end
            #date
            start = start + prof[start:].find('endorsement-date')
            mid = prof[start:].find('>')+1
            end = prof[start+mid:].find('<')
            recDate = prof[start+mid:start+mid+end]
            
            recommendations = recommendations+ 'G||'+ rec +'||'+ recCompany +'||'+ recQuote +'||'+ recDate+'||||'
        
        
        
        recommendations = recommendations[:len(recommendations)-4]
        
        recommendations=recommendations.replace('\t','').replace('\n','')
        if recommendations=='':
            recommendations='0'
        
        #--------------------------------------------------        
        #patents-----------------------------------------
        #--------------------------------------------------
        patents = ''
        start=prof.find('<h3>Patents</h3>')
        for i in range(1,50):
            if start==-1:
                patents = '0||||'
                break
            if prof[start:].find('id="patent')==-1:
               if i==1:
                   patents = '0||||'
               break
            patent = 'noname'
            patentId = 'nocompany'
            patentDate = 'nodate' 
            invNumber = 'nonumber'
            #patentName
            start = start + prof[start:].find('id="patent')+1
            start = start + prof[start:].find('id="patent')
            start = start + prof[start:].find('dir="auto">')+11
            end = prof[start:].find('<')
            patent = prof[start:start+end]
            start = start+end
            #patentId
            start = start + prof[start:].find('dir="auto">')+11
            end = prof[start:].find('<')
            patentId = prof[start:start+end]
            start = start + end
            #patentDate
            start = start + prof[start:].find('Issued')+12
            end = prof[start:].find('<')
            patentDate = prof[start:start+end]
            if patentDate=='>':
                patentDate = 'nodate'
            start = start + end
            #inventorsNumber
            start = start + prof[start:].find('inventor')
            invNumber = prof[start-2:start-1]
            if invNumber.isdigit()==False:
                invNumber='1'

                
            patents = patents+ patent +'||'+patentId +'||'+ patentDate +'||'+ invNumber+'||||'
        patents = patents[:len(patents)-4]  
        
        patents=patents.replace('\t','').replace('\n','')
        if patents=='':
            patents='0'
        
        #--------------------------------------------------        
        #publications--------------------------------------
        #--------------------------------------------------
        publications = ''
        start=prof.find('<h3>Publications</h3>')
        for i in range(1,50):
            if start==-1:
                publications = '0||||'
                break
            if prof[start:].find('id="publication')==-1:
               if i==1:
                   publications = '0||||'
               break
            publication = 'noname'
            publisher = 'nopublisher'
            patentDate = 'nodate' 
            invNumber = 'nonumber'
            #publicationName
            start = start + prof[start:].find('id="publication')+1
            start = start + prof[start:].find('id="publication')
            start = start + prof[start:].find('dir="auto">')+11
            end = prof[start:].find('<')
            publication = prof[start:start+end]
            start = start+end
            #publisher
            start = start + prof[start:].find('dir="auto">')+11
            end = prof[start:].find('<')
            publisher = prof[start:start+end]
            start = start + end
            #patentDate
            start = start + prof[start:].find('publication-date">')+18
            end = prof[start:].find('<')
            publicationDate = prof[start:start+end]
            start = start + end
          
            publications = publications+ publication +'||'+ publisher +'||'+ publicationDate +'||||'
        publications = publications[:len(publications)-4] 
        
        publications=publications.replace('\t','').replace('\n','')
        if publications=='':
            publications='0'
        
        #--------------------------------------------------        
        #Honors--------------------------------------
        #--------------------------------------------------
        honors = ''
        start=prof.find('<h3>Honors &amp; Awards</h3>')
        stap = prof.find('Additional Honors &amp; Awards')
        if stap == -1:
            stap = 100000000
        for i in range(1,50):
            if start==-1:
                honors = '0||||'
                break  
            if prof[start:].find('class="honoraward')==-1:
               if i==1:
                   honors = '0||||'
               break 
            honorName = '0'
            honorBy = '0'
            honorDate = '0' 
            #honorName
            start = start + prof[start:].find('class="honoraward')+1
            if start +80 >= stap:
                if honors == '':
                   honors = '0||||' 
                break
            start = start + prof[start:].find('dir="auto">')+11
            end = prof[start:].find('<')
            honorName = prof[start:start+end]
            start = start+end
            #honorBy
            start = start + prof[start:].find('dir="auto">')+11
            end = prof[start:].find('<')
            honorBy = prof[start:start+end]
            start = start + end
            #honorDate
            start = start + prof[start:].find('honors-date">')+13
            end = prof[start:].find('</span>')
            honorDate = prof[start:start+end].replace('<time>','').replace('</time>','').replace('&#8211;','-').replace(' ','')
            if len(honorDate) >=35:
                honorDate='0'
          
            honors = honors+ honorName +'||'+ honorBy +'||'+ honorDate +'||||'
        honors = honors[:len(honors)-4] 
        
        honors=honors.replace('\t','').replace('\n','')
        if honors=='':
            honors='0'         
        
        #--------------------------------------------------        
        #certifications--------------------------------------
        #--------------------------------------------------
        certifications = ''
        start=prof.find('<h3>Certifications</h3>')
        for i in range(1,50):
            if start==-1:
                certifications = '0||||'
                break
            if prof[start:].find('id="certification')==-1:
               if i==1:
                   certifications = '0||||'
               break
            certification = 'noname'
            certificationCompany = 'nocompany'
            certificationDate = 'nodate' 
            #certification
            start = start + prof[start:].find('id="certification')
            a = prof[start:].find('trk=profile_certification_company_title')
            b = prof[start:].find('this keyword')
            if a == -1:
                a = 10000
            if b == -1:
                b = 10000
            if a <b:
                start = start + a
            else:
                start = start+b
            start = start + prof[start:].find('>')+1
            end = prof[start:].find('<')
            certification = prof[start:start+end]
            start = start+end
            #certificationCompany
            if prof[start:].find('certification-org_name')!=-1:
                start = start + prof[start:].find('certification-org_name')
                start = start + prof[start:].find('>')+1
                end = prof[start:].find('<')
                certificationCompany = prof[start:start+end]
                start = start + end
                if certificationCompany == '':
                    start = start + prof[start:].find('certification-org_name')
                    start = start + prof[start:].find('>')+1
                    end = prof[start:].find('<')
                    certificationCompany = prof[start:start+end]
                    start = start + end   
            #certificationDate
            if prof[start:].find('certification-date')!=-1:
                start = start + prof[start:].find('certification-date')+20
                end = prof[start:].find('</span>')
                certificationDate = prof[start:start+end].replace('<time>','').replace('</time>','').replace('&#8211;','-')
                if certificationDate =='':
                    certificationDate = 'nodate'
                start = start + end
        
            
            certifications = certifications+ certification +'||'+ certificationCompany +'||'+ certificationDate +'||||'
        certifications = certifications[:len(certifications)-4]    
        
        certifications=certifications.replace('\t','').replace('\n','')
        if certifications=='':
            certifications='0'
        
        
    data = data + profile+'\t'+name+'\t'+miniJob+'\t'+miniArea+'\t'+miniIndustry+'\t'+miniCurrent+'\t'+miniPrevious+'\t'+miniEducation+'\t'+summary+'\t'+miniConnections+'\t'+experience+'\t'+skills+'\t'+education+'\t'+recommendations+'\t'+patents+'\t'+publications+'\t'+honors+'\t'+certifications+'\n'
        
with open('parsed/profiles.txt', mode='w', encoding='utf-8') as g:
    g.write(data.lower().replace('&amp;',' and ').replace('&#39;','\'')) 



from django.shortcuts import render
from jobweb.models import Technologies,Job
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,"home.html")
    
@login_required(login_url='/signup/login')
def search(request):
    #if user logged in then give reult
    #else : goto login page
    
    query=request.GET.get('search')
    
    if len(query)>80:
        allPosts=Job.objects.none()
        
    else:
        allPostsTitle= Job.objects.filter(python__icontains=query)        
        allPostsjava =Job.objects.filter(java__icontains=query)
        allPostsphp =Job.objects.filter(php__icontains=query)
        allPostsReact_js =Job.objects.filter(React_js__icontains=query)
        allinternship =Job.objects.filter(internship__icontains=query)
        allPlacement =Job.objects.filter(Placement__icontains=query)
        allFresher =Job.objects.filter(Fresher__icontains=query)
        
        allPosts=  allPostsTitle.union(allPostsjava,allPostsphp,allPostsReact_js,allinternship,allPlacement,allFresher)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")

    params={'allPosts': allPosts, 'query': query}
    # return render(request, 'search.html',{"s":'this is search result  page'})

    return render(request,"search.html", params)
    

@login_required(login_url='/signup/login')
def jobseeker(request):

    return render(request, 'upcoming.html')


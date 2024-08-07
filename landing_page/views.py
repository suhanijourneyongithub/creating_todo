from django.shortcuts import render, redirect
from .models import Todo, Profile

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~LANDING PAGE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def landing_page(request):
    
    return render(request, "home.html")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TO_DO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def to_do(request):

    user = request.user
    
    todos = Todo.objects.filter(is_completed = False, user = user)#user = user me 1st user is model's attribute and 2nd one is the variable in upper line
    
    parameters = {
        "todos": todos,
        "user": user
    }

    return render(request, "todo.html", parameters)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ADD_TODO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_todo(request):
  
    if request.method == "POST":
        
        #template se view me data la rhe hai
        user_task = request.POST.get("task")
        user_created_at = request.POST.get("created_at")
        user_due_at = request.POST.get("due_at")

        #view wala data model m save ho rha hai
        new_todo = Todo(task = user_task, created_at = user_created_at, due_at = user_due_at, is_completed = False, user = request.user)
        new_todo.save()

        return redirect("to_do")
    
    return render(request, "add_todo.html")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DELETE_TODO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def delete_todo(request, todo_id):

    todo = Todo.objects.get(id = todo_id)
    todo.delete()

    return redirect("to_do")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~UPDATE_TODO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def update_todo(request, todo_id):
 
    todo = Todo.objects.get(id = todo_id)

    if request.method == "POST":

        user_task = request.POST.get("task")
        user_created_at = request.POST.get("created_at")
        user_due_at = request.POST.get("due_at")

        todo.task = user_task
        todo.created_at = user_created_at
        todo.due_at = user_due_at 

        todo.save()
        return redirect("to_do")

    parameters = { "todo": todo }
    return render(request, "update_todo.html", parameters)
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MARK_COMPLETE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def mark_complete(request, todo_id):

    todo = Todo.objects.get(id = todo_id)   #jo todo complete ho gya hai vo todo me save hai
    todo.is_completed = True    #task completed hai ka stamp
    todo.save()     #task completed hai ye save hua

    todos01 = Todo.objects.all()#isme query set me saare todos hai

    lis = []    #list jisme me completed wale todo add karungi

    for i in todos01:
        if i.is_completed == True:
            lis.append(i)
    
    parameters02 = { "todos01": lis }
    
    return render(request, "completed_tasks.html", parameters02)    #me list ko html page me bhej rhi hun
 
 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MARK_COMPLETE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PROFILE_PIC~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def profile_pic(request): #request, pic_id

    if request.method == "POST":
        profile_pic = request.FILES["profile_pic"]
 
        new_profile = Profile(
            title = "demo title",
            profile_pic = profile_pic
        )
        new_profile.save() 

        return redirect("to_do")
    
    image = Profile.objects.get(id = 5) #id = pic_id
    parameters = {"image": image}

    return render(request, "upload_profile_pic.html", parameters)

# def logout(request):
#     auth.logout(request)
#     return redirect("login")
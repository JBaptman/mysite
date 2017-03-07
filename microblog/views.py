from django.http import HttpResponse
from django.http import QueryDict
from django.shortcuts import redirect
from .models import Message
from .forms import PostForm
from django.shortcuts import render
import json 


#View that represents the homepage, when the user hasn't put/delete any post
def home(req): 
    tmpl_vars = {
        'post_list': Message.objects.reverse(),
        'form': PostForm()
    }
    return render(req, 'microblog/index.html', tmpl_vars)

#View that processes the creation of a new post by the user
def create_post(request):
    if request.method == 'POST':

        #We get the message from the POST request
        msg_text = request.POST.get('new_msg')
        response_data = {}

        #Creation of a new instance of Message
        msg = Message(text=msg_text, user=request.user)
        msg.save()


        #Preperation of what the view will return
        response_data['result'] = 'Your post has been added successfully!'
        response_data['postpk'] = msg.pk
        response_data['text'] = msg.text
        response_data['created'] = msg.created.strftime('%B %d, %Y %I:%M %p') 
        response_data['author'] = msg.user.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"que dalle"}),
            content_type="application/json"
        )


#View that processes the deletion of a post by the user
def delete_post(request):
    if request.method == 'DELETE':

        #We get the ID of the post the user wants to delete
        msg = Message.objects.get(pk=int(QueryDict(request.body).get('postpk')))
        response_data = {}
        response_data['msg'] = 'The post has been deleted'
        response_data['msg_user'] = msg.user.id
        response_data['req_user'] = request.user.id
        response_data['issuperuser'] = request.user.is_superuser


        #Here we check if the user is the author of the post he wants to delete, or if he is an admin. If it is the case, then we allow the deletion, otherwise we don't.
        #NB : IF YOU WANT TO TRY THE FEATURE THAT A USER CAN'T DELETE A POST WRITTEN BY AN OTHER USER, PLEASE UNCOMMENT "OR (REQUEST.USER.IS_SUPERUSER)"
        if ((request.user.id == msg.user.id) or (request.user.is_superuser)):
            msg.delete()
            response_data['isvalid'] = True
        else:
            response_data['isvalid'] = False
        


        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"que dalle"}),
            content_type="application/json"
        )
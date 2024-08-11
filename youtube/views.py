from django.shortcuts import render,redirect
from django.views import generic
from .models import Post,Comment
from django.urls import reverse_lazy
from .forms  import PostCreateForm,CommentCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin,generic.ListView):
    model=Post
    login_url='youtube:login'
    
    
def detailfunc(request,pk):
    post=Post.objects.get(pk=pk)
    post.read += 1 #閲覧数をインクリメント
    post.save()
    return render(request,'youtube/post_detail.html',{'post':post})
    
class CreateView(generic.CreateView):
    model=Post
    form_class=PostCreateForm
    success_url=reverse_lazy('youtube:index')
    def form_valid(self, form):
      '''
      フォームの保存(post)時にログインユーザをモデルに保存
      '''
      # ユーザーを投稿者として保存できるようにする
      object = form.save(commit=False) #　入力値をモデルに保存せず保留
      object.user_name = self.request.user # ログインユーザ取得
      object.save() # モデルに保存
      return super().form_valid(form)
    
class DeleteView(generic.DeleteView):
    model=Post
    success_url=reverse_lazy('youtube:index')
    
class UpdateView(generic.UpdateView):
    model=Post
    form_class=PostCreateForm
    success_url=reverse_lazy('youtube:index')
    
def signupfunc(request):
    if request.method=='POST':
        username2=request.POST['username']
        password2=request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request,'youtube/signup.html',{'error':'このユーザーはすでに使用されています'})
        except:
            user = User.objects.create_user(username2, "", password2)
            return redirect('youtube:index')
    return render(request,'youtube/signup.html',{'some':100})

def loginfunc(request):
    if request.method=='POST':
        username2=request.POST['username']
        password2=request.POST['password']
        user = authenticate(username=username2, password=password2)
        if user is not None:
            login(request,user)
            return redirect('youtube:index')
        else:
            return render(request,'youtube/signup.html',{'error':'登録されていません'})
    return render(request,'youtube/login.html')

def logoutfunc(request):
    logout(request)
    return redirect('youtube:index')

def goodfunc(request,pk):
    post=Post.objects.get(pk=pk)
    post2=request.user.get_username()
    if post2 in post.usertext:
        return redirect('youtube:index')
    else:
        post.good+=1
        post.usertext=post.usertext + ' ' + post2
        post.save()
        return redirect('youtube:index')
    
class MypageView(generic.ListView):
    model=Post
    model=User
    template_name = "youtube/user_list.html"
    
    def get_queryset(self):
        current_user = self.request.user.username # ログイン中のユーザ名を取得（CustomUserモデルのusernameレコードの値を取得）
        user_data = User.objects.get(username=current_user) # QuerySet(条件が一致するレコードを全て取得)
        if user_data:
            queryset = Post.objects.filter(user_name=user_data).all() # QuerySet（一致するレコード全て取得）
          
        return queryset

    

class CommentView(generic.CreateView):
    model=Comment
    form_class=CommentCreateForm
    def form_valid(self,form):
        post_pk=self.kwargs['post_pk']
        comment=form.save(commit=False)
        comment.post=get_object_or_404(Post,pk=post_pk)
        comment.save()
        return redirect('youtube:detail',pk=post_pk)
    

    
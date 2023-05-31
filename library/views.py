from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Document
from .forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    return render(request, 'main/home.html', { 'documents': documents })

@login_required(login_url="/login/")
def upload_form(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'main/upload.html', {
        'form': form
    })

@login_required(login_url="/login/")
def delete_document(request, document_id):
    document = Document.objects.get(id=document_id)
    if request.method == 'POST':
        document.document.delete()
        document.delete()
        return redirect('home')
    return render(request, 'main/delete.html', {'document': document})

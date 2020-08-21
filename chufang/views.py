from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
import shortuuid


@staff_member_required
def index(request):

    if request.method == 'POST':
        uploaded_file = request.FILES.get('uploaded-file')
        if uploaded_file:
            for line_data in uploaded_file.readlines():
                pass

    return render(request, 'chufang/index.html')

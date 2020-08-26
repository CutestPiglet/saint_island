from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from chufang import utils


@staff_member_required
def index(request):

    context = {}

    if request.method == 'POST':
        sequence_listing_file = request.FILES.get('uploaded-sequence-listing-file')
        if sequence_listing_file:
            context['filename'] = sequence_listing_file.name

            try:
                seq_dict = utils.convert_sequence(sequence_listing_file)
            except Exception as e:
                messages.error(request, str(e), extra_tags='Oops! Unexpected exception occured')
            else:
                context['seq_dict'] = seq_dict

    return render(request, 'chufang/index.html', context)

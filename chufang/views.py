from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from chufang import utils


@staff_member_required
def index(request):

    context = {}

    if request.method == 'POST':
        sequence_listing_file = request.FILES.get('uploaded-sequence-listing-file')
        manual_files = request.FILES.getlist('uploaded-manual-files')
        if sequence_listing_file and manual_files:
            context.update({
                'sequence_listing_filename': sequence_listing_file.name,
                'manual_filenames': ', '.join([f.name for f in manual_files])
            })

            try:
                seq_dict = utils.convert_sequence(sequence_listing_file)
            except Exception as e:
                messages.error(request, str(e), extra_tags='Oops! Unexpected exception occured')
            else:
                context['seq_dict'] = seq_dict

    return render(request, 'chufang/index.html', context)

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.utils.html import format_html

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

                for manual_file in manual_files:
                    utils.compare_sequence(seq_dict, manual_file)
            except Exception as e:
                messages.error(request, str(e), extra_tags='Oops! Unexpected exception occured')
            else:
                not_found_seqs = []
                for index, seq_content in seq_dict.items():
                    if not seq_content['is_found']:
                        not_found_seqs.append(format_html(f'<a href="#{index}">{index}</a>'))

                context.update({
                    'seq_dict': seq_dict,
                    'not_found_seqs': ', '.join(not_found_seqs),
                    'num_of_not_found_seqs': len(not_found_seqs),
                })

    return render(request, 'chufang/index.html', context)

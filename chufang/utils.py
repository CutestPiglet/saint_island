def convert_amino_acid_abbreviation(three_letter_abbreviation):

    one_letter_abbreviation = {
        'ala': 'A',
        'arg': 'R',
        'asn': 'N',
        'asp': 'D',
        'cys': 'C',
        'gln': 'Q',
        'glu': 'E',
        'gly': 'G',
        'his': 'H',
        'ile': 'I',
        'leu': 'L',
        'lys': 'K',
        'met': 'M',
        'phe': 'F',
        'pro': 'P',
        'ser': 'S',
        'thr': 'T',
        'trp': 'W',
        'tyr': 'Y',
        'val': 'V',
        'asx': 'B',
        'glx': 'Z',
        'xaa': 'X',  # unknow or other
    }.get(three_letter_abbreviation.lower())

    if not one_letter_abbreviation:
        raise Exception(f'Cannot find One-letter abbreviation of {three_letter_abbreviation}')

    return one_letter_abbreviation


def convert_sequence(sequence_listing_file):

    SEQ_INDEX_LABEL = '<210>'
    SEQ_LEN_LABEL = '<211>'
    SEQ_TYPE_LABEL = '<212>'
    SEQ_CONTENT_LABEL = '<400>'
    PRT_TYPE = 'PRT'

    seq_dict = {}
    while True:
        line = sequence_listing_file.readline().decode()
        if not line:
            break

        if SEQ_INDEX_LABEL in line:
            seq_index = int(line.split(SEQ_INDEX_LABEL)[1].strip())
            seq_len = int(sequence_listing_file.readline().decode().split(SEQ_LEN_LABEL)[1].strip())
            seq_type = sequence_listing_file.readline().decode().split(SEQ_TYPE_LABEL)[1].strip()

            dna_or_rna_seq = prt_seq = ''
            while True:
                line = sequence_listing_file.readline().decode()
                if SEQ_CONTENT_LABEL in line:
                    target_seq = ''
                    while len(target_seq) < seq_len:
                        line = sequence_listing_file.readline().decode()
                        for fragment in line.split(' '):
                            if fragment.isalpha():
                                if fragment.islower():
                                    dna_or_rna_seq += fragment.strip()
                                else:
                                    prt_seq += convert_amino_acid_abbreviation(fragment)
                        target_seq = prt_seq if seq_type.upper() == PRT_TYPE else dna_or_rna_seq
                    break

            seq_dict.update({
                seq_index: {
                    'len': seq_len,
                    'type': seq_type,
                    'dna_or_rna_seq': dna_or_rna_seq,
                    'prt_seq': prt_seq,
                },
            })

    return seq_dict

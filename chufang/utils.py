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
    }.get(three_letter_abbreviation.lower())

    if not one_letter_abbreviation:
        raise Exception(f'Cannot find One-letter abbreviation of {three_letter_abbreviation}')

    return one_letter_abbreviation

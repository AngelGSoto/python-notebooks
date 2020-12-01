'''
Taken from: https://github.com/will-henney/orion-bowshock-catalog/blob/master/luis-angel-ll.org
'''
region_hdr_lines = [
    '# Region file format: DS9 version 4.1',
    'global color=yellow dashlist=8 3 width=1 font=\"helvetica 10 normal roman\" '
    + 'select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1',
    'fk5',
]

def region_box_to_string(ra='5:34:40.800', dec='-5:22:43.00', text='LL2',
                         color='yellow', width=2, height=2, angle=0.0):
                         pattern = 'box({},{},{}\",{}\",{}) # text={{{}}} color={}'
                         return pattern.format(ra, dec, width, height, angle, text, color)


def region_lines_from_table(table, ra='RAJ2000', dec='DEJ2000',
                            name='Name', color='yellow'):
    """Create DS9 region lines for all sources in an astropy `table`

    Coordinates come from the columns named `ra` and `dec`, while
    source names come the column named `name` and are formatted
    according to `name_fmt`"""

    region_lines = region_hdr_lines[:]
    for row in table:
        region_lines.append(
                    region_box_to_string(row[ra], row[dec],
                                              row[name], color))

    return region_lines

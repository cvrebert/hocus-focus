#!/usr/bin/env python2.7
from __future__ import absolute_import, print_function, division

from glob import glob
from os import mkdir
from os.path import abspath, dirname, isdir, join as joinpath

from lxml import etree
from lxml.html import parse as parse_html


HOCUS_ROOT = dirname(abspath(__file__))
_EXAMPLE_TEMPLATE_FILEPATH = joinpath(HOCUS_ROOT, 'example_template.html')

with open(_EXAMPLE_TEMPLATE_FILEPATH, 'r') as example_template_file:
    EXAMPLE_TEMPLATE = example_template_file.read()


def log(*args, **kwargs):
    print(*args, **kwargs)


def extract_examples(docs_html_filepaths, output_directory):
    for docs_html_filepath in docs_html_filepaths:
        with open(docs_html_filepath, 'r') as docs_html_file:
            dom = parse_html(docs_html_file)
        log('Extracting from', docs_html_filepath)

        examples = dom.xpath('//*[@data-example-id]')
        for example in examples:
            example_id = example.get('data-example-id')
            if not example_id:
                continue

            example_filename = example_id + '.html'
            example_filepath = joinpath(output_directory, example_filename)

            example_html = EXAMPLE_TEMPLATE.format(example_html=etree.tostring(example))

            with open(example_filepath, 'w') as example_html_file:
                example_html_file.write(example_html)
                log('Wrote', example_filepath)


def main():
    # Assumes that CWD is /bootstrap/
    docs_html_filepaths = glob(abspath('./_gh_pages/*/index.html'))
    example_html_files_output_dir = abspath('./_gh_pages/extracted-examples')
    if not isdir(example_html_files_output_dir):
        mkdir(example_html_files_output_dir)
    extract_examples(docs_html_filepaths, example_html_files_output_dir)


if __name__ == '__main__':
    main()

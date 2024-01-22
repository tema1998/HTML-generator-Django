from tailwind_generator import settings
from tailwind_generator.settings import BASE_DIR
from bs4 import BeautifulSoup
import os


# class Index(View):
#
#     def get(self, request):
#         base_path = os.path.join(BASE_DIR, 'tailwind_generator/static/files', 'base.html')
#         for_header_path = os.path.join(BASE_DIR, 'tailwind_generator/static/files', 'for_header.html')
#         file2_path = os.path.join(BASE_DIR, 'tailwind_generator/static/files', 'file2.html')
#
#         with open(base_path, 'r') as html:
#             base = BeautifulSoup(html.read(), 'html.parser')
#
#         with open(for_header_path, 'r') as html:
#             for_header = BeautifulSoup(html.read(), 'html.parser')
#
#         base.find('header').insert(0, for_header)
#         print(base.prettify())
#
#         file2 = open(file2_path, 'w+', encoding='utf-8')
#         file2.write(base.prettify())
#         file2.close()
#         return render(request, 'core/base.html', {})

def get_path_to_file_from_media(file):
    return os.path.join(BASE_DIR, 'media', str(file))


def generate_html_file(result_id, title, header, footer):
    path_to_base = get_path_to_file_from_media('base/base.html')
    full_path_to_result = get_path_to_file_from_media(f'generated_html/{result_id}.html')

    path_to_header = get_path_to_file_from_media(header)
    path_to_footer = get_path_to_file_from_media(footer)

    with open(path_to_base, 'r') as html:
        base_bs = BeautifulSoup(html.read(), 'html.parser')

    with open(path_to_header, 'r') as html:
        header_bs = BeautifulSoup(html.read(), 'html.parser')

    with open(path_to_footer, 'r') as html:
        footer_bs = BeautifulSoup(html.read(), 'html.parser')

    base_bs.find('title').insert(0, title)
    base_bs.find('header').insert(0, header_bs)
    base_bs.find('main').insert_after(footer_bs)

    result = open(full_path_to_result, 'w+', encoding='utf-8')

    result.write(base_bs.prettify())
    result.close()

    return f'media/generated_html/{result_id}.html'

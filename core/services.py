from tailwind_generator import settings
from tailwind_generator.settings import BASE_DIR
from bs4 import BeautifulSoup
import os


def get_path_to_file_from_media(file):
    return os.path.join(BASE_DIR, 'media', str(file))


def get_bs_object_by_path_to_html(path_to_html):
    with open(path_to_html, 'r') as html:
        bs_object = BeautifulSoup(html.read(), 'html.parser')
    return bs_object


def paste_result_in_base_html(result):
    base_bs = get_path_to_base_html_converted_to_bs()
    base_bs.find('title').insert(0, result.title)

    processed_components_name = result.default_processed_components

    for component_name in processed_components_name:
        component = getattr(result, component_name)
        path_to_component = get_path_to_file_from_media(component.html)
        component_bs = get_bs_object_by_path_to_html(path_to_component)
        try:
            base_bs.find(component_name).insert(0, component_bs)
        except AttributeError:
            new_component_name = 'main'
            base_bs.find(new_component_name).insert(0, component_bs)
    return base_bs


def get_path_to_base_html_converted_to_bs():
    path_to_base = get_path_to_file_from_media('base/base.html')
    base_bs = get_bs_object_by_path_to_html(path_to_base)
    return base_bs


def save_result_html_file(result_id, base_bs):
    full_path_to_result = get_path_to_file_from_media(f'generated_html/{result_id}.html')
    result = open(full_path_to_result, 'w+', encoding='utf-8')
    result.write(base_bs.prettify())
    result.close()


def generate_html_file(result):
    processed_base_bs = paste_result_in_base_html(result)
    save_result_html_file(result.id, processed_base_bs)

    return f'media/generated_html/{result.id}.html'
#
# def generate_html_file(result_id, processed_components, title, header, footer, signin=None, signup=None):
#     path_to_base = get_path_to_file_from_media('base/base.html')
#     full_path_to_result = get_path_to_file_from_media(f'generated_html/{result_id}.html')
#
#     path_to_header = get_path_to_file_from_media(header)
#     path_to_footer = get_path_to_file_from_media(footer)
#
#     base_bs = get_bs_object_by_path_to_html(path_to_base)
#     header_bs = get_bs_object_by_path_to_html(path_to_header)
#     footer_bs = get_bs_object_by_path_to_html(path_to_footer)
#
#     base_bs.find('title').insert(0, title)
#     base_bs.find('header').insert(0, header_bs)
#     base_bs.find('footer').insert(0, footer_bs)
#
#     result = open(full_path_to_result, 'w+', encoding='utf-8')
#
#     result.write(base_bs.prettify())
#     result.close()
#
#     return f'media/generated_html/{result_id}.html'

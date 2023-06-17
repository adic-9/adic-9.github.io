import re

def replace_asterisks_with_bold(text):
    pattern = r'\*(.*?)\*'  # Matches substrings surrounded by asterisks
    
    def repl(match):
        return '<b>' + match.group(1) + '</b>'
    
    replaced_text = re.sub(pattern, repl, text)
    return replaced_text


def wrap_blocks_with_paragraphs(text):
    pattern = r'(\n\n.*?\n\n)'  # Matches blocks separated by double line breaks
    
    def repl(match):
        return '<p>' + match.group(1) + '</p>'
    
    wrapped_text = re.sub(pattern, repl, text, flags=re.DOTALL)
    return wrapped_text


def convert_markdown_links(text):
    pattern = r'\[(.*?)\]\((.*?)\)'  # Matches [link name](website.com)
    
    def repl(match):
        link_name = match.group(1)
        url = match.group(2)
        return f'<a href="{url}">{link_name}</a>'
    
    converted_text = re.sub(pattern, repl, text)
    return converted_text

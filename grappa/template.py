# -*- coding: utf-8 -*-
import functools
from colorama import Fore, Style

from .config import config


class ErrorTemplate(object):
    """
    ErrorTemplate is used to compose and render a human-friendly
    descriptive error message.
    """

    separator = ' ' * 6

    section_separator = '\n\n  '

    def __init__(self):
        self.sections = []

    @property
    def color(self):
        return Style.BRIGHT + Fore.GREEN if config.use_colors else ''

    @property
    def reset(self):
        return Style.RESET_ALL if config.use_colors else ''

    def map_iterable(self, content):
        margin = ' ' * 4

        if type(content[0]) is str:
            return ('\n' + margin).join(
                '> ' + item for item in content if item
            )

        return ('\n\n' + margin).join(
            item.render(ErrorTemplate.separator)
            for item in content
            if hasattr(item, 'render')
        )

    def block(self, title, content):
        # If no content, just exit
        if not content:
            return self

        # If iterable type, aggregate elements and format them
        if isinstance(content, (tuple, list)):
            content = self.map_iterable(content)

        # Register section object
        self.sections.append({
            'title': title,
            'content': content
        })

        return self

    def render(self):
        def add_section(buf, section):
            buf.append('{color}{title}{reset}\n    {content}'.format(
                color=self.color,
                title=section['title'],
                reset=self.reset,
                content=section['content']
            ))
            return buf

        sections = functools.reduce(add_section, self.sections, [])
        return self.section_separator.join(sections)

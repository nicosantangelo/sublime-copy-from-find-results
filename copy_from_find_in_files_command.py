import sublime, sublime_plugin, re

class CopyFromFindInFilesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command('copy')

        if not self.in_find_results_view():
            return

        clipboard_contents = sublime.get_clipboard()

        if clipboard_contents:
            keep_intermediate_dots = sublime.load_settings('CopyFromFindInFiles.sublime-settings').get('keep_intermediate_dots', False)
            new_clipboard = RegexStruct(keep_intermediate_dots).sub(clipboard_contents)
            sublime.set_clipboard(new_clipboard)

    def in_find_results_view(self):
        return self.view.settings().get('syntax') == 'Packages/Default/Find Results.hidden-tmLanguage'

class RegexStruct():
    default = r'^\s*\d+\:?'
    without_dots = r'^\s*(\d+\:?|.+)'

    def __init__(self, keep_dots=True):
        self.keep_dots = keep_dots

    def sub(self, text):
        return re.sub(self.construct(), '', text, flags=re.MULTILINE)

    def construct(self):
        return RegexStruct.default if self.keep_dots else RegexStruct.without_dots

import sublime, sublime_plugin, re

class CopyFromFindInFilesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("copy")

        if not self.in_find_results_view():
            return

        self.settings = sublime.load_settings("CopyFromFindInFiles.sublime-settings")
        clipboard_contents = sublime.get_clipboard()

        if clipboard_contents:
            re.sub(r'insert_regex_here', '', clipboard_contents)
            sublime.set_clipboard(clipboard_contents)

    def in_find_results_view(self):
        return self.view.settings().get('syntax') == 'Packages/Default/Find Results.hidden-tmLanguage'


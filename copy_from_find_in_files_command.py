import sublime, sublime_plugin, re

class CopyFromFindInFilesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if not self.in_find_results_view():
            print("nay")
            return self.view.run_command("copy")

        print("yay")
        self.settings = sublime.load_settings("CopyFromFindInFiles.sublime-settings")

    def in_find_results_view(self):
        return self.view.settings().get('syntax') == 'Packages/Default/Find Results.hidden-tmLanguage'

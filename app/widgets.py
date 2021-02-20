from django import forms
from django.core.serializers.json import json


class CodeMirrorWidget(forms.Textarea):
    config = {
        'indentUnit': 4,
        'tabSize': 4,
        'theme': "dracula",
        'lineNumbers': True,
        'matchTags': {'bothTags': True}
    }

    class Media:
        js = (
            'codemirror/lib/codemirror.js',
            'codemirror/addon/mode/overlay.js',
            'codemirror/addon/edit/matchbrackets.js',
            'codemirror/addon/edit/matchtags.js',
            'codemirror/addon/fold/xml-fold.js',
            'codemirror/addon/lint/lint.js',
            'codemirror/addon/lint/javascript-lint.js',
            'codemirror/addon/lint/json-lint.js',
            'codemirror/mode/javascript/javascript.js',
            'codemirror/mode/htmlmixed/htmlmixed.js',
        )
        css = {
            'all': (
                'codemirror/lib/codemirror.css',
                'codemirror/addon/lint/lint.css',
                'codemirror/theme/dracula.css'
            )
        }

    def __init__(self, **kwargs):
        self.config.update(kwargs)
        super(CodeMirrorWidget, self).__init__()

    def render(self, name, value, attrs=None, renderer=None):
        field = super(CodeMirrorWidget, self).render(name, value, attrs, renderer)
        template = """%s
            <script type="text/javascript">
                function betterTab(cm) {
                    if (cm.somethingSelected()) {
                        cm.indentSelection("add");
                    } else {
                        cm.replaceSelection(cm.getOption("indentWithTabs")? "\t":
                        Array(cm.getOption("indentUnit") + 1).join(" "), "end", "+input");
                    }
                }
                CodeMirror.fromTextArea(
                    document.getElementById('%s'), Object.assign(%s, {'extraKeys':{'Tab': betterTab}})
                )
            </script>
            """ % (field, attrs['id'], json.dumps(self.config))
        return template

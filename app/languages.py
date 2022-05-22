def get_lang_ext(progLang):
    if(lang_ext.get(progLang, 0)):
        return lang_ext[progLang]
    if("Python" in progLang):
        return ".py"
    if("C++" in progLang):
        return ".cpp"
    if("Java" in progLang):
        return ".java"
    
lang_ext = {
    'mysql': 'sql',
    'ms sql server': 'sql',
    'oracle' : 'sql',
    'csharp': 'cs',
    'python': 'py',
    'python3': 'py',
    'javascript': 'js',
    'ruby': 'rb',
    'kotlin' : 'kt',
    'rust' : 'rs',
    'typescript': 'ts',
    'racket': 'rkt',
    'erlang' : 'erl',
    'elixir' : 'exs',
    'bash' : 'sh'
}

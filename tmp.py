def remove_markup(text):
  # 強調マークアップの除去
  pattern = r'\'{2,5}'
  print(pattern)
  text = re.sub(pattern, '', text)

  # 内部リンクマークアップの除去
  pattern = r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]'
  text = re.sub(pattern, r'\1', text)

  return text

result_rm = {k: remove_markup(v) for k, v in result.items()}
for k, v in result_rm.items():
    print(k + ': ' + v)

remove_markup("aaaaaaaa")

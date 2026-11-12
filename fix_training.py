from pathlib import Path
import re
p = Path('training.html')
text = p.read_text('utf-8')
pattern = r"(document\.getElementById\('lineChart'\)\.addEventListener\('mouseout', hideTooltip\);\s*)renderProgressCharts\(\);"
replacement = r"\1// 默认统一显示‘法治课程’数据，避免首次加载与刷新结果不一致\n    document.querySelector('[data-section=\"course\"]').click();\n\n    renderProgressCharts();"
new_text, count = re.subn(pattern, replacement, text, count=1)
print('replaced:', count)
if count > 0:
    p.write_text(new_text, 'utf-8')
else:
    print('pattern not found')
